# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

import torch

import cerebras.pytorch as cstorch
from cerebras.appliance import logger


def one_hot(array, num_classes):
    """Cerebras specific implementation of one_hot"""
    if num_classes == -1:
        logger.error("num_class argument to one_hot cannot be -1")
    init = torch.zeros(
        array.shape + (num_classes,), device=array.device, dtype=torch.int
    )
    res = init.scatter_(-1, array.unsqueeze(-1), 1)
    return res


# CIRH ScopeBoundary op boundary_type enum
BEGIN_FORWARD = 'BEGIN_FORWARD'
BEGIN_BACKWARD = 'BEGIN_BACKWARD'
END_FORWARD = 'END_FORWARD'
END_BACKWARD = 'END_BACKWARD'


def scope_boundary(input, boundary_type, scope_name):
    """
    This function is used to set a boundary after input, or place the cirh.ScopeBoundary op
    after `input` in the CIRH graph.

    Args:
        boundary_type (str): The type of the boundary. One of `BEGIN_FORWARD`, 'BEGIN_BACKWARD',
            'END_FORWARD`, or `END_BACKWARD`.
        scope_name (str): The name of the scope.
    """

    if cstorch.use_cs():
        from cerebras.pytorch import cirh

        return cirh.ScopeBoundary(
            input,
            boundary_type=boundary_type,
            scope_name=scope_name,
        )
    return input


def enter_scope(input, scope_name):
    """
    This module is used as a wrapper function of 'EnterFunction' autograd functions,
    which can set the "BEGIN" boundaries in CIRH graph.
    """
    return EnterFunction.apply(input, scope_name)


def exit_scope(input, scope_name):
    """
    This module is used as a wrapper function of 'ExitFunction' autograd functions,
    which can set the "END" boundaries in CIRH graph.
    """
    return ExitFunction.apply(input, scope_name)


class EnterFunction(torch.autograd.Function):
    """
    This module is used to set a boundary after 'input'. In the foward pass, the type of
    boundary is BEGIN_FORWARD. In the backward, the type of boundary is END_BACKWARD.

    `scope_boundary()` is used to invoke the custom call to generate cirh.ScopeBoundary.
    """

    @staticmethod
    def forward(ctx, input, scope_name):
        ctx.scope_name = scope_name
        return scope_boundary(input, BEGIN_FORWARD, scope_name)

    @staticmethod
    def backward(ctx, grad_output):
        return (
            scope_boundary(grad_output, END_BACKWARD, ctx.scope_name),
            None,
            None,
        )


class ExitFunction(torch.autograd.Function):
    """
    This module is used to set a boundary after 'input'. In the foward pass, the type of
    boundary is END_FORWARD. In the backward, the type of boundary is BEGIN_BACKWARD.

    `scope_boundary()` is used to invoke the custom call to generate cirh.ScopeBoundary.
    """

    @staticmethod
    def forward(ctx, input, scope_name):
        ctx.scope_name = scope_name
        return scope_boundary(input, END_FORWARD, scope_name)

    @staticmethod
    def backward(ctx, grad_output):
        return (
            scope_boundary(grad_output, BEGIN_BACKWARD, ctx.scope_name),
            None,
            None,
        )
