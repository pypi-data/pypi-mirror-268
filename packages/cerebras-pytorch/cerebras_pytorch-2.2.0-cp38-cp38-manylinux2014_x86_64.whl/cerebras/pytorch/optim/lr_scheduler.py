# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Implementations for Cerebras specific learning rate schedulers"""
import abc
import math
import warnings
from typing import List

import numpy
import torch
from torch.optim.lr_scheduler import _enable_get_lr_call

import cerebras.pytorch as cstorch
from cerebras.appliance.utils.classes import retrieve_all_subclasses
from cerebras.pytorch.backend import current_backend_impl, use_cs


# pylint: disable=protected-access
class LRScheduler(torch.optim.lr_scheduler._LRScheduler, abc.ABC):
    """
    Cerebras specific learning rate scheduler base class.

    The learning rate schedulers implemented in this file are specifically
    designed to be run on a Cerebras system. This means that there are certain
    caveats to these custom schedulers that differ from a typical LR scheduler
    found in core PyTorch.

    The learning rate schedulers here are intended to be stepped at every
    iteration. This means `lr_scheduler.step()` should be called after every
    `optimizer.step()`. Hence, the learning rate schedulers operate on a
    step-by-step basis. Having said that, there are some variables used such as
    `last_epoch` that might indicate otherwise. The only reason these variables
    are used is to match what is used in core PyTorch. It does *not* indicate
    that things are operating on an epoch-by-epoch basis.

    Also, note that the above means that our LR schedulers are incompatible with
    the LR schedulers found in core PyTorch. The state cannot simply be
    transferred between the two. So, one of the LR schedulers defined here must
    be used in order to have LR scheduling on the Cerebras system.
    """

    def __init__(self, optimizer, total_iters, last_epoch=-1):
        # To be changed by the backend on setup
        self.device = None
        # filled with default dummy values
        self._last_lr = [group["lr"] for group in optimizer.param_groups]

        self.total_iters = total_iters

        super().__init__(optimizer, last_epoch)

        self._get_lr_called_within_step = False

        backend = current_backend_impl()
        backend.setup_lr_scheduler(self)

        if not isinstance(self.last_epoch, torch.Tensor):
            # The tensor representation of last_epoch
            self.last_epoch = torch.tensor(self.last_epoch, device=self.device)

        self._post_init()

    def _post_init(self):
        if not use_cs():
            # For non-CS backends, we need to update the learning
            # rate on initialization
            self.update_last_lr()

    def get_lr(self):
        if not self._get_lr_called_within_step:
            warnings.warn(
                "To get the last learning rate computed by the scheduler, "
                "please use `get_last_lr()`."
            )

        lr_tensor = self._get_closed_form_lr()
        return [lr_tensor for _ in self.optimizer.param_groups]

    @abc.abstractmethod
    def _get_closed_form_lr(self):
        pass

    def state_dict(self):
        state = super().state_dict()
        state.pop("device")
        return state

    def load_state_dict(self, state_dict):
        ignored_keys = [
            # In older releases, _step_count wasn't updated and always had value
            # 0. In this iteration of the LR schedulers, step_count is updated
            # during LRS construction and its value is used to determine if the
            # LR tensor should be computed. However, its value is still not used
            # in a substantial way (just for some warning messages in vanilla
            # PT). We pop it from the state_dict to avoid overriding the
            # increment during construction.
            "_step_count",
            # Pop the deprecated disable_lr_steps_reset flag from the state_dict
            "disable_lr_steps_reset",
        ]
        ignored_kwargs = {
            key: state_dict.pop(key)
            for key in ignored_keys
            if key in state_dict
        }

        super().load_state_dict(state_dict)

        # Restore state_dict keys in order to prevent side effects
        state_dict.update(ignored_kwargs)

        # This causes `self` to be registered in the LR scheduler registry of
        # the optimizers. LR scheduler subclasses that act as a wrapper around
        # other LR schedulers may need to remove the wrapped LR schedulers from
        # the registery to avoid double registration.
        current_backend_impl().setup_lr_scheduler(self)

    def increment_last_epoch(self):
        """Increments the last epoch by 1"""
        # Mark the tensor to conditionally skip its update in the case where
        # DLS is active and NaN/inf is detected in the gradients
        cstorch.amp.update_if_finite(self.optimizer, self.last_epoch)
        self.last_epoch += 1

    def step(self, *args, **kwargs):
        """
        Steps the scheduler and computes the latest learning rate

        Only sets the last_epoch if running on CS
        """
        self.increment_last_epoch()
        self._step_count += 1

        if self._step_count == 1:
            # don't calculate the learning rate on initialization
            # as we need to recalculate it anyways just before
            # optimizer step
            return

        self.update_last_lr()
        self.update_groups(self._last_lr)

    def update_last_lr(self):
        with _enable_get_lr_call(self):
            self._last_lr = self.get_lr()

        # Update the optimizer param groups so that the latest value is
        # available for use during optimizer step
        for param_group, lr in zip(self.optimizer.param_groups, self._last_lr):
            param_group['lr'] = lr

    @cstorch.step_closure
    def update_groups(self, values):
        """Update the optimizer groups with the latest learning rate values"""

        # Update the last lr values so that they are available after training
        # The _last_lr values are tensors here to reflect the fact that
        # they are tensors during training
        # This should be compatible with cpu/gpu runs as well
        self._last_lr = values

        # Update the optimizer param groups so that the latest value is
        # available for checkpointing
        for param_group, lr in zip(self.optimizer.param_groups, self._last_lr):
            param_group['lr'] = lr


