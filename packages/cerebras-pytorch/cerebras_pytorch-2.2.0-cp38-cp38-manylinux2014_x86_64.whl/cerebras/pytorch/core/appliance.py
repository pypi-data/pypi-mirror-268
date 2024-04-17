# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Appliance Support For Pytorch"""
import functools
import itertools
import logging
import multiprocessing
import multiprocessing.dummy
import multiprocessing.pool
import sys
from collections import defaultdict
from contextlib import ExitStack
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import dill
import grpc
import torch
from tqdm import tqdm

import cerebras.pytorch as cstorch
from cerebras.appliance.appliance_client import ApplianceClient
from cerebras.appliance.appliance_manager import (
    ApplianceManager,
    TensorGrouper,
    TensorTransferTracker,
)
from cerebras.appliance.cluster.client import ClusterManagementClient
from cerebras.appliance.CSConfig import CSConfig
from cerebras.appliance.errors import (
    ApplianceClientException,
    register_grpc_error_pickler,
)
from cerebras.appliance.pb.framework.appliance_service_pb2 import (
    CompileRequest,
    LoadRequest,
    RunRequest,
    SendCheckRequest,
)
from cerebras.appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
    FrameworkType,
)
from cerebras.appliance.pb.workflow.appliance.common.message_queue_pb2 import (
    ValidTopics,
)
from cerebras.appliance.pb.ws.cross_compile_state_pb2 import CrossCompileState
from cerebras.appliance.run_utils import set_ini
from cerebras.appliance.utils import limit_mp_threads, short_temp_dir
from cerebras.pytorch.backend import current_backend_impl
from cerebras.pytorch.saver.checkpoint_reader import CheckpointReader
from cerebras.pytorch.saver.pt_h5_saver import PyTorchH5Saver
from cerebras.pytorch.saver.storage import lazy_tensor_data_wrapper
from cerebras.pytorch.utils.call_once import call_once
from cerebras.pytorch.utils.nest import serialize_visit_fns


