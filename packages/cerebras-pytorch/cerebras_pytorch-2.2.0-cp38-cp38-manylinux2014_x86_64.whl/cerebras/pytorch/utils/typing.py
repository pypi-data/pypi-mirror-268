#
# CC BY-SA 4.0 from Daniil Fajnberg
# From https://stackoverflow.com/a/73966151/381313
#
# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: CC-BY-SA-4.0
#

from collections.abc import Callable
from inspect import Parameter, Signature
from typing import get_args, get_origin


def param_matches_type_hint(
    param: Parameter,
    type_hint: type,
    strict: bool = False,
) -> bool:
    """
    Returns `True` if the parameter annotation matches the type hint.

    For this to be the case:
    In `strict` mode, both must be exactly equal.
    If both are specified generic types, they must be exactly equal.
    If the parameter annotation is a specified generic type and
    the type hint is an unspecified generic type,
    the parameter type's origin must be that generic type.
    """
    param_origin = get_origin(param.annotation)
    type_hint_origin = get_origin(type_hint)
    if (
        strict
        or (param_origin is None and type_hint_origin is None)
        or (param_origin is not None and type_hint_origin is not None)
    ):
        return param.annotation == type_hint
    if param_origin is None and type_hint_origin is not None:
        return False
    return param_origin == type_hint


def signature_matches_type_hint(
    sig: Signature,
    type_hint: type,
    strict: bool = False,
) -> bool:
    """
    Returns `True` if the function signature and `Callable` type hint match.

    For details about parameter comparison, see `param_matches_type_hint`.
    """
    if get_origin(type_hint) != Callable:
        raise TypeError("type_hint must be a `Callable` type")
    type_params, return_type = get_args(type_hint)
    if sig.return_annotation != return_type:
        return False
    if len(sig.parameters) != len(type_params):
        return False
    return all(
        param_matches_type_hint(sig_param, type_param, strict=strict)
        for sig_param, type_param in zip(sig.parameters.values(), type_params)
    )