class ConstantLR(LRScheduler):
    r"""Maintains a constant learning rate for each parameter group (no decaying).

    Args:
        optimizer: The optimizer to schedule
        val: The learning_rate value to maintain
        total_iters: The number of steps to decay for
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        learning_rate: float,
        total_iters: int = None,
    ):
        self.learning_rate = learning_rate

        super().__init__(optimizer, total_iters=total_iters)

    def _get_closed_form_lr(self):
        return torch.tensor(self.learning_rate, device=self.device)


class PolynomialLR(LRScheduler):
    r"""Decays the learning rate of each parameter group using a polynomial function
    in the given `total_iters`.

    This class is similar to the `Pytorch PolynomialLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        end_learning_rate: The final learning rate
        total_iters: Number of steps to perform the decay
        power: Exponent to apply to "x" (as in y=mx+b),
            which is ratio of step completion (1 for linear)
            Default: 1.0 (only Linear supported at the moment)
        cycle: Whether to cycle

    .. _Pytorch PolynomialLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.PolynomialLR.html#torch.optim.lr_scheduler.PolynomialLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        end_learning_rate: float,
        total_iters: int,
        power: float = 1.0,
        cycle: bool = False,
    ):
        self.initial_learning_rate = initial_learning_rate
        self.end_learning_rate = end_learning_rate
        self.power = power
        self.cycle = cycle

        super().__init__(optimizer, total_iters=total_iters)

    def _get_closed_form_lr(self):
        lr_diff = self.initial_learning_rate - self.end_learning_rate
        alpha = torch.tensor(1.0, dtype=torch.float32, device=self.device)
        if self.cycle:
            alpha = torch.add(self.last_epoch, 1).div(self.total_iters).ceil()

        return torch.where(
            self.last_epoch >= self.total_iters,
            torch.tensor(
                self.end_learning_rate,
                dtype=torch.float32,
                device=self.device,
            ),
            torch.sub(
                1,
                torch.div(self.last_epoch, torch.mul(self.total_iters, alpha)),
            )
            .pow(self.power)
            .mul(lr_diff)
            .add(self.end_learning_rate)
            .float(),
        )


class LinearLR(PolynomialLR):
    """Alias for Polynomial LR scheduler with a power of 1"""

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        end_learning_rate: float,
        total_iters: int,
        cycle: bool = False,
    ):
        super().__init__(
            optimizer=optimizer,
            initial_learning_rate=initial_learning_rate,
            end_learning_rate=end_learning_rate,
            total_iters=total_iters,
            power=1.0,
            cycle=cycle,
        )


class ExponentialLR(LRScheduler):
    r"""Decays the learning rate of each parameter group by `decay_rate` every step.

    This class is similar to the `Pytorch ExponentialLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        total_iters: Number of steps to perform the decay
        decay_rate: The decay rate
        staircase: If True decay the learning rate at discrete intervals

    .. _Pytorch ExponentialLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.ExponentialLR.html#torch.optim.lr_scheduler.ExponentialLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        total_iters: int,
        decay_rate: float,
        staircase: bool = False,
    ):
        self.initial_learning_rate = float(initial_learning_rate)
        self.decay_rate = decay_rate
        self.staircase = staircase

        super().__init__(optimizer, total_iters=total_iters)

    def _get_closed_form_lr(self):
        power = torch.div(self.last_epoch, self.total_iters)
        if self.staircase:
            power.floor_()
        return torch.pow(self.decay_rate, power).mul(self.initial_learning_rate)


class InverseExponentialTimeDecayLR(LRScheduler):
    r"""Decays the learning rate inverse-exponentially over time, as described
    in the `Keras InverseTimeDecay class`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        step_exponent: Exponential value.
        total_iters: Number of steps to perform the decay.
        decay_rate: The decay rate.
        staircase: If True decay the learning rate at discrete intervals.

    .. _Keras InverseTimeDecay class:
        https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        step_exponent: int,
        total_iters: int,
        decay_rate: float,
        staircase: bool = False,
    ):
        self.initial_learning_rate = initial_learning_rate
        self.step_exponent = step_exponent
        self.decay_rate = decay_rate
        self.staircase = staircase

        super().__init__(optimizer, total_iters=total_iters)

    def _get_closed_form_lr(self):
        alpha = torch.div(
            torch.pow(self.last_epoch.float(), self.step_exponent),
            self.total_iters,
        )
        if self.staircase:
            alpha.floor_()
        return torch.div(
            torch.tensor(
                self.initial_learning_rate,
                dtype=torch.float32,
                device=self.device,
            ),
            torch.mul(alpha, self.decay_rate).add(1.0),
        )


class InverseSquareRootDecayLR(LRScheduler):
    r"""Decays the learning rate inverse-squareroot over time, as described
    in the following equation:

    .. math::
        \begin{aligned}
            lr_t & = \frac{\text{scale}}{\sqrt{\max\{t, \text{warmup_steps}\}}}.
        \end{aligned}

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        scale: Multiplicative factor to scale the result.
        warmup_steps: use initial_learning_rate for the first warmup_steps.
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float = 1.0,
        scale: float = 1.0,
        warmup_steps: int = 1.0,
    ):
        self.initial_learning_rate = initial_learning_rate
        self.scale = scale
        self.warmup_steps = warmup_steps

        super().__init__(optimizer, total_iters=None)

    def _get_closed_form_lr(self):
        return torch.div(
            torch.tensor(self.scale, dtype=torch.float32, device=self.device),
            torch.sqrt(
                torch.max(
                    torch.tensor(
                        self.warmup_steps,
                        dtype=torch.float32,
                        device=self.device,
                    ),
                    self.last_epoch,
                )
            ),
        ).mul(self.initial_learning_rate)


