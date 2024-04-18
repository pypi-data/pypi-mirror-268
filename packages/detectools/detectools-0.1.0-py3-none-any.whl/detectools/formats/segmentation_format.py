from __future__ import annotations

from typing import Any, Dict, List, Literal, Tuple, Union

import torch
from detectools import Task
from detectools.formats.detection_format import DetectionAnnotation, DetectionFormat
from detectools.utils.mask_utils import cocopolygons2mask, cocoseg2masks, mask2polygons
from torch import Tensor, is_floating_point
from torch.nn.functional import one_hot
from torchvision.ops import masks_to_boxes
from torchvision.transforms.v2 import ConvertBoundingBoxFormat
from torchvision.transforms.v2.functional import crop_mask, pad_mask
from torchvision.tv_tensors import BoundingBoxes, Mask
from detectools.formats.mask import DetectMask

class SegmentationAnnotation(DetectionAnnotation):
    """Class to wrap informations of detection objects."""

    def __init__(
        self,
        spatial_size: Tuple[int],
        label: Tensor,
        boxe: Tensor,
        mask: Tensor,
        score: Tensor = None,
    ):
        # assert Task mode is "instance_segmentation"
        assert (
            Task.mode == "instance_segmentation"
        ), f"Task mode should be 'instance_segmentation' to create SegmentationAnnotation, got {Task.mode}"
        # assert mask is a stacked class maks
        super().__init__(spatial_size, label, boxe, score)
        self.mask = mask

    def object_to_coco(
        self, annotation_id: int = 1, image_id: int = 1
    ) -> Dict[str, Any]:
        """Return COCO annotation dict from self.

        Args:
            annotation_id (int): id to write on "id" field in annotation dict.
            image_id (int): id to write for "image_id" field in annotation dict.

        Returns:
            Dict[str, Any]: COCO like annotation dict.
        """
        # convert mask tensor to polygons
        polygons, area = mask2polygons(self.mask)
        annotation = {
            "id": annotation_id,
            "bbox": self.boxe.tolist(),
            "segmentation": polygons,
            "area": area,
            "category_id": self.label.item(),
            "image_id": image_id,
        }
        if self.score:
            annotation["score"] = self.score.item()

        return annotation


