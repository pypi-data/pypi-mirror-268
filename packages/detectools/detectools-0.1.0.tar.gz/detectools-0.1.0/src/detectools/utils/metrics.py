from typing import Any, Callable, Dict, List, Tuple

import torch
from torch import Tensor
from torchmetrics import Metric
from torchmetrics.classification import StatScores
from torchvision.ops import box_iou
from detectools import Task
from detectools.formats import Format


def match_boxes(
    prediction: Format, target: Format, iou_threshold: float = 0.5
) -> Tuple[Tensor, Tensor, Tensor, Tuple[Tensor, Tensor]]:
    """Match better prediction boxes candidates with target boxes. Return indexes of
    prediction and target boxes that match and compute statistics of detection quality (Tp, FP, FN).

    Args:
        prediction (Format): Prediction.
        target (Format): Target.
        iou_threshold (float, optional): IoU threshold to discard some matchs with overlapping < to thr. Defaults to 0.5.

    Returns:
        Tuple[Tensor, Tensor, Tensor, Tuple[Tensor, Tensor]]: Detection statsitics (TP, FN, FN)
        & prediction and target boxes indexes that match well.
    """
    # set box format to XYXY for torch box iou computation
    prediction.set_boxes_format("XYXY")
    target.set_boxes_format("XYXY")
    # extract boxes
    pred_boxes = prediction.get("boxes")
    target_boxes = target.get("boxes")
    # compute cross matrix of ious
    cross_ious = box_iou(pred_boxes, target_boxes)
    # boolean matrix of max pred iou == max target iou --> true positives candidates
    max_matchs = (
        torch.max(cross_ious, dim=1)[0][..., None]
        == torch.max(cross_ious, dim=0)[0][None, ...]
    ).view(cross_ious.shape)

    # true positive if iou of max_matchs > iou threshold
    tp = torch.sum((max_matchs > 0) & (cross_ious > iou_threshold))
    # false positive: all boxes with no match with targets
    fp = torch.sum(pred_boxes.shape[0] - torch.sum(tp))
    # false negative if target has no pred box with iou > threshold
    fn = torch.sum(torch.max(cross_ious, dim=0)[0] < 0.5)
    # tp pairs index
    pred_idxs, target_idxs = torch.where(
        (max_matchs > 0) & (cross_ious > iou_threshold)
    )
    # extract indexes
    pred_idxs = pred_idxs.tolist() if pred_idxs.nelement() > 0 else []
    target_idxs = target_idxs.tolist() if target_idxs.nelement() > 0 else []
    match_idxs = (torch.tensor(pred_idxs).long(), torch.tensor(target_idxs).long())

    return tp, fp, fn, match_idxs


# functionnals metrics
def f1score(tp, fp, tn, fn):
    return (2 * tp) / (2 * tp + fp + fn)


def precision(tp, fp, tn, fn):
    return (tp) / (tp + fp)


def recall(tp, fp, tn, fn):
    return (tp) / (tp + fn)


def iou(tp: Tensor, fp: Tensor, tn: Tensor, fn: Tensor) -> Tensor:
    """Compute IoU from statistics."""
    return tp / (tp + fp + fn)


def accuracy(tp: Tensor, fp: Tensor, tn: Tensor, fn: Tensor):
    """Compute accuracy from statistics."""
    return (tp + tn) / (tn + tp + fp + fn)


