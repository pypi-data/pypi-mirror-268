from torchmetrics.detection import MeanAveragePrecision

import detectools.utils.metrics as M
from detectools.formats import Format


## Detection metrics


class DetectF1score(M.DetectMetric):

    def __init__(self, *args, **kwargs):
        super().__init__(func=M.f1score, name="DetectF1score", *args, **kwargs)


class DetectPrecision(M.DetectMetric):

    def __init__(self, *args, **kwargs):
        super().__init__(func=M.precision, name="DetectPrecision", *args, **kwargs)


class DetectRecall(M.DetectMetric):

    def __init__(self, *args, **kwargs):
        super().__init__(func=M.recall, name="DetectRecall", *args, **kwargs)


class MeanAP(MeanAveragePrecision):
    """Child class of torchmetrics MAP to take Format as input."""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = "MeanAP"

    def prepare_input(self, input: Format):
        """Transform Format in format of torchmetrics MAP"""
        boxes, labels = input.get(["boxes", "labels"])
        prepared = {"boxes": boxes, "labels": labels}
        if "scores" in input:
            prepared.update({"scores": input.get("scores")})
        return [prepared]

    def update(self, prediction: Format, target: Format):
        """Prepare inputs and call MAP"""
        prediction = self.prepare_input(prediction)
        target = self.prepare_input(target)
        super().update(prediction, target)


## classification metrics


class ClassifF1score(M.ClassifMetric):

    def __init__(self, *args, **kwargs):
        super().__init__(func=M.f1score, name="ClassifF1score", *args, **kwargs)
        
## semantic segmentation metrics

class SemanticF1score(M.SemanticSegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func=M.f1score, name="SemanticF1score", *args, **kwargs)
        
class SemanticIoU(M.SemanticSegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func=M.iou, name="SemanticIoU", *args, **kwargs)
        
class SemanticAccuracy(M.SemanticSegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func=M.accuracy, name="SemanticAccuracy", *args, **kwargs)