class CosineDecayLR(LRScheduler):
    r"""Applies the cosine decay schedule as described
    in the `Keras CosineDecay class`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        end_learning_rate: The final learning rate
        total_iters: Number of steps to perform the decay

    .. _Keras CosineDecay class:
        https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        end_learning_rate: float,
        total_iters: int,
    ):
        self.initial_learning_rate = initial_learning_rate
        self.end_learning_rate = end_learning_rate

        super().__init__(optimizer, total_iters=total_iters)

    def _get_closed_form_lr(self):
        lr_diff = self.initial_learning_rate - self.end_learning_rate
        # clip the steps to be at most total_iters

        step = torch.minimum(
            torch.tensor(
                self.total_iters, dtype=torch.float32, device=self.device
            ),
            self.last_epoch,
        )
        # where we are at the cosine curve
        progress = (
            torch.div(math.pi, self.total_iters).mul(step).cos().add(1).mul(0.5)
        )
        return torch.mul(progress, lr_diff).add(self.end_learning_rate)


class SequentialLR(LRScheduler):
    r"""Receives the list of schedulers that is expected to be called sequentially
    during optimization process and milestone points that provides exact
    intervals to reflect which scheduler is supposed to be called at a given
    step.

    This class is a wrapper around the `Pytorch SequentialLR LRS`_.

    Args:
        optimizer: Wrapped optimizer
        schedulers (list): List of chained schedulers.
        milestones (list): List of integers that reflects milestone points.
        last_epoch (int): The index of last epoch. Default: -1.

    .. _Pytorch SequentialLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.SequentialLR.html#torch.optim.lr_scheduler.SequentialLR
    """

    def __init__(self, optimizer, schedulers, milestones, last_epoch=-1):
        if isinstance(milestones, numpy.ndarray):
            milestones = milestones.tolist()
        if isinstance(milestones, (list, tuple)):
            if any(not isinstance(milestone, int) for milestone in milestones):
                raise TypeError(
                    f"Expected milestones to be a list of integers. "
                    f"Got: {[type(milestone) for milestone in milestones]}"
                )
        else:
            raise TypeError(
                f"Expected milestones to be a list of integers. "
                f"Got: {type(milestones)}"
            )

        for scheduler_idx in range(len(schedulers)):
            if schedulers[scheduler_idx].optimizer != optimizer:
                raise ValueError(
                    f"Sequential Schedulers expects all schedulers to belong "
                    f"to the same optimizer, but got schedulers at index "
                    f"{scheduler_idx} to be different than the optimizer "
                    f"passed in."
                )

            if schedulers[scheduler_idx].optimizer != schedulers[0].optimizer:
                raise ValueError(
                    f"Sequential Schedulers expects all schedulers to belong "
                    f"to the same optimizer, but got schedulers at index {0} "
                    f"and {scheduler_idx} to be different."
                )
        if len(milestones) != len(schedulers) - 1:
            raise ValueError(
                f"Sequential Schedulers expects number of schedulers provided "
                f"to be one more than the number of milestone points, but got "
                f"number of schedulers {len(schedulers)} and the number of "
                f" milestones to be equal to {len(milestones)}"
            )
        self._schedulers = schedulers
        self._milestones = milestones

        for scheduler in schedulers:
            optimizer._lr_scheduler_registry.remove(scheduler)

        super().__init__(optimizer, total_iters=None, last_epoch=last_epoch)

    def _get_closed_form_lr(self):
        new_lr = self._schedulers[0]._get_closed_form_lr()
        for idx, milestone in enumerate(self._milestones):
            # If current global step is equal or greater than
            # the 'milestone', we will choose the corresponding
            # LR scheduler which is indexed 'idx+1' in 'self._schedulers`.
            # Otherwise, we will use the LR scheduler from previous iteration.
            res = torch.where(
                self.last_epoch < milestone,
                new_lr,
                self._schedulers[idx + 1]._get_closed_form_lr(),
            )
            new_lr = res
        return new_lr

    def increment_last_epoch(self, *args, **kwargs):
        """Increments the last_epoch of the scheduler whose milestone we are on"""
        super().increment_last_epoch()

        # All schedulers have already been incremented before the first step
        if self._step_count == 0:
            return

        # Mark the tensors to conditionally skip their update in the case where
        # DLS is active and NaN/inf is detected in the gradients
        for scheduler in self._schedulers:
            cstorch.amp.update_if_finite(self.optimizer, scheduler.last_epoch)
        self._schedulers[0].last_epoch += 1
        for idx, milestone in enumerate(self._milestones):
            # Increment next scheduler's last_epoch if we are on the correct milestone
            self._schedulers[idx + 1].last_epoch += torch.where(
                self.last_epoch <= milestone, 0, 1
            )

    def state_dict(self):
        s = super().state_dict()

        schedulers = s.pop("_schedulers")
        s["_schedulers"] = []
        for scheduler in schedulers:
            s['_schedulers'].append(scheduler.state_dict())

        return s

    def load_state_dict(self, state_dict):
        """Loads the schedulers state.
        Args:
            state_dict (dict): scheduler state. Should be an object returned
                from a call to :meth:`state_dict`.
        """
        _schedulers = state_dict.pop('_schedulers')
        super().load_state_dict(state_dict)
        # Restore state_dict keys in order to prevent side effects
        # https://github.com/pytorch/pytorch/issues/32756
        state_dict['_schedulers'] = _schedulers

        for idx, s in enumerate(_schedulers):
            self._schedulers[idx].load_state_dict(s)
            self.optimizer._lr_scheduler_registry.remove(self._schedulers[idx])


class PiecewiseConstantLR(SequentialLR):
    r"""Adjusts the learning rate to a predefined constant at each milestone and
    holds this value until the next milestone. Notice that such adjustment can
    happen simultaneously with other changes to the learning rate from outside
    this scheduler.

    Args:
        optimizer: The optimizer to schedule
        learning_rates: List of learning rates to maintain before/during each
            milestone.
        milestones: List of step indices. Must be increasing.
    """

    def __init__(
        self,
        optimizer,
        learning_rates: List[float],
        milestones: List[int],
    ):
        schedulers = []
        boundaries = [0]
        boundaries.extend(milestones)
        for lr, b1, b2 in zip(learning_rates, boundaries[:-1], boundaries[1:]):
            schedulers.append(ConstantLR(optimizer, lr, b2 - b1))
        # Final learning rate
        schedulers.append(ConstantLR(optimizer, learning_rates[-1]))

        super().__init__(optimizer, schedulers, milestones)


class MultiStepLR(LRScheduler):
    r"""Decays the learning rate of each parameter group by gamma once the number of
    steps reaches one of the milestones. Notice that such decay can happen
    simultaneously with other changes to the learning rate from outside this
    scheduler.

    This class is similar to the `Pytorch MultiStepLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        gamma: Multiplicative factor of learning rate decay.
        milestones: List of step indices. Must be increasing.

    .. _Pytorch MultiStepLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.MultiStepLR.html#torch.optim.lr_scheduler.MultiStepLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        gamma: float,
        milestones: List[int],
    ):
        self.initial_learning_rate = initial_learning_rate
        self.gamma = gamma
        self.milestones = milestones
        super().__init__(optimizer, total_iters=None)

    def _get_closed_form_lr(self):
        new_lr = torch.tensor(
            self.initial_learning_rate,
            dtype=torch.float32,
            device=self.device,
        )
        for milestone in self.milestones:
            res = torch.where(
                self.last_epoch < milestone,
                new_lr,
                torch.mul(
                    torch.tensor(
                        self.gamma,
                        dtype=torch.float32,
                        device=self.device,
                    ),
                    new_lr,
                ),
            )
            new_lr = res
        return new_lr


class StepLR(LRScheduler):
    r"""Decays the learning rate of each parameter group by gamma every `step_size`.
    Notice that such decay can happen simultaneously with other changes to the
    learning rate from outside this scheduler.

    This class is similar to the `Pytorch StepLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        step_size: Period of learning rate decay.
        gamma: Multiplicative factor of learning rate decay.

    .. _Pytorch StepLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.StepLR.html#torch.optim.lr_scheduler.StepLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        step_size: int,
        gamma: float,
    ):
        self.initial_learning_rate = float(initial_learning_rate)
        self.gamma = gamma
        self.step_size = step_size
        super().__init__(optimizer, total_iters=None)

    def _get_closed_form_lr(self):
        return torch.mul(
            torch.pow(
                torch.tensor(
                    self.gamma, dtype=torch.float32, device=self.device
                ),
                torch.div(self.last_epoch, self.step_size).floor_(),
            ),
            self.initial_learning_rate,
        )


