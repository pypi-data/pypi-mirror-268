# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

import torch


def named_parameters_requiring_grad(model):
    """
    Returns the named paramters that should be passed to the optimizer
    i.e. are trainable because they require gradients.
    """
    for name, param in model.named_parameters():
        if param.requires_grad:
            yield name, param


def get_adaptive_lr_layers(model, lr_adjustment_layer_type):
    """
    Args:
        model: Pytorch model
        lr_adjustment_layer_type list: type of layer for which lr scaler is provided

    Returns:
        list: list of layer names for the given lr_adjustment_layer_type
    """
    adaptive_lr_layers = []
    for n, _ in model.named_parameters():
        if lr_adjustment_layer_type == 'decoder_kernel':
            if 'weight' in n:
                if 'linear' in n or 'dense' in n:
                    adaptive_lr_layers.append(n)
        elif lr_adjustment_layer_type == 'embedding':
            if 'embedding' in n and 'weight' in n:
                adaptive_lr_layers.append(n)
    return adaptive_lr_layers


def should_apply_weight_decay(model, param_name):
    """

    Args:
        model: Pytorch model
        param_name (torch.nn.Parameter): model param name

    Returns:
        bool: whether to apply weight decay for the give param_name
    """
    norm_modules = (
        torch.nn.LayerNorm,
        torch.nn.BatchNorm1d,
        torch.nn.BatchNorm2d,
        torch.nn.BatchNorm3d,
        torch.nn.InstanceNorm1d,
        torch.nn.InstanceNorm2d,
        torch.nn.InstanceNorm3d,
        torch.nn.GroupNorm,
        torch.nn.SyncBatchNorm,
    )
    if 'bias' in param_name:
        return False
    for name, module in model.named_modules():
        if name in param_name:
            if isinstance(module, norm_modules):
                return False
    return True


def partition_params_groups_with_weight_decay(
    model, param_groups, weight_decay
):
    """
    Args:
        model : Pytorch model
        param_groups (list): optimizer param_groups. Currently it will be just 1 group
        weight_decay (float): value of weight decay rate

    Returns:
        list: param_groups as list of dicts, split based on the weight_decay rate
    """
    refined_params_groups = []
    for _ in range(2 * len(param_groups)):
        refined_params_groups.append({"params": []})
    for idx, param_group_ in enumerate(param_groups):
        # Set group's weight decay params
        refined_params_groups[2 * idx]["weight_decay"] = weight_decay
        refined_params_groups[2 * idx + 1]["weight_decay"] = 0.0
        for name, param in param_group_["params"]:
            if should_apply_weight_decay(model, name):
                refined_params_groups[2 * idx]["params"].append((name, param))
            else:
                refined_params_groups[2 * idx + 1]["params"].append(
                    (name, param)
                )

    return refined_params_groups


def partition_params_groups_with_adjusted_lr(
    model,
    param_optimizer_grouped,
    lr_adjustment_layers,
    lr_adjustment_scalars,
):
    """
    Generates param_groups based on the lr_adjustment_layers
    Each lr adjustment layer_type will have a group asociated with it.

    Args:
        model : Pytorch model
        param_optimizer_grouped (list): param_groups before the split based on lr_adjustment_layers
        lr_adjustment_layers (list): list of layer types with different lr adjustment scalars
        lr_adjustment_scalars (list): lr adjustment scalars

    Returns:
        list: list of dicts of param groups
    """
    if lr_adjustment_layers:
        param_groups_with_lr_adjustment = []
        for param_group in param_optimizer_grouped:
            refined_param_groups = []
            for idx in range(len(lr_adjustment_layers) + 1):
                refined_param_groups.append(
                    {
                        "params": [],
                        "weight_decay": param_group["weight_decay"],
                        "adjust_learning_rate": lr_adjustment_scalars[idx]
                        if idx < len(lr_adjustment_layers)
                        else 1.0,
                    }
                )
            # collect all the params whose layer_type is not in lr_adjustment_layers
            # in the last param group
            adaptive_lr_layers = [
                get_adaptive_lr_layers(model, lr_adjust_layer_type_)
                for lr_adjust_layer_type_ in lr_adjustment_layers
            ]
            for name, param in param_group["params"]:
                param_in_adjust_lr_groups = False
                for idx, _ in enumerate(lr_adjustment_layers):
                    # check if param belongs to one of the adaptive lr layer types
                    if any(
                        adaptive_lr_layer_ in name
                        for adaptive_lr_layer_ in adaptive_lr_layers[idx]
                    ):
                        refined_param_groups[idx]["params"].append(
                            (name, param)
                        )
                        param_in_adjust_lr_groups = True
                # if param doesn't belongs to one of the adaptive lr layer types,
                # put it in the last refined_param_group
                if not param_in_adjust_lr_groups:
                    refined_param_groups[-1]["params"].append((name, param))

            # remove empty param groups
            refined_param_groups = [
                param_group_
                for param_group_ in refined_param_groups
                if param_group_["params"]
            ]
            param_groups_with_lr_adjustment.append(refined_param_groups)

    else:
        param_groups_with_lr_adjustment = param_optimizer_grouped

    # flatten the param group list if nested
    param_groups_with_lr_adjustment_flattened = []
    for groups in param_groups_with_lr_adjustment:
        if isinstance(groups, list):
            for group_ in groups:
                param_groups_with_lr_adjustment_flattened.append(group_)
        else:
            param_groups_with_lr_adjustment_flattened.append(groups)

    return param_groups_with_lr_adjustment_flattened
