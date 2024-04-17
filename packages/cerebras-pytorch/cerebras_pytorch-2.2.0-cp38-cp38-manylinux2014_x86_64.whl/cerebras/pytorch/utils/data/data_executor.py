# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""The executor used to configure the run"""
import math
from contextlib import ExitStack, nullcontext
from pathlib import Path
from threading import Event
from typing import Dict, List, Literal, Optional, Type, Union

from cerebras.appliance.CSConfig import CSConfig
from cerebras.appliance.log import ClassLogger, named_class_logger
from cerebras.appliance.pb.framework.appliance_service_pb2 import LoadRequest
from cerebras.appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
)
from cerebras.appliance.run_utils import clear_ini, set_ini
from cerebras.appliance.utils.file import create_symlink
from cerebras.pytorch.backend import current_backend_impl
from cerebras.pytorch.experimental.listener import (
    BaseTensorListener,
    ListenerMode,
)
from cerebras.pytorch.profiler import ProfilerRegistry
from cerebras.pytorch.utils.tensorboard import SummaryWriter
from cerebras.pytorch.utils.utils import UNSPECIFIED

from ..profiler import Activity, Profiler
from .dataloader import DataLoader

# Type hint for micro_batch_size settings
MbsSetting = Union[
    None, int, Literal["explore", "auto"], Dict[str, Dict[str, int]]
]