class CosineAnnealingLR(LRScheduler):
    r"""Set the learning rate of each parameter group using a cosine annealing
    schedule, where :math:`\eta_{max}` is set to the initial lr and
    :math:`T_{cur}` is the number of steps since the last restart in SGDR:

    .. math::
        \begin{aligned}
            \eta_t & = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1
            + \cos\left(\frac{T_{cur}}{T_{max}}\pi\right)\right),
            & T_{cur} \neq (2k+1)T_{max}; \\
            \eta_{t+1} & = \eta_{t} + \frac{1}{2}(\eta_{max} - \eta_{min})
            \left(1 - \cos\left(\frac{1}{T_{max}}\pi\right)\right),
            & T_{cur} = (2k+1)T_{max}.
        \end{aligned}

    Notice that because the schedule is defined recursively, the learning rate
    can be simultaneously modified outside this scheduler by other operators.
    If the learning rate is set solely by this scheduler, the learning rate at
    each step becomes:

    .. math::
        \eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1 +
        \cos\left(\frac{T_{cur}}{T_{max}}\pi\right)\right)

    It has been proposed in
    `SGDR: Stochastic Gradient Descent with Warm Restarts`_. Note that this only
    implements the cosine annealing part of SGDR, and not the restarts.

    This class is similar to the `Pytorch CosineAnnealingLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        T_max: Maximum number of iterations.
        eta_min: Minimum learning rate.

    .. _SGDR\: Stochastic Gradient Descent with Warm Restarts:
        https://arxiv.org/abs/1608.03983

    .. _Pytorch CosineAnnealingLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.CosineAnnealingLR.html#torch.optim.lr_scheduler.CosineAnnealingLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        T_max: int,
        eta_min: float = 0.0,
    ):
        self.initial_learning_rate = float(initial_learning_rate)
        self.T_max = float(T_max)
        self.eta_min = eta_min
        super().__init__(optimizer, total_iters=None)

    def _get_closed_form_lr(self):
        lr_diff = self.initial_learning_rate - self.eta_min
        a = torch.div(
            torch.mul(torch.div(self.last_epoch, self.T_max), math.pi)
            .cos()
            .add(1),
            2,
        )
        return torch.add(torch.mul(a, lr_diff), self.eta_min)


class LambdaLR(LRScheduler):
    r"""Sets the learning rate of each parameter group to the initial lr times a
    given function (which is specified by overriding `set_lr_lambda`).

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
    ):
        self.initial_learning_rate = initial_learning_rate
        super().__init__(optimizer, total_iters=None)

    def set_lr_lambda(self):  # pylint: disable=no-self-use
        """Sets learning lambda functions"""
        lambda1 = lambda epoch: torch.div(epoch, 30)
        lambda2 = lambda epoch: torch.pow(
            torch.tensor(0.95, dtype=torch.float32, device=epoch.device),
            epoch,
        )
        lr_lambda = [lambda1, lambda2]
        return lr_lambda

    def _get_closed_form_lr(self):
        new_lr = torch.tensor(
            1.0,
            dtype=torch.float32,
            device=self.device,
        )
        lr_lambda = self.set_lr_lambda()
        for lr in lr_lambda:
            new_lr = torch.mul(
                torch.mul(
                    torch.tensor(
                        self.initial_learning_rate,
                        dtype=torch.float32,
                        device=self.device,
                    ),
                    lr(self.last_epoch),
                ),
                new_lr,
            )
        return new_lr


