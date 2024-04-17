# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

from contextlib import contextmanager
from warnings import warn

import torch

from cerebras.pytorch.backend import current_backend_impl

from ._amp_state import _amp_state


@contextmanager
def autocast(dtype: torch.dtype = None):
    """Context manager that invokes torch.autocast() if on GPU"""

    backend = current_backend_impl()

    if backend.backend_type.is_csx:
        warn("autocast() has no effect on CSX runs")
        yield None
    else:
        if (
            backend.backend_type.is_cpu
            and _amp_state.half_dtype != torch.bfloat16
        ):
            raise ValueError(
                "Mixed precision on CPU is only supported with bfloat16. "
                "Please call cstorch.amp.set_half_dtype(torch.bfloat16)"
            )

        if dtype is None:
            dtype = _amp_state.half_dtype

        with torch.autocast(
            backend.device.torch_device.type, dtype=dtype
        ) as ctx:
            yield ctx
