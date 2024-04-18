import random as rd
import shutil
from pathlib import Path
from typing import List, Tuple, Union

from segmentools import (
    IMAGES_FOLDER,
    MASKS_FOLDER,
    check_image_dataset,
    get_images_paths,
)
from tqdm import tqdm


def split_data(
    images_names: List[Union[str, Path]], proportions: Tuple[float]
) -> Tuple[List[Union[str, Path]]]:
    """This function split a dataset into subsets for train, valid & test.

    Args:
        images_names (Union[str, Path]]): List of image names.
        proportions (Tuple[float]): Proportion of subsets from source dataset (train, test, valid).

    Returns:
        Tuple Union[str, Path]]: return 3 lists containing image names, one for each subset.
    """

    assert (
        round(sum(list(proportions)), 2) == 1.0
    ), "sum of split tuple is not equal to 1.0"

    # get all images paths and shuffle
    rd.shuffle(images_names)
    dataset_size = len(images_names)
    # assign number of images for each subset
    train_proportion, valid_proportion, test_proportion = proportions
    train_size = int(train_proportion * dataset_size)
    valid_size = int(valid_proportion * dataset_size)
    test_size = int(test_proportion * dataset_size)
    # add remaining images to train set
    remains = dataset_size - (train_size + valid_size + test_size)
    train_size += remains
    # dispatch names into subsets
    train_set = images_names[:train_size]
    valid_set = images_names[train_size : (train_size + valid_size)]
    test_set = images_names[-test_size:] if test_size > 0 else []

    return train_set, valid_set, test_set


def copy_image(image_path: Union[str, Path], destination_folder: Union[str, Path]):
    """Copy an image to a specific destination folder.

    Args:
        image_path Union[str, Path]: image path
        destination_folder Union[str, Path]: destination folder
    """
    dest_folder = (
        destination_folder
        if isinstance(destination_folder, Path)
        else Path(destination_folder)
    )
    img_path = image_path if isinstance(image_path, Path) else Path(image_path)
    dest_folder.mkdir(parents=True, exist_ok=True)
    new_path = dest_folder / img_path.name
    shutil.copy(img_path.as_posix(), new_path.as_posix())


def split_dataset(
    source_dataset: Union[str, Path, List[Union[str, Path]]],
    destination: Union[str, Path],
    proportions: Tuple[float] = (0.8, 0.2, 0.0),
) -> None:
    """Split images and masks of a dataset into subsets and write each subsets in destination folder.

    Args:
        source_dataset (Union[str, List[Union[str, Path]]]): Path of source dataset to split or list of datasets paths.
        destination (str): Path to folder where to write subsets
        proportions (Tuple[float], optional): proportions of each subset. Defaults to (0.8, 0.2, 0.0).
    """
    # if source_datasets is a string wrap it in list
    if isinstance(source_dataset, str) or isinstance(source_dataset, Path):
        source_dataset = [source_dataset]
    destination = destination if isinstance(destination, Path) else Path(destination)
    # for each source dataset do the split
    for dataset_path in source_dataset:
        # get images paths
        dataset_path = (
            dataset_path if isinstance(dataset_path, Path) else Path(dataset_path)
        )
        check_image_dataset(dataset_path)
        images_paths = get_images_paths(dataset_path / IMAGES_FOLDER)
        # split paths into subsets
        subset_images_paths = split_data(images_paths, proportions)
        subset_names: Tuple = ["train", "valid", "test"]
        for c, subset in enumerate(subset_names):
            # define destination path
            subset_images_path = destination / subset / IMAGES_FOLDER
            subset_masks_path = destination / subset / MASKS_FOLDER
            subset_images = subset_images_paths[c]
            # for each image path in subset copy image & corresponding mask to destination folder
            for image_path in tqdm(subset_images, desc=f"Copy {subset} data"):
                mask_path = image_path.parent.parent / MASKS_FOLDER / image_path.name
                copy_image(image_path, subset_images_path)
                copy_image(mask_path, subset_masks_path)


def merge_datasets(
    datasets: List[Union[str, Path]], destination_dataset: Union[str, Path]
):
    """Merge images and masks of multiple datasets in a new one.

    Args:
        datasets (List[str]): List of paths to datasets.
        destination_dataset (str): Path to create a new dataset.
    """
    destination_dataset = (
        destination_dataset
        if isinstance(destination_dataset, Path)
        else Path(destination_dataset)
    )
    # define destinations sub directories
    destination_images = destination_dataset / IMAGES_FOLDER
    destination_masks = destination_dataset / MASKS_FOLDER
    # create destination folders
    destination_images.mkdir(parents=True)
    destination_masks.mkdir(parents=True)
    # for each dataset
    for dataset in tqdm(datasets, desc="merging datasets : "):
        dataset = dataset if isinstance(dataset, Path) else Path(dataset)
        # check sanity of dataset
        check_image_dataset(dataset)
        images_folder = dataset / IMAGES_FOLDER
        masks_folder = dataset / MASKS_FOLDER
        # copy image and mask to destination folders
        for imgp in images_folder.iterdir():
            maskp = masks_folder / imgp.name
            shutil.copy(imgp.as_posix(), destination_images.as_posix())
            shutil.copy(maskp.as_posix(), destination_masks.as_posix())