class CosineAnnealingWarmRestarts(LRScheduler):
    r"""Set the learning rate of each parameter group using a cosine annealing
    schedule, where :math:`\eta_{max}` is set to the initial lr, :math:`T_{cur}`
    is the number of steps since the last restart and :math:`T_{i}` is the number
    of steps between two warm restarts in SGDR:

    .. math::
        \eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1 +
        \cos\left(\frac{T_{cur}}{T_{i}}\pi\right)\right)

    When :math:`T_{cur}=T_{i}`, set :math:`\eta_t = \eta_{min}`.
    When :math:`T_{cur}=0` after restart, set :math:`\eta_t=\eta_{max}`.

    It has been proposed in
    `SGDR: Stochastic Gradient Descent with Warm Restarts`_.

    This class is similar to the `Pytorch CosineAnnealingWarmRestarts LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        T_0: Number of iterations for the first restart.
        T_mult: A factor increases Ti after a restart. Currently T_mult must be
            set to 1.0
        eta_min: Minimum learning rate.

    .. _SGDR\: Stochastic Gradient Descent with Warm Restarts:
        https://arxiv.org/abs/1608.03983

    .. _Pytorch CosineAnnealingWarmRestarts LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.CosineAnnealingWarmRestarts.html#torch.optim.lr_scheduler.CosineAnnealingWarmRestarts
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        T_0: int,
        T_mult: int = 1,
        eta_min: float = 0.0,
    ):
        if T_mult != 1.0:
            raise ValueError(
                f"Unsupported value of Parameters 'T_mult' for LR scheduler "
                f"type CosineAnnealingWarmRestarts, Only supported default "
                f"T_mult value: 1.0. "
            )
        self.initial_learning_rate = float(initial_learning_rate)
        self.T_0 = T_0
        self.T_mult = T_mult
        self.eta_min = eta_min
        super().__init__(optimizer, total_iters=None)

    def _get_closed_form_lr(self):
        tensor_t_i_1 = torch.tensor(
            self.T_0, dtype=torch.float32, device=self.device
        )

        tensor_t_cur_1 = self.last_epoch.float()
        tensor_t_cur_2 = torch.sub(
            torch.torch.mul(
                torch.div(self.last_epoch, self.T_0).floor_(), self.T_0
            ),
            self.T_0,
        )

        tensor_t_mul = torch.tensor(
            self.T_mult, dtype=torch.float32, device=self.device
        )
        nn = torch.mul(
            torch.div(self.last_epoch, self.T_0), tensor_t_mul.sub(1)
        ).add(1)
        n = torch.div(torch.log(nn), torch.log(tensor_t_mul)).floor_()

        tensor_t_i_3 = torch.pow(tensor_t_mul, n).mul(self.T_0)
        tensor_t_cur_3 = torch.sub(
            self.last_epoch,
            torch.div(
                torch.pow(tensor_t_mul, n).sub(1), tensor_t_mul.sub(1)
            ).mul(self.T_0),
        ).float()

        T_i = torch.where(tensor_t_mul == 1, tensor_t_i_1, tensor_t_i_3)
        T_cur = torch.where(
            self.last_epoch < self.T_0,
            tensor_t_cur_1,
            torch.where(tensor_t_mul == 1, tensor_t_cur_2, tensor_t_cur_3),
        )
        lr_diff = self.initial_learning_rate - self.eta_min
        a = torch.div(
            torch.mul(torch.div(T_cur, T_i), math.pi).cos().add(1),
            2,
        )
        return torch.add(torch.mul(a, lr_diff), self.eta_min)


class MultiplicativeLR(LRScheduler):
    r"""Multiply the learning rate of each parameter group by the supplied
    coefficient.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: The initial learning rate.
        coefficient: Multiplicative factor of learning rate.
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        coefficient: float,
    ):
        self.initial_learning_rate = initial_learning_rate
        self.coefficient = coefficient
        super().__init__(optimizer, total_iters=None)

    def set_lr_lambda(self):
        """Sets learning lambda functions"""
        lr_lambda = lambda epoch: self.coefficient
        return lr_lambda

    def _get_closed_form_lr(self):
        new_lr = None
        lr_lambda = self.set_lr_lambda()
        new_lr = torch.mul(
            torch.pow(
                torch.tensor(
                    lr_lambda(self.last_epoch),
                    dtype=torch.float32,
                    device=self.device,
                ),
                self.last_epoch,
            ),
            self.initial_learning_rate,
        )
        return new_lr


