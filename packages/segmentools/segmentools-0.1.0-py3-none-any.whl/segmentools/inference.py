from typing import Callable, Literal, Tuple, Union

import segmentools.utils.inference as I
import torch
from computervisiontools import load_image, save_image
from computervisiontools.preprocessing import build_preprocessing
from segmentools import activation, logits_to_mask
from segmentools.utils.visualisation import visualisation
from torch import Tensor
from torch.nn import Module
from torch.utils.data import DataLoader, TensorDataset


class InferenceImage:
    """Class to process Image for inference. It provides methods fore patchification & unpatchification."""

    def __init__(
        self,
        image: Tensor,
        patch_size=Tuple[int],
        overlap: float = 0.0,
        smoothing: Literal["uniform", "gaussian"] = "uniform",
        operator: Literal["min", "avg", "max"] = "avg",
    ):
        """Create Image for inference with pacthes.

        Args:
            image (Tensor): Image to
            patch_size (Tuple, optional): Size of patches wanted if patchification.
            overlap (float, optional): proprotion of overlapping wetween patches. Defaults to 0.3.
            operator (Literal['min', 'avg', 'max'], optional): Operator to aggragate overlapping predictions from overlapping patches. Defaults to 'avg'.
            smoothing (Literal['uniform','gaussian'], optional): To weight or not the prediction patches importance for averaging aggregator. Defaults to "uniform".
        """
        self.size = image.shape[-2:]
        self.patch_size = patch_size
        self.overlap = overlap
        self.smoothing = smoothing
        self.operator = operator
        # process patchification with overlap & patch size
        # patchification may need to proceed with padding, patchification return value of
        # padded image to rebuild after with the correct size
        self.patches, self.coordinates, self.padded_size = I.patchification(
            image, patch_size, overlap
        )

    def get_patches(self) -> TensorDataset:
        """Return patches as TensorDataset for batchification.

        Returns:
            TensorDataset: Patches Dataset.
        """
        return TensorDataset(self.patches)

    def rebuild(self, patches: Tensor) -> Tensor:
        """Rebuild array of patches at origin size with applying aggragation operator over patches overlaps
        & smoothing of values.

        Args:
            patches (Tensor): Pacthes.

        Returns:
            Tensor: Array after rebuild from patches.
        """
        padded = I.unpatchification(
            patches, self.coordinates, self.padded_size, self.operator, self.smoothing
        )
        # crop rebuild array to origin size.
        array = I.crop_to(padded, self.size)
        return array


class Predictor:
    def __init__(
        self,
        model: Module,
        patch_size: Tuple,
        preprocessing: Callable = build_preprocessing(),
        overlap: float = 0.3,
        operator: Literal["min", "avg", "max"] = "avg",
        smoothing: Literal["uniform", "gaussian"] = "uniform",
        offset: int = 100,
        binary_threshold: float = 0.5,
        batch_size: int = 32,
        device="cpu",
    ):
        """Build Predictor.

        Args:
            model (Module): Model to practice inference.
            preprocessing: preprocessing to apply on image before running forward pass. efaults to build_preprocessing().
            patch_size (Tuple, optional): Size of patches wanted if patchification.
            overlap (float, optional): proprotion of overlapping wetween patches. Defaults to 0.3.
            operator (Literal['min', 'avg', 'max'], optional): Operator to aggragate overlapping predictions from overlapping patches. Defaults to 'avg'.
            smoothing (Literal['uniform','gaussian'], optional): To weight or not the prediction patches importance for averaging aggregator. Defaults to "uniform".
            offset (int, optional): To primarly pad (and how much) or not orin image to avoid border effects. Defaults to 100.
            binary_threshold (float, optional): Value to threshold with for binary segmentation tasks. Defaults to 0.5.
            device (str, optional): On whic device to precess with prediction. Defaults to "cpu".
        """
        self.model = model
        self.preprocessing = preprocessing
        self.patch_size = patch_size
        self.operator = operator
        self.smoothing = smoothing
        self.overlap = overlap
        self.offset = offset
        self.binary_threshold = binary_threshold
        self.device = device
        self.model.to(device)
        self.model.eval()
        self.batch_size = batch_size

    def to_device(self, device: Literal["cpu", "cuda"]):
        """Send model to device and change device attribute.

        Args:
            device (_type_): _description_
        """
        self.device = device
        self.model = self.model.to(device)

    def forward_pass(self, batch_patch: Tensor, activate=True) -> Tensor:
        """Process forward pass on patches.
        Args:
            batch_patch (Tensor): batch of image patch to predict.
            activate (bool): To apply activation function (sigmoid or sigmoid) to scale outputs between 0 & 1.
        Returns:
            Tensor: batch of predictions.
        """
        
        with torch.no_grad():
            # output raw probabilities
            logits = self.model(batch_patch[0].to(self.device))
            # get number of classes in prediction
            num_classes = logits.shape[1]
            # transform raw proba in logits
            if activate:
                logits = activation(logits, num_classes=num_classes)

        return logits

    def get_logits(self, image: Tensor, activate=True) ->Tensor:
        """From RGB tensor image return a mask of logits (after activation, between 0 & 1).

        Args:
            image (Tensor): RGB image.

        Returns:
            Tensor: Segmentation mask.
        """
        # prepare image
        image = self.preprocessing(image)
        # build inference dataset
        inference_image = InferenceImage(
            image, self.patch_size, self.overlap, self.smoothing, self.operator
        )
        # wrap image patches as TensorDataset in DataLoader fro batch predictions
        inference_loader = DataLoader(inference_image.get_patches(), self.batch_size)
        # get predictions
        patches_predictions = [self.forward_pass(batch_patch, activate=activate) for batch_patch in inference_loader]
        patches_predictions = torch.cat(patches_predictions)
        # rebuild final segmentation mask from coordinates of inference image
        mask_logits = inference_image.rebuild(patches_predictions)

        return mask_logits

    def predict(self, image: Union[Tensor, str], visualisation_path: str = "", activate=True) -> Tensor:
        """Predict a segmentation mask from RGB image.

        Args:
            image (Union[Tensor, str]): either a RGB image as Tensor or a filepath to rgb image.
            visualisation_path (str, optional): path to save visualisation of the prediction. Defaults to "" (no visualisation).

        Returns:
            Tensor: Segmentation mask.
        """
        # if image is a file load image as Tensor
        if isinstance(image, str):
            image = load_image(image)
        # add offset, get logits & remove offsets
        image_prepared = I.add_offset(image, self.offset)
        logits = self.get_logits(image_prepared, activate=True)
        mask = logits_to_mask(logits, self.binary_threshold)
        mask = I.remove_offset(mask, self.offset)
        # do visualisation & save it
        if visualisation_path:
            visu = visualisation(image, mask)
            save_image(visu, visualisation_path)

        return mask
