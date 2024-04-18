from itertools import product
from typing import Dict, List, Literal, Tuple, Union
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
from computervisiontools import load_image, save_image
from segmentools import IMAGES_FOLDER
from segmentools.dataset import SegmentDataset
from segmentools.inference import Predictor
from segmentools.metrics import _available_metrics
from segmentools.utils.metrics import SegmentationMetric
from segmentools.utils.visualisation import apply_color_masks
from torch import Tensor
from torchmetrics.classification import ConfusionMatrix
from tqdm import tqdm
from xlsxwriter.workbook import Workbook

# from xlsxwriter.worksheet import Worksheet


class EvalDataset(SegmentDataset):
    """Child class of segment dataset to retrieve image_name in getitem method."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preprocessing = None

    def __getitem__(self, index: int) -> Tuple[Tensor, str]:
        image, target = super().__getitem__(index)
        name = self.images[index].name
        return image, target, name


class Evaluator:
    """Class to evaluate a model on a dataset."""

    def metrics_versions(self):
        """Return list of metrics , one for each metric fn * method values (2) * aggregation values (2)."""
        # get metrics
        available_metrics = _available_metrics()
        methods = ["global", "samplewise"]
        class_aggregation = ["micro", "macro"]
        # combine all parameters options
        combinations = product(available_metrics, methods, class_aggregation)
        # define metrics
        metrics = [
            M(
                num_classes=self.num_classes,
                method=method,
                class_aggregation=aggregation,
            )
            for M, method, aggregation in combinations
        ]
        return metrics

    def __init__(
        self,
        num_classes: int,
        evaluation_path: Union[str, Path],
        predictor: Predictor,
        dataset: EvalDataset,
        cls_names: dict = {},
        metrics: List[SegmentationMetric] = [],
        device="cpu",
        confusion_matrix_normalisation: Literal["all", "true", "none", "pred"] = "all",
    ):
        """
        Args:
            num_classes (int): Number of classes of the task.
            evaluation_path (str): Path to store evaluations results.
            predictor (Predictor): Predictore with inference hyperparameters & model.
            dataset (EvalDataset): EvalDataset on eval data.
            cls_names (dict) : Equivalences cls number and cls names as dict. For e.g : {0: "dog", 1: cat, etc.}. Default {} lead to cls names = cls number
            metrics (List[SegmentMetric], optional): List of metric needed for evaluation, defaults is [] and leads to all metrics used. Defaults to [].
            device (str, optional): Device to do inbference on. Defaults to "cpu".
            confusion_matrix_normalisation (Literal['all'; 'true', 'none','pred'], optional): On which axis process confusion matrix normalisation. Defaults to "all".
        """
        self.num_classes = num_classes
        # if no metrics passed, gather all metrics combinations
        if not metrics:
            metrics = self.metrics_versions()
        self.metrics = metrics
        self.device = device
        self.predictor = predictor
        self.predictor.to_device(self.device)
        self.dataset = dataset
        # wrap eval_path as pathlib Path
        self.eval_path = (
            evaluation_path
            if isinstance(evaluation_path, Path)
            else Path(evaluation_path)
        )
        # define class naming dict
        self.cls_naming = (
            cls_names if cls_names else {i: i for i in range(self.num_classes)}
        )
        # create dataframes to store metrics/image values
        self.sheets: List[pd.DataFrame] = []
        self.task = "binary" if num_classes == 1 else "multiclass"
        ## TODO rewrite confusion matrix and add full normalisation one
        # create confusion matrix & send to device
        if self.task == "binary":
            self.confusion_matrix = ConfusionMatrix(
                task=self.task, normalize=confusion_matrix_normalisation
            )
        elif self.task == "multiclass":
            self.confusion_matrix = ConfusionMatrix(
                task="multiclass",
                num_classes=num_classes,
                normalize=confusion_matrix_normalisation,
            )
        self.confusion_matrix.to(device)
        # define names of dataframes
        for metric in self.metrics:
            if self.task == "binary":
                columns = ["image", metric.name]
            else:
                columns = ["image"]
                columns.append(f"{metric.name}/micro_aggregated")
                columns.append(f"{metric.name}/macro_aggregated")
                for i in range(self.num_classes):
                    columns.append(f"{metric.name}/cls-{self.cls_naming[i]}")

            self.sheets.append(pd.DataFrame(columns=columns))

    def sample_eval(self, name: Tensor, prediction: Tensor, target: Tensor):
        """Process evaluation for one sample. Add row for image on each sheet.
        Plus update metrics for dataset evaluation.

        Args:
            name (Tensor): Name of image.
            prediction (Tensor): Image preediction.
            target (Tensor): Target.
        """
        # create dummy dim if batch = 1
        if prediction.ndim != 3:
            prediction = prediction[None, :]
        if target.ndim != 3:
            target = target[None, :]
        # iterate over all metrics
        for i, metric in enumerate(self.metrics):
            # update metric (save states) and compute samplewise using __call__ of torchmetrics Metrics
            metric_dict = metric(prediction, target)
            # fill pandas dataframe with each class value
            row = {"image": name}
            if self.task == "binary":
                upd = {metric.name: metric_dict["samplewise"].item()}
            else:
                upd = {
                    f"{metric.name}/micro_aggregated": metric_dict[
                        "samplewise_micro"
                    ].item(),
                    f"{metric.name}/macro_aggregated": metric_dict[
                        "samplewise_macro"
                    ].item(),
                }
            for j, cls_result in enumerate(self.sheets[i].columns[3:]):
                upd.update({cls_result: metric_dict[f"/{j}"].item()})

            # Add image row with corresponding values in dict
            row.update(upd)
            # gather corresponding sheet
            sheet = self.sheets[i]
            # add row to sheet
            sample_row = pd.DataFrame(row, index=[len(self.sheets[i])])
            sheet = pd.concat([sheet, sample_row], axis=0)
            self.sheets[i] = sheet

    def end_sheets(self):
        """Finalize sheets before writng in excel file. Compute mean and std over images."""
        for i, sheet in enumerate(self.sheets):
            # sort in descending order
            sheet = sheet.sort_values(sheet.columns[1], ascending=False).reindex()
            # compute means and std
            mean = np.nanmean(sheet[sheet.columns[1:]], axis=0)
            std = np.nanstd(sheet[sheet.columns[1:]], axis=0)
            # add both mean & std in datframe
            mean_row = {"image": "Mean"}
            std_row = {"image": "std"}
            for j, c in enumerate(sheet.columns[1:]):
                mean_row.update({c: mean[j]})
                std_row.update({c: std[j]})
            stats = pd.concat(
                [
                    pd.DataFrame(mean_row, index=[0]),
                    pd.DataFrame(std_row, index=[0]),
                ],
                ignore_index=True,
            )
            sheet = pd.concat([stats, sheet], ignore_index=True)
            self.sheets[i] = sheet

    def create_summary(self):
        """Create Summary sheet with metric value over dataset for all metrics."""
        # summary columns names
        df_rows = []
        for metric in self.metrics:
            metric_dict = metric.compute()
            summary_row = {"Metric": metric.name}
            if self.task == "binary":
                summary_row.update(
                    {
                        "global": metric_dict["global"].item(),
                        "samplewise": metric_dict["samplewise"].item(),
                    }
                )
            else:
                # update with all aggregation methods
                summary_row.update(
                    {
                        "global micro": metric_dict["global_micro"].item(),
                        "global macro": metric_dict["global_macro"].item(),
                        "samplewise micro": metric_dict["samplewise_micro"].item(),
                        "samplewise macro": metric_dict["samplewise_macro"].item(),
                    }
                )
                # update for every class
                summary_row.update(
                    {
                        f"cls-{self.cls_naming[i]}": metric_dict[f"/{i}"].item()
                        for i in range(self.num_classes)
                    }
                )
            df_rows.append(pd.DataFrame(summary_row, index=[0]))
        # create summary sheet
        self.summary_sheet = pd.concat(df_rows, ignore_index=True)

    def write_excel(self):
        """Export multi sheet writer into excel."""
        # create writer
        # TODO fix url writing on windows & linux with relatives paths.
        writer = pd.ExcelWriter(
            self.eval_path / "evaluation.xlsx",
            engine="xlsxwriter",
            engine_kwargs={"options": {"strings_to_urls": True}},
        )
        # send summary to writer
        self.summary_sheet.to_excel(writer, sheet_name="Summary", index=False)
        # send each metric sheet to writer & store sheet coordinates for outliers
        cells_coordinates = []
        for i, sheet in enumerate(self.sheets):
            metric = self.metrics[i]
            sheet_name = metric.name
            sheet.to_excel(writer, sheet_name=sheet_name, index=False)

        # add confusion matrix on summary sheet
        summary_sheet = writer.sheets["Summary"]
        summary_sheet.insert_image(14, 5, self.eval_path / "confusion_matrix.png")
        # close writer
        writer.close()

    def get_prediction(self, image: Tensor) -> Tensor:
        """Take image and return classes predictions.

        Args:
            image (Tensor): Image to predict

        Returns:
            Tensor: classes predictions/segmentation mask.
        """
        # send to device
        image = image.to(self.device)
        # get prediction
        prediction = self.predictor.predict(image)
        return prediction

    def get_visualisation(
        self, image: Tensor, prediction: Tensor, target: Tensor
    ) -> Tensor:
        """Return visualisation with concatenation of results for target and prediction.

        Args:
            image (Tensor): Raw rgb image.
            prediction (Tensor): Predicted Segmentation mask.
            target (Tensor): Target segmentation mask.

        Returns:
            Tensor: Tensor of both prediction adn target visualisations concatenate.
        """
        # create visualisation
        predict_visualisation = apply_color_masks(image, prediction)
        target_visualisation = apply_color_masks(image, target)
        visualisation = torch.cat([target_visualisation, predict_visualisation], axis=2)

        return visualisation

    def plot_confusion_matrix(self):
        """Normalize confusion matrix & plot to eval path."""

        conf_mat = torch.round(self.confusion_matrix.compute(), decimals=2)
        ax = plt.subplot()
        sns.heatmap(conf_mat.cpu().numpy(), annot=True, fmt="g", ax=ax)
        # labels, title and ticks
        ax.set_xlabel("Predicted labels")
        ax.set_ylabel("True labels")
        ax.set_title("Confusion Matrix")
        conf_mat_labels = 2 if self.num_classes == 1 else self.num_classes
        classes_labels = list(range(conf_mat_labels))
        ax.xaxis.set_ticklabels(classes_labels)
        ax.yaxis.set_ticklabels(classes_labels)
        plt.savefig(f"{self.eval_path}/confusion_matrix.png")

    def eval(self):
        """Run evaluation on dataset."""
        # disable graph computation
        torch.set_grad_enabled(False)
        for image, target, name in tqdm(self.dataset, desc="Evaluation"):
            assert isinstance(
                self.dataset, EvalDataset
            ), "dataset is not an instance of EvalDataset"
            # get raw image, prediction & visualisation
            raw_image = load_image(self.dataset.data_path / IMAGES_FOLDER / name)
            image = image.to(self.device)
            target = target.to(self.device)
            prediction = self.get_prediction(image)
            visualisation = self.get_visualisation(raw_image, prediction, target)
            # update confusion matrix
            self.confusion_matrix.update(prediction, target)
            # save visualisation
            save_image(visualisation, self.eval_path / "visualisations" / f"{name}")
            # get evaluation for sample
            self.sample_eval(name, prediction, target)

        # save confusion matrix & store it in excel
        self.plot_confusion_matrix()
        plt.savefig(f"{self.eval_path}/confusion_matrix.png")
        # end sheets preparation
        self.end_sheets()
        # create summary sheet
        self.create_summary()
        # write excel
        self.write_excel()
        torch.set_grad_enabled(True)
