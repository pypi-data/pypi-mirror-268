# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
This module includes features that are currently under development,
and we're actively working to enhance them. Please be aware that
backward compatibility is not guaranteed at this stage.

Users are advised to proceed with caution and acknowledge all
associated risks when using these features.
"""

from typing import List, Optional

import torch


def run_implicit_autoregressive_loop(
    input_tensor: torch.IntTensor,
    output_tensor: torch.IntTensor,
    loop_dim: int,
    start_token: int,
    stop_sequences: List[List[int]],
    max_tokens: Optional[int] = None,
):
    """
    Sets up an implicit inner autoregressive loop over the whole model.
    At each step, input_tensor[..., i+1] = output_tensor[..., i]
    along ``loop_dim``.

    This is equivalent to the following pseudocode for one loop:

        def inner_loop(input_tensor, loop_dim, start_token, stop_sequences, model):
            output_tensor = model(input_tensor)
            shape = list(input_tensor.shape)
            extent = shape[loop_dim]
            del shape[loop_dim:]
            started = torch.zeros(shape, dtype=torch.bool)
            stopped = torch.zeros(shape, dtype=torch.bool)
            for i in range(extent-1):
                started |= (
                    input_tensor.index_select(
                        loop_dim, torch.tensor(i)
                    ) == start_token
                ).view(shape+[-1]).all(dim=-1)

                if not started.any():
                    # optimization to skip re-running model when no input would
                    # be updated.
                    continue

                output_token = output_tensor.index_select(
                    loop_dim, torch.tensor(i)
                )
                stopped |= (
                    output_token == stop_sequences
                ).view(shape+[-1]).all(dim=-1)

                if stopped.all()
                    # optimization to stop running updates onces all outputs
                    # have stopped.
                    break

                # autoregress this position and run again
                update = started && ~stopped
                updated_input = input_tensor.index_copy(
                    loop_dim, torch.tensor(i+1), output_token
                )

                input_tensor = torch.where(
                    update,
                    updated_input_tensor,
                    input_tensor,
                )
                output_tensor = model(input_tensor)

    Args:
        input_tensor: This tensor will be updated before re-running the model
        output_tensor: One token of this tensor will be assigned to the
                       subsequent position along ``loop_dim`` in
                       ``input_tensor`` each inner-step. Must have same shape
                       and type as ``input_tensor``.
        loop_dim: The dimension of ``input_tensor`` to loop over.
        start_token: For LM autoregessive use, this token in the input marks
                     the beginning of generation. All tokens before it are left
                     unmodified.
        stop_sequences: For LM autoregessive use, this list of stop token sequences
                    in the output marks the end of generation. Once a stop sequence
                    from the list is seen, the inner autorgressive loop is exited.
    """
    from cerebras.pytorch.backend import current_backend_impl

    current_backend_impl().run_implicit_autoregressive_loop(
        input_tensor,
        output_tensor,
        loop_dim,
        start_token,
        stop_sequences,
        max_tokens,
    )
