# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

import os
from contextlib import contextmanager

# An object to signifiy an argument that's unspecified by the caller
UNSPECIFIED = object()


def is_true(value):
    if value is None:
        return False
    if isinstance(value, str):
        value = value.lower()
        if value in {"t", "true", "y", "yes"}:
            return True
        if value in {"f", "false", "n", "no"}:
            return False
        return bool(int(value))
    return not (not value)


@contextmanager
def override_env_vars(**kwargs):
    """Temporarily override env variables from kwargs.

    Args:
        kwargs: List of key/value pairs to set.
    """
    old_values = {k: os.environ.get(k, None) for k in kwargs}

    try:
        for k, v in kwargs.items():
            os.environ[k] = v
        yield
    finally:
        for k, v in old_values.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size
