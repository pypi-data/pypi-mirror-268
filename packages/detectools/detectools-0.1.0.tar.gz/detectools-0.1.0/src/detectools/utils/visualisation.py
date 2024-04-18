from typing import List, Union, Tuple

from detectools import COLORS
from detectools.formats import BaseFormat, BaseAnnotation, SegmentationAnnotation, SegmentationFormat
from torch import Tensor
from torchvision.transforms.v2 import ConvertBoundingBoxFormat
from torchvision.utils import draw_bounding_boxes, draw_segmentation_masks


def draw_object(image: Tensor, obj: BaseAnnotation, classes: List[str] = [], colors: List[Tuple[int, int, int]]=COLORS) -> Tensor:
    """Draw bounding boxe & mask to image.

    Args:
        image (Tensor): Tensor image (uint8 & RGB)
        obj (Union[Annotation]): Annotation to draw.
        classes ( List[str]) : Names of classes to draw.  Defaults to [].
        colors (List[Tuple[int, int, int]]): List of colors for visualisations.

    Returns:
        Tensor: Image with object box drawed on.
    """
    # convert box for torch drawing bb
    format_converter = ConvertBoundingBoxFormat("XYXY")
    # wrap in object data in list
    boxe = format_converter(obj.boxe)
    color = [colors[obj.label]]
    label = obj.label.item()
    # class is either name of class if passed of label.
    if classes:
        upstring = [f"{classes[label]}"]
    else:
        upstring = [f"{label}"]
    # if score in object write it next to class
    if obj.score:
        upstring += [f" - {round(obj.score, 2)}"]
    # draw object on image
    image = draw_bounding_boxes(image, boxe, upstring, color, width=4)

    if isinstance(obj, SegmentationAnnotation):
        image = draw_segmentation_masks(image, obj.masks)


    return image


def draw_objects(image: Tensor, objects: BaseFormat, classes: List[str] = [], colors: List[Tuple[int, int, int]]=COLORS):
    """Draw all bounding boxes of an object on image.

    Args:
        image (Tensor): Tensor image (uint8 & RGB)
        objects (DetectionTarget): DetectionTargets to draw.
        classes (List[str], optional): Names of classes to draw. Defaults to [].
        colors (List[Tuple[int, int, int]]): List of colors for visualisations.


    Returns:
        Tensor: Image with objects boxes drawed on.
    """
    # convert boxes format
    labels, boxes = objects.get("labels", "boxes")
    format_converter = ConvertBoundingBoxFormat("XYXY")
    boxes = format_converter(boxes)
    # either write class names if passed or labels.
    if classes:
        upstring = [f"{classes[label.item()]}" for label in labels]
    else:
        upstring = [f"{label}" for label in labels]
    # if scores draw it next to class
    if "scores" in objects:
        new_upstrings = []
        scores = objects.get("scores")
        for i, string in enumerate(upstring):
            new_upstrings.append(f"{string} - {round(scores[i].item(), 2)}")
        upstring = new_upstrings
    # set COLORS according to classes
    colors = [colors[label] for label in labels]
    # draw objects on image
    image = draw_bounding_boxes(image, boxes, upstring, colors, width=6)

    if isinstance(objects, SegmentationFormat) and objects.size != 0:
        masks = objects.get("masks").to_binary_masks()
        image = draw_segmentation_masks(image, masks.bool(), colors=colors, alpha=0.5)

    return image


def visualisation(
    image: Tensor,
    target: Union[BaseFormat, SegmentationFormat],
    classes: List[str] = [],
    colors: List[Tuple[int, int, int]]=COLORS
) -> Tensor:
    """Draw boxe(s) on image from DetectionTarget or DetectionObject.

    Args:
        image (Tensor): _description_
        objects (Union[DetectionTarget, DetectionObject]): _description_
        classes (List[str], optional): _description_. Defaults to [].
        colors (List[Tuple[int, int, int]]): List of colors for visualisations.
    Returns:
        Tensor: Image with objects boxes drawed on.
    """

    if isinstance(target, BaseAnnotation):
        image = draw_object(image, target, classes, colors)

    if isinstance(target, BaseFormat):
        if target.size > 0:
            image = draw_objects(image, target, classes, colors)

    return image
