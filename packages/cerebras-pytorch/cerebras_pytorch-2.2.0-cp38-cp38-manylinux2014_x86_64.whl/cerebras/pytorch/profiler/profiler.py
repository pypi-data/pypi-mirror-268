# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

from enum import Enum
from typing import Callable, Iterable, List, Optional

__all__ = ["ProfilerActivity", "ProfilerRegistry", "profile", "schedule"]


class ProfilerRegistry:
    """Registry which stores the cstorch op profiler instance"""

    _profiler = None

    @classmethod
    def set_profiler(cls, profiler):
        """Stores the profiler instance

        Args:
            profiler: The profiler instance which needs to be stored.
        """
        if cls._profiler is not None:
            raise RuntimeError(
                "A profiler has already been set. Only one profiler instance is allowed."
            )
        cls._profiler = profiler

    @classmethod
    def get_profiler(cls):
        """Returns the profiler instance"""
        return cls._profiler

    @classmethod
    def unset_profiler(cls):
        """Deletes the profiler instance stored with it"""
        cls._profiler = None


class ProfilerActivity(Enum):
    """Enum to store different kinds of host
    which the op profiler can profile
    """

    HOST = 0
    CSX = 1
    ALL = 2


def schedule(*, start_step: int, end_step: int) -> Callable:
    """
    This function is used to set the range of profiling iterations
    for the cstorch op profiler.

    Args:
        start_step (int): The starting step from where the profiling starts.
        end_step (int): The end step (including) after which the profiling ends.
    """
    if start_step > end_step:
        raise ValueError(
            "The value of start step should be less than or equal to end_step"
        )

    def schedule_fn() -> List[int]:
        return [start_step, end_step]

    return schedule_fn


class profile:
    """Class to encapsulate all the profiling info
    that user requests.
    """

    def __init__(
        self,
        *,
        schedule: Callable[[], List[int]],
        activities: Optional[Iterable[ProfilerActivity]] = None,
    ):
        """Initialize the profiler with schedule and profilerActivity

        Args:
            schedule: The input schedule which encapsulates the range of
                      profiling interation.
            activities: List of activities which stores different devices
                        where the profiling needs to be done.
        """
        # Will use the activities flag in the future releases
        # once the profiler is capable of filtering the profiles based on the
        # node location
        self.activities_set = (
            set(activities) if activities else [ProfilerActivity.ALL]
        )
        self.schedule = schedule
        self.op_profiler_json = None

    def __enter__(self):
        # Start the profiler
        # Register the profiler instance
        ProfilerRegistry.set_profiler(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Unregister the profiler instance
        ProfilerRegistry.unset_profiler()

    def get_summary(self):
        if self.op_profiler_json:
            import json

            import pandas as pd
            from tabulate import tabulate

            op_profiler_json = json.loads(self.op_profiler_json)
            total_exec_time = (
                op_profiler_json["traceEvents"][-1]["dur"]
                + op_profiler_json["traceEvents"][-1]["ts"]
            )
            df = pd.DataFrame(
                data=op_profiler_json["traceEvents"], columns=['name', 'dur']
            )
            df = (
                df[~((df["name"].str.contains(" = ")))]
                .groupby('name', as_index=False)['dur']
                .sum()
                .sort_values(by=['dur'], ascending=False)
                .reset_index(drop=True)
                .head(10)
            )
            df["% CSX TIME"] = (df["dur"] * 100) / total_exec_time
            df["dur"] = df["dur"].div(100).round(2)  # Change the time to ms
            df.rename(
                columns={
                    'name': 'PYTORCH MODULE NAME',
                    'dur': 'CSX TIME (in ms)',
                },
                inplace=True,
            )
            return tabulate(df, headers='keys', tablefmt='psql')
