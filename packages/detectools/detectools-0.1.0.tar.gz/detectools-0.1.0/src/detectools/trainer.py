import shutil
from pathlib import Path
from typing import Dict, List, Literal, Tuple

import torch
from torch import Tensor
from torch.optim import Optimizer
from torch.utils.tensorboard import SummaryWriter
from torchmetrics import Metric
from tqdm import tqdm

from detectools.dataset import DetectionLoader
from detectools.models.base import BaseModel
from detectools.formats import BatchedFormats
from detectools.utils.trainer import Aggregator


class Trainer:

    def __init__(
        self,
        model: BaseModel,
        otpimizer: Optimizer,
        log_dir: str = "",
        metrics: List[Metric] = [],
        device: Literal["cpu", "cuda"] = "cpu",
        nms_threshold: float = 0.45,
        confidence_threshold: float = 0.5,
    ):
        """Create Trainer object.

        Args:
            model (BaseModel): Model from detectools.
            otpimizer (Optimizer): Optimizer (from torch.optim).
            log_dir (str, optional): Path to store tensorboard logs. Defaults to "".
            metrics (List[Metric], optional): List of detectools metrics that will be computed at valid. Defaults to [].
            device (Literal['cpu', 'cuda'], optional): Device to use for trainning. Defaults to "cpu".
            nms_thr (float, optional): IoU threshold to consider 2 boxes as overlapping in NMS algorithm using for valid loop. Defaults to 0.45.
            confidence_thr (float, optional): Minimum confidence score for each predicted object to be kept, used for valid loop. Defaults to 0.5.
        """

        self.model = model
        self.model.to_device(device)
        self.optimizer = otpimizer
        metrics = [metric.to(device) for metric in metrics]
        self.metrics = metrics
        self.log_dir = log_dir
        self.device = device
        self.nms_threshold = nms_threshold
        self.confidence_threshold = confidence_threshold

        # create log dir and board for tensorboard
        if log_dir:
            # if log dir exist remove it
            if Path(log_dir).exists():
                shutil.rmtree(log_dir)

            Path(log_dir).mkdir(parents=True)
            self.board = SummaryWriter(log_dir)
        else:
            self.board = False

    def train_step(self, images: Tensor, targets: BatchedFormats) -> Dict[str, Tensor]:
        """Run train step, return loss dict.

        Args:
            images (Tensor): Batch images RGB
            target (BatchedFormats): Batched target.

        Returns:
        Dict [str, Tensor]: Dict of losses containing gobal loss : "loss"
        """

        loss_dict = self.model.run_forward(images, targets, predict=False)
        loss = loss_dict["loss"]
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        return loss_dict

    def compute_metrics(
        self, predictions: BatchedFormats, targets: BatchedFormats, batch_size: int
    ) -> Dict[str, Tensor]:
        """Compute metrics.

        Args:
            predictions (BatchedFormats): Predictions.
            targets (BatchedFormats): Targets.
            batch_size (int): Batch size to not forget image or predictions with no objects in splitting.

        Returns:
            Dict[Dict[str, float]]: Dict of metrics.
        """
        # split predictions to compute metric individual images # TODO make batchification possible
        splitted_predictions = predictions.split()
        splitted_targets = targets.split()
        # for each pair pred/target
        for i, target in enumerate(splitted_targets):
            pred = splitted_predictions[i]
            # update each metrics
            for metric in self.metrics:
                metric.update(pred, target)
        # after all updates recompute to get averaged values of metrics
        metric_dict = {}
        for metric in self.metrics:
            results = metric.compute()
            metric_dict.update({metric.name: results})

        return metric_dict

    def valid_step(
        self, images: Tensor, targets: BatchedFormats
    ) -> Tuple[Dict[str, Tensor], Dict[str, Dict[str, Tensor]]]:
        """Run train step, return loss dict.

        Args:
            images (Tensor): Batch images RGB
            target (BatchedFormats): Batched target.

        Returns:
        Tuple[Dict [str, Tensor], Dict [str, Tensor]]: Dict of losses containing gobal loss : "loss" and dict of metrics.
        """
        if self.model.training:
            self.model.eval()
        batch_size = images.shape[0]
        loss_dict, predictions = self.model.run_forward(images, targets, predict=True)
        predictions.apply("set_device",self.device)
        metrics = self.compute_metrics(predictions, targets, batch_size)
        return loss_dict, metrics

    def log_string(self, epoch_dict: Dict[str, Tensor]) -> str:
        """Get epoch dict and return string to display in terminal.

        Args:
            epoch_dict (Dict[str, Tensor]): Dict of metric & loss values to display.

        Returns:
            str: string to print with epoch values.
        """
        flattened_dict = epoch_dict.copy()
        for key, value in flattened_dict.items():
            if isinstance(value, dict):
                flattened_dict[key] = value[list(value.keys())[0]]

        log = ""
        for key, value in flattened_dict.items():
            log += f"{key} : {str(round(value.item(), 3))} "

        return log

    def epoch(
        self,
        loader: DetectionLoader,
        ep_number: int,
        mode: Literal["Train", "Valid"] = "Train",
        tag: str = "",
    ) -> Dict[str, Tensor]:
        """Run trainning epoch.

        Args:
            loader (DetectionLoader): DetectionLoader.
            ep_number (int): Epoch nb.

        Returns:
            Dict[str, Tensor]: Loss dict.
        """
        # create aggregator for loss averged accros samples
        loss_aggregator = Aggregator()
        iterator = tqdm(loader, total=len(loader), desc=f"Epoch {ep_number}/{tag}")
        # iterate over batches
        for images, targets, names in iterator:
            batch_size = images.shape[0]
            # send to device
            images = images.to(self.device)
            targets: BatchedFormats
            targets.apply("set_device", self.device)
            # gather loss & metrics (if valid)
            if mode == "Train":
                loss_dict = self.train_step(images, targets)
                loss_aggregator(loss_dict, batch_size)
                epoch_dict = loss_aggregator.compute()
            elif mode == "Valid":
                loss_dict, metric_dict = self.valid_step(images, targets)
                loss_aggregator(loss_dict, batch_size)
                epoch_dict = loss_aggregator.compute()
                epoch_dict.update(metric_dict)
            # extract str from log to display in terminal
            log_str = self.log_string(epoch_dict)
            iterator.set_postfix_str(f"{log_str}")
        # reset all metrics
        for metric in self.metrics:
            metric.reset()
        # write tensorboard
        if self.log_dir:
            for key, value in epoch_dict.items():
                if isinstance(value, dict):
                    self.board.add_scalars(key, value, ep_number)
                else:
                    self.board.add_scalars(key, {tag: value}, ep_number)

        return epoch_dict

    def train_epoch(
        self,
        loader: DetectionLoader,
        ep_number: int,
        tag: str = "Train",
        *args,
        **kwargs,
    ):
        torch.set_grad_enabled(True)
        self.model.train()
        epoch_dict = self.epoch(loader, ep_number, mode="Train", tag=tag, *args, **kwargs)
        return epoch_dict

    def valid_epoch(
        self,
        loader: DetectionLoader,
        ep_number: int,
        tag: str = "Valid",
        *args,
        **kwargs,
    ):
        torch.set_grad_enabled(False)
        self.model.eval()
        epoch_dict = self.epoch(loader, ep_number, mode="Valid", tag=tag, *args, **kwargs)
        torch.set_grad_enabled(True)
        return epoch_dict
