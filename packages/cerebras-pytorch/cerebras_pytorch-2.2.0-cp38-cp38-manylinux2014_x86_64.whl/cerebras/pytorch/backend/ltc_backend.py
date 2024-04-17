# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" The PyTorch/LTC backend implementation """
import atexit
import inspect
import os
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack
from pathlib import Path
from threading import Event
from typing import Any, List, Optional, Set, Union

import torch
import torch._lazy  # pylint: disable=import-error

import cerebras.pytorch as cstorch
from cerebras.appliance.appliance_client import fw_user_serialize
from cerebras.appliance.log import ClassLogger, named_class_logger
from cerebras.appliance.pb.framework.appliance_service_pb2 import RunRequest
from cerebras.appliance.saver.h5_saver import hdf5_locking
from cerebras.appliance.utils.file import create_symlink
from cerebras.pytorch.amp import init as amp_init
from cerebras.pytorch.amp._amp_state import _amp_state
from cerebras.pytorch.backend.base_backend import (
    COMPILE_ONLY_MSG,
    COMPILE_SUCCESS_MSG,
    PROGRAMMING_CS_MSG,
    BaseBackend,
)
from cerebras.pytorch.checks import add_checks
from cerebras.pytorch.core.appliance import ApplianceMode
from cerebras.pytorch.core.constants import INPUT_NAME_PREFIX, STATE_NAME_PREFIX
from cerebras.pytorch.core.device import LazyDevice
from cerebras.pytorch.core.modes import EVAL
from cerebras.pytorch.core.name_scope import ScopeName
from cerebras.pytorch.lib import cerebras_pytorch_lib
from cerebras.pytorch.saver.checkpoint_reader import CheckpointReader
from cerebras.pytorch.saver.pt_h5_saver import PyTorchH5Saver
from cerebras.pytorch.saver.storage import (
    DeferredTensor,
    lazy_tensor_data_wrapper,
)
from cerebras.pytorch.utils.nest import visit_device_tensors
from cerebras.pytorch.utils.utils import UNSPECIFIED