class ChainedScheduler(LRScheduler):
    r"""Chains list of learning rate schedulers.
    It takes a list of chainable learning rate schedulers and
    performs consecutive step() functions belonging to them by just one call.
    """

    def __init__(self, schedulers):
        self._schedulers = list(schedulers)
        super().__init__(schedulers[0].optimizer, total_iters=None)

    def _post_init(self):
        for i, scheduler in enumerate(self._schedulers):
            if scheduler.optimizer != self.optimizer:
                raise ValueError(
                    f"ChainedScheduler expects all schedulers to belong to the "
                    f"same optimizer, but got schedulers at index 0 and "
                    f"{i} to be different"
                )

            scheduler.last_epoch = self.last_epoch

            self.optimizer._lr_scheduler_registry.remove(scheduler)

        super()._post_init()

    def _get_closed_form_lr(self):
        new_lr = self._schedulers[0]._get_closed_form_lr()
        for scheduler in self._schedulers[1:]:
            new_lr = torch.mul(
                new_lr,
                torch.div(
                    scheduler._get_closed_form_lr(),
                    scheduler.initial_learning_rate,
                ),
            )
        return new_lr

    def state_dict(self):
        s = super().state_dict()

        schedulers = s.pop("_schedulers")
        s["_schedulers"] = []
        for scheduler in schedulers:
            s['_schedulers'].append(scheduler.state_dict())

        return s

    def load_state_dict(self, state_dict):
        """Loads the schedulers state.
        Args:
            state_dict (dict): scheduler state. Should be an object returned
                from a call to :meth:`state_dict`.
        """
        _schedulers = state_dict.pop('_schedulers')
        super().load_state_dict(state_dict)
        # Restore state_dict keys in order to prevent side effects
        # https://github.com/pytorch/pytorch/issues/32756
        state_dict['_schedulers'] = _schedulers

        for idx, s in enumerate(_schedulers):
            self._schedulers[idx].load_state_dict(s)
            self._schedulers[idx].last_epoch = self.last_epoch
            self.optimizer._lr_scheduler_registry.remove(self._schedulers[idx])


