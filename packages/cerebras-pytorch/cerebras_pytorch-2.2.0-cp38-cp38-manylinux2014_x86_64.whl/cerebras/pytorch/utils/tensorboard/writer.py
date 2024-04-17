# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Module containing classes for writing and reading scalar and tensor summaries
"""

import json
import time
import weakref
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Union

import torch
from tensorboard.backend.event_processing.event_accumulator import (
    EventAccumulator,
    ScalarEvent,
)

from ..utils import override_env_vars

# Tensorboard uses some TF binaries that emit warnings if the TF installation wasn't optimized for
# the hardware. This is to avoid printing that warning when loading.
with override_env_vars(TF_CPP_MIN_LOG_LEVEL="1"):
    from torch.utils import tensorboard

from cerebras.appliance.log import ClassLogger, named_class_logger

_METADATA = "__metadata__"
_VERSION_KEY = "__version__"
_VERSION = 1.1


@dataclass(frozen=True)
class TensorDescriptor:
    """Descriptor for a summarized tensor.

    Args:
        step: Step at which the tensor was summarized.
        ns_since_epoch: Nanoseconds since "epoch" (e.g., UNIX time).
        tensor: The summarized tensor.
    """

    step: int
    ns_since_epoch: int
    tensor: torch.Tensor

    @property
    def utctime(self) -> datetime:
        """Returns the UTC time when this tensor was saved."""
        return datetime.utcfromtimestamp(float(self.ns_since_epoch) / 1e9)

    def to_dict(self) -> dict:
        """Returns the descriptor converted to a dict."""
        return asdict(self)

    @staticmethod
    def from_dict(values) -> "TensorDescriptor":
        """Returns a descriptor from a dict of values."""
        return TensorDescriptor(**values)


@named_class_logger("SummaryWriter")
class SummaryWriter(tensorboard.SummaryWriter, ClassLogger):
    """Thin wrapper around torch.utils.tensorboard.SummaryWriter

    Additional features include the ability to add a tensor summary

    Args:
        base_step: The base step to use in summarize_{scalar,tensor}
            functions
        *args, **kwargs: Any other positional and keyword arguments
            are forwarded directly to the base class
    """

    def __init__(self, *args, base_step: int = 1, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_step = base_step

        events_file = Path(self.file_writer.event_writer._file_name)

        # Use same name as tensorboard events_file if is file
        # Otherwise, generated name using current datetime
        if events_file.is_dir():
            cs_events_dir = (
                f"events.out.csevents.{datetime.now():%Y-%m-%dT%H:%M:%S.%f}"
            )
        else:
            cs_events_dir = events_file.name.replace(
                "events.out.tfevents.", "events.out.csevents."
            )
        self.cs_events_dir = events_file.parent.joinpath(cs_events_dir)
        self.cs_events_dir.mkdir(parents=True, exist_ok=True)

        self.log_dir = str(self.cs_events_dir.parent)

        # write metadata to cs events dir
        metadata = self.cs_events_dir.joinpath(_METADATA)
        if not metadata.exists():
            metadata.write_text(json.dumps({_VERSION_KEY: _VERSION}))

        def close(writers):
            if not writers:
                return  # already manually closed
            for writer in writers.values():
                writer.flush()
                writer.close()

        self._finalizer = weakref.finalize(self, close, self.all_writers)

    def add_tensor(self, name: str, tensor: torch.Tensor, step: int):
        """
        Write a tensor summary to a summary file

        Args:
            name: The name of the tensor
            tensor: The tensor to write
            step: The step at which to write the tensor
        """
        tensor_dir = self.cs_events_dir.joinpath("tensors", name)
        tensor_dir.mkdir(parents=True, exist_ok=True)

        curr_time = time.time_ns()
        curr_datetime = datetime.fromtimestamp(curr_time / 1e9)
        filepath = tensor_dir.joinpath(
            f"{step}.{curr_datetime:%Y-%m-%dT%H:%M:%S.%f}.pt"
        )

        # Write the tensor data to file
        torch.save(
            TensorDescriptor(
                step=int(step),
                ns_since_epoch=curr_time,
                tensor=tensor,
            ).to_dict(),
            str(filepath),
        )

    def close(self):
        all_writers = self.all_writers

        super().close()

        if all_writers:
            # clear the dictionary so that it doesn't get double closed on
            # finalize
            all_writers.clear()


# pylint: disable=super-init-not-called
@named_class_logger("SummaryReader")
class SummaryReader(ClassLogger):
    """Class for reading summaries saved using the SummaryWriter"""

    def __init__(self, log_dir: str, **kwargs):
        """
        Args:
            log_dir: The directory at which the event files can be found
            kwargs: The remaining keyword arguments are forwarded to the internal
                EventAccumulator object
        """
        self.log_dir = Path(log_dir).resolve(strict=True)
        if not self.log_dir.exists():
            raise RuntimeError(f"Provided log dir does not exist: {log_dir}")

        # Detect the root cerebras summary dirs
        self.cs_summary_dirs = []
        for root in self.log_dir.glob("events.out.csevents.*"):
            if not root.is_dir():
                self.logger.warning(
                    f"Expected {root} to be a directory containing Cerebras "
                    f"summaries, but it is a file. Skipping as it has an "
                    f"unknown format."
                )
                continue

            metadata = root.joinpath(_METADATA)
            if not metadata.exists():
                raise FileNotFoundError(
                    f"Could not detect version of Cerebras summaries at "
                    f"directory {root}. This may lead to unexpected behavior."
                )

            version = json.loads(metadata.read_text())[_VERSION_KEY]
            if version != _VERSION:
                self.logger.warning(
                    f"Unknown version {version} for Cerebras summaries at "
                    f"directory {root}. Skipping this directory."
                )
                continue

            self.cs_summary_dirs.append(root)

        self.summary_dirs = [
            root.joinpath("tensors")
            for root in self.cs_summary_dirs
            if root.joinpath("tensors").exists()
        ]

        self.accumulator = None
        self.accumulator_params = kwargs

    def reload(self):
        """Reloads the event accumulator"""
        if not self.accumulator:
            self.accumulator = EventAccumulator(
                str(self.log_dir), **self.accumulator_params
            )
        self.accumulator.Reload()

    def read_scalar(self, name: str, step: int = None) -> List[ScalarEvent]:
        """
        Loads and returns scalar(s) with given name at the given step.

        Args:
            name: name of the scalar.
            step: step at which the scalar was summarized.
        """
        if not self.accumulator:
            self.reload()

        scalars = self.accumulator.Scalars(name)
        if step is not None:
            for scalar in scalars:
                if scalar.step == step:
                    return scalar

            raise RuntimeError(f"Could not find scalar {name} at step {step}")

        return scalars

    def read_tensor(
        self, name: str, step: int = None, latest_only: bool = True
    ) -> Union[
        TensorDescriptor,
        List[TensorDescriptor],
        Dict[int, List[TensorDescriptor]],
        None,
    ]:
        """Loads and returns tensor(s) with given name at the given step.

        Args:
            name: name of the tensor.
            step: step at which the tensor was summarized. If None, return all
                tensors with the given name.
            latest_only: if false, return all if there are multiple tensors with
                the same name and step. if true, only return the latest value.
        Returns:
            a single tensor, multiple tensors, or no tensors matching the given
                name and step.
        """
        glob_pattern = f"{step}.*" if step is not None else "*"

        descriptors = defaultdict(list)
        for summary_dir in self.summary_dirs:
            for path in summary_dir.joinpath(name).glob(glob_pattern):
                if path.exists():
                    content = torch.load(str(path))
                    descriptor = TensorDescriptor.from_dict(content)
                    descriptors[descriptor.step].append(descriptor)

        if not descriptors:
            self.logger.warning(
                f"No tensor with name {name} has been summarized"
                + (f" at step {step}" if step is not None else "")
            )
            return None

        if not latest_only:
            if step is not None:
                return descriptors[step]
            return descriptors
        else:

            def map_fn(step, descriptor_list):
                if len(descriptor_list) > 1:
                    self.logger.warning(
                        f"Multiple summarized tensors with name {name} found at "
                        f"step {step}. returning the latest one."
                    )
                return max(descriptor_list, key=lambda x: x.ns_since_epoch)

            if step is not None:
                return map_fn(step, descriptors[step])
            return {
                step: map_fn(step, descriptor_list)
                for step, descriptor_list in descriptors.items()
            }

    def scalar_names(self) -> List[str]:
        """Returns a list of available scalar names."""
        self.reload()
        return sorted(self.accumulator.Tags().get("scalars"))

    def tensor_names(self) -> List[str]:
        """Returns a list of available tensor names."""
        return sorted(
            set(
                str(subdir.relative_to(summary_dir))
                for summary_dir in self.summary_dirs
                for subdir in summary_dir.rglob("*")
                if subdir.is_dir()
                and not any([dx.is_dir() for dx in subdir.glob("*")])
            )
        )
