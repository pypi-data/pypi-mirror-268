from abc import abstractclassmethod
from typing import Any, Dict, Literal, Tuple, Union

from detectools.formats import BaseFormat, BatchedFormats
from torch import Tensor
from torch.nn import Module


class BaseModel(Module):
    """Abstract class for Detection models."""

    confidence_thr: float = 0.5
    max_detection: int = 300
    nms_threshold: float = 0.45
    num_classes: int = 1

    @classmethod
    def to_device(self, device: Literal["cpu", "cuda"]):
        """Send both model & all dependencies (like criterion) to device."""

    @classmethod
    def prepare(
        self, images: Tensor, targets: BaseFormat = None
    ) -> Union[Any, Tuple[Any]]:
        """Transform images and targets into model specific format for prediction & loss computation.

        Args:
            images: (Tensor): Batch images.
            targets (BaseFormat): Targets from DetectionDataset.

        Returns:
            (Union[Any, Tuple[Any]]) : In function of target input either:
                - Image prepared for model
                - Image prepared for model + Target prepared for model
        """

    @classmethod
    def build_results(self, raw_outputs: Any) -> BaseFormat:
        """Transform model outputs into BaseFormat for results.
        This function also apply instances selection on results according to args:

        - confidence_thr
        - max_detection
        - nms_threshold

        Args:
            raw_outputs (Any): Model outputs.
        Returns:
            (BaseFormat): Model output as BaseFormat.
        """

    @classmethod
    def get_predictions(self, images: Tensor) -> BaseFormat:
        """Prepare images, Apply model forward pass and build results.

        Args:
            images (Tensor): RGB images Tensor.
        Returns:
            (BaseFormat): predictions for images as BaseFormat.
        """

    @classmethod
    def run_forward(
        self, images: Tensor, targets: BaseFormat, predict: bool = False
    ) -> Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], BatchedFormats]]:
        """Either only compute loss from images or, if target pass, compute loss & return both images
        and results.

        Args:
            images (Tensor): Batch RGB images.
            target (BaseFormat): Batched BaseFormat.
            predict (bool): to return predictions or not.
            nms_thr (float): Threhsold for NMS algorithm.
            confidence_thr (float): Confidence threshold for predicted instances selection.

        Returns:
            Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], BaseFormat]]: Loss Dict & optionnaly BaseFormat.
        """