class SegmentationFormat(DetectionFormat):
    """Data format for instance segmentation task. Contain labels, boxes & masks data."""

    # override
    def empty(spatial_size: Tuple[int]) -> SegmentationFormat:
        """Return an empty SegmentationFormat.

        Args:
            spatial_size (Tuple[int]): Spatial size for future objects in SegmentationFormat.

        Returns:
            SegmentationFormat: SegmentationFormat with no objects in.
        """
        boxes = torch.tensor([[]])
        labels = torch.tensor([])
        masks = Mask(torch.zeros((spatial_size)).int())  # mask full of 0
        detection_format = SegmentationFormat(
            spatial_size=spatial_size, labels=labels, boxes=boxes, masks=masks
        )
        return detection_format

    # override
    def from_coco(
        coco_annotations: List[Dict[str, Any]], spatial_size: Tuple[int]
    ) -> SegmentationFormat:
        """Create a format from a list of COCO annotations.

        Args:
            coco_annotations (List[Dict[str, Any]]): List of annotations (from COCO json file or other COCO data structure).
            spatial_size (Tuple[int]): Dimension of corresponding image.

        Returns:
            DetectionFormat: Format with COCO objects informations stored in data dict.
        """
        boxes = torch.tensor([ann["bbox"] for ann in coco_annotations])
        labels = torch.tensor([ann["category_id"] for ann in coco_annotations])
        masks: DetectMask = DetectMask(torch.zeros(spatial_size))
        # assign obj id to DetecMask
        for i, ann in enumerate(coco_annotations):
            ann_mask = cocoseg2masks(ann["segmentation"], spatial_size)
            masks.add_binary_mask(ann_mask.int(), i)
        # remove objects with no masks (also overwritted masks)
        keep_indexes = masks.reindex() - 1
        boxes = boxes[keep_indexes]
        labels = labels[keep_indexes]
        # build SegmentationFormat
        segmentation_format = SegmentationFormat(spatial_size, labels, boxes, masks)
        return segmentation_format

    def __init__(
        self,
        spatial_size: Tensor,
        labels: Tensor,
        boxes: Tensor,
        masks: Tensor,
        scores: Tensor = None,
        box_format: Literal["XYWH", "XYXY", "CXCYWH"] = "XYWH",
    ):

        # assert Task mode is "instance_segmentation"
        assert (
            Task.mode == "instance_segmentation"
        ), f"Task mode should be 'instance_segmentation' to create SegmentationFormat, got {Task.mode}"
        
        # create DetectMask
        if not isinstance(masks, DetectMask):
            masks = DetectMask(masks)
        
        if labels.nelement():
            keep_indexes = masks.reindex()
            boxes = boxes[keep_indexes]
            labels = labels[keep_indexes]
            # store all data in data dict
        boxes = BoundingBoxes(boxes.int(), canvas_size=spatial_size, format=box_format)
        self.data: Dict[str, Tensor] = {
            "boxes": boxes,
            "labels": labels,
            "masks": masks,
        }
        if isinstance(scores, Tensor):
            self.data["scores"] = scores[keep_indexes]

        self.box_format = box_format
        self.size = labels.nelement()
        self.spatial_size = spatial_size

    def set(self, key: str, value: Tensor):
        """Set a new pair of key/value. Value should be of shape (N, ...) with N == self.size.
        if key is "masks" and value is binary masks (N, H, W), size is N, if value is stacked mask (H,W). size is unstacked_masks.
        """

        # get shape of new value and assert it's equal to self.size
        if key == "masks":
            if not isinstance(value, DetectMask):
                value: DetectMask = DetectMask(value)
            data_size = value.n_objects
        else:  # value is not mask
            data_size = value.size()[0] if value.nelement() else 0

        assert (
            data_size == self.size
        ), f"New value size should be equal to self.size, got {data_size} and {self.size}."
        # assign value to key with correct device
        device = self.get_device()
        value = value.to(device)
        self.data[key] = value

    def get_object(self, indice: int) -> SegmentationAnnotation:
        """Return a SegmentationAnnotation object at position indice."""
        single_object_format = self[indice]
        bbox, label, mask = single_object_format.get("boxes", "labels", "masks")
        segmentation_object = SegmentationAnnotation(
            self.spatial_size, label, bbox.squeeze(), mask._mask
        )
        if "scores" in single_object_format:
            segmentation_object.score = self.get("scores")

        return segmentation_object

    # Methods that changes internal states of Formats
    def crop(self, top: int, left: int, height: int, width: int):
        """Crop boxes and mask and update spatial size."""
        self.spatial_size = (height, width)
        if self.size == 0:
            return self
        super().crop(top, left, height, width)
        masks: DetectMask = self.get("masks")
        cropped_masks = crop_mask(masks._mask, top=top, left=left, height=height, width=width)
        cropped_masks = DetectMask(cropped_masks)
        keep_indexes = cropped_masks.reindex()
        self.__dict__ = self[keep_indexes].__dict__.copy() # only copy dict to avoid duplicating object and loose masks change
        self.set("masks", cropped_masks)

    def pad(self, left: int, top: int, right: int, bottom: int):
        """Pad boxes and mask and update spatial size."""
        super().pad(left, top, right, bottom)
        if self.size == 0:
            return
        masks: DetectMask = self.get("masks")
        padded_masks = pad_mask(masks._mask, padding=[left, top, right, bottom])
        self.set("masks", padded_masks)

    def rescale_boxes_from_masks(self):
        """Iter over objects, for each masks compute all objects contours:
        - If there is only one contour rescale the box with the mask contour.
        - If there is more than one object duplicate label to have one mask, box and label for one object.
        """

        masks: DetectMask = self.get("masks")
        new_boxes = []
        new_masks: DetectMask = DetectMask(torch.zeros(self.spatial_size))
        # store indexes of objetc to duplicate for other data than masks and boxes
        duplicates_indexes = []
        for i, mask in enumerate(masks):
            # get coco polygons from mask
            polygons, _ = mask2polygons(mask._mask)
            # iter over polygons/object
            for polygon in polygons:
                sub_mask = cocopolygons2mask([polygon], self.spatial_size)
                box = masks_to_boxes(sub_mask.unsqueeze(0)).squeeze(0)
                new_boxes.append(box)
                new_masks.add_binary_mask(sub_mask)
                duplicates_indexes.append(i)

        # assign values
        new_boxes = BoundingBoxes(
            torch.stack(new_boxes), canvas_size=self.spatial_size, format="XYXY"
        )
        format_converter = ConvertBoundingBoxFormat(self.box_format)
        new_boxes: BoundingBoxes = format_converter(new_boxes)
        self.data["boxes"] = new_boxes
        self.data["masks"] = new_masks
        # add other data with duplicates
        for key, value in self.data.items():
            if key in ["boxes", "masks"]:
                continue
            self.data[key] = value[duplicates_indexes]
        # change format size
        self.size = new_boxes.shape[0]
