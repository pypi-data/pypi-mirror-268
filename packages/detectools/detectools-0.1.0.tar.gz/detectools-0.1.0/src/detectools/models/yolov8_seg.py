from math import ceil, floor
from typing import Any, Dict, List, Literal, Tuple, Union

import torch
import torchvision.transforms.v2.functional as F
from detectools import Task
from detectools.formats import BatchedFormats, SegmentationFormat
from detectools.models.base import BaseModel
from torch import Tensor
from torchvision.ops import nms
from torchvision.transforms.v2 import ConvertBoundingBoxFormat
from torchvision.tv_tensors import BoundingBoxes
from ultralytics.cfg import get_cfg
from ultralytics.nn.tasks import SegmentationModel, attempt_load_one_weight
from ultralytics.utils import DEFAULT_CFG
from ultralytics.utils.ops import scale_masks
from detectools.formats.mask import DetectMask


class Yolov8Segmentation(SegmentationModel, BaseModel):

    def __init__(
        self,
        architecture: str = "yolov8n-seg",
        pretrained=True,
        confidence_thr: float = 0.5,
        max_detection: int = 300,
        nms_threshold: float = 0.45,
        num_classes: int = 1,
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
            Task.mode == "instance_segmentation"
        ), f"Task mode should be 'instance_segmentation' to construct Yolov8Segmentation object, got {Task.mode}"
        # build model from ultralytics config
        super().__init__(f"{architecture}.yaml", nc=num_classes, *args, **kwargs)
        self.args = get_cfg(DEFAULT_CFG)
        self.criterion = self.init_criterion()
        self.num_classes = num_classes
        self.confidence_thr = confidence_thr
        self.max_detection = max_detection
        self.nms_threshold = nms_threshold
        # load weights from ultralytics repo if pretrained
        if pretrained:
            architecture = attempt_load_one_weight(
                f"{architecture}.pt",
            )
            self.load(architecture[0])

    def to_device(self, device: Literal["cpu", "cuda"]):
        """Send both model & criterion to device."""
        self.to(device)
        self.criterion = self.init_criterion()

    def prepare(
        self, images: Tensor, targets: BatchedFormats = None
    ) -> Union[Any, Tuple[Any]]:
        """Transform images and targets into model specific format for prediction & loss computation.

        Args:
            images: (Tensor): Batch images.
            targets (InstanceFormat): Targets from DetectionDataset.

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

    def build_results(
        self,
        raw_output: Tuple[Tensor, ...],
    ) -> BatchedFormats:
        """Build results from eval mode raw outputs of architecture.

        Args:
            raw_output (Tuple[Tensor, ...]): Raw output of eval mode.

        Returns:
            BatchedFormats: BatchedFormats with 1 format for each image passed in forward.
        """

        # TODO reduce size of this function by splitting in smaller ones
        # extract informations from raw_results
        boxes, cls_scores, mask_weights, protos = self.prebuild_output(raw_output)
        # gather device & spatila_size
        spatial_size = self.retrieve_spatial_size(raw_output)
        # init converter for nms
        box_converter = ConvertBoundingBoxFormat("XYXY")

        results = []
        # iter over image results
        for i, image_boxes in enumerate(boxes):
            # get image values
            image_boxes = boxes[i]
            image_cls_scores = cls_scores[i]
            image_mask_weights = mask_weights[i]
            image_protos = protos[i]
            # get best class and corresponding score
            image_cls_scores, best_class = torch.max(image_cls_scores, dim=1)
            # filter by confidence thr
            confidence_indexes = torch.nonzero(
                image_cls_scores > self.confidence_thr
            ).squeeze()
            # if only 1 value unsqueeze first dimension to get sequence
            if confidence_indexes.nelement() == 1:
                confidence_indexes = confidence_indexes.unsqueeze(0)
            # apply confidence to all values
            image_boxes = image_boxes[confidence_indexes]
            image_cls_scores = image_cls_scores[confidence_indexes]
            image_mask_weights = image_mask_weights[confidence_indexes]
            image_labels = best_class[confidence_indexes]
            # if no objects with good confidence return empty DetectionFormat
            if image_labels.nelement() == 0:
                result = SegmentationFormat.empty(spatial_size)
                results.append(result)
                continue

            # apply NMS on boxes to retrieve non overlapped objects
            image_boxes = BoundingBoxes(
                image_boxes,
                canvas_size=spatial_size,
                format="CXCYWH",
            )
            # send to xyxy
            image_boxes = box_converter(image_boxes)
            nms_indexes = nms(image_boxes, image_cls_scores, self.nms_threshold)
            # apply nms to all values
            image_boxes = image_boxes[nms_indexes]
            image_cls_scores = image_cls_scores[nms_indexes]
            image_mask_weights = image_mask_weights[nms_indexes]
            image_labels = image_labels[nms_indexes]
            # select N objects (N== self.max_detections) with highest scores
            indexes = torch.argsort(image_cls_scores)
            image_boxes = image_boxes[indexes][-self.max_detection:]
            image_cls_scores = image_cls_scores[indexes][-self.max_detection:]
            image_mask_weights = image_mask_weights[indexes][-self.max_detection:]
            image_labels = image_labels[indexes][-self.max_detection:]
            # compute binary masks per remaining obj
            image_masks = self.proto2mask(
                image_protos, image_mask_weights, image_boxes, spatial_size
            )
            # apply "logits" thresholding to mask (logit > 0.5 belong to object) # TODO pass this to model attribute
            image_masks = image_masks.gt_(0.5)
            # create DetectMask and remove objects with no mask
            segmentation_mask: DetectMask = DetectMask.from_binary_masks(image_masks.int())
            keep_indexes = segmentation_mask.reindex()
            if not keep_indexes.nelement():
                result = SegmentationFormat.empty(spatial_size)
                results.append(result)
                continue
            image_boxes = image_boxes[keep_indexes]
            image_cls_scores = image_cls_scores[keep_indexes]
            image_labels = image_labels[keep_indexes]
            # create SegmentationFormat
            result = SegmentationFormat(
                spatial_size,
                image_labels,
                image_boxes,
                segmentation_mask,
                scores=image_cls_scores,
                box_format="XYXY",
            )
            # send boxes to xywh
            result.set_boxes_format("XYWH")
            results.append(result)

        if len(results) == 0:
            results = [SegmentationFormat.empty(spatial_size)]

        results = BatchedFormats(results)
        return results

    def run_forward(
        self, images: Tensor, targets: BatchedFormats, predict: bool = False
    ) -> Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], BatchedFormats]]:
        """Either only compute loss from images or, if target pass, compute loss & return both images
        and results.

        Args:
            images (Tensor): Batch RGB images.
            target (DetectionTarget): Batched DetectionTarget.

        Returns:
            Union[Dict[str, Tensor], Tuple[Dict[str, Tensor], DetectionTarget]]: Loss Dict & otpionnaly SegmentationFormat.
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
            raw_outputs = self(prepared_images)
        # compute loss
        loss_dict = self.compute_loss(raw_outputs, prepared_targets)
        # return predictions if needed
        if predict:
            predictions = self.build_results(raw_outputs)
            return loss_dict, predictions
        else:
            return loss_dict

    def get_predictions(self, images: Tensor) -> BatchedFormats:
        """Prepare images, Apply model forward pass and build results.

        Args:
            images (Tensor): RGB images Tensor.
            nms_thr (float): Threhsold for NMS algorithm.
            confidence_thr: Confidence threshold for predicted instances selection.
        Returns:
            (BatchedFormats): Predictions for images as BatchedFormats.
        """
        self.eval()
        # get original spatial size
        ori_h, ori_w = images.shape[-2:]
        # pad images
        images, (left, top, _, _) = self.prepare_image(images)
        # predict
        raw_outputs = self(images)
        results = self.build_results(raw_outputs)
        # crop to back at original spatial size
        results.apply("crop", top, left, ori_h, ori_w)
        return results

    def prebuild_output(self, raw_output: Tuple[Tensor, ...]) -> Tuple[Tensor, ...]:
        """Unpack Yolov8-seg (eval mode) raw results.

        Args:
            raw_output (Tuple): Yolov8 raw eval mode results

        Returns:
            Tuple[Tensor]: boxes (N_batch, N_obj, cxcywh), cls_scores (N_batch, N_cls), mask_weights (N_batch, N_obj, 32), protos (N_batch, protos)
        """
        output0, output1 = raw_output
        output0 = output0.permute(0, 2, 1)  # permute in N_batch, N_obj, obj_length
        boxes = output0[:, :, 0:4]
        cls_indx = 4 + self.num_classes
        cls_scores = output0[:, :, 4:cls_indx]
        mask_weights = output0[:, :, -32:]
        protos = output1[2]
        return boxes, cls_scores, mask_weights, protos

    def prepare_image(self, images: Tensor) -> Tuple[Tensor, int]:
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

    def prepare_target(self, target: BatchedFormats) -> Dict[str, Tensor]:
        """Convert InstanceFormat to a yolov8-seg loss computation compatible format.

        Args:
            InstanceFormat (InstanceFormat): The target to transform.

        Returns:
            Dict: a dict containing all info as per yolov8-seg loss format.
        """
        target.apply("set_boxes_format", "CXCYWH")
        target.apply("normalize")
        targets: List[SegmentationFormat] = target.split()
        boxes = torch.cat([t.get("boxes") for t in targets])
        labels = torch.cat([t.get("labels") for t in targets])
        device = labels.device
        masks = torch.stack([t.get("masks")._mask for t in targets])
        images_indices = torch.cat(
            [torch.full((t.size,), i, device=device) for i, t in enumerate(targets)]
        )
        # put labels and batch_idx in yolo dormat : Tensor (N, 1)
        batch_idx = images_indices[:, None]
        classes = labels[:, None]
        yolotarget = {
            "masks": masks,
            "bboxes": boxes,
            "cls": classes,
            "batch_idx": batch_idx,
        }
        return yolotarget

    def yolo_pad_requirements(
        self, input_object: Union[Tensor, SegmentationFormat]
    ) -> Tuple[int, ...]:
        """Return values for padding to fit 'divisible by 32' requirement.

        Args:
            input_object (Union[Tensor, Format]): Batch images.
        """
        # get spatial size
        if isinstance(input_object, SegmentationFormat):
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

    def retrieve_spatial_size(self, raw_outputs: List[Tensor]) -> Tuple[int, int]:
        """Retrieve image shape from raw_outputs and stride values.

        Args:
            raw_outputs (List[Tensor]): Yolo model output.

        Returns:
            Tuple[int]: H, W shape of input.
        """
        if self.training:
            h = int(raw_outputs[0][0].shape[-2] * self.stride[0])
            w = int(raw_outputs[0][0].shape[-1] * self.stride[0])
        else:
            h = int(raw_outputs[1][0][0].shape[-2] * self.stride[0])
            w = int(raw_outputs[1][0][0].shape[-1] * self.stride[0])
        return (h, w)

    def compute_loss(self, predictions: Tuple, target: Dict) -> Dict[str, Tensor]:
        """Compute yolov8-seg loss.

        Args:
            predictions (Tuple): forward from yolo model
            target (Dict): batch target in yolo_format

        Returns:
            (Dict[str, Tensor]) : yolov8-seg loss and detailled losses.
        """
        loss, loss_detail = self.criterion(predictions, target)
        loss_dict = {
            "loss": loss,
            "loss_box": loss_detail[0],
            "loss_seg": loss_detail[1],
            "loss_cls": loss_detail[2],
            "loss_dfl": loss_detail[3],
        }
        return loss_dict

    def mask2yolo(self, mask: Tensor) -> Tensor:
        """convert stacked binary to yolo mask, i.e (1, h, w) with values in [0, ... , Nobjs]
        This shape is suitable for yolov8 loss.

        Args:
            mask (Tensor): stacked binary mask (1 per obj)

        Returns:
            (Tensor) : yolo mask
        """
        if mask.ndim < 3:
            mask = mask[None, :]
        reindexing = torch.tensor(range(1, mask.shape[0] + 1)).to(mask.device)
        # convert to yolomask: stacked h, w with values in [0, ..., Nobjs], 0 being absence of object
        yolomask, _ = torch.max(mask * reindexing[:, None, None], dim=0)
        return yolomask[None, :]

    def proto2mask(
        self, protos: Tensor, weights: Tensor, boxes: Tensor, shape: Tuple[int]
    ) -> Tensor:
        """combine protos and weights to get masks, then crop instances from boxes
            Useful in predictions
        Args:
            protos (Tensor) : normal is 32 sub masks
            weights (Tensor) : yolo weights (normal is 32)
            boxes (Tensor) : [N, 4] in xyxy
            shape : original image size (h, w)
        Returns:
            (Tensor) : yolo mask
        """
        c, mh, mw = protos.shape  # CHW
        masks = (weights @ protos.float().view(c, -1)).sigmoid().view(-1, mh, mw)
        masks: Tensor = scale_masks(masks[None], shape)[0]  # CHW
        for m in range(masks.shape[0]):
            xl, yl, xr, yr = boxes.int()[m]
            masks[m, 0:yl, :] = 0
            masks[m, yr:, :] = 0
            masks[m, :, 0:xl] = 0
            masks[m, :, xr:] = 0
        return masks
