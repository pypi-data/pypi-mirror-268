# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provide an "optimizer" implementing static sparsity.
"""

import torch

import cerebras.pytorch as cstorch

from .base import SparsityAlgorithm


class Static(SparsityAlgorithm):
    def __init__(self, sparsity: float = None, **kwargs):
        """
        Args:
            sparsity: A float specifying the level of sparsity to apply to each parameter
        """
        if sparsity is not None and not (0.0 <= sparsity < 1.0):
            raise ValueError(
                f"Invalid sparsity level {sparsity}. Must be 0.0 <= s < 1.0"
            )

        super().__init__(sparsity, **kwargs)

    def csx_annotate_sparsity(self, param: "SparseParameter"):
        if cstorch.use_cs():
            # This simple scalar computation does not need to be traced
            with torch.device("cpu"):
                # We can just take the sparsity value at step 0
                # as the sparsity value is constant
                sparsity = self.sparsity[param.data](step=0).item()
                min_max_end = (sparsity, sparsity, sparsity)

            min_v, max_v, ending_v = min_max_end
            param.annotate("min_sparsity", min_v)
            param.annotate("max_sparsity", max_v)
            param.annotate("sparsity", ending_v)

    @torch.no_grad()
    def update(self, optimizer):
        # Ensure we've called apply_sparsity before update
        self._ensure_sparsity_applied()

        # Merely apply the mask to maintain initial sparsity pattern.
        self.prune_weights()
