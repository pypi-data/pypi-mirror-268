"""Contain custom torch dataset to iterate over segmentools organized data and return batched & prepared images."""

from __future__ import annotations

from typing import Callable, Tuple, Union
from pathlib import Path
import segmentools
import torch
from computervisiontools import load_image, load_mask
from computervisiontools.preprocessing import build_preprocessing
from segmentools import check_image_dataset, get_images_paths
from segmentools.augmentation import Augmentation
from torch import Tensor
from torch.utils.data import Dataset, Sampler


class SegmentDataset(Dataset):
    """Torch dataset for segmentation."""

    def __init__(
        self,
        dataset_path: Union[str, Path],
        augmentation: Augmentation = None,
        preprocessing: Callable = build_preprocessing(),
    ):
        """Dataset to load, prepare and return data for model trainning.

        Args:
            dataset_path Union[str, Path]: Path to dataset.
            augmentation (Callable): Augmentation pipeline to add diversity wihtout create new image on folders.
            preprocessing (Callable, optional): Conventionnal transformation for image data (value scaling & normalization). Defaults to build_preprocessing().
        """
        self.data_path = (
            dataset_path if isinstance(dataset_path, Path) else Path(dataset_path)
        )
        # check sanity of data
        check_image_dataset(self.data_path)
        # images are paths to images
        self.images = get_images_paths(dataset_path / segmentools.IMAGES_FOLDER)
        # correpsonding masks
        self.masks = get_images_paths(dataset_path / segmentools.MASKS_FOLDER)

        self.augmentation = augmentation
        self.preprocessing = preprocessing

    def __getitem__(self, index: int) -> Tuple[Tensor]:
        """Gather, prepare and return as tensors image & mask corresponding to index.

        Args:
            index (int): index of one element in dataset.

        Returns:
            Tuple[Tensor]: image (3, H, W) & mask (H, W) as Tensor.
        """
        # get paths
        image_path = self.images[index]
        mask_path = self.masks[index]
        # load both image & mask
        image = load_image(image_path)
        mask = load_mask(mask_path).long()
        # apply augmentation if needed
        if self.augmentation:
            image, mask = self.augmentation(image, mask)
        # preprocess image for trainning
        if self.preprocessing:
            image = self.preprocessing(image)

        if mask.shape == 4:
            mask.unsqueeze(1)

        return image, mask

    def __iter__(self):
        for x in range(len(self)):
            yield self[x]

    def __len__(self):
        return len(self.images)


class RandomSampler(Sampler):
    """Sampler that allow to select a random subsample of Dataset of images to run for one epoch."""

    def __init__(self, dataset: Dataset, num_samples: int = 0):
        self.data_source = dataset
        self._num_samples = num_samples

        if not isinstance(self.num_samples, int) or self.num_samples <= 0:
            raise ValueError(
                "num_samples should be a positive integer "
                "value, but got num_samples={}".format(self.num_samples)
            )

    @property
    def num_samples(self):
        # dataset size might change at runtime
        if self._num_samples is None:
            return len(self.data_source)
        return self._num_samples

    def __iter__(self):
        """return a random subset of num_samples indexes from dataset"""
        n = len(self.data_source)
        return iter(torch.randperm(n, dtype=torch.int64)[: self.num_samples].tolist())

    def __len__(self):
        return self.num_samples