class DetectMetric(Metric):
    """Base class for custom detection metric with torchmetrics engine."""

    is_differentiable = None
    higher_is_better = True
    full_state_update: bool = False

    def __init__(
        self,
        func: Callable,
        iou_threshold: float = 0.5,  # to consider as TP or FP
        name: str = "DetectionMetric",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.add_state("tp", default=torch.tensor(0), dist_reduce_fx="sum")
        self.add_state("fp", default=torch.tensor(0), dist_reduce_fx="sum")
        self.add_state("fn", default=torch.tensor(0), dist_reduce_fx="sum")
        self.add_state("samplewise", default=[], dist_reduce_fx="cat")
        self.func = func
        self.iou_threshold = iou_threshold
        self.name = name

    def update(self, prediction: Format, target: Format):
        """Update internal states of metric."""

        # if no objects in prediction or target: stats are neutral (0)
        # else compute match box and stats
        if prediction.size != 0 and target.size != 0:
            tp, fp, fn, _ = match_boxes(prediction, target, self.iou_threshold)
        elif prediction.size != 0 and target.size == 0:
            tp, fp, fn, _ = 0, prediction.size, 0, None
        elif prediction.size == 0 and target.size != 0:
            tp, fp, fn, _ = 0, 0, target.size, None
        else:
            return

        self.tp += tp
        self.fp += fp
        self.fn += fn
        # None because of no tn in detection
        self.samplewise.append(self.func(tp, fp, None, fn))

    def compute(self) -> Dict[str, Tensor]:
        """Return metric computed with internal state.

        Returns:
             Dict[str, Tensor]: _description_
        """
        global_value = self.func(self.tp, self.fp, None, self.fn)
        samplewise_value = torch.mean(torch.tensor(self.samplewise))
        metric_dict = {"global": global_value, "samplewise": samplewise_value}

        return metric_dict


class ClassifMetric(Metric):
    """Child class of torchmetrics metrics for classification.
    Allow to take Format as inputs and return dict of metric."""

    def __init__(
        self,
        func: Callable,  # metric functionnal
        num_classes: int = 1,
        name: str = "ClassifMetric",
        **kwargs: Any,
    ):

        super().__init__(**kwargs)
        self.func = func
        self.task = "binary" if num_classes == 1 else "multiclass"
        self.nc = num_classes
        # use tm engine to get statistics (tp,tn,fp,fn,sup)
        self.stat_score = StatScores(
            task=self.task,
            multidim_average="samplewise",
            average="none",
            num_classes=num_classes,
        )
        self.add_state("stats", default=[], dist_reduce_fx="cat")
        self.name = name

    def update(self, prediction: Format, target: Format):
        """Update internal states."""
        # if no predictions or target, no classification evaluation
        if prediction.size == 0 or target.size == 0:
            return
        target_labels = target.get("labels")
        # match boxes
        _, _, _, (pred_idxs, target_idxs) = match_boxes(prediction, target)
        pred_idxs = pred_idxs.to(prediction.get_device())
        target_idxs = target_idxs.to(target.get_device())
        prediction = prediction[pred_idxs]
        target = target[target_idxs]
        # if no box match, add all targets in fn
        if prediction.size == 0:
            device = target.get("boxes").device
            class_stats = torch.zeros((self.nc, 5)).to(device)
            values = torch.tensor(
                [torch.sum(target_labels == i) for i in range(self.nc)]
            )
            class_stats[:, 4] = values
            self.stats.append(class_stats[None, ...])
            return
        # get labels
        pred_labels = prediction.get("labels")
        target_labels = target.get("labels")
        # if binary pass label 0 to 1
        if self.task == "binary":
            pred_labels += 1
            target_labels += 1
        # compute stats
        stats = self.stat_score(pred_labels[None, ...], target_labels[None, ...]).view(
            1, self.nc, 5
        )
        self.stats.append(stats)

    def global_micro_compute(self) -> Tensor:
        """Compute metric with global/micro averagging."""
        n_samples = len(self.stats)
        samples_stack = torch.cat(self.stats).view(n_samples, self.nc, 5)  # (N, NC, 5)
        # sum stats accross samples
        samples_stack = samples_stack.sum(dim=0)  # (NC, 5)
        # sum stats accross classes
        micro_stack = torch.sum(samples_stack, dim=0)  # (5,)
        # compute metric
        tp, fp, tn, fn, _ = micro_stack.unbind(0)
        return self.func(tp, fp, tn, fn)

    def global_macro_compute(self) -> Tuple[Tensor, Tensor]:
        """Compute metric with global/macro averraging.
        Return also metric/class tensor."""
        n_samples = len(self.stats)
        samples_stack = torch.cat(self.stats).view(n_samples, self.nc, 5)  # (N, NC, 5)
        # sum stats accross samples
        samples_stack = samples_stack.sum(dim=0)  # (NC, 5)
        # compute metric/class
        tp, fp, tn, fn, _ = samples_stack.unbind(1)
        class_metrics = self.func(tp, fp, tn, fn)  # (NC,)
        return torch.nanmean(class_metrics), class_metrics

    def samplewise_micro(self) -> Tensor:
        """Compute metric with samplewise/micro averagging."""
        n_samples = len(self.stats)
        samples_stack = torch.cat(self.stats).view(n_samples, self.nc, 5)  # (N, NC, 5))
        # sum stat accross classes
        samples_stack = samples_stack.sum(dim=1)  # (NC, 5)
        # compute metric/sample
        tp, fp, tn, fn, _ = samples_stack.unbind(dim=1)
        samples_metrics = self.func(tp, fp, tn, fn)
        # mean accross samples
        return torch.nanmean(samples_metrics)

    def samplewise_macro(self) -> Tensor:
        """Compute metric with samplewise/macro averagging."""
        n_samples = len(self.stats)
        samples_stack = torch.cat(self.stats).view(n_samples, self.nc, 5)  # (N, NC, 5)
        # compute metric/class/sample
        tp, fp, tn, fn, _ = samples_stack.unbind(2)
        class_metrics = self.func(tp, fp, tn, fn)  # (N,NC)
        # mean accross classes
        macro = torch.nanmean(class_metrics, dim=1)  # (N,)
        # mean accross samples
        macro_samplewise = torch.nanmean(macro, dim=0)

        return macro_samplewise

    def compute(self):
        """Comput metric with all averag strategy and return a dict with all values."""
        if not self.stats:
            return {self.name: torch.tensor(torch.nan)}
        # if binary no need for macro aggregation
        metric_dict = {}
        if self.task == "multiclass":
            # global micro
            global_micro = self.global_micro_compute()
            metric_dict.update({"_global_micro": global_micro})
            # global macro
            global_macro, class_metrics = self.global_macro_compute()
            classes_dict = {
                f"/cls_{i}": class_metrics[i] for i in range(class_metrics.nelement())
            }
            metric_dict.update({"_global_macro": global_macro})
            metric_dict.update(classes_dict)
            # samplewise micro
            samplewise_micro = self.samplewise_micro()
            metric_dict.update({"_samplewise_micro": samplewise_micro})
            # samplewise macro
            samplewise_macro = self.samplewise_macro()
            metric_dict.update({"_samplewise_macro": samplewise_macro})
        else:
            # global micro
            global_micro = self.global_micro_compute()
            metric_dict.update({"_global": global_micro})
            # samplewise micro
            samplewise_micro = self.samplewise_micro()
            metric_dict.update({"_samplewise": samplewise_micro})
            return metric_dict

        return metric_dict


class SemanticSegmentationMetric(ClassifMetric):
    """Child class of classification metric. Move from instance to semantic segmentation
    paradigm to provide stats based on classes masks (instead of objects).
    """

    def __init__(
        self,
        func: Callable,  # metric functionnal
        num_classes: int = 1,
        name: str = "ClassifMetric",
        **kwargs: Any,
    ):
        assert (
            Task.mode == "instance_segmentation"
        ), "lib mode must be instance_segmentation to use SemanticSegmentationMetric, please set mode by using Task.set_lib_mode() at the begining of script "
        # init from ClassifMetric and
        # redefine stat score num_classes for multiclass detection to include background as a class (+1 class)
        # Note that background is later removed in update (background is meaningless regarding instance segmentation) but important for stats calculations
        super().__init__(func, num_classes=num_classes, name=name, **kwargs)
        if num_classes > 1:
            self.stat_score.num_classes = num_classes + 1

    # override
    def update(self, prediction: Format, target: Format):
        """Convert target & prediction to semantic mask to compute stats in semantic segmentation paradigm. Update internal state."""
        # handling empty target
        if target.size == 0:
            semantic_target_mask = torch.zeros(target.spatial_size).to(self.device)
        else:
            target_mask = target.get("masks")._mask.clone()
            target_labels = target.get("labels").clone()
            target_obj_idx = torch.tensor(range(1, target_labels.nelement() + 1)).to(
                self.device
            )
            # convert object stacked mask to semantic
            semantic_target_mask = (
                torch.zeros(target_mask.shape).to(self.device).to(target_labels.dtype)
            )
            for cls in target_labels.unique():
                obj_filt = target_obj_idx[target_labels == cls]
                # cls +1 because detect classes start at 0 and 0 is background in semantic
                semantic_target_mask[torch.isin(target_mask, obj_filt)] = cls + 1
        # handling empty prediction
        if prediction.size == 0:
            semantic_prediction_mask = torch.zeros(prediction.spatial_size).to(
                self.device
            )
        else:
            prediction_mask = prediction.get("masks")._mask.clone()
            prediction_labels = prediction.get("labels").clone()
            prediction_obj_idx = torch.tensor(
                range(1, prediction_labels.nelement() + 1)
            ).to(self.device)
            # convert object stacked mask to semantic : all objects with given class replaced by their class
            semantic_prediction_mask = (
                torch.zeros(prediction_mask.shape)
                .to(self.device)
                .to(prediction_labels.dtype)
            )
            for cls in prediction_labels.unique():
                obj_filt = prediction_obj_idx[prediction_labels == cls]
                # cls +1 because detect classes start at 0 and 0 is background in semantic
                semantic_prediction_mask[torch.isin(prediction_mask, obj_filt)] = (
                    cls + 1
                )
        # add dummy dim for stat score
        flatpred = torch.flatten(semantic_prediction_mask)[None, :]
        flattarget = torch.flatten(semantic_target_mask)[None, :]
        if self.task == "binary":
            self.stats.append(self.stat_score(flatpred, flattarget))
        else:
            # for multiclass will remove the background scores to avoid crazy high scores
            self.stats.append(self.stat_score(flatpred, flattarget)[:, 1:, :])


class MetricCompose:
    """Wrap multiple DetectTM in a same object:
    - Merge metrics in same dictionnary output
    - Allow all metrics to be displayed on same graph.
    """

    def __init__(self, metrics: List[Metric], name="MetricCompose"):
        self.metrics = metrics
        self.name = name

    def update(self, prediction: Format, target: Format):
        """Update all metrics."""
        for metric in self.metrics:
            metric.update(prediction, target)

    def compute(self):
        """Compute on each metrics and merge metric dicts together."""
        metric_dict = {}
        for metric in self.metrics:
            subdict = metric.compute()
            subdict = {f"{metric.name}_{key}": value for key, value in subdict.items()}
            metric_dict.update(subdict)

        return metric_dict

    def reset(self):
        """Reset all metrics."""
        for metric in self.metrics:
            metric.reset()

    def __call__(self, prediction: Format, target: Format):
        """Call each metric and merge outptu dicts."""
        metric_dict = {}
        for metric in self.metrics:
            subdict = metric(prediction, target)
            subdict = {f"{metric.name}_{key}": value for key, value in subdict}
            metric_dict.update(subdict)

        return metric_dict
