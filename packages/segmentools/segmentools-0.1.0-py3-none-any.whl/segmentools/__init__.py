# -*- coding: utf-8 -*-

"""All classes and functions to train and use segmentation models to process RGB images using PyTorch."""

from pathlib import Path
from typing import List, Union
import torch
from torch import Tensor
from torch.nn.functional import threshold

__version__ = "0.1.0"

### Module variables

IMAGES_FOLDER = Path("images")  # name of dataset subfolder for images
MASKS_FOLDER = Path("masks")  # name of dataset subfolder for masks
COLORS = [
    (0, 102, 204),
    (51, 255, 51),
    (255, 0, 0),
    (51, 51, 255),
    (255, 51, 255),
    (255, 255, 0),
    (86, 255, 255),
]  # set of colors for visualisation (max 7 classes for now)


def get_images_paths(image_directory: Union[str, Path]) -> List[Path]:
    """Gather paths of all images in a directory.

    Args:
        image_directory (Path): directory of images path to gather

    Returns:
        List[Path]: list of images paths.
    """
    image_directory = (
        image_directory if isinstance(image_directory, Path) else Path(image_directory)
    )
    images_paths = list(image_directory.glob("*"))
    return images_paths


def get_images_names(image_directory: Union[str, Path]) -> List[Path]:
    """Return names of all images in directory.

    Args:
        image_directory (Union[str, Path]): directory of images.

    Returns:
        List[str]: List of image names in directory
    """
    image_directory = (
        image_directory if isinstance(image_directory, Path) else Path(image_directory)
    )
    names = [path.name for path in image_directory.iterdir()]
    return names


def check_image_dataset(data_set: Union[str, Path]):
    """Check sanity of the dataset.

    Args:
        data_set (Union[str, Path]): path to a dataset.

    Raises:
        ValueError(s) for many cases.
    """
    dataset = data_set if isinstance(data_set, Path) else Path(data_set)

    if not dataset.is_dir():
        raise ValueError(f"dataset folder : {dataset.as_posix()} does not exist")

    if not any(dataset.iterdir()):
        raise ValueError(f"dataset {dataset.as_posix} is empty")

    image_directory = dataset / IMAGES_FOLDER
    mask_directory = dataset / MASKS_FOLDER

    images_stem = [path.name for path in image_directory.iterdir()]
    masks_stem = [path.name for path in mask_directory.iterdir()]
    isolated_images = set(images_stem) - set(masks_stem)
    isolated_masks = set(masks_stem) - set(images_stem)
    if isolated_images:
        raise ValueError(f"some images do not have any mask : {isolated_images}")
    if isolated_masks:
        raise ValueError(f"some masks do not have any images : {isolated_masks}")
    if not images_stem:
        raise ValueError(f"dataset {dataset} is empty")


def activation(prediction: Tensor, num_classes: int):
    """Return activated predictions by sigmoid (single class) of softmax (multi class).

    Args:
        prediction (Tensor): Raw model ouput/raw probabilities.
        num_classes (int): number of classes in task.
    """
    prediction_dims = prediction.ndim
    assert prediction_dims in [
        3,
        4,
    ], f"Number of dimension in prediction should be 3 or 4 (batch), got {prediction_dims}"
    channel = 0 if prediction_dims == 3 else 1
    if num_classes == 1:
        prediction = prediction.sigmoid()
    elif num_classes > 1:
        prediction = prediction.softmax(dim=channel)  # Channels dimension

    return prediction


def logits_to_mask(logits: Tensor, thr: float = 0.5) -> Tensor:
    """Transform logits predictions to segmentation mask.

    Args:
        logits (Tensor): Logits (values from 0 to 1.)
        thr (float, optional): threshold for binary task class differenciation. Defaults to 0.5.

    Returns:
        Tensor: Segmentation mask with integers values for predicted classes.
    """
    channel_dim = 1 if len(logits.shape) == 4 else 0
    # get classes number
    nb_classes = logits.shape[channel_dim]
    # if binary task apply binary threshold
    if nb_classes == 1:
        mask = threshold(logits, thr, 0)
        mask[mask > 0] = 1
        mask = mask.squeeze(channel_dim).int()
    # else apply argmax
    elif nb_classes > 1:
        mask = torch.argmax(logits, dim=channel_dim)

    return mask