@named_class_logger
class DataExecutor(ClassLogger):
    """Defines a single execution run on a Cerebras wafer scale cluster"""

    # pylint: disable=super-init-not-called
    def __init__(
        self,
        dataloader: DataLoader,
        num_steps: Optional[int] = None,
        checkpoint_steps: Optional[int] = None,
        activation_steps: Optional[int] = None,
        cs_config: Optional[CSConfig] = None,
        writer: Optional[SummaryWriter] = None,
        profiler_activities: Optional[List[Type[Activity]]] = None,
        listeners: Optional[List[BaseTensorListener]] = None,
        micro_batch_size: MbsSetting = UNSPECIFIED,
    ):
        """
        Args:
            dataloader: the dataloader to use for the run
            num_steps: the number of steps to run. Defaults to 1 if the backend
                was configured for compile or validate only
            checkpoint_steps: the interval at which to schedule fetching
                checkpoints from the cluster
            activation_steps: the interval at which to schedule fetching
                activations from the cluster
            cs_config: optionally, a
                :py:class:`~cerebras.pytorch.utils.CSConfig` object can be passed
                in to configure the cerebras wafer-scale cluster. if none provided
                the default configuration values will be used.
            writer: The summary writer to be used to write any summarized
                scalars or tensors to tensorboard
            profiler_activities: The list of activities to profile.
                By default the total samples, the client side rate and global
                rate are tracked and accessible via the profiler attribute
            micro_batch_size: Micro-batch size settings for tiling input data. This setting can
                only be specified in CSX runs and defaults to "auto".
                See :ref:`automatic_batch_exploration` for more details.
        """
        self.dataloader = dataloader

        self.backend = current_backend_impl()

        self.listener_mode = ListenerMode(listeners)

        self.op_profiler_config = None
        self._artifact_dir: Optional[Path] = None

        if cs_config is not None:
            if not isinstance(cs_config, CSConfig):
                raise TypeError(
                    f"Expected cs_config to be a CSConfig object. "
                    f"Got: {type(cs_config)}"
                )
        else:
            cs_config = CSConfig()

        if writer is not None and not isinstance(writer, SummaryWriter):
            raise TypeError(
                f"Expected writer to be a "
                f"cstorch.utils.tensorboard.SummaryWriter object. "
                f"Got: {type(writer)}"
            )

        if not self.backend.is_e2e_execution:
            if num_steps and num_steps > 1:
                self.logger.warning(
                    "Specified num_steps > 1 when backend was configured "
                    "for compile/validate only. Setting num_steps to 1."
                )
            num_steps = 1
        elif num_steps is None:
            # If num_steps is not specified, we will try to infer the number of
            # steps from the dataloader.
            try:
                num_steps = len(dataloader)
            except TypeError:
                # Dataset length is not known
                raise RuntimeError(
                    "Could not infer the number of steps as the length of the "
                    "dataloader is not known. Please provide num_steps to the data executor"
                )
        elif num_steps < 1:
            raise RuntimeError(f"Expected num_steps >= 1, but got {num_steps}.")

        if self.backend.is_csx:
            if (
                self.backend._deprecated_micro_batch_size is not UNSPECIFIED
                and micro_batch_size is not UNSPECIFIED
            ):
                raise ValueError(
                    "Please refrain from specifying `micro_batch_size` in both the backend and "
                    "the DataExecutor. Make sure to only specify this option when creating the "
                    "DataExecutor."
                )
            elif self.backend._deprecated_micro_batch_size is not UNSPECIFIED:
                micro_batch_size = self.backend._deprecated_micro_batch_size

            if micro_batch_size is UNSPECIFIED:
                micro_batch_size = "auto"

            sanitized_mbs = _apply_mbs_setting(
                micro_batch_size, cs_config.debug_args
            )
            if (
                sanitized_mbs == "explore"
                and not self.backend.config.compile_only
            ):
                raise ValueError(
                    "Setting micro_batch_size == 'explore' is only "
                    "supported in compile_only mode."
                )
        elif micro_batch_size not in [UNSPECIFIED, None]:
            raise ValueError(
                "`micro_batch_size` is a valid option only for the CSX backend."
            )

        op_profiler_config = ProfilerRegistry.get_profiler()
        # For the models authored by the user, op_profiler_config would be
        # None, if profiling was not asked for.
        if op_profiler_config is not None:
            [start_step, end_step] = op_profiler_config.schedule()
            # For modelzoo models, the default value of -1 means that the
            # profiling was not asked for.
            if start_step != -1:
                if self.backend.is_csx:
                    if num_steps >= end_step >= start_step >= 1:
                        self.op_profiler_config = LoadRequest.OpProfilerConfig()
                        self.op_profiler_config.start_step = start_step
                        self.op_profiler_config.end_step = end_step
                    else:
                        raise ValueError(
                            f"profiling step range should be between 1 and {num_steps}, instead it is {start_step}:{end_step}"
                        )
                elif start_step >= 0:
                    raise RuntimeError(f"Only CSX backend can be profiled")

        def check_steps(name, value, lowerbound):
            if value is not None:
                if not isinstance(value, int):
                    raise TypeError(
                        f"Expected {name} to be have \"int\" or \"None\" type. "
                        f"Got: \"{type(activation_steps)}\""
                    )
                if not (
                    value >= lowerbound
                ):  # pylint: disable=superfluous-parens
                    raise RuntimeError(
                        f"Expected {name} to be an integer >= {lowerbound} or \"None\". "
                        f"Got: {value}"
                    )

        # Validate steps parameters
        check_steps("activation_steps", activation_steps, 1)
        check_steps("checkpoint_steps", checkpoint_steps, 0)

        # Sync activation steps with checkpoint steps.
        if activation_steps and checkpoint_steps:
            aligned_activation_steps = math.gcd(
                checkpoint_steps, activation_steps
            )
            if aligned_activation_steps != activation_steps:
                self.logger.warning(
                    f"Activation frequency was reduced from {activation_steps} to "
                    f"{aligned_activation_steps} because of checkpoint_steps ({checkpoint_steps}). "
                    f"This is because some activations may be accessed at checkpoint steps."
                    f"To avoid the reduction make sure that checkpoint_step % activation_steps == 0"
                )
                activation_steps = aligned_activation_steps

        # Limit activation and checkpoint steps to total steps
        if activation_steps:
            activation_steps = min(num_steps, activation_steps)
        if checkpoint_steps:
            checkpoint_steps = min(num_steps, checkpoint_steps)

        self.run_context = RunContext(
            dataloader,
            num_steps,
            checkpoint_steps,
            activation_steps,
            cs_config,
            writer,
            profiler_activities,
        )

    def __len__(self) -> int:
        return len(self.run_context)

    @property
    def iteration(self) -> int:
        """Returns the current 0-indexed step that the executor is on."""
        return self.run_context.iteration

    @property
    def user_iteration(self) -> int:
        """Returns the current 1-indexed step that the executor is on."""
        return self.run_context.user_iteration

    @property
    def on_final_iteration(self) -> bool:
        """Returns whether the executor is on the final step."""
        return self.run_context.is_final_step

    @property
    def profiler(self) -> Optional[Profiler]:
        """Returns the profiler object, if it exists."""
        return self.run_context.profiler

    @property
    def writer(self) -> Optional[SummaryWriter]:
        """Returns the writer object, if it exists."""
        return self.run_context.writer

    @property
    def cs_config(self) -> CSConfig:
        """Returns CsConfig object"""
        return self.run_context.cs_config

    @property
    def artifact_dir(self) -> Path:
        """Returns the artifact directory of the executor."""
        if self._artifact_dir is None:
            raise RuntimeError(
                "DataExecutor must be iterated before having an artifact directory."
            )
        return self._artifact_dir

    def _setup_artifact_dir(self):
        """Sets up the artifact directory of this executor."""

        def _get_executor_dir(name) -> Path:
            if isinstance(name, int):
                name = f"{name:06d}"
            return Path(self.backend.artifact_dir) / "executors" / name

        self.backend.executor_counter += 1
        self._artifact_dir = _get_executor_dir(self.backend.executor_counter)
        self._artifact_dir.mkdir(parents=True, exist_ok=True)

        latest_symlink = _get_executor_dir("latest")
        create_symlink(
            latest_symlink,
            Path(self._artifact_dir).relative_to(latest_symlink.parent),
        )

    def __enter__(self):
        self._setup_artifact_dir()
        self.backend.data_executor_stack.append(self)
        self.backend.register_dataloader(self.dataloader)
        self.run_context.__enter__()

    def __exit__(self, *args):
        self.run_context.__exit__(*args)
        self.backend.data_executor_stack.pop()

    def __iter__(self):
        with self:

            def get_batches():
                while True:
                    iterable = iter(self.dataloader)
                    try:
                        batch = next(iterable)
                    except StopIteration:
                        raise RuntimeError(
                            "Iterating the dataloader did not return any values. "
                            "This is possibly because the dataset is too small "
                            "for the specified batch_size or drop_last settings. "
                            "Please make sure that the dataloader is able to generate "
                            "at least one batch."
                        )

                    yield batch

                    if self.backend.backend_type.is_csx:
                        while True:
                            yield batch

                    try:
                        while True:
                            yield next(iterable)
                    except StopIteration:
                        # If the iterable is exhausted, we need to start again
                        pass

            for _step, batch in zip(self.run_context, get_batches()):
                ctx = self.listener_mode or nullcontext()
                with ctx:
                    yield self.backend.on_batch_start(batch)
                self.backend.on_batch_end()