@named_class_logger("LtcBackend")
class PyTorchLtcBackendImpl(BaseBackend, ClassLogger):
    """The backend subclass for PyTorch/LTC runs"""

    def __init__(
        self,
        backend_type,
        artifact_dir: str = None,
        compile_dir: str = None,
        compile_only: bool = False,
        validate_only: bool = False,
        drop_data: bool = False,
        log_initialization: bool = True,
        micro_batch_size: Any = UNSPECIFIED,
        retrace_every_iteration: bool = False,
    ):
        super().__init__(backend_type, LazyDevice())
        if artifact_dir is None:
            self.config.artifact_dir = Path.cwd().joinpath("cerebras_logs")
        else:
            self.config.artifact_dir = Path(artifact_dir)

        self.config.artifact_dir.mkdir(parents=True, exist_ok=True)

        if compile_dir is not None:
            self.config.compile_dir = compile_dir

        self.config.compile_only = compile_only
        self.config.validate_only = validate_only
        self.config.log_initialization = log_initialization

        if micro_batch_size is not UNSPECIFIED:
            warnings.warn(
                "Specifying `micro_batch_size` when constructing the backend is deprecated. "
                "Please set this value in the DataExecutor as follows: "
                "\ndata_executor = cstorch.utils.data.DataExecutor(..., micro_batch_size=<value>)",
                category=DeprecationWarning,
            )
        self._deprecated_micro_batch_size = micro_batch_size

        if compile_only or validate_only:
            # No need to initialize the weights if we are only compiling or
            # validating, so disable tracing the initialization altogether.
            # Note: technically, we don't actually skip tracing the
            # initialization, but we do skip the actual initialization of the
            # weights if this is set to False. This is so that we can still
            # trace and initialize the weights if the user wants to save the
            # initial checkpoint.
            self.device.config.lazy_initialization = False
            # We can drop any tensor data that already exists as soon as it's
            # moved to the device
            self.device.config.drop_data = True
        elif drop_data:
            # Trace the initialization, but don't actually initialize the weights
            self.device.config.lazy_initialization = True
            self.device.config.drop_data = True

        self.appliance = None
        self._appliance_execute_cleanup_stack = None

        self._compile_appliance = None

        self._has_worker_image = False

        # Set of weight available in appliance from previous session
        # that needs to be moved to the tensor repository.
        self._alive_weights = None

        # List of tensors ptid that needs to be removed from
        # the persistance tensor repository sicne they have
        # no usages on the framework side.
        self._tensors_to_remove = set()

        self.initial_state_file = None
        self._initial_ckpt_id = 0

        # A dictionary to store the compile cache. The key is the hash of the
        # compile that includes cross_compile_state, cirh and debug_args. The value is the
        # compile response.
        self._compile_cache = {}

        debug = bool(int(os.environ.get("CSTORCH_DEBUG", "1")))

        cerebras_pytorch_lib.initialize(ir_debug=debug)
        atexit.register(self.shutdown)

        if debug:
            os.environ["LTC_IR_DEBUG_ROOT_PATH"] = ":".join(
                # sys.path entries in order from longest to shortest
                sorted(
                    (path + "/" for path in sys.path if path),
                    key=lambda x: -len(x),
                )
            )

        # Set the number of OMP threads to 1 to avoid issues with
        # multiprocessing/forking
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["OPENBLAS_NUM_THREADS"] = "1"
        torch.set_num_threads(1)

        self.logger.verbose("Running using LTC backend")

        # Disable retrace every iteration
        self._retrace_every_iteration = retrace_every_iteration
        cerebras_pytorch_lib.retrace_every_iteration(
            self._retrace_every_iteration
        )

        # add prehook checks
        add_checks(self.device.type)

    def _generate_tensor_names(
        self, prefix: str, tensors: list, delimiter: str
    ):
        for scope, tensor in visit_device_tensors(
            data_structure=tensors,
            device_type=self.torch_device.type,
            scope=[prefix] if prefix else None,
        ):
            yield delimiter.join(scope), tensor

    def _generate_state_names(self, tensors: list):
        yield from self._generate_tensor_names(
            STATE_NAME_PREFIX,
            tensors,
            '.',
        )

    def _generate_input_names(self, tensors: list):
        yield from self._generate_tensor_names(
            INPUT_NAME_PREFIX,
            tensors,
            '_',
        )

    def _generate_output_names(self, tensors: list):
        yield from self._generate_tensor_names(
            "output",
            tensors,
            '_',
        )

    def mark_output(self, struct, force=False):
        name_mapping = {}
        for name, tensor in self._generate_output_names(struct):
            name_mapping[id(tensor)] = name

        def map_fn(arg):
            if isinstance(arg, torch.Tensor) and (
                arg.device.type == self.torch_device.type
            ):
                name = name_mapping[id(arg)]

                # a reshape to ensure that the mark output gets sent to function mode
                if self._retrace_every_iteration and self.backend_type.is_csx:
                    arg.reshape(arg.size())

                # This might return a new tensor
                # pylint: disable=c-extension-no-member
                return cerebras_pytorch_lib.mark_output_tensor(
                    arg, name=name, force=force
                )

            return arg

        return torch.utils._pytree.tree_map(map_fn, struct)

    ################################################
    #               DataLoader hooks               #
    ################################################

    def initial_mark_step(self, async_compute: bool = True):
        """Run the initial mark step"""
        prev_async = self.device.config.async_parallel_compute
        try:
            self.device.config.async_parallel_compute = async_compute

            if self.device.config.drop_data:
                msg = "Skipping weight initialization"
                if not self.is_e2e_execution:
                    msg += " as the backend was configured for compile/validation only."
                self.logger.info(msg)

            # Sync all functional tensors so that if any of their views
            # were updated inplace, the updates are visible to the original tensor
            # After syncing the tensors, reset the functional storage so that
            # the base tensor is the same as the latest value tensor
            for tensor in self.device.functional_tensors:
                cerebras_pytorch_lib.sync_functional_tensor(tensor)
                cerebras_pytorch_lib.reset_functional_tensor(tensor)

            self.logger.trace("Calling initial mark step")

            # Call initial mark_step to trigger asynchronous lazy initialization
            # pylint: disable=protected-access
            with self.device:
                torch._lazy.mark_step()

            self.logger.trace("Finished initial mark step")

        finally:
            self.device.config.async_parallel_compute = prev_async

    def on_run_start(self):
        self.appliance_tracker.stop("Initialization")

        super().on_run_start()

        # pylint: disable=protected-access,c-extension-no-member
        cerebras_pytorch_lib.get_appliance().artifact_dir = str(
            self.data_executor.artifact_dir
        )
        cerebras_pytorch_lib.set_pol(self.cs_config.precision_opt_level)

        # TODO: only call this if not already initialized
        # initialize automatic mixed precision
        amp_init(verbose=(_amp_state.verbosity == 2))

        # Create the run request to be used in execute
        run_request = RunRequest(
            num_iterations=self.run_context.num_steps,
            checkpoint_freq=self.run_context.checkpoint_steps,
            activation_freq=self.run_context.activation_steps,
            live_dataloaders=list(self._dataloaders.keys()),
            dataloader=RunRequest.DataLoaderConfig(
                id=self.run_context.dataloader.id,
                builder=fw_user_serialize(
                    self.run_context.dataloader.input_fn,
                    name="DataLoader function",
                    from_usr=True,
                ),
                builder_inputs=fw_user_serialize(
                    self.run_context.dataloader.input_fn_params,
                    name="DataLoader input arguments",
                    from_usr=True,
                ),
            ),
        )
        if self.run_context.dataloader.is_restartable:
            state = self.run_context.dataloader.cached_state
            if state == cstorch.utils.data.DataLoader.STATE_UNAVAILABLE:
                raise RuntimeError(
                    "DataLoader state is not available. This can happen when the "
                    "DataExecutor using this DataLoader instance was not fully iterated "
                    "in a previous session or it was stopped at a step other than a "
                    "checkpoint step. To avoid this, please fully iterate the DataExecutor "
                    "from previous sessions."
                )
            elif state != cstorch.utils.data.DataLoader.STATE_UNKNOWN:
                run_request.dataloader.initial_state = fw_user_serialize(
                    state,
                    name="DataLoader state",
                    from_usr=True,
                )

        if self.appliance is None:
            self.appliance = ApplianceMode(
                self.data_executor.artifact_dir,
                self.config.compile_dir,
                self.cs_config,
                checkpoint_reader_cls=CheckpointReader,
                op_profiler_config=self.data_executor.op_profiler_config,
            )

        cerebras_pytorch_lib.set_fp16_type(
            cstorch.amp._amp_state.half_dtype_str
        )

        save_initial_state_future = None
        terminate = Event()

        # Dictionary of all materialized tensors that needs to be send to the appliance.
        initial_state_dict = {}
        # List of all weights that needs to be carried over from previous session to the new one.
        appliance_weights = {}

        def save_initial_state(weights):
            nonlocal save_initial_state_future

            weights_iteration = None

            for weight in weights:
                # We need to carry over only the weights that were not changed beween sessions.
                # If a weight has appliance info, it means that tensor is available in appliance
                # and it was not changed between sessions. Otherwise, modified tensor will replace
                # appliance info with graph info.
                # In case of the first session run, all tensors will be meterialized and will be
                # sent to the appliance within initial ckpt.
                appliance_info = weight.get_appliance_info()
                if not appliance_info:
                    self.logger.debug(
                        f"Weight {weight.name} has materialized tensor: {weight}"
                    )
                    initial_state_dict[weight.name] = weight
                    continue

                if not weight.is_weight:
                    raise RuntimeError(
                        f"Cerebras backend has detected that activation tensor \'{weight.name}\' was reused between sessions which is currently unsupported."
                    )

                if (
                    appliance_info.state
                    != cerebras_pytorch_lib.ApplianceInfoState.InRepo
                ):
                    raise RuntimeError(
                        f"Weight tensor \"{weight.name}\" with tensor_id={appliance_info.uid}, state={appliance_info.state} is not available in the repository, so it can not be carried over to the new session."
                    )

                appliance_info.state = (
                    cerebras_pytorch_lib.ApplianceInfoState.InBuffer
                )
                appliance_weights[weight.name] = appliance_info

            self.logger.debug(
                f"Initialized weights {initial_state_dict.keys()}"
            )
            self.logger.debug(f"Carried over weights {appliance_weights}")

            # Sync initialized weights.
            if initial_state_dict:

                def sync_initialized_weights(weights):
                    try:
                        for name, weight in weights.items():
                            if terminate.is_set():
                                break

                            # Call to wait will raise an exception if file write failed
                            weight.wait()
                    except:
                        if self._compile_appliance is not None:
                            self._compile_appliance.done(wait=True)

                        raise

                    return True

                # TODO: need to compute only necessary weights, not all.
                executor = ThreadPoolExecutor(max_workers=1)
                save_initial_state_future = executor.submit(
                    sync_initialized_weights, initial_state_dict
                )
                # Shutting down without wait allows existing futures to finish
                # before the executor is cleaned up
                executor.shutdown(wait=False)

        # pylint: disable=redefined-builtin
        def compile(
            batch_size: int,
            cirh_str: str,
            weights,
        ) -> bool:
            if self.is_e2e_execution:
                save_initial_state(weights)

            self.logger.info(COMPILE_ONLY_MSG)

            with self.appliance.build_worker_image(
                should_skip=self.compile_only
                or self.validate_only
                or self._has_worker_image
            ):
                try:
                    self._has_worker_image = True

                    compile_hash = None
                    cross_compile_state = None
                    if self.appliance.compile_resp is not None:
                        cross_compile_state = (
                            self.appliance.compile_resp.cross_compile_state
                        )
                        compile_hash = self.appliance.compute_compile_hash(
                            cirh_str, batch_size
                        )

                    if (
                        compile_hash is None
                        or compile_hash not in self._compile_cache
                    ):
                        # Instantiate new ApplianceMode for compile job only.
                        self._compile_appliance = ApplianceMode(
                            self.data_executor.artifact_dir,
                            self.config.compile_dir,
                            self.cs_config,
                            checkpoint_reader_cls=CheckpointReader,
                        )
                        self.appliance.compile_resp = (
                            self._compile_appliance.compile(
                                batch_size,
                                cirh_str,
                                cross_compile_state,
                                self.validate_only,
                            )
                        )
                        if self.appliance.compile_resp is not None:
                            self._compile_cache[
                                self.appliance.compute_compile_hash(
                                    cirh_str, batch_size
                                )
                            ] = self.appliance.compile_resp
                    else:
                        self.appliance.compile_resp = self._compile_cache[
                            compile_hash
                        ]

                    # Check if exists as it won't for system runs
                    if self.appliance.compile_resp and os.path.exists(
                        self.appliance.compile_resp.cache_compile_dir
                    ):
                        create_symlink(
                            self.data_executor.artifact_dir.joinpath(
                                "remote_compile_dir"
                            ),
                            self.appliance.compile_resp.cache_compile_dir,
                        )

                    # Reset the compile appliance so we don't accidentally
                    # use it for anything else.
                    self._compile_appliance = None
                except Exception as e:
                    terminate.set()
                    if save_initial_state_future is not None:
                        raise e from save_initial_state_future.exception()
                    else:
                        raise

            self.logger.info(COMPILE_SUCCESS_MSG)
            return True

        def execute(batch_size: int) -> Set[str]:
            if not self.is_e2e_execution:
                return set()

            self.logger.info(PROGRAMMING_CS_MSG)

            if self.mode is None:
                # This means that the user did not call optimizer.step()
                # So, assume that the user wants to run eval
                self.mode = EVAL

                if self.model and self.model.training:
                    self.logger.warning(
                        "Model is in training mode but no optimizer.step() "
                        "call was detected. The model will be compiled for "
                        "eval mode but numerics may be affected if ops "
                        "like dropout are present in the model."
                    )

            with self.appliance_tracker.entry(
                "Initialization"
            ), self.appliance_tracker.entry("wait_for_init"):
                # This is just a sanity check. It should always be not None if
                # we aren't in compile/validate only
                if save_initial_state_future is not None:
                    self.logger.info(
                        f"Waiting for weight initialization to complete"
                    )
                    assert save_initial_state_future.result()

            self.initial_state_file = None

            if initial_state_dict:
                self.initial_state_file = os.path.join(
                    self.device.device_data_dir,
                    f"initial_state_{self._initial_ckpt_id}.hdf5"
                    if self._initial_ckpt_id
                    else "initial_state.hdf5",
                )
                self._initial_ckpt_id += 1
                assert not os.path.exists(
                    self.initial_state_file
                ), f"Initial checkpoint file {self.initial_state_file} already exists"

                # After all weights were synced (computed) and available, we can
                # save them to the initial checkpoint.
                init_ckpt_dict = {}
                for name, weight in initial_state_dict.items():
                    if weight.is_tensor_available:
                        tensor = lazy_tensor_data_wrapper(weight)
                        if isinstance(tensor, DeferredTensor):
                            # Deferred tensors are created using `torch.empty()`
                            # which allocates virtual memory. But since the empty
                            # storage is never actually accessed in a defered
                            # tensor, we close that storage here to avoid spikes
                            # in virtual memory which may lead to OOM during fork.
                            cerebras_pytorch_lib.close_tensor_storage(tensor)

                        init_ckpt_dict[name] = tensor

                # We intermittently see HDF5 locking failures here. It's not clear what's
                # causing it, but given that `initial_state_file` is guaranteed to be unique
                # and only written to here, disabling file locking is ok.
                saver = PyTorchH5Saver()
                with cstorch.saver.storage.use_external_link(
                    value=True
                ), hdf5_locking(value=False):
                    saver.save(self.initial_state_file, init_ckpt_dict)

                del init_ckpt_dict

                # After we finished weights initialization and saved a checkpoint, we can update
                # weight tensors from the initial state dict with deferred tensors. This will update
                # weights with appliance descriptors to have materialized tensor which means that
                # these tensor won't require fetching from the appliance.
                self.load_deferred_tensors(
                    self.initial_state_file, initial_state_dict
                )

            if self._appliance_execute_cleanup_stack is None:
                self._appliance_execute_cleanup_stack = ExitStack()
                self._appliance_execute_cleanup_stack.__enter__()

            self.appliance.execute(
                run_request,
                self._appliance_execute_cleanup_stack,
                self.initial_state_file,
                appliance_weights,
                send_weights_grouper=None,
            )

            # Manually update the skipped weights
            self.appliance.skipped_weights.update(
                self._param_names
                - initial_state_dict.keys()
                - set(appliance_weights.keys())
            )
            self.logger.debug(
                f"Assigning skipped weights: {self.appliance.skipped_weights}"
            )

            return self.appliance.skipped_weights

        def get_tensor(name, iteration, output_data):
            if self.appliance is None:
                raise RuntimeError(
                    "Trying to fetch tensor from appliance before it is initialized"
                )

            self.logger.debug(
                f"Fetching tensor {name} from the appliance on {iteration=}"
            )

            tensor = self.appliance.receive_output(iteration, name)
            try:
                # Make the tensor writable so that we don't have to copy it
                # in `cstorch.from_numpy()`. Some arrays cannot be modified
                # so we ignore the error and copy the array instead.
                tensor.flags.writeable = True
            except Exception:  # pylint: disable=broad-except
                pass

            tensor = cstorch.from_numpy(tensor)

            # Update ApplianceInfo storage with materialized tensor.
            # This part specifically moved to the python, so we can
            # use device context to avoid dropping the tensor. This
            # may happen when lazy initialization is enabled, so the
            # get_tensor call may outlive device context used for init
            # mark_step.
            with self.device:
                output_data.share_storage(
                    cerebras_pytorch_lib.ApplianceDataInfo(tensor=tensor)
                )

        def delete_tensor(
            appliance_info: cerebras_pytorch_lib.ApplianceDataInfo,
        ):
            if (
                appliance_info.state
                != cerebras_pytorch_lib.ApplianceInfoState.InRepo
            ):
                self.logger.debug(
                    f"Skip deleting tensor with ptid={appliance_info.uid} as it is not in the repository"
                )
                return

            self._tensors_to_remove.add(appliance_info.uid)

        # pylint: disable=c-extension-no-member
        cerebras_pytorch_lib.get_appliance().set_callbacks(
            compile_callback=compile,
            execute_callback=execute,
            get_tensor_callback=get_tensor,
            release_tensor_callback=delete_tensor,
        )

        self.initial_mark_step()

        self.run_step_closures()

        # Before we start the run, we need to move all the tensors that are
        # alive from the previous session to the tensor repository.
        # Note: we need to move tensors to repo only after the initial mark step
        # since some of the tensors may be used by the init computation graph, so
        # we need to keep them alive until this point.
        if self._alive_weights and self.is_e2e_execution:
            for name, uid in self._alive_weights:
                assert (
                    self.appliance is not None
                ), "Appliance is not initialized"

                # If the tensor should be dropped, we don't move, so it gets
                # automatically erased.
                if uid in self._tensors_to_remove:
                    self._tensors_to_remove.remove(uid)
                    continue

                self.appliance.move_to_ptr(name, uid)

            self._alive_weights = None

        if self._tensors_to_remove and self.is_e2e_execution:
            for ptid in self._tensors_to_remove:
                self.appliance.delete_from_ptr(ptid)

            self._tensors_to_remove = set()

        self._param_names = set()

    def on_run_end(self, exec_type=None, exec_value=None, traceback=None):
        if (
            self._appliance_execute_cleanup_stack is not None
            and exec_type is None
        ):
            response = self.appliance.finalize()

            if response.op_profiler_json:
                from cerebras.pytorch.profiler import ProfilerRegistry

                ProfilerRegistry.get_profiler().op_profiler_json = (
                    response.op_profiler_json
                )
                with open(
                    self.data_executor.artifact_dir / "chrome_trace.json", "w"
                ) as text_file:
                    text_file.write(response.op_profiler_json)

        if exec_type:
            self.shutdown_appliance(
                exec_type=exec_type, exec_value=exec_value, traceback=traceback
            )

        # pylint: disable=import-error
        from torch._lazy.closure import AsyncClosureHandler

        async_closure_handler = AsyncClosureHandler()
        if async_closure_handler._closure_queue.qsize() > 0:
            self.logger.info("Waiting for async closures to finish running")
            async_closure_handler._closure_queue.join()

        self.step_closures = []

        # Save all availabe weights so we can later move them to the repo.
        if (
            not exec_type
            and self.appliance is not None
            and self.is_e2e_execution
        ):
            # Move all weight tensors to the persistance tensor repository, so they can be
            # accessed in the next session.
            self._alive_weights = set()
            for appliance_data in cerebras_pytorch_lib.get_cached_output_data():
                appliance_info = appliance_data.get_appliance_info()
                if appliance_data.is_weight and appliance_info is not None:
                    if (
                        appliance_info.state
                        != cerebras_pytorch_lib.ApplianceInfoState.InBuffer
                    ):
                        raise RuntimeError(
                            f"Tensor \"{appliance_data.name}\" with tensor_id={appliance_info.uid}, state={appliance_info.state} is not available in runtime, so it can not be moved to tensor repository."
                        )

                    self._alive_weights.add(
                        (appliance_data.name, appliance_info.uid)
                    )
                    appliance_info.state = (
                        cerebras_pytorch_lib.ApplianceInfoState.InRepo
                    )

        # Cleanup all cached computation and outputs.
        cerebras_pytorch_lib.clear_cached_computation()
        cerebras_pytorch_lib.clear_cached_outputs()

        if not exec_type:
            # In the multisession run we may have a state between sessions where
            # some of the LTC tensors are still alive from previous session, so they
            # can interfere with following session. This happens when autograd is enabled
            # or if some of the python tensors (like loss) hold the reference to the
            # LTC tensors. To avoid this we need to cleanup all tensors before the next session.
            with cerebras_pytorch_lib.MarkStepContextManager(
                cerebras_pytorch_lib.MarkStepType.DUMMY
            ):
                torch._lazy.mark_step()

        super().on_run_end(exec_type, exec_value, traceback)

    def on_batch_start(self, batch):
        batch = super().on_batch_start(batch)

        # Clear amp cache for the next iteration
        # pylint: disable=protected-access
        _amp_state.handle._clear_cache()

        def set_tensor_name(tensors: list, names_generator, is_param):
            for name, tensor in names_generator(tensors):
                # pylint: disable=protected-access,c-extension-no-member
                self.logger.debug(
                    f"Setting name {name} for tensor {cerebras_pytorch_lib.get_tensor_info(tensor)}"
                )
                if cerebras_pytorch_lib.set_parameter_name(tensor, name):
                    if is_param:
                        self._param_names.add(name)
                elif self.run_context.activation_steps == 1:
                    raise RuntimeError(
                        f"Failed to set name \"{name}\" for tensor: "
                        f"{cerebras_pytorch_lib.get_tensor_info(tensor)}"
                    )
                else:
                    # We have a case when some of the tensors in state dict are not accessable
                    # because they store some intermediate lazy tensor but not model parameter.
                    # This is the case for `lr` tensor which we set on every lr_scheduler step and
                    # in case activation frequency > 1 we skip `update_groups` step closure which
                    # sets the CPU `lr` tensor to the optimizer.param_group.
                    self.logger.debug(
                        f"Tensor: ({name}) {cerebras_pytorch_lib.get_tensor_info(tensor)} is not "
                        f"accessible at iteration {self.run_context.user_iteration}"
                    )

        set_tensor_name(batch, self._generate_input_names, False)
        set_tensor_name(self.state_dict(), self._generate_state_names, True)

        for optimizer in self.optimizer_registry:
            if hasattr(optimizer, "_amp_stash"):
                optimizer._amp_stash.dls_update_manager.__enter__()

        return batch

    def on_batch_end(self):
        for optimizer in self.optimizer_registry:
            for lr_scheduler in optimizer._lr_scheduler_registry:
                # The lr_scheduler step should always be one greater than the optimizer
                # step if the lr_scheduler was stepped.
                # If the lr_scheduler was not stepped, we still need to update the group
                # with the scalar values.
                # If an lr_scheduler was not stepped, its probably a user error.
                # But we should still support this behaviour anyways as its
                # supported in eager mode
                if optimizer._step_count >= lr_scheduler._step_count:
                    lr_scheduler.update_groups(lr_scheduler._last_lr)
                if hasattr(optimizer, "_amp_stash") and (
                    self.retrace_every_iteration
                    or self.run_context.is_initial_step
                ):
                    optimizer._amp_stash.dls_update_manager.__exit__()

        for name, tensor in self._generate_state_names(self.state_dict()):
            if name not in self._param_names:
                continue
            # The following set_alias call also marks the tensor as an output.
            # pylint: disable=protected-access,c-extension-no-member
            assert cerebras_pytorch_lib.set_alias(tensor, name), (
                f"failed to set alias {name} for tensor: "
                f"{cerebras_pytorch_lib.get_tensor_info(tensor)}"
            )

        self._update_dataloader_state()

        self._is_tracing = False

        # pylint: disable=import-error
        # Seed the ltc backend for e.g. dropout. This doesn't influence model
        # initialization or dataloader shuffling.
        # Use the initial seed value set via torch.manual_seed()
        cerebras_pytorch_lib.set_rng_state(torch.initial_seed())

        cerebras_pytorch_lib.get_appliance().set_iteration(
            self.run_context.iteration
        )

        # pylint: disable=protected-access
        if self.retrace_every_iteration or self.run_context.is_initial_step:
            self.logger.trace("Calling Mark Step")
            # In case we had no tensors to sync during the initial mark_step,
            # we need to force regular mark_step here.
            with cerebras_pytorch_lib.MarkStepContextManager(
                cerebras_pytorch_lib.MarkStepType.EXECUTION
            ):
                torch._lazy.mark_step()

        # Update the profiler as we have processed a batch. Note that this is
        # done after mark_step so that we don't jump the gun and updated samples
        # processed before compile/execute is actually done.
        if self.run_context.profiler is not None:
            self.run_context.profiler.step(
                self.run_context.dataloader.batch_size
            )

        # Workaround to handle the case when retracing is disabled and appliance info
        # insdie the tensor points to 0 iteration. So we make an assumption that the
        # iteration of the tensor is the same as the current iteration.
        if not self.retrace_every_iteration:
            for appliance_data in cerebras_pytorch_lib.get_cached_output_data():
                appliance_info = appliance_data.get_appliance_info()
                if not appliance_info or appliance_info.allows_updates:
                    # In case if current iteration is different from the iteration of the tensor,
                    # it will reset materialized tensor underneath, so the new tensor will be
                    # fetched from the appliance.
                    appliance_data.iteration = self.run_context.iteration

        self.run_step_closures()

    def setup_model(self, model):
        super().setup_model(model)
        self.shutdown_appliance()

    def forward(self, model, *args, **kwargs):  # pylint: disable=no-self-use
        """Runs the forward pass for the model"""
        return model(*args, **kwargs)

    def set_scope_name(self, scope_name):
        old_scope = super().set_scope_name(scope_name)
        if scope_name is None:
            scope_name = ScopeName()
        cerebras_pytorch_lib.set_scope_name(str(scope_name))
        return old_scope

    def shutdown_appliance(
        self, exec_type=None, exec_value=None, traceback=None
    ):
        """Shutdown the appliance"""
        if self._appliance_execute_cleanup_stack is not None:
            self._appliance_execute_cleanup_stack.__exit__(
                exec_type, exec_value, traceback
            )
            self._appliance_execute_cleanup_stack = None

        self.appliance = None

    def shutdown(self):
        """Shutdown the backend"""
        self.shutdown_appliance()
        cerebras_pytorch_lib.shutdown()

    ###################################################
    #               Training Loop hooks               #
    ###################################################

    def pre_backward(self, loss):
        """Run just before the call to loss.backward()"""
        if self.grad_scaler is not None:
            self.mark_output({"grad_scalar": self.grad_scaler.state_dict()})
        return loss

    #######################################################
    #               Optimizer related hooks               #
    #######################################################

    def setup_optimizer(self, optimizer):
        super().setup_optimizer(optimizer)
        self.post_optimizer_load_state_dict(optimizer)

        optimizer.register_load_state_dict_post_hook(
            self.post_optimizer_load_state_dict
        )

        def set_lr_value(optimizer, args, kwargs):
            # Set the lr value to be the tensor
            for lr_scheduler in optimizer._lr_scheduler_registry:
                lr_scheduler.update_last_lr()

        optimizer.register_step_pre_hook(set_lr_value)

    def post_optimizer_load_state_dict(self, optimizer):
        """
        Post-process the optimizer param groups and state
        after loading the state dict
        """

        def tensor_cast(value):
            if isinstance(value, torch.Tensor) and value.device.type == "lazy":
                # When we load the optimizer state dict, tensors are moved to
                # device. But we don't want to trace param groups. So we move
                # them back to CPU here.
                value = lazy_tensor_data_wrapper(value).to("cpu")
            elif isinstance(value, int):
                value = torch.tensor(value, dtype=torch.int32)
            elif isinstance(value, float):
                value = torch.tensor(value, dtype=torch.float32)
            elif isinstance(value, (list, tuple)):
                value = type(value)(map(tensor_cast, value))
            return value

        # Convert all python scalars in the param groups to 32 bit torch tensors
        # This is because python int/float are represented as 64-bit scalars,
        # whereas compile can only handle 32-bit scalars.
        for param_group in optimizer.param_groups:
            keys = list(param_group.keys())
            for key in keys:
                if key == "params":
                    continue
                value = param_group.pop(key)
                param_group[key] = tensor_cast(value)

        # Make optimizer state tensors into appliance tensors. When we load a
        # normal torch checkpoint, it's loaded onto CPU. But optimizer state
        # needs to be on the device. Note that loading an optimizer state dict
        # replaces the state variables. This is in constrast to loading a model
        # state dict, which updates the state variables using `param.copy_()`.
        def make_appliance(value):
            if isinstance(value, torch.Tensor) and value.device.type != "lazy":
                return value.to(self.device.torch_device)
            return None

        with self.device:
            optimizer.visit_state(make_appliance)

    def setup_grad_scaler(self, grad_scaler):
        super().setup_grad_scaler(grad_scaler)

        with self.device:
            state_dict = {
                name: tensor.to(self.torch_device)
                if isinstance(tensor, torch.Tensor)
                else tensor
                for name, tensor in grad_scaler.state_dict().items()
            }
        grad_scaler.load_state_dict(state_dict)

    def _get_cpu_tensor(self, arg: torch.Tensor):
        """Get a CPU tensor from the appliance"""
        # pylint: disable=c-extension-no-member
        name = cerebras_pytorch_lib.get_tensor_name(arg)

        if cerebras_pytorch_lib.is_weight_tensor(arg):
            raise RuntimeError(
                f"Attempting to get weight tensor \"{name}\" with info "
                f"{cerebras_pytorch_lib.get_tensor_info(arg)} in a step "
                f"closure but this is not supported yet. Please use "
                f"\"cstorch.save()\" API to save model weights."
            )

        # Getting tensor from the appliance may create underlying memory or file backed tensor,
        # so we need to make the following call using device context not to drop the tensor.
        with self.device:
            return cerebras_pytorch_lib.get_appliance_data(arg).tensor

    def set_attribute(
        self,
        tensor: torch.Tensor,
        attribute: str,
        value: Union[bool, int, float, str, list, dict],
    ):
        """
        Adds an attribute to the traced tensor at compile time to communicating
        with the Cerebras Compiler Stack.

        Args:
            tensor: A tensor on the backend device.
            attribute: Name of the attribute to set
            value: Value of the attribute to set.
        """

        # These attributes eventally land in MLIR attributes, potentially on
        # the arguments to the main function. MLIR requires such attributes be
        # scoped to a dialect, so ensure the attribute name is prefixed with
        # `cs.`
        name = "cs." + attribute

        from cerebras.pytorch.lib import cerebras_pytorch_lib

        cerebras_pytorch_lib.set_attribute(tensor, name, value)

    #################################################
    #               Appliance related               #
    #################################################

    def add_step_closure(
        self,
        closure,
        args,
        kwargs,
        run_async: bool = False,
        repeat: bool = False,
    ):
        if hasattr(closure, "__wrapped__"):
            pos_arg_names = inspect.getfullargspec(closure.__wrapped__).args
        else:
            pos_arg_names = inspect.getfullargspec(closure).args

        if len(pos_arg_names) == len(args) and not any(
            pos_arg_name in kwargs for pos_arg_name in pos_arg_names
        ):
            # Use the names of the positional arguments in the step closure as
            # the output name.
            kwargs.update(dict(zip(pos_arg_names, args)))
            kwargs = self.mark_output(kwargs, force=True)
            # Strip positional arguments back out
            args = type(args)(
                kwargs.pop(arg_name) for arg_name in pos_arg_names
            )
        else:
            # Use anonymous positional arguments
            args, kwargs = self.mark_output((args, kwargs), force=True)

        self.step_closures.append((closure, args, kwargs, run_async, repeat))

    def run_step_closures(self):
        step_closures = self.step_closures
        self.step_closures = []

        if self.compile_only or self.validate_only:
            self.logger.debug(
                f"Skipping runnning step closures since backend is configured "
                f"for {'compile' if self.compile_only else 'validate'}_only "
                f"mode."
            )
            return

        # pylint: disable=import-error
        from torch._lazy.closure import AsyncClosureHandler

        async_closure_handler = AsyncClosureHandler()

        for closure, args, kwargs, run_async, repeat in step_closures:
            if self.run_context.is_activation_step:
                # fetching tensors from appliance here
                # pylint: disable=protected-access
                cpu_args, cpu_kwargs = torch.utils._pytree.tree_map(
                    lambda arg: (
                        self._get_cpu_tensor(arg)
                        if isinstance(arg, torch.Tensor)
                        and arg.device.type == self.torch_device.type
                        else arg
                    ),
                    (args, kwargs),
                )

                if run_async:
                    async_closure_handler.run(
                        lambda c=closure, a=cpu_args, k=cpu_kwargs: c(*a, **k)
                    )
                else:
                    closure(*cpu_args, **cpu_kwargs)
            else:
                self.logger.trace(
                    f"Skipping step closure at iteration {self.run_context.user_iteration} as it "
                    f"is not an activation step."
                )

            if repeat:
                self.step_closures.append(
                    (closure, args, kwargs, run_async, repeat)
                )

    def save(self, state_dict, checkpoint_file):
        saver = PyTorchH5Saver()
        flattened, spec = saver.flatten_state_dict(state_dict)
        # save the spec before saving tensors so we know what was
        # intended to be saved, even if something fails
        saver.save_spec(checkpoint_file, spec)

        if not self.data_executor_stack or self.run_context.is_pre_initial_step:
            # If we are on the first step, we don't need to fetch the
            # tensor from the appliance since it is already the initial
            # tensor value (initial weights).
            # pylint: disable=protected-access,c-extension-no-member
            for key, val in flattened.items():
                if isinstance(val, torch.Tensor):
                    val = lazy_tensor_data_wrapper(val)
                saver.save_tensor(checkpoint_file, key, val)
        else:
            # TODO: extract iteration from the tensor appliance data, so we can save checkpoint
            # after the training step is done.
            if not self.in_run_context:
                raise RuntimeError(
                    "Cannot save weights outside of a run context"
                )

            self.appliance.save_weights(
                flattened.items(),
                checkpoint_file,
                self.run_context.iteration,
            )

        # Now do some verification that all the tensors in spec were saved
        saved_tensors = PyTorchH5Saver.tensor_names(checkpoint_file)
        missing = set(flattened.keys()) - set(saved_tensors)

        if (
            self.data_executor_stack
            and not self.run_context.is_pre_initial_step
        ):
            # Don't throw an error for known skipped weights
            missing -= set(self.appliance.skipped_weights)

        if missing:
            missing = ', '.join(missing)
            extras = ", ".join(set(saved_tensors) - set(flattened.keys()))
            if extras:
                extra_str = (
                    f"\nUnexpected weights found in checkpoint are: "
                    f"{extras}."
                )
            else:
                extra_str = ""
            raise RuntimeError(
                f"Not all weights from the state dict were saved to the "
                f"checkpoint file `{checkpoint_file}`. This may point to "
                f"an internal error."
                f"\nWeights missing in checkpoint are: {missing}."
                f"{extra_str}"
            )

        # To avoid excess fetching from the appliance, we udpate appliance info
        # tensors with deferred tensors, so they won't be fetched from the appliance.
        self.load_deferred_tensors(checkpoint_file, state_dict)

    def load_deferred_tensors(self, checkpoint_file, state_dict):
        """
        Load deferred appliance data from checkpoint file into the state dict tensors.
        """
        from cerebras.pytorch.saver import _cstorch_load

        # Since this is rather an internal checkpoint load, we don't want to
        # do extra logging, so we are calling intenal _cstorch_load.
        ckpt_state_dict = _cstorch_load(checkpoint_file, map_location='lazy')

        for name, tensor in state_dict.items():
            if isinstance(tensor, cerebras_pytorch_lib.ApplianceDataInfo):
                appliance_data = tensor
            elif isinstance(tensor, torch.Tensor):
                if tensor.device.type != "lazy":
                    continue
                appliance_data = cerebras_pytorch_lib.get_appliance_data(tensor)
            else:
                continue

            # If tensor is already available there is no need
            # to update the storage with deferred tensor.
            if appliance_data.is_tensor_available:
                continue

            assert (
                name in ckpt_state_dict
            ), f"Tensor {name} is not found in checkpoint {checkpoint_file}"
            ckpt_tensor = ckpt_state_dict[name]
            ckpt_appliance_data = cerebras_pytorch_lib.get_appliance_data(
                ckpt_tensor
            )
            ckpt_appliance_data.tensor_descriptor = (
                appliance_data.tensor_descriptor
            )

            # In case we have appliance info underneath, we update its
            # storage with the deferred tensor, so we can later defferintiate
            # applinace info tensors (that can be carried over between sessions)
            # from the materialized tensors that needs to be send as a part of
            # initial checkpoint.
            # Note: if the tensor with appliance info was modified, so the appliance
            # info will be replaced with graph/file/memory info which means that this
            # tensor will be sent as a part of initial checkpoint and the original
            # tensor inside PTR will be dropped.
            if appliance_info := appliance_data.get_appliance_info():
                appliance_info.share_storage(ckpt_appliance_data)
            else:
                appliance_data.share_storage(ckpt_appliance_data)

    def run_implicit_autoregressive_loop(
        self,
        input_tensor: torch.IntTensor,
        output_tensor: torch.IntTensor,
        loop_dim: int,
        start_token: Union[int, List[int]],
        stop_sequences: List[List[int]],
        max_tokens: Optional[int] = None,
    ) -> torch.IntTensor:
        """
        Experimental implcit autoregressive loop. Configures the runtime inner
        loop via attributes.
        """
        if not isinstance(input_tensor, torch.Tensor):
            raise TypeError(
                f"Expected input_tensor to be a torch Tensor. "
                f"Got: {type(input_tensor)}"
            )
        if not isinstance(output_tensor, torch.Tensor):
            raise TypeError(
                f"Expected output_tensor to be a torch Tensor. "
                f"Got: {type(output_tensor)}"
            )

        if not isinstance(loop_dim, int):
            raise TypeError(
                f"loop_dim must be an integer. Got: {type(loop_dim)}"
            )
        elif not ((1 - input_tensor.dim()) <= loop_dim < input_tensor.dim()):
            raise ValueError(
                f"Expected {1 - input_tensor.dim()} <= loop_dim < "
                f"{input_tensor.dim()}. Got: {loop_dim}"
            )
        if loop_dim < 0:
            loop_dim = input_tensor.dim() - loop_dim
            # This is a sanity check
            assert loop_dim >= 0

        start_tok_err = "start_token must be non-negative integer or list of non-negative integers."
        if isinstance(start_token, list):
            if len(start_token) == 0:
                raise ValueError(f"{start_tok_err} Got empty list")
            for t in start_token:
                if not isinstance(t, int) or t < 0:
                    raise ValueError(f"{start_tok_err} One element was {t}")
        elif not isinstance(start_token, int) or start_token < 0:
            raise ValueError(f"{start_tok_err} Got: {start_token}")
        else:
            start_token = [start_token]

        stop_seq_err = (
            "stop_sequences must be a list of list of non-negative integers."
        )
        if isinstance(stop_sequences, list):
            for seq in stop_sequences:
                if not isinstance(seq, list) or len(seq) == 0:
                    raise ValueError(f"{stop_seq_err} One element was {seq}")
                for tok in seq:
                    if not isinstance(tok, int) or tok < 0:
                        raise ValueError(
                            f"{stop_seq_err} In stop sequence {seq}, one element was {tok}"
                        )
        if (
            max_tokens is not None
            and not isinstance(max_tokens, int)
            or max_tokens < 0
        ):
            raise ValueError(
                f"max_tokens must be a non-negative integer. Got: {max_tokens}"
            )

        autoregressive = {}
        for name, value in (
            ("loop_dim", loop_dim),
            ("start_token", start_token),
            ("stop_sequences", stop_sequences),
            ("max_tokens", max_tokens),
        ):
            if value is not None:
                autoregressive[name] = value
            elif name != "max_tokens":
                raise ValueError(
                    f"Expected {name} to be an integer but got None"
                )
        self.set_attribute(input_tensor, "autoregressive", autoregressive)

        input_name = cerebras_pytorch_lib.get_tensor_name(input_tensor)
        output_name = input_name.replace("input", "autoregressive", 1)
        output_tensor = cerebras_pytorch_lib.mark_output_tensor(
            output_tensor, output_name, force=True
        )
        assert cerebras_pytorch_lib.set_alias(
            output_tensor, input_name, is_weight=False
        ), "Failed to set alias between output and input for autoregressive loop"
        return output_tensor