class ApplianceMode(ApplianceManager):
    """Manage pytorch interactions with the appliance"""

    # pylint: disable=signature-differs
    def __init__(
        self,
        artifact_dir: str,
        compile_dir: str,
        cs_config: CSConfig,
        checkpoint_reader_cls=CheckpointReader,
        op_profiler_config: Optional[LoadRequest.OpProfilerConfig] = None,
    ):
        super().__init__(
            cs_config,
            Path(compile_dir),
            Path(artifact_dir),
            FrameworkType.PYTORCH,
            op_profiler_config,
        )

        if (
            cstorch.amp._amp_state.half_dtype_str == "cbfloat16"
            and not self._debug_args.ini.bools["cirh_rewrite_proxy_to_cbfloat"]
        ):
            set_ini(self._debug_args, ws_treat_f16_as_cb16=True)

        self._last_fetched_iteration = 0
        self._compile_resp = None
        self.output_names = []
        self.weight_names = {}
        self._output_name_to_idx = {}
        self.auxilliary_state_names = {}

        self.tracker_execute = current_backend_impl().appliance_tracker

        self.checkpoint_reader_cls = checkpoint_reader_cls

        # A set of rt tensor names that are sparsity masks.
        self._sparsity_mask_names = set()

    def receive_activations(self, iteration: int):
        """Get activations from appliance.

        Args:
            iteration: Iteration to receive activations for. Note that
                activations are received sequentially. So, if this number is
                a few steps ahead of the last iteration that was received, then
                it counts from last fetched iteration up to this iteration, but
                only returns activations for the requested iteration.
        """
        for i in range(iteration, iteration + 1):
            activations = super().receive_activations(i)

            activation_map = dict()
            received_activations = dict()
            for name, tensor in activations.items():
                if name not in self._output_name_to_idx:
                    raise RuntimeError(
                        f"Received activation with name {name} at iteration {i}"
                        f", but no such name has been registered. Expected "
                        f"activation names are: "
                        f"{self._output_name_to_idx.values()}"
                    )
                activation = cstorch.from_numpy(tensor)
                activation_map[self._output_name_to_idx[name]] = activation
                received_activations[name] = activation

        self.tracker_execute.stop("recv_first_activation")
        self.tracker_execute.stop("execute_till_recv_loss")

        return received_activations

    def receive_output(self, iteration, name):
        out = super().receive_output(iteration, name)

        self.tracker_execute.stop("recv_first_activation")
        self.tracker_execute.stop("execute_till_recv_loss")

        return out

    # pylint: disable=arguments-differ
    def compile(
        self,
        batch_size: int,
        cirh_str: str,
        cross_compile_state: Optional[CrossCompileState] = None,
        validate_only: bool = False,
    ):
        """
        Send a compile request to the coordinator
        """
        with self.tracker_execute.entry("compile"):
            with self.tracker_execute.entry("pt_cirh"):
                if validate_only:
                    logging.info("Compile validated locally")
                    return None

                compile_request = CompileRequest(
                    cirh_content=cirh_str,
                    compile_dir=str(self._compile_dir),
                    batch_size=batch_size,
                    num_csx=self._num_csx,
                    max_wgt_servers=self._max_wgt_servers,
                    num_workers_per_csx=self._num_workers_per_csx,
                    max_act_per_csx=self._max_act_per_csx,
                )
                if cross_compile_state is not None:
                    compile_request.cross_compile_state.CopyFrom(
                        cross_compile_state
                    )

            self._compile_resp = super().compile(compile_request)
        return self._compile_resp

    @property
    def compile_resp(self):
        return self._compile_resp

    @compile_resp.setter
    def compile_resp(self, compile_resp):
        self._compile_resp = compile_resp

    @call_once()
    def execute_prep(self, cleanup_stack: ExitStack):
        """Prepare for execution"""
        with self.tracker_execute.entry("execute_prep_details"):
            mgmt_client = cleanup_stack.enter_context(
                ClusterManagementClient(
                    tracker_execute=self.tracker_execute,
                    **self._mgmt_client_args,
                )
            )
            response = self.request_execute_job(mgmt_client, self._compile_resp)
            self.stage_execute_coordinator(response)

            cleanup_stack.enter_context(self.subscribe(ValidTopics.STALL))

            # From this point on, if we error out, we try to do a clean exit
            cleanup_stack.enter_context(
                self.clean_shutdown(mgmt_client, response['job_id'])
            )

        with self.tracker_execute.entry("execute_init_transfer_setup"):
            self.initialize_servers()

    def execute_session(
        self,
        initial_checkpoint_file: Optional[str] = None,
        appliance_weights: Optional[
            Dict[str, "cerebras_pytorch_lib.ApplianceInfo"]
        ] = None,
        send_weights_grouper: Optional[TensorGrouper] = None,
    ):
        """Prepares weights and starts execution

        Args:
            initial_checkpoint_file: Saved checkpoint values to initialize model on appliance.
            appliance_weights: List of weights that need to be carried over from PTR.
            send_weights_grouper: Callable to process TensorSendPayloads into TensorGroups
        """
        tensor_rt_groups = self.grpc_client.send_check(
            0, info_type=SendCheckRequest.InfoType.GROUP
        )

        initial_weights = list(
            self._weight_iterator([initial_checkpoint_file])
            if initial_checkpoint_file
            else []
        )
        appliance_weights = appliance_weights or {}

        rt_initial_weights = set(
            self._map_wgt_name_fw_to_rt(fw_name)
            for fw_name, _ in initial_weights
        )

        rt_appliance_weights = {
            self._map_wgt_name_fw_to_rt(fw_name): info
            for fw_name, info in appliance_weights.items()
        }

        self._sparsity_mask_names = set()

        skipped_weights = set()

        for group in tensor_rt_groups:
            tensor_names = group.tensor_names
            if len(tensor_names) <= 1:
                continue

            # Make an assumption that first tensor in the group is a sparsity mask
            sparsity_mask, weights = tensor_names[0], tensor_names[1:]
            self._sparsity_mask_names.add(sparsity_mask)

            # Check if all tensors from the group are either in initial checkpoint or in the appliance,
            # otherwise, we need to send all tensors from the group to the appliance.
            if all([name in rt_initial_weights for name in tensor_names]):
                continue

            if all([name in rt_appliance_weights for name in tensor_names]):
                # We do not carry over sparsity mask if it wasn't changed.
                skipped_weights.add(sparsity_mask)
                del appliance_weights[sparsity_mask]
                continue

            # SW-115883: Support sparsity algorithm change or weights change by moving the weights
            # from the appliance_weight to initial_checkpoint (create if doesn't exist).
            if any(
                name in self._sparsity_mask_names for name in rt_initial_weights
            ):
                raise RuntimeError(
                    "Detected sparsity algorithm change between different DataExecutor "
                    "instances, which is currently not supported. Please ensure apply the "
                    "same sparsity algorithm to the model once and not change it."
                )

            raise RuntimeError(
                f"Modifying weight between DataExecutor instances when sparsity is enabled "
                f"is currently not supported. Changed weights are: {list(initial_weights)}"
            )

        appliance_weights = (
            [(name, info.uid) for name, info in appliance_weights.items()]
            if appliance_weights
            else []
        )

        return super().execute_session(
            [initial_checkpoint_file] if initial_checkpoint_file else [],
            appliance_weights,
            skipped_weights,
            send_weights_grouper,
        )

    def execute(
        self,
        run_request: RunRequest,
        cleanup_stack: ExitStack,
        initial_checkpoint_file: Optional[str] = None,
        appliance_weights: Optional[
            Dict[str, "cerebras_pytorch_lib.ApplianceInfo"]
        ] = None,
        send_weights_grouper: Optional[TensorGrouper] = None,
    ):
        """Run a model on the appliance"""
        self.tracker_execute.start("execute_till_recv_loss")

        self.execute_prep(cleanup_stack)
        with self.tracker_execute.entry("execute_init_transfer_setup"):
            self.initialize_session(
                run_request,
                self._compile_resp,
            )
            self.execute_session(
                initial_checkpoint_file,
                appliance_weights,
                send_weights_grouper,
            )

        self.tracker_execute.start("recv_first_activation")

    def move_to_ptr(self, tensor_name: str, tensor_id: int) -> None:
        """Move a tensor to PTR which makes is available for the next session."""
        rt_name = self._map_wgt_name_fw_to_rt(tensor_name)
        if rt_name in self._sparsity_mask_names:
            self.logger.debug(
                f"Skip moving to PTR {tensor_name=}, {tensor_id=} as it is a sparsity mask"
            )
            return
        return super().move_to_ptr(rt_name, tensor_id)

    def construct_debug_args(self) -> DebugArgs:
        debug_args = super().construct_debug_args()

        # Populate the visit_fn_map in the debug_args so that they
        # can be propagated to the workers
        for (
            serialized_types,
            serialized_visit_fn,
        ) in serialize_visit_fns().items():
            debug_args.debug_wrk.visit_fn_map[
                serialized_types
            ] = serialized_visit_fn

        return debug_args

    def compute_compile_hash(self, cirh_str: str, batch_size: int):
        """
        Compute the hash for the compile request. When modifying this function,
        please make sure that the hashing logic is in sync with logic in CRD.
        Note that the purpose of this function is to define a compile hash
        which is going to be used only locally (within this process), so we
        doesn't include static information (like fabric info, release id, etc.)
        to compute the hash.
        """
        checksum = [
            cirh_str,
            self._debug_args.debug_crd.stop_compile_at,
            self._debug_args.debug_crd.autogen_policy,
            self._debug_args.debug_crd.numeric_config,
            self._debug_args.debug_crd.disable_ws_incremental_compile,
            self._debug_args.debug_crd.disable_autogen_leftover_conversion,
            self._num_csx,
            batch_size,
            self._max_wgt_servers,
            self._max_act_per_csx,
            self._compile_resp.cross_compile_state,
        ]
        return hash("".join([str(item) for item in checksum]))

    @property
    def _checkpoint_reader_cls(self):
        return self.checkpoint_reader_cls

    def _map_wgt_name_fw_to_rt(self, tensor_name):
        if tensor_name in self.weight_names:
            return self.weight_names[tensor_name]
        if tensor_name in self.auxilliary_state_names:
            return self.auxilliary_state_names[tensor_name]
        return tensor_name

    def save_weights(
        self,
        weights: List[Tuple[str, Union[torch.Tensor, Any]]],
        file_name: str,
        iteration: int,
        fetch_only: bool = False,
    ) -> None:
        """Request weights from appliance and save to the file_name.

        Args:
            weights: List of weights to save. Each weight is a tuple of the
                weight name and the tensor (or other objects) to fetch from
                the appliance and save.
            file_name: Name of the file to save the weights to.
            iteration: Appliance iteration number to save the weights for.
            fetch_only: If True, forces weights fetching from the appliance.
        """

        def get_parameter_name(tensor):
            if (
                isinstance(tensor, torch.Tensor)
                and tensor.device.type == "lazy"
            ):
                from cerebras.pytorch import cerebras_pytorch_lib

                # pylint: disable=c-extension-no-member
                # pylint: disable=no-member
                return cerebras_pytorch_lib.get_tensor_name(tensor)
            return getattr(tensor, "_parameter_name", None)

        def get_tensors():
            seen_weights = set()

            # Create a map between the weight name and the external name
            # to handle duplicate weights
            alias_map = defaultdict(list)
            for external_name, obj in weights:
                parameter_name = get_parameter_name(obj)
                if parameter_name is not None:
                    # pylint: disable=protected-access
                    alias_map[parameter_name].append(external_name)

            # external_name: The name seen by the user (what's saved in ckpt)
            # weight_name: The name of the weight in the model
            # tensor_name: The name of the weight seen by the appliance
            for external_name, obj in weights:
                ckpt_indices = [external_name]

                weight_name = get_parameter_name(obj)
                if weight_name is not None:
                    ckpt_indices.extend(
                        alias
                        for alias in alias_map[weight_name]
                        if alias != external_name
                    )
                else:
                    weight_name = external_name

                if weight_name in seen_weights:
                    continue
                else:
                    seen_weights.add(weight_name)

                tensor_name = None

                if isinstance(obj, torch.Tensor):
                    tensor_name = self.weight_names.get(weight_name)

                    if weight_name in self.skipped_weights:
                        logging.debug(f"Not fetching skipped: {weight_name}")
                        if obj.device.type == "lazy":
                            obj = lazy_tensor_data_wrapper(obj)
                        tensor_name = None
                    elif tensor_name is None and obj.device.type == "lazy":
                        tensor_name = weight_name

                    if tensor_name is None:
                        logging.debug(
                            f"Saving tensor {external_name} to indices: {ckpt_indices}"
                        )
                        # Save the object as is
                        yield None, ckpt_indices, obj
                    else:
                        logging.debug(
                            f"Fetching {tensor_name} and saving to indices: {ckpt_indices}"
                        )
                        # Fetch tensor before saving
                        yield tensor_name, ckpt_indices, None
                elif fetch_only:
                    logging.debug(
                        f"Fetching {weight_name} and saving to indices: {ckpt_indices}"
                    )
                    # Fetch tensor before saving
                    yield weight_name, ckpt_indices, None
                else:
                    logging.debug(
                        f"Saving object {external_name} to indices: {ckpt_indices}"
                    )
                    # Save the object as is
                    yield None, ckpt_indices, obj

        recv_tensors = list(get_tensors())

        # Build unique tensor names for validating.
        recv_tensor_names = {name for name, _, _ in recv_tensors}

        # Some related tensors should be requested together to minimize peak
        # memory. Each tensor is independent from the other tensors; the
        # grouping is just to control the fetch order.
        recv_groups = []

        # self.recv_groups is a (possibly empty) list of list of tensor names.
        if self.recv_groups:
            # Build a lookup from tensor_name->(tensor_name, indices, obj)
            # the `None` key will have overlaps, but thats fine. All tensors
            # with a name are guaranteed unique.
            recv_tensor_dict = {t[0]: t for t in recv_tensors}

            # For each group of tensor names, build a matching "group" of
            # recv_tensor input (tuples of (name, indices, obj) )
            for group in self.recv_groups:
                recv_group = []
                for tensor_name in group:
                    inputs = recv_tensor_dict.get(tensor_name, None)
                    if inputs is not None:
                        # Move from global recv list to this group.
                        recv_tensors.remove(inputs)
                        recv_group.append(inputs)
                recv_groups.append(recv_group)

        # Each remaining tensor (maybe all of them) is its own group.
        recv_groups.extend([t] for t in recv_tensors)

        transfer_tracker = TensorTransferTracker()

        with self.tracker_execute.entry(
            "Retrieve and Save weights"
        ), limit_mp_threads():
            if self._transfer_threads > 1:
                ctx = multiprocessing.get_context('spawn')
                pool_cls = functools.partial(
                    multiprocessing.pool.Pool,
                    context=ctx,
                )
            else:
                ctx = multiprocessing.get_context()
                pool_cls = multiprocessing.dummy.Pool
            with short_temp_dir():
                m = ctx.Manager()
            lock = m.Lock()
            with cstorch.saver.storage.use_cstorch_types(True), pool_cls(
                processes=self._transfer_threads,
                initializer=WeightReceiver.initializer,
                initargs=(
                    self._coord_address,
                    self._certificate_bytes,
                    self._default_authority,
                    file_name,
                    iteration,
                    lock,
                ),
            ) as pool:
                try:
                    iter_recv = itertools.chain.from_iterable(
                        pool.imap_unordered(WeightReceiver.runner, recv_groups)
                    )
                    for pkl in tqdm(
                        iter_recv,
                        total=len(recv_tensor_names),
                        desc="Transferring weights from server",
                        dynamic_ncols=True,  # Match console width
                        unit=" tensors",
                        file=sys.stdout,
                        disable=None,  # Disable on non-TTY
                    ):
                        tensor_name, outcome = WeightReceiver.deserialize(pkl)
                        transfer_tracker.add(tensor_name, outcome)
                except ApplianceClientException as ex:
                    raise ex

            transfer_tracker.validate(recv_tensor_names)


