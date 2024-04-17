# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" PyTorch Input Generator for Weight Streaming Mode"""
import os
import pprint
from typing import Any, Callable, Dict, Iterable, Optional

import numpy as np

import cerebras.pytorch as cstorch
from cerebras.appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
)
from cerebras.pytorch.backend import Backend, backend, current_backend
from cerebras.pytorch.distributed import service_resolver
from cerebras.pytorch.utils.data.dataloader import (
    DataLoaderCheckpoint,
    RestartableDataLoader,
)
from cerebras.pytorch.utils.data.streamer.data_pipe import (
    BlockValidator,
    DataLoaderCheckpointer,
    MegaBatcher,
    NameRemapper,
    RateProfiler,
    Repeater,
    SampleSaver,
    SampleSpec,
    TensorNamer,
)


class InputGeneratorPyTorch:
    """PyTorch Input Generator"""

    def __init__(
        self,
        dataloader_fn: Callable,
        input_spec: SampleSpec,
        batch_size: int,
        checkpoint_schedule: Optional[Iterable[int]] = None,
        state_dict: Optional[Dict[str, Any]] = None,
        debug_args: DebugArgs = None,
    ):
        """Constructs a `InputGeneratorPyTorch` instance.

        Args:
            dataloader_fn: Callable that returns `torch.utils.data.DataLoader` dataloader.
            input_spec: Specification of input tensors.
            batch_size: Per-box batch size.
            checkpoint_schedule: Iterable that yields the steps at which to take checkpoints.
            state_dict: DataLoader state dict from a previous run.
            debug_args: Debug args for this run.
        """
        backend_instance = current_backend(
            raise_exception=False, raise_warning=False
        )
        if backend_instance is None:
            # No need to initialize the backend here as it won't be used
            Backend._init_impl = False
            # initialize the cstorch device so that cstorch.use_cs() is True
            self._cstorch_backend = backend("CSX")
        else:
            assert backend_instance.is_csx
            self._cstorch_backend = backend_instance

        self._debug_args = debug_args or DebugArgs()
        self._input_spec = input_spec

        # PyTorch DataLoader in multi-processing mode will try to create sockets
        # with temporary file descriptors when using fork. If the direcotry name
        # is too long, it causes "AF_UNIX path too long". So we reset TMPDIR to
        # avoid these issues.
        os.environ["TMPDIR"] = ""

        if self._debug_args.debug_wrk.skip_dataloading:
            self._dataloader = map(
                lambda data: {k: cstorch.to_numpy(v) for k, v in data.items()},
                cstorch.utils.data.SyntheticDataset(
                    {
                        spec.source: cstorch.from_numpy(
                            np.zeros(spec.shape, dtype=spec.dtype)
                        )
                        for spec in input_spec.tensors
                    }
                ),
            )
            self._data_pipe = self._dataloader
        else:
            self._dataloader = dataloader_fn()
            self._data_pipe = Repeater(self._dataloader)
            self._data_pipe = TensorNamer(self._data_pipe)

        self._data_pipe = BlockValidator(self._data_pipe, input_spec)

        self._dataloader_checkpointer = None
        if isinstance(self._dataloader, RestartableDataLoader):
            if state_dict is not None:
                # Deaggregate here first to fetch WRK state_dict
                worker_state_dict = self._dataloader.deaggregate_state_dict(
                    state_dict
                )
                # Now load state for this WRK using user-defined `load_state_dict`
                self._dataloader.load_state_dict(worker_state_dict)

            if checkpoint_schedule is not None:
                cluster_spec = service_resolver().cluster_spec
                worker_ckpt = DataLoaderCheckpoint(
                    local_worker_id=cluster_spec.task().local_rank,
                    num_workers_per_csx=cluster_spec.num_workers_per_csx,
                    num_csx=cluster_spec.num_csx,
                    wse_id=cluster_spec.task().wse_id,
                    appliance_step=0,
                    worker_step=0,
                    samples_streamed=0,
                    user_state_dict=None,
                )

                self._dataloader_checkpointer = DataLoaderCheckpointer(
                    self._data_pipe,
                    self._dataloader,
                    worker_ckpt,
                    batch_size,
                    checkpoint_schedule,
                )
                self._data_pipe = self._dataloader_checkpointer

        self._mega_batcher = MegaBatcher(
            self._data_pipe, input_spec.tensors[0].shape[0]
        )
        self._data_pipe = self._mega_batcher

        self._inject_post_megabatcher_pipes(input_spec)

    def state_dict(self, step: int) -> Optional[DataLoaderCheckpoint]:
        if self._dataloader_checkpointer is None:
            raise RuntimeError(
                f"Attempting to fetch dataloader state, but the dataloader hasn't been configured "
                f"for checkpointing. Please ensure that the dataloader implements the "
                f"\"{RestartableDataLoader.__name__}\" protocol and dataloader checkpointing has "
                f"been enabled."
            )
        return self._dataloader_checkpointer.state_dict(step)

    def supports_checkpointing(self) -> bool:
        """Returns whether this generator can return checkpoints."""
        return self._dataloader_checkpointer is not None

    def update_spec(self, input_spec: SampleSpec):
        """Updates the sample spec but reuses the existing dataloader pipe."""
        if self._dataloader_checkpointer is not None:
            raise RuntimeError(
                "Updating the input sample spec for an existing input generator when dataloader "
                "checkpoint is enabled is not allowed."
            )

        if len(input_spec.tensors) != len(self._input_spec.tensors) or any(
            (
                lhs.source != rhs.source
                or lhs.shape[1:] != rhs.shape[1:]
                or lhs.dtype != rhs.dtype
            )
            for lhs, rhs in zip(input_spec.tensors, self._input_spec.tensors)
        ):
            raise RuntimeError(
                f"The new input spec must match the existing input spec in terms of "
                f"source, shape, and dtype."
                f"\n\tCurrent spec: {pprint.pformat(self._input_spec.tensors)}"
                f"\n\tNew spec: {pprint.pformat(input_spec.tensors)}"
            )

        self._mega_batcher.set_block_size(input_spec.tensors[0].shape[0])
        self._data_pipe = self._mega_batcher

        self._inject_post_megabatcher_pipes(input_spec)

    def _inject_post_megabatcher_pipes(self, input_spec: SampleSpec):
        """Injects extra data pipes after mega batcher."""
        if self._debug_args.debug_wrk.save_samples:
            self._data_pipe = SampleSaver(self._data_pipe)
        self._data_pipe = NameRemapper(
            self._data_pipe,
            mapping={t.source: t.tensor_id for t in input_spec.tensors},
        )
        self._data_pipe = RateProfiler(self._data_pipe)

    def __iter__(self):
        yield from self._data_pipe
