# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provides utilities around operation/module name scopes.
"""
import contextlib
from dataclasses import dataclass
from typing import Optional

import torch


@dataclass
class ScopeName:
    scope_name: Optional[str] = None
    scope_type: Optional[str] = None
    scope_func: Optional[str] = None

    def __repr__(self):
        scope_name_args = []
        if self.scope_name:
            scope_name_args.append(self.scope_name)
        if self.scope_type:
            scope_name_args.append(self.scope_type)
        if self.scope_func:
            scope_name_args.append(self.scope_func)

        return ".".join(scope_name_args)


@contextlib.contextmanager
def name_scope(name: str, raw: bool = False):
    """
    A context manager that names operations in PyTorch

    Example usage:
    ```
    class Model(nn.Module):

        def __init__(self):
            self.fc1 = nn.Linear(10, 256)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(256, 2)

        def forward(self, x):
            x = self.fc1(x)
            with cstorch.name_scope("my_scope") as scope:
                x = self.fc2(self.relu(x))
            return F.log_softmax(x, dim=1)
    ```
    """
    from cerebras.pytorch.backend import current_backend_impl

    backend_impl = current_backend_impl()
    with backend_impl.name_scope(name):
        yield


def set_debug_scope(name: str):
    """
    Set global state such that all traced operation will get a unique debug
    name starting with the given scope name, even those created during
    autograd.

    Note that the debug scope must be cleared before mark_step to avoid error.

    Args:
        name: The name of the debug scope to use, or None to clear scope.
    """
    from cerebras.pytorch.lib.cerebras_pytorch_lib import set_scope_name

    if not name:
        name = ""
    set_scope_name(name)


def add_debug_name(module: torch.nn.Module, root_name: Optional[str] = None):
    """
    Adds an invasive _debug_name string attribute to the module and all its
    children. This name will contain the full "." seperated module hierarchy
    name starting from the given module as the root.
    """

    def add_name(module, name):
        module._debug_name = name  # pylint: disable=protected-access
        for cname, child in module.named_children():
            add_name(child, ".".join(filter(len, (name, cname))))

    add_name(module, name=root_name or "")


def get_debug_name(module: torch.nn.Module) -> str:
    """
    Returns the _debug_name string attribute of the module, or assigns a new
    one for un-named modules.
    """
    name = getattr(module, "_debug_name", None)
    if not name:
        # Then assign one based on the module's type name + instance number
        cls = module.__class__
        instance_num = getattr(cls, "_num_instances", 0) + 1
        # Cache the number of seen instances in the __class__ itself.
        cls._num_instances = instance_num  # pylint: disable=protected-access
        name = f"{cls.__name__}_{instance_num}"
        module._debug_name = name
    return name
