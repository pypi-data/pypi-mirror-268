from __future__ import annotations

from copy import deepcopy
from typing import Callable, Dict, List, Literal, Tuple, Union

import torch
from torch import Tensor
from torchmetrics import Metric, StatScores


def f1_score(tp: Tensor, fp: Tensor, tn: Tensor, fn: Tensor) -> Tensor:
    """Compute F1 score from statistics."""
    return 2 * tp / (2 * tp + fp + fn)


def iou(tp: Tensor, fp: Tensor, tn: Tensor, fn: Tensor) -> Tensor:
    """Compute IoU from statistics."""
    return tp / (tp + fp + fn)


def accuracy(tp: Tensor, fp: Tensor, tn: Tensor, fn: Tensor):
    """Compute accuracy from statistics."""
    return (tp + tn) / (tn + tp + fp + fn)


class SegmentationMetric(Metric):
    """Child class of torchmetrics metrics for segmentation.
    Allow to take segmentools format as input
    save for each sample tp, fp, fn for each class in self.stats to compute metrics in compute
    """

    is_differentiable = None
    higher_is_better = True
    full_state_update: bool = False

    def __init__(
        self,
        func: Callable,
        num_classes: int = 1,
        name: str = "SegmentationMetric",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.num_classes = num_classes
        self.task = "binary" if num_classes == 1 else "multiclass"
        self.add_state("stats", default=[], dist_reduce_fx="cat")
        self.func = func
        self.name = name
        self.stat_score = StatScores(
            task=self.task,
            multidim_average="samplewise",
            average="none",
            num_classes=num_classes,
        )

    def update(self, prediction: Tensor, target: Tensor):
        """update internal states."""
        # redefine
        if prediction.ndim != 3:
            prediction = prediction[None, :]
        if target.ndim != 3:
            target = target[None, :]
        # flatten batched preds and targets masks into (N_batch, flattened pred/target)
        flatpreds = torch.flatten(prediction.clone(), start_dim=1).unsqueeze(1)
        flattarget = torch.flatten(target.clone(), start_dim=1).unsqueeze(1)
        # use StatScores from tm to get tp, fp, tn, fn, sup and append to state "stats"
        for t in range(flatpreds.shape[0]):
            stats = self.stat_score(flatpreds[t], flattarget[t])
            # reshape to obtain tensor of shape (1, NC, 5) to be later computed in different methods
            stats = stats.view(1, self.num_classes, 5)
            self.stats.append(stats)

    def global_micro_compute(self) -> Tensor:
        """Compute metric using self.func with global/micro averaging."""
        samples_stack = torch.cat(self.stats, dim=0)  # (N, NC, 5)
        # sum stats across samples
        samples_stack = samples_stack.sum(dim=0)  # (NC, 5)
        # sum stats accross classes
        micro_stack = torch.sum(samples_stack, dim=0)  # (5,)
        # compute metric
        tp, fp, tn, fn, _ = micro_stack.unbind(0)
        return self.func(tp, fp, tn, fn)

    def global_macro_compute(self) -> Tuple[Tensor, Tensor]:
        """Compute metric with global/macro averraging.
        Return also metric/class tensor."""
        samples_stack = torch.cat(self.stats, dim=0)  # (N, NC, 5)
        samples_stack = samples_stack.sum(dim=0)  # (NC, 5)
        # compute metric/class
        tp, fp, tn, fn, _ = samples_stack.unbind(1)
        class_metrics = self.func(tp, fp, tn, fn)  # (NC,)
        return torch.nanmean(class_metrics), class_metrics

    def samplewise_micro_compute(self) -> Tensor:
        """Compute metric with samplewise/micro averagging."""
        # sum stat accross classes
        samples_stack = torch.cat(self.stats, dim=0)  # (N, NC, 5)
        samples_stack = samples_stack.sum(dim=1)  # (N, 5)
        # compute metric/sample
        tp, fp, tn, fn, _ = samples_stack.unbind(dim=1)
        samples_metrics = self.func(tp, fp, tn, fn)
        # mean accross samples
        return torch.nanmean(samples_metrics)

    def samplewise_macro_compute(self) -> Tensor:
        """Compute metric with samplewise/macro averagging."""
        samples_stack = torch.cat(self.stats, dim=0)  # (N, NC, 5)
        # compute metric/class/sample
        tp, fp, tn, fn, _ = samples_stack.unbind(2)
        class_metrics = self.func(tp, fp, tn, fn)  # (N,NC)
        # mean accross classes
        macro = torch.nanmean(class_metrics, dim=1)  # (N,)
        # mean accross samples
        macro_samplewise = torch.nanmean(macro, dim=0)
        return macro_samplewise

    def compute(self):
        """Comput metric with all 4 averag strategy and return a dict with all values."""
        metric_dict = {}
        if self.task == "binary":
            # global micro
            global_micro = self.global_micro_compute()
            metric_dict.update({"global": global_micro})
            # samplewise micro
            samplewise_micro = self.samplewise_micro_compute()
            metric_dict.update({"samplewise": samplewise_micro})
        else:
            # global micro compute
            global_micro = self.global_micro_compute()
            # global macro compute
            global_macro, class_metrics = self.global_macro_compute()
            classes_dict = {
                f"/{i}": (
                    class_metrics[i]
                    if class_metrics.ndim != 0
                    else class_metrics.item()
                )
                for i in range(class_metrics.nelement())
            }

            # write only global macro + class wise for accuracy : 4 modalities are equal
            if self.name == "accuracy":
                metric_dict.update({"global": global_macro})
                metric_dict.update(classes_dict)
                return metric_dict

            # samplewise_macro / micro compute
            samplewise_macro = self.samplewise_macro_compute()
            samplewise_micro = self.samplewise_micro_compute()

            metric_dict.update({"global_micro": global_micro})
            metric_dict.update({"global_macro": global_macro})
            metric_dict.update(classes_dict)
            metric_dict.update({"samplewise_micro": samplewise_micro})
            metric_dict.update({"samplewise_macro": samplewise_macro})

        return metric_dict