def current_executor() -> DataExecutor:
    """Returns current data executor"""
    return current_backend_impl().data_executor


class RunContext:
    """Defines a single run of the appliance"""

    def __init__(
        self,
        dataloader: DataLoader,
        num_steps: int,
        checkpoint_steps: Optional[int] = None,
        activation_steps: Optional[int] = None,
        cs_config: Optional[CSConfig] = None,
        writer: Optional[SummaryWriter] = None,
        profiler_activities: Optional[List[Type[Activity]]] = None,
    ):
        self.backend = current_backend_impl()

        if not isinstance(dataloader, DataLoader):
            raise TypeError(
                "Detected that dataloader was not wrapped using a "
                "cstorch.utils.data.DataLoader.\n"
                "Please wrap your dataloader in a Cerebras Dataloader:\n\n"
                "\tdataloader = cstorch.utils.data.DataLoader(input_fn, ...)\n\n"
                "where `input_fn` is a callable that returns a PyTorch dataloader. "
                "For more details, please see the documentation for "
                "cstorch.utils.data.DataLoader."
            )

        self.dataloader = dataloader
        self.num_steps = num_steps
        self.checkpoint_steps = checkpoint_steps or 0
        self.activation_steps = activation_steps or 1

        # Event that keeps track of whether tracing has occurred
        self.traced = Event()

        self.cs_config = cs_config if cs_config else CSConfig()

        self.writer = writer

        self.step = -1
        self.cleanup_stack = None

        self.profiler: Optional[Profiler] = None
        self.profiler_activities = profiler_activities

    @property
    def is_pre_initial_step(self) -> bool:
        """Returns true if the current step less than zero"""
        return self.step < 0

    @property
    def is_initial_step(self) -> bool:
        """Returns true if the current step is zero"""
        return self.step == 0

    @property
    def is_final_step(self) -> bool:
        """Returns true if the current step is the final step"""
        return self.user_iteration >= self.num_steps

    @property
    def is_checkpoint_step(self) -> bool:
        """Returns true if the current step is a checkpoint step"""
        return self.checkpoint_steps and (
            self.user_iteration % self.checkpoint_steps == 0
            or self.is_final_step
        )

    @property
    def is_activation_step(self) -> bool:
        """Returns true if the current step is an activation step

        Technically when iteration = 0 the condition iteration % freq == 0 is true, however on the
        appliance side the activation is not available. To have correct iteration indexing we need
        to check that user_iteration % activation_steps == 0, where user_itaration = iteration + 1,
        otherwise in case we have 4 iterations [0, 1, 2, 3] and activation_steps = 2 we will get
        only one activation from the iteration=2, however we should return activations from
        iterations [1, 3].
        """
        assert self.activation_steps > 0  # Already validated in the constructor
        return (
            self.user_iteration % self.activation_steps == 0
            or self.is_final_step
        )

    @property
    def iteration(self) -> int:
        """Returns current step"""
        return self.step

    @property
    def user_iteration(self) -> int:
        """Returns user facing iteration number"""
        return self.step + 1

    def __len__(self) -> int:
        return self.num_steps

    def __enter__(self):
        self.step = -1  # set step < 0 before the run starts
        self.backend.on_run_start()
        self.step = 0  # set step to 0 as we enter the context
        self.cleanup_stack = ExitStack()
        self.cleanup_stack.__enter__()

        if self.backend.is_e2e_execution:
            self.profiler = Profiler(
                outdir=self.backend.data_executor.artifact_dir,
                activities=self.profiler_activities,
            )
            self.profiler.__enter__()

    def __exit__(self, *args):
        self.cleanup_stack.__exit__(*args)
        self.backend.on_run_end(*args)
        self.cleanup_stack = None

        if self.profiler is not None:
            self.profiler.__exit__(*args)

    def __iter__(self):
        # sanity check as the user should never use RunContext directly
        assert self.cleanup_stack is not None

        while self.step < self.num_steps:
            yield self.step
            self.step += 1

            if self.backend.retrace_every_iteration:
                self.traced.clear()


