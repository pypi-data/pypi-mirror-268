from itertools import product
from math import ceil, floor
from typing import Tuple
import torch
from torch import List, Tensor
from torchvision.transforms.v2.functional import crop, pad
from detectools.formats import Format
from detectools import Task
from detectools.formats.mask import DetectMask


def add_offset(image: Tensor, offset: int) -> Tensor:
    """Pad fix number of pixels around sides of image

    Args:
        image (Tensor): Image to pad.
        offset (int): Number of pixels to pad.

    Returns:
        Tensor: Image padded.
    """
    return pad(image, offset)


def remove_offset(image: Tensor, offset: int) -> Tensor:
    """Remove fix number of pixels on each side of image.

    Args:
        image (Tensor): Image.
        offset (int): Border size to remove.

    Returns:
        Tensor: Image without offset.
    """
    h, w = image.shape[-2:]
    new_h, new_w = h - 2 * offset, w - 2 * offset
    return crop(image, offset, offset, new_h, new_w)


def pad_to(image: Tensor, size: Tuple, fill_value: int = 0) -> Tensor:
    """Pad array with fill value to fit size with origin image in center of padded image.

    Args:
        image (Tensor): Image to be padded.
        size (Tuple, optional): Size to fit with padding.
        fill_value (int) : value to use for filling new pixels.
    Returns:
        Tensor: Padded image
    """
    # get sizes
    h, w = image.shape[-2:]
    padded_h, padded_w = size
    # compute difference
    delta_h = padded_h - h
    delta_w = padded_w - w
    # get left, top, right, bot thickness
    top, bot = ceil(delta_h / 2), floor(delta_h / 2)
    left, right = ceil(delta_w / 2), floor(delta_w / 2)
    # pad image
    padded = pad(image, padding=[left, top, right, bot], fill=fill_value)
    return padded


def crop_to(image: Tensor, size: Tuple) -> Tensor:
    """Crop array in center.

    Args:
        image (Tensor): Image to crop.
        size (Tuple): Cropped size.

    Returns:
        Tensor: image cropped.
    """
    # get sizes
    h, w = image.shape[-2:]
    cropped_h, cropped_w = size
    # compute delta of sizes
    delta_h = h - cropped_h
    delta_w = w - cropped_w
    # get top left coordinates
    top, left = ceil(delta_h / 2), ceil(delta_w / 2)
    # crop image at center
    cropped = crop(image, top, left, cropped_h, cropped_w)
    return cropped


def patchification(
    image: Tensor, patch_size: Tuple, overlap: float
) -> Tuple[Tensor, List[Tuple[int]], Tuple[int]]:
    """Cut image in patches according to patch size and overlapping.
    If needed padding is applied to fit patch size multiplicator on H & W.

    Args:
        image (Tensor): Large image to patchify.
        patch_size (Tuple): size of patch.
        overlap (float): Overlap between patches.
    Returns:
        Tuple[Tensor, List[Tuple[int]]]: Tensor of N pacthes & coordinates according to padded image.
    """
    # get shapes of image and pateches
    c, h, w = image.shape[-3:]
    h_patch, w_patch = patch_size
    # compute strides values
    stride_h = h_patch - round(h_patch * overlap)
    stride_w = w_patch - round(w_patch * overlap)
    # get number of pacthes on axis
    nb_h_patches = ceil(h / stride_h)
    nb_w_patches = ceil(w / stride_w)
    # padded image shape (H,W)
    h_padded = (nb_h_patches - 1) * stride_h + h_patch
    w_padded = (nb_w_patches - 1) * stride_w + w_patch
    # pad image
    padded_image = pad_to(image, size=(h_padded, w_padded))
    # get coordinates
    top_corners = range(0, nb_h_patches * stride_h, stride_h)
    left_corners = range(0, nb_w_patches * stride_w, stride_w)
    origins = list(product(top_corners, left_corners))
    # Create patches tensors
    patches = torch.zeros(
        (nb_h_patches * nb_w_patches, c, h_patch, w_patch), device=image.device
    )
    #  Fill the patches tensors
    for idx, (y, x) in enumerate(origins):
        patches[idx] = padded_image[:, y : y + h_patch, x : x + w_patch]

    return patches, origins, (h_padded, w_padded)

def unpatchification(
    predictions: List[Format],
    coordinates: List[Tuple[int]],
    spatial_size: Tuple[int],
) -> Format:
    """Build a prediction from multiple patch predictions and coordinates.

    Args:
        predictions (List[Format]): Patches predictions.
        coordinates (List[Tuple[int]]): List of Y, X coordinates.
        spatial_size (Tuple[int]): Size of merged prediction.
        nms_threshold (float): Iou Threshold to consider boxes as overlapping for NMS algorithm.
    Returns:
        (Format): Target of whole image.
    """
    h, w = spatial_size
    # remove 0 size patchs
    non_empty_predictions = [p for p in predictions if p.size > 0]
    if len(non_empty_predictions) == 0:
        return Format.empty(spatial_size=spatial_size)

    merged_patch = predictions[0]
    patch_h, patch_w = merged_patch.spatial_size
    merged_patch.pad(0, 0, w - patch_w, h - patch_h)
    # for each patch / coordinates
    for i, (y, x) in enumerate(coordinates[1:]):
        # pad patch target to fit spatial size
        patch_pred = predictions[i + 1]
        if patch_pred.size == 0:
            continue
        patch_h, patch_w = patch_pred.spatial_size
        patch_pred.pad(x, y, w - patch_w - x, h - (patch_h + y))
        boxes = torch.cat([merged_patch.get("boxes"), patch_pred.get("boxes")])
        scores = torch.cat([merged_patch.get("scores"), patch_pred.get("scores")])
        labels = torch.cat([merged_patch.get("labels"), patch_pred.get("labels")])
        values = [labels, boxes, scores]

        if Task.mode == "instance_segmentation":
            merged_mask, merged_scores = merged_patch.get("masks", "scores")
            patch_mask, patch_scores = patch_pred.get("masks", "scores")
            concat_mask, valid_indices = DetectMask.merge(
                merged_mask, patch_mask, merged_scores, patch_scores
            )
            boxes = boxes[valid_indices]
            scores = scores[valid_indices]
            labels = labels[valid_indices]
            values = [labels, boxes, concat_mask, scores]

        merged_patch = Format((h, w), *values, box_format="XYWH")
        merged_patch = merged_patch.nms()

    return merged_patch