class CyclicLR(LRScheduler):
    r"""Sets the learning rate of each parameter group according to
    cyclical learning rate policy (CLR). The policy cycles the learning
    rate between two boundaries with a constant frequency, as detailed in
    the paper `Cyclical Learning Rates for Training Neural Networks`_.
    The distance between the two boundaries can be scaled on a per-iteration
    or per-cycle basis.

    Cyclical learning rate policy changes the learning rate after every batch.
    `step` should be called after a batch has been used for training.

    This class has three built-in policies, as put forth in the paper:

    * "triangular": A basic triangular cycle without amplitude scaling.
    * "triangular2": A basic triangular cycle that scales initial amplitude by
        half each cycle.
    * "exp_range": A cycle that scales initial amplitude by
        :math:`\text{gamma}^{\text{cycle iterations}}` at each cycle iteration.

    This class is similar to the `Pytorch CyclicLR LRS`_.

    Args:
        optimizer: The optimizer to schedule.
        base_lr: Initial learning rate which is the lower boundary in the cycle.
        max_lr: Upper learning rate boundaries in the cycle.
        step_size_up: Number of training iterations in the increasing half of a
            cycle.
        step_size_down: Number of training iterations in the decreasing half of
            a cycle.
        mode: One of {'triangular', 'triangular2', 'exp_range'}.
        gamma: Constant in 'exp_range' scaling function:
            gamma**(cycle iterations).
        scale_mode: {'cycle', 'iterations'} Defines whether scale_fn is
            evaluated on cycle number or cycle iterations.

    .. _Cyclical Learning Rates for Training Neural Networks:
            https://arxiv.org/abs/1506.01186

    .. _Pytorch CyclicLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.CyclicLR.html#torch.optim.lr_scheduler.CyclicLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        base_lr: float,
        max_lr: float,
        step_size_up: int = 2000,
        step_size_down: int = None,
        mode: str = "triangular",
        gamma: float = 1.0,
        scale_mode: str = "cycle",
    ):
        self.base_lr = base_lr
        self.max_lr = max_lr
        self.step_size_up = step_size_up
        self.step_size_down = step_size_down
        self.mode = mode
        self.gamma = gamma
        self.scale_mode = scale_mode

        if self.step_size_down == None:
            self.step_size_down = step_size_up

        super().__init__(optimizer, total_iters=None)

    def _triangular_scale_fn(self, x):  # pylint: disable=no-self-use
        return 1.0

    def _triangular2_scale_fn(self, x):  # pylint: disable=no-self-use
        return torch.div(
            torch.tensor(1, dtype=torch.float32, device=x.device),
            torch.pow(
                torch.tensor(2, dtype=torch.float32, device=x.device),
                torch.sub(x, 1),
            ),
        )

    def _exp_range_scale_fn(self, x):
        return torch.pow(
            torch.tensor(self.gamma, dtype=torch.float32, device=x.device), x
        )

    def set_scale_fn(self):
        """Sets the scaling function"""
        scale_fn = None
        if self.mode == 'triangular':
            scale_fn = self._triangular_scale_fn
            self.scale_mode = 'cycle'
        elif self.mode == 'triangular2':
            scale_fn = self._triangular2_scale_fn
            self.scale_mode = 'cycle'
        else:
            scale_fn = self._exp_range_scale_fn
            self.scale_mode = 'iterations'
        return scale_fn

    def _get_closed_form_lr(self):
        scale_fn = self.set_scale_fn()
        total_size = self.step_size_up + self.step_size_down
        step_ratio = self.step_size_up / total_size
        cycle = torch.floor(torch.div(self.last_epoch, total_size).add(1))
        x = torch.sub(torch.div(self.last_epoch, total_size), cycle).add(1)
        scale_factor = torch.where(
            x <= step_ratio,
            torch.div(x, step_ratio),
            torch.div(torch.sub(x, 1), torch.sub(step_ratio, 1)),
        )

        base_height = torch.mul((scale_factor), (self.max_lr - self.base_lr))
        if self.scale_mode == "cycle":
            return torch.add(
                torch.mul(base_height, scale_fn(cycle)), self.base_lr
            )
        else:
            return torch.add(
                torch.mul(base_height, scale_fn(self.last_epoch)),
                self.base_lr,
            )


class OneCycleLR(LRScheduler):
    r"""Sets the learning rate of each parameter group according to the
    1cycle learning rate policy. The 1cycle policy anneals the learning
    rate from an initial learning rate to some maximum learning rate and then
    from that maximum learning rate to some minimum learning rate much lower
    than the initial learning rate.
    This policy was initially described in the paper `Super-Convergence:
    Very Fast Training of Neural Networks Using Large Learning Rates`_.

    This scheduler is not chainable.

    This class is similar to the `Pytorch OneCycleLR LRS`_.

    Args:
        optimizer: The optimizer to schedule
        initial_learning_rate: Initial learning rate. Compared with PyTorch,
            this is equivalent to max_lr / div_factor.
        max_lr: Upper learning rate boundaries in the cycle.
        total_steps: The total number of steps in the cycle.
        pct_start: The percentage of the cycle (in number of steps) spent
            increasing the learning rate.
        final_div_factor: Determines the minimum learning rate via
            min_lr = initial_lr/final_div_factor.
        three_phase: If True, use a third phase of the schedule to annihilate
            the learning rate
        anneal_strategy: Specifies the annealing strategy:
            "cos" for cosine annealing, "linear" for linear annealing.

    .. _Super-Convergence\:
        Very Fast Training of Neural Networks Using Large Learning Rates:
        https://arxiv.org/abs/1708.07120

    .. _Pytorch OneCycleLR LRS:
        https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.OneCycleLR.html#torch.optim.lr_scheduler.OneCycleLR
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        initial_learning_rate: float,
        max_lr: float,
        total_steps: int = 1000,
        pct_start: float = 0.3,
        final_div_factor: float = 1e4,
        three_phase: bool = False,
        anneal_strategy: str = "cos",
    ):
        self.initial_learning_rate = initial_learning_rate
        self.max_lr = max_lr
        self.total_steps = total_steps
        self.pct_start = pct_start
        self.final_div_factor = final_div_factor
        self.three_phase = three_phase
        self.anneal_strategy = anneal_strategy
        super().__init__(optimizer, total_iters=None)

    def _annealing_cos(self, start, end, pct):  # pylint: disable=no-self-use
        "Cosine anneal from `start` to `end` as pct goes from 0.0 to 1.0."
        cos_out = torch.mul(pct, math.pi).cos().add(1)
        return torch.add(torch.mul(cos_out, ((start - end) / 2.0)), end)

    def _annealing_linear(self, start, end, pct):  # pylint: disable=no-self-use
        "Linearly anneal from `start` to `end` as pct goes from 0.0 to 1.0."
        return torch.add(torch.mul(pct, (end - start)), start)

    def _get_closed_form_lr(self):
        min_lr = self.initial_learning_rate / self.final_div_factor
        if self.three_phase:
            milestones = [
                self.pct_start * self.total_steps - 1,
                2 * self.pct_start * self.total_steps - 2,
                self.total_steps - 1,
            ]
            lr_start = [
                self.initial_learning_rate,
                self.max_lr,
                self.initial_learning_rate,
            ]
            lr_end = [self.max_lr, self.initial_learning_rate, min_lr]
        else:
            milestones = [
                self.pct_start * self.total_steps - 1,
                self.total_steps - 1,
            ]
            lr_start = [self.initial_learning_rate, self.max_lr]
            lr_end = [self.max_lr, min_lr]

        if self.anneal_strategy == "cos":
            anneal_func = self._annealing_cos
        else:
            anneal_func = self._annealing_linear

        start_step = 0
        pct = torch.div(
            torch.sub(self.last_epoch, start_step),
            (milestones[0] - start_step),
        )
        lr = anneal_func(lr_start[0], lr_end[0], pct)
        start_step = milestones[0]
        for idx, milestone in enumerate(milestones[1:]):
            pct = torch.div(
                torch.sub(self.last_epoch, start_step),
                (milestone - start_step),
            )
            lr = torch.where(
                self.last_epoch > milestones[idx],
                anneal_func(lr_start[idx + 1], lr_end[idx + 1], pct),
                lr,
            )
            start_step = milestone
        return lr


