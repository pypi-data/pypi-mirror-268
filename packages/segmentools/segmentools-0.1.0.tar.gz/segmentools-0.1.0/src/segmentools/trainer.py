import shutil
from pathlib import Path
from typing import Dict, List, Literal, Tuple, Union
from segmentools.utils.metrics import SegmentationMetric
import torch
from segmentools import activation, logits_to_mask
from segmentools.utils.trainning import Aggregator
from torch import Tensor
from torch.nn import Module
from torch.nn.modules.loss import _Loss
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm


class Trainer:
    """Container class for all trainning process."""

    def __init__(
        self,
        model: Module,
        num_classes: int,
        optimizer: Optimizer,
        loss: _Loss,
        metrics: List[SegmentationMetric] = [],
        device: Literal["cpu", "cuda"] = "cpu",
        log_dir: str = "",
    ):
        """Buil a Trainer instances.

        Args:
            model (Module): Neural network.
            num_classes (int): Number of classe of the task.
            optimizer (Optimizer): Torch optimizer.
            loss (_Loss): Loss function to compute loss.
            metrics (List[SegmentMetric], optional): List of SegmentMetric to compute for the valid epoch. Defaults to List[SegmentMetric].
            device (str, optional): Device to run on. Defaults to "cpu".
            log_dir (str, optional): Path to store tensorboard logs. Defaults to "".
        """

        self.model = model
        self.num_classes = num_classes
        self.optim = optimizer
        self.loss = loss
        # loss name to write on tensorboard
        self.loss_name = str(loss).replace("()", "")
        self.device = device
        self.metrics: List[SegmentationMetric] = metrics
        self.model.to(device)
        # create log dir and board for tensorboard
        if log_dir:
            # if log dir exist remove it
            if Path(log_dir).exists():
                shutil.rmtree(log_dir)

            Path(log_dir).mkdir(parents=True)
            self.board = SummaryWriter(log_dir)
        else:
            self.board = False

    def _forward_pass(self, image: Tensor) -> Tensor:
        """Apply forward pass and return logits.

        Args:
            image (Tensor): RGB image prepared for model.

        Returns:
            Tensor: Logits of class probabilities (after sigmoid or softmax).
        """
        return activation(self.model(image), num_classes=self.num_classes)

    def _backward_pass(self, loss: Tensor):
        """Run the bakcward pass by applying gradient.

        Args:
            loss (Tensor): Tensor of loss value.
        """
        # reset optimizer
        self.optim.zero_grad()
        # run gradient descent
        loss.backward()
        # apply gradient to weights
        self.optim.step()

    def _compute_loss(self, logits: Tensor, target: Tensor) -> Tensor:
        """Compute loss

        Args:
            logits (Tensor): Predictions as logits.
            targets (Tensor): Target.
        """
        return self.loss(logits, target)

    def _step(self, image: Tensor, target: Tensor, backward: False) -> Tensor:
        """Run a train step on sample.

        Args:
            image (Tensor): RGB image prepared for model.
            target (Tensor): Target.
        Returns:
            Tensor : loss value.
        """
        # train step
        logits = self._forward_pass(image)
        loss_value = self._compute_loss(logits, target)
        if backward:
            self._backward_pass(loss_value)

        return loss_value, logits

    def get_metrics(self) -> Tuple[Dict[str, float]]:
        """Compute mmetric for the sample.

        Args:
            prediction (Tensor): Predictions as classes (H, W)
            target (Tensor): Target (H, W)
        """
        # get both general values & detail (if multiclass) for each metrics.
        metric_global = {m.name: m.compute() for m in self.metrics}
        return metric_global

    def log_to_string(self, log: Dict[str, Tensor]):
        """Take a log dict and return string for terminal display."""
        log_str = ""
        for k, v in log.items():
            # if v is a metric dict extract global micro value for terminal
            if isinstance(v, dict):
                log_str += f", {k}: {str(round(list(v.values())[0].item(),4))}"
            else:
                log_str += f", {k}: {str(round(v.item(),4))}"

        log_str = log_str[2:]  # remove first ', '
        return log_str

    def _run_epoch(
        self,
        loader: DataLoader,
        epoch_number: int,
        epoch_tag: str,
        compute_metrics=False,
        backward=False,
    ):
        """Run an epoch. According on backward & compute metrics the epoch can be either a train or a valid epoch.

        Args:
            loader (DataLoader): DataLoader.
            epoch_number (int): Num of the epoch.
            epoch_tag (str): Prefix of the tqdm bar.
            compute_metrics (bool, optional): To compute or not metrics. Defaults to False.
            backward (bool, optional): To apply backward pass or not. Defaults to False.
        """

        # create an aggragator for loss value
        loss_aggregator = Aggregator()
        # create iterator with progressbar
        iterator = tqdm(
            loader, total=len(loader), desc=f"Epoch {epoch_number}/{epoch_tag}"
        )
        for batch_image, batch_target in iterator:
            # send to device
            batch_image = batch_image.to(self.device)
            batch_target = batch_target.to(self.device)
            # run train spet
            loss_value, logits = self._step(
                image=batch_image, target=batch_target, backward=backward
            )
            # add sample loss value to aggregator
            loss_aggregator.update(loss_value)
            # define a log dict for the step & store loss value
            epoch_dict = {self.loss_name: {epoch_tag: loss_aggregator.compute()}}
            # compute metrics if wanted & update log
            if compute_metrics:
                # get class predictions
                prediction = logits_to_mask(logits)
                # update each metric with sample evaluation
                for m in self.metrics:
                    m.update(prediction, batch_target)
                # gather metric results & update log
                metrics_global_values = self.get_metrics()
                epoch_dict.update(metrics_global_values)
            # pass log to a string to write on tqdm bar
            log_string = self.log_to_string(epoch_dict)
            iterator.set_postfix_str(f"{log_string}")

        epoch_loss = loss_aggregator.compute()
        # if board need to be updated
        if self.board:
            self.write_board(epoch_dict, epoch_nb=epoch_number)

        # reset both loss and metrics
        loss_aggregator.reset()
        for m in self.metrics:
            m.reset()

        return epoch_loss

    def train_epoch(self, train_loader: DataLoader, epoch_number: int):
        """Train epoch"""
        torch.set_grad_enabled(True)
        loss_value = self._run_epoch(
            train_loader, epoch_number, epoch_tag="Train", backward=True
        )
        return loss_value

    def valid_epoch(self, valid_loader: DataLoader, epoch_number: int):
        """Valid epoch"""
        # disable gradient computation
        torch.set_grad_enabled(False)
        loss_value = self._run_epoch(
            valid_loader, epoch_number, epoch_tag="Valid", compute_metrics=True
        )
        # retablish gradient computation
        torch.set_grad_enabled(True)
        return loss_value

    def write_board(
        self, scalars: Dict[str, Union[Tensor, Dict[str, Tensor]]], epoch_nb: int
    ):
        """Add scalars to tensorboard.

        Args:
            scalars (Dict[str, Union[Tensor, Dict[str,Tensor]]]): List of dict, one dict for each metric/loss to write on board.
            epoch_nb (int): num of the epoch.
        """
        for k, v in scalars.items():
            # if there is a lower level of metric detail write multiple scalars on same board (i.e. multiclass metric)
            if isinstance(v, dict):
                self.board.add_scalars(k, v, global_step=epoch_nb)
            # else write only the correspondig value
            else:
                self.board.add_scalar(k, v, global_step=epoch_nb)