def _apply_mbs_setting(
    micro_batch_size: MbsSetting, debug_args: DebugArgs
) -> MbsSetting:
    """Apply micro batch size settings to the debug arg."""
    error_msg = (
        f'Invalid value "{micro_batch_size}" for "micro_batch_size". Expected one of:'
        f'\n\t"auto": Automatically choose an optimal micro batch size.'
        f'\n\t"explore": Search for an optimal micro batch size and return.'
        f'\n\t{{"explore": {{"min": Optional[<positive_int>], "max": Optional[<positive_int>]}}}}: '
        'Search for an optimal micro batch size within the min and max bounds and return.'
        f"\n\t<positive_int>: Use this micro batch size."
        f"\n\tNone: Disable micro batch tiling."
    )

    # First clear any INIs already set
    clear_ini(
        debug_args,
        "ws_opt_disable_grad_accum",
        "ws_opt_explore_batch_sizes",
        "ws_opt_batch_exploration_min_micro_batch",
        "ws_opt_batch_exploration_max_micro_batch",
        "ws_opt_force_min_grad_accum_batch",
        "ws_opt_force_max_grad_accum_batch",
    )

    set_ini(debug_args, ws_opt_disable_grad_accum=micro_batch_size is None)

    if micro_batch_size is None:
        # Already handled above, nothing to do here
        pass
    elif isinstance(micro_batch_size, str):
        if micro_batch_size == "auto":
            # Already handled above, nothing to do here
            pass
        elif micro_batch_size == "explore":
            set_ini(
                debug_args,
                ws_opt_explore_batch_sizes=True,
            )
        else:
            raise ValueError(error_msg)
    elif isinstance(micro_batch_size, dict):
        if isinstance(micro_batch_size.get("explore"), dict):
            set_ini(
                debug_args,
                ws_opt_explore_batch_sizes=True,
            )
            if "min" in micro_batch_size["explore"]:
                min_micro_batch = micro_batch_size["explore"]["min"]
                set_ini(
                    debug_args,
                    ws_opt_batch_exploration_min_micro_batch=min_micro_batch,
                )
            if "max" in micro_batch_size["explore"]:
                max_micro_batch = micro_batch_size["explore"]["max"]
                set_ini(
                    debug_args,
                    ws_opt_batch_exploration_max_micro_batch=max_micro_batch,
                )
            micro_batch_size = "explore"
        else:
            raise ValueError(error_msg)
    elif isinstance(micro_batch_size, int):
        if micro_batch_size > 0:
            set_ini(
                debug_args,
                ws_opt_force_max_grad_accum_batch=micro_batch_size,
            )
            set_ini(
                debug_args,
                ws_opt_force_min_grad_accum_batch=micro_batch_size,
            )
        else:
            raise ValueError(error_msg)
    else:
        raise ValueError(error_msg)

    return micro_batch_size