class ScalePerParamLR(LRScheduler):
    r"""Wrapper around the LRScheduler to scale the learning rate of
    each optimizer parameter group by the scaling factor `adjust_learning_rate`.
    Learning rate scaling is proposed in the Maximal Update Parameterization work
    that aids one-shot hyperparameter transfer from a smaller base model to larger
    models.
    It also serves a generic use case of layer-wise/param_group-wise adaptation
    of the learning rate.
    This wrapper doesn't work with ChainedLR scheduler.

    Args:
        optimizer: The optimizer to schedule
        scheduler: wrapped scheduler
    """

    def __init__(self, optimizer, scheduler):
        self.lr_adjustment_scalars = [
            param_group.get('adjust_learning_rate', 1.0)
            for param_group in optimizer.param_groups
        ]
        self._scheduler_nested = scheduler

        optimizer._lr_scheduler_registry.remove(scheduler)

        super().__init__(optimizer, total_iters=None)

    def state_dict(self):
        s = super().state_dict()
        s["_scheduler"] = self._scheduler_nested.state_dict()
        s.pop("_scheduler_nested", None)
        s["_scheduler"].pop("_get_lr_called_within_step", None)
        return s

    def load_state_dict(self, state_dict):
        super().load_state_dict(state_dict)
        _scheduler_dict = state_dict.pop('_scheduler')
        state_dict['_scheduler'] = _scheduler_dict
        self._scheduler_nested.load_state_dict(_scheduler_dict)
        self.optimizer._lr_scheduler_registry.remove(self._scheduler_nested)

    def increment_last_epoch(self, *args, **kwargs):
        """Increments the last_epoch of the scheduler whose milestone we are on"""
        super().increment_last_epoch()
        if self._step_count == 0:
            return
        self._scheduler_nested.increment_last_epoch()

    def get_lr(self):
        if not self._get_lr_called_within_step:
            warnings.warn(
                "To get the last learning rate computed by the scheduler, "
                "please use `get_last_lr()`."
            )
        lr_tensor = self._get_closed_form_lr()
        return [
            lr_tensor * self.lr_adjustment_scalars[group_idx]
            for group_idx, _ in enumerate(self.optimizer.param_groups)
        ]

    def _get_closed_form_lr(self):
        return self._scheduler_nested._get_closed_form_lr()


__all__ = ["LRScheduler"] + [
    cls.__name__
    for cls in retrieve_all_subclasses(
        LRScheduler, condition=lambda subcls: subcls.__module__ == __name__
    )
]
