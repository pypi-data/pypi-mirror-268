from math import ceil
from typing import Callable, List, Literal, Tuple, Union

import detectools.utils.inference as I
from computervisiontools import load_image, save_image
from computervisiontools.preprocessing import build_preprocessing
from detectools.formats import Format
from detectools.models.base import BaseModel
from detectools.utils.visualisation import visualisation
from torch import Tensor
from torch.utils.data import DataLoader, TensorDataset


class InferenceImage:
    """Class to process patchification/unpatchification in inference pipeline."""

    def __init__(
        self,
        image: Tensor,
        patch_size=Tuple[int],
        overlap: float = 0.5,
    ):
        """Create Image for inference with pacthes.
        Args:
            image (Tensor): Image to
            patch_size (Tuple, optional): Size of patches wanted if patchification.
            overlap (float, optional): proprotion of overlapping wetween patches. Defaults to 0.3.
        """
        # store original image size
        self.size = image.shape[-2:]
        self.patch_size = patch_size
        self.overlap = overlap
        # process patchification and store patches coords and padded size
        self.patches, self.coordinates, self.padded_size = I.patchification(
            image, patch_size, overlap
        )

    def get_patches(self) -> TensorDataset:
        """Return patches as TensorDataset for batchification.

        Returns:
            TensorDataset: Patches Dataset.
        """
        return TensorDataset(self.patches)

    def rebuild_prediction(self, predictions: List[Format]) -> Format:
        """Merge predictions at corresponding positions the retroieve original image size by cropping predictions.

        Args:
            predictions (List[Format]): Patches predictions

        Returns:
            Format: Final result.
        """
        # merge patches predictions
        prediction = I.unpatchification(predictions, self.coordinates, self.padded_size)
        pad_h, pad_w = self.padded_size
        h, w = self.size
        # crop padded predictions to fit original size
        top, left, height, width = ceil((pad_h - h) / 2), ceil((pad_w - w) / 2), h, w
        prediction.crop(top, left, height, width)
        return prediction


class Predictor:
    """Class to wrap prediction process."""

    def __init__(
        self,
        model: BaseModel,
        patch_size: Tuple[int] = None,
        overlap: float = 0.0,
        nms_thr: float = 0.45,
        confidence_thr: float = 0.5,
        max_detection: int = 300,
        batch_size: int = 16,
        preprocessing: Callable = build_preprocessing(),
        device: Literal["cpu", "cuda"] = "cpu",
    ):
        """Build a Predictor.

        Args:
            model (BaseModel): Model from detectools.
            patch_size (Tuple[int], optional): the size of patch to predict on. Defaults to None so the patch size will be image shape.
            overlap (float, optional): To crop patches that overlap. Defaults to 0.0.
            nms_thr (float, optional): IoU threshold to consider 2 boxes as overlapping in NMS algorithm. Defaults to 0.45.
            confidence_thr (float, optional): Minimum confidence score for each predicted object to be kept. Defaults to 0.5.
            max_detection (int, optional): Maximum objects to keep in each prediction, the ones with higer scores are kept. Defaults to 300.
            batch_size (int, optional): Batch size for inference process, patches will be process in batch. Defaults to 16.
            preprocessing (Callable, optional): Callable that preprocess image images (i.e. Scale values to 0-1 then normalize with image weights channels mean). Defaults to build_preprocessing().
            device (Literal['cpu', 'cuda'], optional): Device to use for prediction. Defaults to "cpu".
        """

        self.model = model.eval()
        self.model.to_device(device)
        self.model.confidence_thr = confidence_thr
        self.model.nms_threshold = nms_thr
        self.model.max_detection = max_detection
        self.overlap = overlap
        self.nms_thr = nms_thr
        self.confidence_thr = confidence_thr
        self.batch_size = batch_size
        self.preprocessing = preprocessing
        self.device = device
        self.patch_size = patch_size

    def forward_pass(self, batch_patchs: Tensor) -> List[Format]:
        """Get predictions for patches.

        Args:
            batch_patchs (Tensor):Batch of image patches.

        Returns:
            List[Format]: Patches predictions.
        """
        predictions = self.model.get_predictions(batch_patchs)
        # split in N predictions for N == batch size (avoid forgetting empty predictions)
        return predictions.split()

    def predict(
        self, image: Union[Tensor, str], visualisation_path: str = ""
    ) -> Format:
        """Predict a segmentation mask from RGB image.

        Args:
            image (Union[Tensor, str]): either a RGB image as Tensor or a filepath to rgb image.
            visualisation_path (str, optional): path to save visualisation of the prediction. Defaults to "" (no visualisation).

        Returns:
            Format: Predictions..
        """
        # if image is a file load image as Tensor
        if isinstance(image, str):
            image = load_image(image)
        # send to device
        image = image.to(self.device)
        # apply preprocessing
        image_prepared: Tensor = self.preprocessing(image)
        # create inference image with patchification
        patch_size = self.patch_size if self.patch_size else image_prepared.shape[-2:]
        inference_image = InferenceImage(image_prepared, patch_size, self.overlap)
        # predict on patches
        patches = DataLoader(inference_image.get_patches(), batch_size=self.batch_size)
        batch_predictions = [self.forward_pass(batch[0]) for batch in patches]
        patches_prediction = [p for b in batch_predictions for p in b]
        # merge patches predictions
        image_prediction = inference_image.rebuild_prediction(patches_prediction)
        # re run nms for != patches objects overlapping
        if image_prediction.size > 0:
            image_prediction = image_prediction.nms(self.nms_thr)
        # do visualisation & save it
        if visualisation_path:
            visu = visualisation(image, image_prediction)
            save_image(visu, visualisation_path)

        return image_prediction
