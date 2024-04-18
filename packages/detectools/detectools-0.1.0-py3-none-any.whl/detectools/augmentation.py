from typing import List, Tuple

import torchvision.transforms.v2 as T
from torch import Tensor
from torchvision.tv_tensors import BoundingBoxes, Image, Mask
import torch
from detectools.formats import Format, SegmentationFormat
from detectools.formats.mask import DetectMask


class Augmentation:
    def __init__(self, augmentations: List[T.Transform] = [], min_size: int = 1):
        """Generate Augmentation instance with list of transformations.

        Args:
            augmentations (List[T.Transform], optional): List of torchvision v2 transforms. Defaults to [].
        """
        # Make the compose of all the augmentations
        self.min_size = min_size
        self.transform = T.Compose(augmentations)

    def __call__(self, image: Tensor, target: Format) -> Tuple[Tensor, Format]:
        """Apply intern transfomrations to image & target and return augmented pair.

        Args:
            image (Tensor): RGB tensor image.
            target (Format): All targets for image.

        Returns:
            Tuple[Tensor, Format]: Pair of augmented image & Format.
        """
        # send image & annotations to TVTensors
        image = Image(image)
        labels, boxes = target.get("labels", "boxes")
        boxes: BoundingBoxes = target.get("boxes")
        # wrap into list
        originals = [image, labels, boxes]
        if isinstance(target, SegmentationFormat):
            originals.append(Mask(target.get("masks")._mask))
        # apply augmentation
        transformed = self.transform(*originals)

        # create augmented_target
        augmented_target = target.clone()
        augmented_image, augmented_labels, augmented_boxes = transformed[:3]
        augmented_boxes: BoundingBoxes
        spatial_size = augmented_boxes.canvas_size
        # pass augmented values in augmented target 
        augmented_target.set("boxes", augmented_boxes)
        augmented_target.set("labels", augmented_labels)
        augmented_target.spatial_size = spatial_size
        augmented_target.spatial_size = augmented_boxes.canvas_size
        
        if isinstance(augmented_target, SegmentationFormat):
            augmented_masks = DetectMask(transformed[3])
            keep_index = augmented_masks.reindex()
            augmented_target = augmented_target[keep_index]
            augmented_target.set("masks", augmented_masks)

        return augmented_image, augmented_target
