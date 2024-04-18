"""contain utilities function to create visualisation by combining RGB image and segmentation masks."""

from typing import List, Tuple

import torch
from segmentools import COLORS
from torch import Tensor
from torchvision.utils import draw_segmentation_masks


def get_masks_and_colors(
    image: Tensor,
    segmentation_mask: Tensor,
    ignore_classes_values: List[int] = [0],
) -> Tuple[Tensor, List[Tuple[int]]]:
    """given a multilabel segmentation mask return binary masks for each class and associated colors.

    Args:
        image (Tensor): RGB image as tensor.
        mask (Tensor): Segmentation mask tensor (H, W).
        ignore_classes_values (List[int], optional): list classes values to ignore when makeing visualisation. Defaults to [0].

    Returns:
        Tensor: Stack of binary/bool masks (nclass, H, W).
        List[Tuple[int]]: List of associated colors (len nclass).
    """
    assert (
        image.shape[-2:] == segmentation_mask.shape[-2:]
    ), f"image and segmentation_mask should have the same H, W shape, got {image} & {segmentation_mask}"

    # get all classes in segmentation mask
    classes = torch.unique(segmentation_mask).tolist()
    # remove classe not wanted for visualisation
    classes = [cl for cl in classes if cl not in ignore_classes_values]
    # stack masks on dim 0 as binary masks, one for each class
    binary_masks = [segmentation_mask == cl for cl in classes]
    binary_masks = torch.stack(binary_masks) if binary_masks else torch.tensor(binary_masks)
    
    # get corresponding colors for each class
    colors = [COLORS[cl] for cl in classes]

    return binary_masks, colors


def apply_color_masks(
    image: Tensor, segmentation_mask: Tensor, alpha: float = 0.5, ignore_classes_values: List[int] = [0]
) -> Tensor:
    """Generate visualisation of the segmentation by applying transparency mask color from mask to image.

    Args:
        image (Tensor): RGB image as tensor.
        segmentation_mask (Tensor): Segmentation mask tensor.
        colors (List[Tuple[int]]): List of RGB colors
        alpha (float, optional): Transparency parameter. Defaults to 0.5.
        ignore_classes_values (List[int], optional): List classes values to ignore when makeing visualisation. Defaults to [0].

    Returns:
        Tensor: RGB image with transparency color for pixels of segmentation mask.
    """
    # clone image
    visualisation = torch.clone(image)
    # get binary masks for classes of interest
    binary_masks, colors = get_masks_and_colors(image, segmentation_mask, ignore_classes_values)
    # draw mask for each class
    for c, mask in enumerate(binary_masks.unbind()):
        visualisation = draw_segmentation_masks(visualisation, mask, alpha=alpha, colors=colors[c])
    
    return visualisation

def visualisation(image: Tensor, segmentation_mask: Tensor, alpha: float = 0.5, ignore_classes_values: List[int] = [0])-> Tensor:
     """Generate visualisation of the segmentation by applying transparency mask color from mask to image and concatenate with raw img.

    Args:
        image (Tensor): RGB image as tensor.
        segmentation_mask (Tensor): Segmentation mask tensor.
        colors (List[Tuple[int]]): List of RGB colors
        alpha (float, optional): Transparency parameter. Defaults to 0.5.
        ignore_classes_values (List[int], optional): List classes values to ignore when makeing visualisation. Defaults to [0].

    Returns:
        Tensor: RGB image with transparency color for pixels of segmentation mask.
    """
     
     color_mask = apply_color_masks(image, segmentation_mask, alpha, ignore_classes_values)
     visualisation = torch.cat([image, color_mask], axis=2)
     return visualisation