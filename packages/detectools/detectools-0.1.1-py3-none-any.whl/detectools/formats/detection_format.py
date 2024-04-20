from __future__ import annotations

from typing import Any, Dict, List, Literal, Tuple, Union

import torch
from detectools import Task
from detectools.formats.base import BaseAnnotation, BaseFormat
from torch import Tensor
from torchvision.transforms.v2.functional import crop_bounding_boxes, pad_bounding_boxes
from torchvision.tv_tensors import BoundingBoxes


class DetectionAnnotation(BaseAnnotation):
    """Class to wrap informations of detection objects."""

    def __init__(
        self,
        spatial_size: Tuple[int],
        label: Tensor,
        boxe: Tensor,
        score: Tensor = None,
    ):

        self.boxe = boxe
        self.label = label
        self.spatial_size = spatial_size
        self.score = score

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
        annotation = {
            "id": annotation_id,
            "bbox": self.boxe.tolist(),
            "category_id": self.label.item(),
            "image_id": image_id,
        }
        if isinstance(self.score, Tensor):
            annotation["score"] = self.score.item()

        return annotation


class DetectionFormat(BaseFormat):
    """Data format for detection task. Contains only boxes & labels data."""

    # override
    def empty(spatial_size: Tuple[int]) -> DetectionFormat:
        """Return an empty DetectionFormat.

        Args:
            spatial_size (Tuple[int]): Spatial size for future objects in DetectionFormat.

        Returns:
            DetectionFormat: DetectionFormat with no objects in.
        """
        boxes = BoundingBoxes([[]], canvas_size=spatial_size, format="XYWH")
        labels = torch.tensor([])
        detection_format = DetectionFormat(
            spatial_size=spatial_size,
            labels=labels,
            boxes=boxes,
        )
        return detection_format

    # override
    def from_coco(
        coco_annotations: List[Dict[str, Any]], spatial_size: Tuple[int]
    ) -> DetectionFormat:
        """Create a DetectionFormat from a list of COCO annotations.

        Args:
            coco_annotations (List[Dict[str, Any]]): List of annotations (from COCO json file or other COCO data structure).
            spatial_size (Tuple[int]): Dimension of corresponding image.

        Returns:
            DetectionFormat: Format with COCO objects informations stored in data dict.
        """
        boxes = torch.tensor([ann["bbox"] for ann in coco_annotations])
        labels = torch.tensor([ann["category_id"] for ann in coco_annotations])
        detection_format = DetectionFormat(spatial_size, labels, boxes)
        return detection_format

    def __init__(
        self,
        spatial_size: Tensor,
        labels: Tensor,
        boxes: Tensor,
        scores: Tensor = None,
        box_format: Literal["XYWH", "XYXY", "CXCYWH"] = "XYWH",
    ):
        """Create DetectionFormat object.

        Args:
            boxes (Tensor): Sequence of sequences of 4 integers for bounding boxes coordinates.
            labels (Tensor): Sequence of label class value for each box.
            spatial_size (Tuple[int]): Spatial size (H, W) of corresponding images.
            scores (Tensor, optionnal): Confidence scores of objects.
            box_format (Literal["XYWH", "XYXY", "CXCYWH"]): Format of bounding boxes.
        """
        # assert Task mode is "instance_segmentation"
        assert (
            Task.mode == "detection"
        ), f"Task mode should be 'detection' to construct DetectionFormat object, got {Task.mode}."

        self.spatial_size = spatial_size
        self.size = labels.nelement()
        self.box_format = box_format
        # send to tv_tensor
        boxes: Tensor = BoundingBoxes(
            boxes.int(), canvas_size=spatial_size, format=box_format
        )
        # store all data in data dict
        self.data: Dict[str, Tensor] = {"boxes": boxes, "labels": labels}
        if scores != None:
            self.data["scores"] = scores

    def __getitem__(self, indexes: Union[int, Tensor]) -> DetectionFormat:
        """ "Return a subset DetectionFormat by keeping only elements of data dict values (tensors) at positions of indexes.

        Args:
            indexes (Union[int, Sequence[int]]): Indexes to slice objects data.

        Returns:
            DetectionFormat: Format with N objects for N indexess.
        """
        sliced = super().__getitem__(indexes)
        if "boxes" in self:
            boxes = self.get("boxes")[indexes]
            boxes = BoundingBoxes(
                boxes,
                canvas_size=self.spatial_size,
                format=self.box_format,
                device=self.get_device(),
            )
            sliced.data["boxes"] = boxes

        return sliced

    def get_object(self, indice: int) -> DetectionAnnotation:
        """Return a DetectionAnnotation object at position indice."""
        single_object_format = self[indice]
        bbox, label = single_object_format.get("boxes", "labels")
        detection_object = DetectionAnnotation(self.spatial_size, label, bbox.squeeze())
        if "scores" in single_object_format:
            detection_object.score = self.get("scores")

        return detection_object

    # Methods that changes internal states of Formats
    # override
    def crop(self, top: int, left: int, height: int, width: int):
        """Crop boxes and update spatial size."""
        if self.size == 0:
            self.spatial_size = (height, width)
            return self
        boxes = self.get("boxes")
        boxes, canvas_size = crop_bounding_boxes(
            boxes,
            format=self.box_format,
            top=top,
            left=left,
            height=height,
            width=width,
        )
        self.set(
            "boxes",
            BoundingBoxes(
                boxes,
                canvas_size=canvas_size,
                format=self.box_format,
                device=self.get_device(),
            ),
        )
        self.spatial_size = canvas_size

    # override
    def pad(self, left: int, top: int, right: int, bottom: int):
        """Pad boxes and update spatial size."""
        if self.size == 0:
            h, w = self.spatial_size
            self.spatial_size = (h + top + bottom, w + left + right)
            return

        boxes: BoundingBoxes = self.get("boxes")
        boxes, canvas_size = pad_bounding_boxes(
            boxes,
            self.box_format,
            self.spatial_size,
            list((left, top, right, bottom)),
        )
        self.set(
            "boxes",
            BoundingBoxes(
                boxes,
                canvas_size=canvas_size,
                format=self.box_format,
                device=self.get_device(),
            ),
        )
        self.spatial_size = canvas_size
