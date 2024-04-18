from math import ceil, floor
from typing import Any, Dict, List, Literal, Tuple, Union

import torch
import torchvision.transforms.v2.functional as F
from detectools import Task
from detectools.formats import BatchedFormats, DetectionFormat
from detectools.models.base import BaseModel
from torch import Tensor
from ultralytics.cfg import get_cfg
from ultralytics.models.yolo.detect.train import DetectionModel
from ultralytics.nn.tasks import attempt_load_one_weight
from ultralytics.utils import DEFAULT_CFG


class YoloDetection(DetectionModel, BaseModel):

    def __init__(
        self,
        architecture: str = "yolov8m",
        num_classes: int = 1,
        pretrained=True,
        confidence_thr: float = 0.5,
        max_detection: int = 300,
        nms_threshold: float = 0.45,
        *args,
        **kwargs,
    ):
        """Load yolo architecture from ultralytics repository. If pretrained load the clasic pretrain model from ultralytics.

        Args:
            architecture (str) : Type of Yolo to load.
            pretrained (bool): to download model or not.
        """
        # assert Task mode is "instance_segmentation"
        assert (
            Task.mode == "detection"
        ), f"Task mode should be 'detection' to construct YoloDetection object, got {Task.mode}"
        # build model from ultralytics config
        super().__init__(f"{architecture}.yaml", nc=num_classes, *args, **kwargs)
        self.args = get_cfg(DEFAULT_CFG)
        self.criterion = self.init_criterion()
        self.confidence_thr = confidence_thr
        self.max_detection = max_detection
        self.nms_threshold = nms_threshold
        self.num_classes = num_classes
        # load weights from ultralytics repo if pretrained
        if pretrained:
            architecture = attempt_load_one_weight(
                f"{architecture}.pt",
            )
            self.load(architecture[0])

    # override
    def to_device(self, device: Literal["cpu", "cuda"]):
        """Send both model & criterion to device."""
        self.to(device)
        self.criterion = self.init_criterion()

    def prepare_image(self, images: Tensor) -> Tuple[int]:
        """Pad images if needed & return padding values.

        Args:
            images (Tensor): Batch_images.

        Returns:
            Tuple[int]: Padded images & coordinates.
        """
        # get borders padding
        coordinates = self.yolo_pad_requirements(images)
        # pad images
        images = F.pad(images, list(coordinates))
        return images, coordinates

    def prepare_target(self, targets: BatchedFormats) -> Tensor:
        """Transform detection target into yolo targets format.
        Args:
            target (Format): Detectools Target.
        Returns:
            (Tensor) targets in yolo shape.
        """
        # transfor boxes
        targets.apply("set_boxes_format", "CXCYWH")
        targets.apply("normalize")
        # get values
        targets: List[DetectionFormat] = targets.split()
        boxes = torch.cat([t.get("boxes") for t in targets])
        labels = torch.cat([t.get("labels") for t in targets])
        device = labels.device
        images_indices = torch.cat(
            [torch.full((t.size,), i, device=device) for i, t in enumerate(targets)]
        )
        # reshape data to fit YoloV8detection loss
        indexes = images_indices[..., None]
        classes = labels[..., None]

        batch_targets = {"batch_idx": indexes, "cls": classes, "bboxes": boxes}

        return batch_targets

    # override
    def prepare(
        self, images: Tensor, targets: BatchedFormats = None
    ) -> Union[Any, Tuple[Any]]:
        """Transform images and targets into model specific format for prediction & loss computation.

        Args:
            images: (Tensor): Batch images.
            targets (Format): Targets from DetectionDataset.

        Returns:
            (Union[Any, Tuple[Any]]) : In function of target input either:
                - Image prepared for model
                - Image prepared for model + Target prepared for model
        """

        (left, top, right, bottom) = self.yolo_pad_requirements(images)
        # pad images & target
        images = F.pad(images, list((left, top, right, bottom)))
        if targets:
            prepared_targets = targets.clone()
            # prepare targets for yolo
            prepared_targets.apply("pad", left, top, right, bottom)
            prepared_targets = self.prepare_target(prepared_targets)
            return images, prepared_targets
        else:
            return images

    def yolo_pad_requirements(
        self, input_object: Union[Tensor, DetectionFormat]
    ) -> List[int]:
        """Return values for padding to fit 'divisible by 32' requirement.

        Args:
            input_object (Union[Tensor, Format]): Batch images.
        """
        # get spatial size
        if isinstance(input_object, DetectionFormat):
            h, w = input_object.spatial_size
        elif isinstance(input_object, Tensor):
            h, w = input_object.shape[-2:]  # (H,W)
        # get pad values
        diff_h, diff_w = h % 32, w % 32
        pad_h = 32 - diff_h if diff_h > 0 else 0
        pad_w = 32 - diff_w if diff_w > 0 else 0
        # define padding for each border
        if pad_h or pad_w:
            half_h, half_w = pad_h / 2, pad_w / 2
            left, top, right, bottom = (
                ceil(half_w),
                ceil(half_h),
                floor(half_w),
                floor(half_h),
            )
        else:
            left, top, right, bottom = (0, 0, 0, 0)
        return (left, top, right, bottom)

    def retrieve_spatial_size(self, raw_outputs: List[Tensor]) -> Tuple[int]:
        """Retrieve image shape from raw_outputs and stride values.

        Args:
            raw_outputs (List[Tensor]): Yolo model output.

        Returns:
            Tuple[int]: H, W shape of input.
        """
        h = int(raw_outputs[0].shape[-2] * self.stride[0])
        w = int(raw_outputs[0].shape[-1] * self.stride[0])
        return (h, w)

    # override
    def build_results(
        self, raw_outputs: List[Tensor], prebuild_output: Tensor
    ) -> BatchedFormats:
        """Transform model outputs into Format for results.

        Args:
            raw_outputs (Any): Model outputs.
            prebuild_outptu (Tensor): Extracted boxes from yolo raw outputs.
        Returns:
            (Format): Model output as Format.
        """

        prebuild_output = prebuild_output.unbind()
        h, w = self.retrieve_spatial_size(raw_outputs)
        # create empty Format to merge batch results
        results = []
        # for each prediction
        for prediction in prebuild_output:
            # send pred in good pshape
            prediction = prediction.permute(1, 0)
            # get best class and corresponding score
            best_class = torch.argmax(prediction[:, 4:], dim=1)
            confidence = torch.max(prediction[:, 4:], dim=1)
            # gather box cxcywh coordinates
            boxes_coordinates = prediction[:, :4]
            # build result
            result = DetectionFormat(
                spatial_size=(h, w),
                boxes=boxes_coordinates,
                labels=best_class,
                scores=confidence.values,
                box_format="CXCYWH",
            )
            # convert boxes in coco
            result.set_boxes_format("XYWH")
            # objects selections
            result = result.confidence(self.confidence_thr)
            result = result.nms(self.nms_threshold)
            result = result.max_detections(self.max_detection)
            # stack batch results
            results.append(result)

        if len(results) == 0:
            results = DetectionFormat.empty((h, w))

        results = BatchedFormats(results)
        return results

    def compute_loss(
        self, raw_outputs: Any, targets: DetectionFormat
    ) -> Dict[str, Tensor]:
        """Compute loss with predictions & targets.

        Args:
            predictions (Any): Raw output of model.
            targets (Format): Prepared targets for loss.

        Returns:
            Dict[str, Tensor]: Loss dict with global loss (key: "loss") & sublosses.
        """
        loss, loss_detail = self.criterion(raw_outputs, targets)
        loss_dict = {
            "loss": loss,
            "loss_box": loss_detail[0],
            "loss_cls": loss_detail[1],
            "loss_dfl": loss_detail[2],
        }
        return loss_dict

    # override
    def run_forward(
        self,
        images: Tensor,
        targets: DetectionFormat,
        predict: bool = False,
    ) -> Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], DetectionFormat]]:
        """Either only compute loss from images or, if target pass, compute loss & return both images
        and results.

        Args:
            images (Tensor): Batch RGB images.
            target (Format): Batched Format.

        Returns:
            Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], Format]]: Loss Dict & otpionnaly Format.
        """
        assert predict == (
            not self.training
        ), f"Model mode should be equal to predict boolean, got {self.training} & {predict}"
        # prepare inputs
        prepared_images, prepared_targets = self.prepare(images, targets=targets)
        # run forward pass
        if self.training:
            raw_outputs = self(prepared_images)
        else:
            prebuild_output, raw_outputs = self(prepared_images)
        # compute loss
        loss_dict = self.compute_loss(raw_outputs, prepared_targets)
        # return predictions if needed
        if predict:
            predictions = self.build_results(raw_outputs, prebuild_output)
            left, top, _, _ = self.yolo_pad_requirements(images)
            h, w = images.shape[-2:]
            predictions.apply("crop", top, left, h, w)
            return loss_dict, predictions
        else:
            return loss_dict

    # override
    def get_predictions(self, images: Tensor) -> DetectionFormat:
        """Prepare images, Apply model forward pass and build results.

        Args:
            images (Tensor): RGB images Tensor.
            nms_thr (float): Threhsold for NMS algorithm.
            confidence_thr: Confidence threshold for predicted instances selection.
        Returns:
            (Format): predictions for images as Format.
        """
        self.eval()
        # get original spatial size
        ori_h, ori_w = images.shape[-2:]
        # pad images
        images, (left, top, _, _) = self.prepare_image(images)
        # predict
        prebuild_output, raw_outputs = self(images)
        results = self.build_results(raw_outputs, prebuild_output)
        # crop to back at original spatial size
        results.apply("crop", top, left, ori_h, ori_w)

        return results