class WeightReceiver:
    """A class to use in a multiprocessing context for receiving weights."""

    impl: Optional["WeightReceiver"] = None

    def __init__(
        self,
        coord_address,
        certificate_bytes: Optional[bytes],
        default_authority,
        file_name,
        iteration,
        lock,
    ):
        """Constructs a `WeightReceiver` instance.

        Args:
            coord_address: Address of the coordinator to send to.
            certificate_bytes: Optional PEM encoded certificate byte string for
                grpc secure channel setup.
            default_authority: Authority to authorize communication.
        """
        credentials = None
        if certificate_bytes:
            credentials = grpc.ssl_channel_credentials(certificate_bytes)

        self._grpc_client = ApplianceClient(
            coord_address,
            credentials=credentials,
            default_authority=default_authority,
        )

        self._file_name = file_name
        self._iteration = iteration
        self._writer_lock = lock

        # Add pickling support to exceptions so that they include their
        # traceback
        from tblib import pickling_support

        pickling_support.install()

        # gRPC exceptions are not picklable by default. Register custom picklers
        # so they can be properly pickled to be sent across processes.
        register_grpc_error_pickler()

    def __call__(self, inputs):
        """Sends the given tensor through gRPC to appliance service."""
        tensor_name = "Unknown"
        ckpt_indices = []
        try:
            tensor_name, ckpt_indices, tensor = inputs
            if tensor_name is not None:
                tensor = self._grpc_client.recv_output(
                    self._iteration, tensor_name
                )

                try:
                    # Make the tensor writable so that we don't have to copy it
                    # in `cstorch.from_numpy()`. Some arrays cannot be modified
                    # so we ignore the error and copy the array instead.
                    tensor.flags.writeable = True
                except Exception:  # pylint: disable=broad-except
                    pass

                tensor = cstorch.from_numpy(tensor)
            with self._writer_lock:
                saver = PyTorchH5Saver()
                saver.save_tensor(self._file_name, ckpt_indices[0], tensor)
                saver.create_links(
                    self._file_name, ckpt_indices[0], ckpt_indices[1:]
                )

            return WeightReceiver.serialize((tensor_name, True))
        except Exception as e:  # pylint: disable=broad-except
            return WeightReceiver.serialize((tensor_name, e))

    @staticmethod
    def serialize(val):
        """Generic serialization using dill."""
        return dill.dumps(val)

    @staticmethod
    def deserialize(pkl_val):
        """Generic de-serialization method using dill."""
        return dill.loads(pkl_val)

    @staticmethod
    def initializer(*args, **kwargs):
        """The initializer to use in multiprocessing."""
        WeightReceiver.impl = WeightReceiver(*args, **kwargs)

    @staticmethod
    def runner(group):
        """The runner method to use in multiprocessing."""
        assert WeightReceiver is not None, "Initializer must be called."
        # pylint: disable=not-callable
        return [WeightReceiver.impl(inputs) for inputs in group]
