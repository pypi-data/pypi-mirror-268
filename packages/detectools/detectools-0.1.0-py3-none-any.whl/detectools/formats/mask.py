from __future__ import annotations

from torchvision.tv_tensors import Mask
from torch import Tensor
import torch
from torch import is_floating_point
from typing import Union, Any, Tuple, Literal
from torch.nn.functional import one_hot


class DetectMask():
    """Mask class for detectools. It inherits from Mask TV_Tensors contain methods to insure that detection data
    are well stored for instance segmentation objects."""

    def from_binary_masks(masks: Tensor) -> DetectMask:
        """Generate DetectMask from stack of binary masks (N,H,W)."""
        detect_mask = DetectMask(torch.zeros(masks.shape[-2:], device=masks.device))
        for i, m in enumerate(masks):
            detect_mask.add_binary_mask(m, i)
        return detect_mask

    def __init__(self, mask:Tensor):
        self._mask = mask.int()
    
    @property
    def device(self):
        return self._mask.device
        
    def to(self, device: Literal["cpu", "cuda"]):
        self._mask = self._mask.to(device)
        return self

    def reindex(self) -> Tensor:
        """Replace mask values such that mask values are in 0 - N range with 0 for background and
        1 - N indices of objects.

        Returns:
            Tensor: Object ids (0 - N-1 objects).
        """
        if not self.n_objects:
            return torch.tensor([])
        object_ids = torch.unique(self._mask[self._mask!=0]).int()
        new_ids = torch.tensor(range(1, torch.max(object_ids)+1), device=self._mask.device).int()
        idxs = torch.nonzero(self._mask.unsqueeze(-1) == object_ids, as_tuple=True)
        self._mask[idxs[:-1]] = new_ids[idxs[2]]

        return object_ids - 1
    
    def add_binary_mask(self, mask: Tensor, value: int = None):
        """Add a binary mask corresponding do one instance segmentation object.

            Args:
                value(int): value to assign to mask==1 in DetectMask. Default to None so value will be max of self +1.        
        """

        assert is_binary(mask), f"Mask to add is not binary."

        self_max = torch.max(self._mask)
        value = value if value else self_max + 1
        self._mask[mask==1] = self_max + 1
    
    def __getitem__(self, indexes) -> DetectMask:

        if isinstance(indexes, int):
            indexes = torch.tensor([indexes])
        elif isinstance(indexes, list):
            indexes = torch.tensor(indexes)
        elif isinstance(indexes, slice):
            indexes = torch.tensor(list(range(self.size))[indexes])

        if indexes.dtype == torch.bool:
            indexes = indexes.nonzero().flatten()
        
        get_mask = DetectMask(self._mask)
        retrieve_mask = torch.isin(get_mask._mask, indexes + 1) # 1 to avoid background 0
        get_mask = DetectMask(torch.where(retrieve_mask, get_mask._mask, 0))
        get_mask.reindex()

        return get_mask
    
    def __iter__(self):
        """Iterate over Mask return binary mask for each value in 1-N range with N objects. Do not iter over
        background class 0."""
        object_ids = torch.unique(self._mask)[torch.unique(self._mask)!=0]
        for x in object_ids:
            yield self[x-1]

    def to_binary_masks(self) -> Tensor:
        """Return one-hot encoded binary masks of shape (N, H, W) with one binary mask (0-1) for each
        of N objects. Do not return binary mask for background with value 0.

        Returns:
            Tensor: Binary masks.
        """
        self_values = torch.unique(self._mask)
        binary_masks = one_hot(self._mask.long()).permute(2, 0, 1)
        # remove background binary mask
        if 0 in self_values:
            binary_masks = binary_masks[1:]
        
        return binary_masks
    
    def __add__(self, mask: DetectMask, other_mask: DetectMask) -> DetectMask:
        """Concatenate masks stacked mask by managing values (positions of objects).

        Args:
            mask (Tensor): Mask with indexes for objects in mask.
            other_mask (Tensor): Mask with indexes for objects in other_mask
        """
        # get max index of mask
        mask_max = torch.max(mask._mask)
        other_mask._mask[other_mask._mask > 0] += mask_max
        # add max index to toher mask at nonzero positions
        mask._mask += other_mask._mask
        mask._mask[other_mask._mask > 0] = other_mask._mask[other_mask._mask > 0]

        return DetectMask(mask._mask)
    
    @property
    def n_objects(self):
        """Return number of objjects in mask"""
        return len(torch.unique(self._mask).nonzero())
    
    def merge(
    mask: DetectMask, other_mask: DetectMask, scores: Tensor, other_scores: Tensor
) -> Tuple[Tensor, ...]:
        """Merge 2 DetectMask with informations of scores. Objects masks are added in the  ascending order of scores such
        that lower score masks are overwritted by higer masks scores.

        Args:
            mask (DetectMask): Stacked mask.
            other_mask (DetectMask): Stacked_mask.
            scores (Tensor): Scores for objects in mask 1.
            other_scores (Tensor): Scores of objects in other mask.

        Returns:
            DetectMask: Merged DetectMask.
            Tensor: List of indices of stacked masks that are not overwritted in original values.
        """
        assert mask._mask.shape == other_mask._mask.shape, "Both mask should have the same shape."
        # add number of objects of mask 1 to mask values of masks 2 for nonzero values
        other_mask._mask[other_mask._mask > 0] += torch.max(mask._mask)

        # merge all scores
        merged_scores = torch.cat([scores, other_scores])
        _, indices = torch.sort(merged_scores)
        merged_mask = DetectMask(torch.zeros(mask._mask.shape, device=mask.device).long())
        value = 1
        valid_indices = []

        for i in indices:
            if i > torch.max(mask._mask):
                indice_mask = other_mask._mask[i] * value
            else:
                indice_mask = mask[i]._mask * value
            # do not add empty masks
            if indice_mask.sum() == 0:
                continue
            
            merged_mask._mask[indice_mask > 0] = indice_mask[indice_mask > 0]

            value += 1
            valid_indices.append(i)

        return merged_mask, torch.tensor(valid_indices)
        


def is_binary(mask: Tensor) -> bool:
    """Check if a mask is binary (values in 0 - 1).

    Args:
        mask (Tensor): Tensor to check.

    Returns:
        bool: True if mask is binary
    """
    binary = True
    if is_floating_point(mask):
        binary = False
    if mask.ndim != 2:
        binary = False
    is_in01 = torch.isin(torch.unique(mask), torch.tensor([0,1], device=mask.device))
    if False in is_in01:
        binary = False
    
    return binary
