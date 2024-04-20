from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import Any, Dict, Generator, List, Literal, Sequence, Tuple, Union

import torch
from torch import Tensor
from torchvision.ops import nms, remove_small_boxes
from torchvision.transforms.v2 import ConvertBoundingBoxFormat
from torchvision.tv_tensors import BoundingBoxes, Mask
from detectools.formats.mask import DetectMask


class BaseAnnotation(ABC):
    """Base class for annotations objects."""

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
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
        pass


class BaseFormat(ABC):
    """Base class for data formats in detectools. This base class is the parent class of DetectionFormat & InstanceFormat.
    Formats in detectool store target & results informations as tensors in the argument data (dict with key/Tensors.). Basic and advanced operations
    can be done directly onf formats objects (padding, cropping, NMS, etc..)."""

    spatial_size: Tuple[
        int, int
    ]  # Store the H, W image size corresponding to objects boxes/masks stored in BaseFormat.
    data: Dict[
        str, Tensor
    ]  # Store all values (labels, boxes/masks at least) corresponding to objects in an image.
    size: int  # Number of objects in image.
    box_format: Literal["XYWH", "XYXY", "CXCYWH"]  # format for bounding boxes.

    ### Class methods that returns a BaseFormat
    def from_coco(
        cls, coco_annotations: List[Dict[str, Any]], spatial_size: Tuple[int]
    ) -> BaseFormat:
        """Create a format from a list of COCO annotations.

        Args:
            coco_annotations (List[Dict[str, Any]]): List of annotations (from COCO json file or other COCO data structure).
            spatial_size (Tuple[int]): Dimension of corresponding image.

        Returns:
            BaseFormat: Format with COCO objects informations stored in data dict.
        """
        pass

    @abstractclassmethod
    def empty(spatial_size: Tuple[int]) -> BaseFormat:
        """Return an empty BaseFormat.

        Args:
            spatial_size (Tuple[int]): Spatial size for future objects in BaseFormat.

        Returns:
            BaseFormat: BaseFormat with no objects in.
        """
        pass

    def clone(self) -> BaseFormat:
        """Clone self and return identical BaseFormat with detached clones tensors of data.

        Returns:
            BaseFormat: Clone of self.
        """
        clone = type(self).empty(spatial_size=self.spatial_size)
        clone.size = self.size
        for key, value in self.data.items():
            if isinstance(value, DetectMask):
                clone.data[key] = DetectMask(value._mask.clone().detach())
            else:
                clone.data[key] = value.clone().detach()

        return clone

    ### Magic methods
    def __getitem__(self, indexes: Union[int, Sequence[int]]) -> BaseFormat:
        """Return a subset BaseFormat by keeping only elements of data dict values (tensors) at positions of indexes.

        Args:
            indexes (Union[int, Sequence[int]]): Indexes to slice objects data.

        Returns:
            BaseFormat: Format with n objects for n indexes in indexes.
        """
        sliced = self.clone()
        # slice each elements of data dict
        for key, value in self.data.items():
            # general case
            if not isinstance(value, BoundingBoxes):
                sliced.data[key] = value[indexes]

        # set size and box_format of sliced format
        sliced.size = sliced.get("labels").nelement()
        sliced.set_boxes_format(self.box_format)
        return sliced

    def __contains__(self, key: str) -> bool:
        """Return True if key in self.data dict, else False.

        Args:
            key (str): Data dictionnary key.
        Returns:
            bool: True if key in self.data else False.
        """
        return key in self.data.keys()

    def __iter__(self) -> Generator[BaseAnnotation]:
        """Iterate through BaseFormat and yield at each index i a BaseAnnotation object
        that contains all informations for object at position i."""

        for object_id in range(self.size):
            yield self.get_object(object_id)

    # Acessibility methods: get or set objects into BaseFormat
    def get_device(self) -> torch.device:
        """Verify that all tensors of data dict are on same device and return device."""
        devices = [value.device for value in self.data.values()]
        devices_set = set(devices)
        assert (
            len(devices_set) == 1
        ), f"All tensors on data dict should be on the same device, got {len(devices_set)} devices : {devices_set}."
        return list(devices_set)[0]

    def set_device(self, device: Union[torch.device, Literal["cuda", "cpu"]]):
        """Set all values in self.data dict to device."""
        for key, value in self.data.items():
            self.data[key] = value.to(device)

    def get(self, *keys: str) -> Union[Tensor, Tuple[Tensor]]:
        """Return data values for each key in *keys.
        Args:
            keys: Key(s) of self.data dict.
        Returns:
            Union[Tensor, Tuple[Tensor]]: Values for each keys.
        """

        outputs = []
        for key in keys:
            assert (
                key in self
            ), f"{key} should be in self.data, got only {list(self.data.keys())}."
            outputs.append(self.data[key])

        if len(outputs) > 1:
            output = tuple(outputs)
        else:
            output = outputs[0]  # single element

        return output

    def set(self, key: str, value: Tensor):
        """Set a new pair of key/value. Value should be of shape (N, ...) with N == self.size."""

        # get shape of new value and assert it's equal to self.size
        data_size = value.size()[0] if value.nelement() else 0
        assert (
            data_size == self.size
        ), f"New value size should be equal to self.size, got {data_size} and {self.size}."
        # assign value to key with correct device
        device = self.get_device()
        value = value.to(device)
        self.data[key] = value

    @abstractclassmethod
    def get_object(self, indice: int) -> BaseAnnotation:
        """Return a BaseAnnotation object at position indice."""
        pass

    # Methods that changes internal states of Formats
    @abstractclassmethod
    def crop(self, top: int, left: int, height: int, width: int):
        """Crop boxes and mask and update spatial size."""
        pass

    @abstractclassmethod
    def pad(self, left: int, top: int, right: int, bottom: int):
        """Pad boxes and mask and update spatial size."""
        pass

    def set_boxes_format(self, box_format: Literal["XYWH", "XYXY", "CXCYWH"]):
        """Change boxes format.

        Args:
            box_format (Literal[XYWH, XYXY, CXCYWH]): Format to set for boxes.
        """
        assert box_format in [
            "XYWH",
            "XYXY",
            "CXCYWH",
        ], f"box_format should be one of these [XYWH, XYXY, CXCYWH], got {box_format}."
        converter = ConvertBoundingBoxFormat(box_format)
        boxes = self.get("boxes")
        self.data["boxes"] = converter(boxes)
        self.format = box_format

    def convert_labels(self, convert_labels_dict: Dict[int, int]):
        """Convert labels of Format.

        Args:
            convert_dict (Dict[int,int]): Conversion dict for labels.
        """
        labels = self.get("labels")
        new_labels = self.get("labels")
        for key, value in convert_labels_dict.items():
            new_labels[labels == key] = value
        self.set("labels", new_labels)

    def normalize(self):
        """Normalize boxes values between 0 & 1 by dividing by spatial_size."""

        # normalize
        h, w = self.spatial_size
        boxes = self.get("boxes")
        boxes = boxes / torch.tensor([h, w, h, w], device=boxes.device)
        # recreate BoundingBoxes with normalized values
        boxes = BoundingBoxes(
            boxes,
            canvas_size=self.spatial_size,
            format=self.box_format,
            device=self.get_device(),
        )
        # set new boxes
        self.set("boxes", boxes)

    def rescale(self):
        """Rescale normalized boxes to true scale with spatial size."""
        boxes: BoundingBoxes = self.get("boxes")
        h, w = self.spatial_size
        boxes = (boxes * torch.tensor([h, w, h, w], device=boxes.device)).int()
        boxes = BoundingBoxes(
            boxes,
            canvas_size=self.spatial_size,
            format=self.box_format,
            device=self.get_device(),
        )
        self.set("boxes", boxes)

    # Method to process objects selection

    def sanitize(self, min_box_sides: float) -> BaseFormat:
        """Remove objects with boxes that have one of their sides smaller than min_box_sides."""
        format_boxes = ConvertBoundingBoxFormat("XYXY")
        boxes = format_boxes(self.get("boxes"))
        safe_objects_indexes = remove_small_boxes(boxes, min_box_sides)
        return self[safe_objects_indexes]

    def sort_by_scores(self, descending: bool = True) -> BaseFormat:
        """Sort objects by scores in decreasing order.

        Args:
            descending (bool, optional): To sort objects in descending order or ascending. Defaults to True.

        Returns:
            BaseFormat: Sorted format.
        """
        assert "scores" in self, "Format should contain scores to run sort_by_scores."
        indexes = torch.argsort(self.get("scores"), descending=descending)
        return self[indexes]

    def max_detections(self, maximum_objects: int) -> BaseFormat:
        """Retrieve N (maximum objects) with highest scores.

        Args:
            maximum_objects (int): Number of object to keep.
        Returns:
            BaseFormat: Format with N objects with highest scores.
        """
        assert "scores" in self, "Format should contain scores to run max_detection."
        return self.sort_by_scores()[:maximum_objects]

    def confidence(self, confidence_threshold: float = 0.5) -> BaseFormat:
        """Keep only objects with confidence above confidence_threshold.

        Args:
            confidence_threshold (float): confidence threshold. Defaut to 0.5.
        Returns:
            BaseFormat: Format with only objects with scores > confidence_thr.
        """
        assert "scores" in self, "Format should contain scores to run confidence."
        if self.size == 0:
            return self
        scores = self.get("scores")
        indexes = scores >= confidence_threshold
        return self[indexes]

    def nms(self, iou_threshold=0.5) -> BaseFormat:
        """Apply non maximum suppression algorithm to format.

        Args:
            iou_threshold (float, optional): Threshold to consider boxes as overlapping. Defaults to 0.5.
        Returns:
            BaseFormat: Format with objects selected by NMS.
        """
        assert "scores" in self, f"Format should contain scores to run nms."
        if self.size == 0:
            return self
        boxes, scores = self.get("boxes", "scores")
        format_convert = ConvertBoundingBoxFormat("XYXY")
        boxes: BoundingBoxes = format_convert(boxes)
        indexes = nms(
            boxes.float(),
            scores=scores,
            iou_threshold=iou_threshold,
        ).to(boxes.device).sort()[0]

        return self[indexes]

        # Method to export Formats objects

    def coco(self, image_id: int = 1, annotation_id: int = 1) -> List[Dict[str, Any]]:
        """Export data as COCO annotations.

        Args:
            image_id (int): id to write for "image_id" field in annotation dict.
            starting_ann_id (int): id to write on the first annotation dict "id" field. Following ones have id count from this one.

        Returns:
            List[Dict[str, Any]]: Coco annotations list for Format corresponding image.
        """

        coco_annotations = []
        for detection_object in self:
            coco_annotations.append(
                detection_object.object_to_coco(
                    image_id=image_id, annotation_id=annotation_id
                )
            )
            annotation_id += 1

        return coco_annotations

    # Protection methods

    def match(format1: BaseFormat, format2: BaseFormat):
        """Check if 2 Formats match for combinations:
        - check if both contains same keys on data dictionnary.
        - check if spatial size is equivalent.
        """

        keys1 = set(list(format1.data.keys()))
        keys2 = set(list(format2.data.keys()))
        return (keys1 == keys2) and format1.spatial_size == format2.spatial_size
