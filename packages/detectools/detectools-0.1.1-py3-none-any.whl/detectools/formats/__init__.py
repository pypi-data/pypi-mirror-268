from __future__ import annotations

from typing import Any, List

from detectools import Task
from detectools.formats.base import BaseAnnotation, BaseFormat
from detectools.formats.detection_format import (DetectionAnnotation,
                                                 DetectionFormat)
from detectools.formats.segmentation_format import (SegmentationAnnotation,
                                                    SegmentationFormat)

__all__ = (
    "BaseAnnotation",
    "BaseFormat",
    "DetectionAnnotation",
    "DetectionFormat",
    "SegmentationAnnotation",
    "SegmentationFormat",
)  # allow simpler import


class Format(BaseFormat):

    def __new__(self, *args, **kwargs) -> BaseFormat:
        if Task.mode == "instance_segmentation":
            return SegmentationFormat(*args, **kwargs)
        else:
            return DetectionFormat(*args, **kwargs)

    def from_coco(*args, **kwargs) -> BaseFormat:
        if Task.mode == "instance_segmentation":
            return SegmentationFormat.from_coco(*args, **kwargs)
        else:
            return DetectionFormat.from_coco(*args, **kwargs)

    def empty(*args, **kwargs) -> BaseFormat:
        if Task.mode == "instance_segmentation":
            return SegmentationFormat.empty(*args, **kwargs)
        else:
            return DetectionFormat.empty(*args, **kwargs)


class Annotation(BaseAnnotation):

    def __new__(self, *args, **kwargs) -> BaseAnnotation:
        if Task.mode == "instance_segmentation":
            return SegmentationAnnotation(*args, **kwargs)
        else:
            return DetectionAnnotation(*args, **kwargs)


class BatchedFormats:
    """Wrap Formats in dict like object. Can apply methods to all inner formats."""

    def __init__(self, formats: List[BaseFormat]):

        n_formats = len(formats)
        # wrap formats in dict
        self.formats = dict(zip(range(n_formats), formats))
        self.set_spatial_size()

    def split(self) -> List[BaseFormat]:
        """Return a list of all inner formats."""
        return list(self.formats.values())

    def clone(self) -> BatchedFormats:
        """Return a clone of BatchedFormats."""
        clones = list(self.formats.values())
        clones = [c.clone() for c in clones]
        clone = BatchedFormats(clones)

        return clone

    def apply(self, method_name: str, *args, **kwargs):
        """Apply a Format method to all format in BatchedFormats.
        *args and *kwargs are all arguemnts to pass to the method used.

        Args:
            method (str): Name of Format specific method that return nothing.

        """
        for k, f in self.formats.items():
            # gather method object
            method = f.__getattribute__(method_name)
            # apply method to format
            output = method(*args, **kwargs)
            # if method output modified format, replace it
            if isinstance(output, BaseFormat):
                self.formats[k] = output

    def get_attributes(self, attribute: str, *args, **kwargs) -> List[Any]:
        """Return a list of Format attribute, one for each Format in BatchedFormats.

        Args:
            attribute (str): Attribute name.

        Returns:
            List[Any]: List of attribute values for each Format.
        """
        outputs = []
        for f in self.formats.values():
            # gather method object
            attr = f.__getattribute__(attribute)
            outputs.append(attr)

        return outputs

    def set_spatial_size(self):
        """Check if all internal Formats have the same spatial_size & set this spatial_size as BatchedFormat spatial_size."""

        spatial_sizes = [f.spatial_size for f in self.formats.values()]
        batch_spatial_size = set(spatial_sizes)
        assert (
            len(batch_spatial_size) == 1
        ), f"All spatial_sizes should be equal to batchify multiple Formats, got {batch_spatial_size}"
        self.spatial_size = list(batch_spatial_size)[0]
