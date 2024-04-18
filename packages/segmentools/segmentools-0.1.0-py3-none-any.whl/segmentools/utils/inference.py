from itertools import product
from math import ceil, floor
from typing import List, Literal, Tuple

import torch
from torch import Tensor
from torchgeometry.image import get_gaussian_kernel2d
from torchvision.transforms.v2.functional import crop, pad


def pad_to(image: Tensor, size: Tuple, fill_value: int = 0) -> Tensor:
    """Pad array with fill value to fit size with origin image in center of padded image.

    Args:
        image (Tensor): Image to be padded.
        size (Tuple, optional): Size to fit with padding.
        fill_value (int) : value to use for filling new pixels.
    Returns:
        Tensor: Padded image
    """
    # get sizes
    h, w = image.shape[-2:]
    padded_h, padded_w = size
    # compute difference
    delta_h = padded_h - h
    delta_w = padded_w - w
    # get left, top, right, bot thickness
    top, bot = ceil(delta_h / 2), floor(delta_h / 2)
    left, right = ceil(delta_w / 2), floor(delta_w / 2)
    # pad image
    padded = pad(image, padding=[left, top, right, bot], fill=fill_value)
    return padded


def crop_to(image: Tensor, size: Tuple) -> Tensor:
    """Crop array in center.

    Args:
        image (Tensor): Image to crop.
        size (Tuple): Cropped size.

    Returns:
        Tensor: image cropped.
    """
    # get sizes
    h, w = image.shape[-2:]
    cropped_h, cropped_w = size
    # compute delta of sizes
    delta_h = h - cropped_h
    delta_w = w - cropped_w
    # get top left coordinates
    top, left = ceil(delta_h / 2), ceil(delta_w / 2)
    # crop image at center
    cropped = crop(image, top, left, cropped_h, cropped_w)
    return cropped


def add_offset(image: Tensor, offset: int) -> Tensor:
    """Pad fix number of pixels around sides of image

    Args:
        image (Tensor): Image to pad.
        offset (int): Number of pixels to pad.

    Returns:
        Tensor: Image padded.
    """
    return pad(image, offset)


def remove_offset(image: Tensor, offset: int) -> Tensor:
    """Remove fix number of pixels on each side of image.

    Args:
        image (Tensor): Image.
        offset (int): Border size to remove.

    Returns:
        Tensor: Image without offset.
    """
    h, w = image.shape[-2:]
    new_h, new_w = h - 2 * offset, w - 2 * offset
    return crop(image, offset, offset, new_h, new_w)


def patchification(
    image: Tensor, patch_size: Tuple, overlap: float
) -> Tuple[Tensor, List[Tuple[int]], Tuple[int]]:
    """Cut image in patches according to patch size and overlapping.
    If needed padding is applied to fit pacth size multiplicator on H & W.

    Args:
        image (Tensor): Large image to patchify.
        patch_size (Tuple): size of patch.
        overlap (float): Overlap between patches.
    Returns:
        Tuple[Tensor, List[Tuple[int]]]: Tensor of N pacthes & coordinates according to padded image.
    """
    # get shapes of image and pateches
    c, h, w = image.shape[-3:]
    h_patch, w_patch = patch_size
    # compute strides values
    stride_h = h_patch - round(h_patch * overlap)
    stride_w = w_patch - round(w_patch * overlap)
    # get number of pacthes on axis
    nb_h_patches = ceil(h / stride_h)
    nb_w_patches = ceil(w / stride_w)
    # padded image shape (H,W)
    h_padded = (nb_h_patches - 1) * stride_h + h_patch
    w_padded = (nb_w_patches - 1) * stride_w + w_patch
    # pad image
    padded_image = pad_to(image, size=(h_padded, w_padded))
    # get coordinates
    top_corners = range(0, nb_h_patches * stride_h, stride_h)
    left_corners = range(0, nb_w_patches * stride_w, stride_w)
    origins = list(product(top_corners, left_corners))
    # Create patches tensors
    patches = torch.zeros((nb_h_patches * nb_w_patches, c, h_patch, w_patch))
    #  Fill the patches tensors
    for idx, (y, x) in enumerate(origins):
        patches[idx] = padded_image[:, y : y + h_patch, x : x + w_patch]

    return patches, origins, (h_padded, w_padded)


def avg_stack(
    output: Tensor, counter: Tensor, patch: Tensor, coordinate: Tuple[int], smooth_kernel: Tensor
) -> Tuple[Tensor]:
    """Apply patch prediction on output & corresponding counter mask to have mean value for overlapping pixels.
    Args:
        output (Tensor): Tensor to store and compute outputs.
        patch (Tensor): Patch prediction.
        counter (Tensor): Tensor to count how much times a pixel has been predicted.
        smooth_kernel (Tensor): Tensor to pultiply patch prediction and counter update with.

    Returns:
        Tuple[Tensor]: Updated output and counter.
    """
    # APPLY SMOOTHING
    patch *= smooth_kernel
    y, x = coordinate
    h_patch, w_patch = patch.shape[-2:]
    # sum without takin count of nan
    output[..., y : y + h_patch, x : x + w_patch] = torch.nansum(
        torch.stack([output[..., y : y + h_patch, x : x + w_patch], patch]), dim=0
    )
    counter[..., y : y + h_patch, x : x + w_patch] += smooth_kernel

    return output, counter


def max_stack(
    output: Tensor, counter: Tensor, patch: Tensor, coordinate: Tuple[int], smooth_kernel: Tensor
) -> Tuple[Tensor]:
    """Apply path prediction on output and taking max for overlapping values.
    Args:
        output (Tensor): Tensor to store and compute outputs.
        patch (Tensor): Patch prediction.
        counter (Tensor): Tensor to count how much times a pixel has been predicted.
        smooth_kernel (Tensor): Tensor to pultiply patch prediction and counter update with. Unused (only for avg_stack)

    Returns:
        Tuple[Tensor]: Updated output and .
    """
    y, x = coordinate
    h_patch, w_patch = patch.shape[-2:]
    output[..., y : y + h_patch, x : x + w_patch] = torch.fmax(
        output[..., y : y + h_patch, x : x + w_patch], patch
    )

    return output, counter


def min_stack(
    output: Tensor, counter: Tensor, patch: Tensor, coordinate: Tuple[int], smooth_kernel: Tensor
) -> Tuple[Tensor]:
    """Apply pathc prediction on output and taking min for overlapping value.
    Args:
        output (Tensor): Tensor to store and compute outputs.
        patch (Tensor): Patch prediction.
        counter (Tensor): Tensor to count how much times a pixel has been predicted.
        smooth_kernel (Tensor): Tensor to pultiply patch prediction and counter update with. Unused (only for avg_stack)

    Returns:
        Tuple[Tensor]: Updated output and counter
    """
    y, x = coordinate
    h_patch, w_patch = patch.shape[-2:]
    output[..., y : y + h_patch, x : x + w_patch] = torch.fmin(
        output[..., y : y + h_patch, x : x + w_patch], patch
    )

    return output, counter


def kernel_smoothing(mode, size: Tuple[int, int]):
    """
    According the mode create a kernel to smooth the
    predictions accross overlaps
    """
    if mode == "uniform":
        kernel = torch.ones(size)
    elif mode == "gaussian":
        h_size, w_size = size
        kernel = torch.zeros(size=size)
        # if kernel size as pair value, reduce size to get imapair value
        if h_size % 2 == 0:
            h_size -= 1
        if w_size % 2 == 0:
            w_size -= 1
        gaussian_values = get_gaussian_kernel2d(ksize=(h_size, w_size), sigma=tuple([s / 4 for s in size]))
        kernel[0:h_size, 0:w_size] = gaussian_values
        kernel += 1

    return kernel


OPERATORS_FUNCTIONS = {"avg": avg_stack, "min": min_stack, "max": max_stack}


def unpatchification(
    patches: Tensor,
    coordinates: List[Tuple[int]],
    image_shape: Tuple[int],
    operator: Literal["avg", "max", "min"] = "avg",
    patch_smoothing: Literal["uniform", "gaussian"] = "uniform",
):
    """Rebuild image sized mask with patch predictions overlapped.

    Args:
        patches (Tensor): Predictions on each patch.
        coordinates (List[Tuple[int]]): List of top, left corners coordinates
    """
    # get operator to merge overlapping patches
    operator_fun = OPERATORS_FUNCTIONS[operator]
    # get number of predictions channels
    channels = patches.shape[1]
    # get devide
    device = patches.device
    # create nan output with corresponding image shape
    # & counter to store how many times each pixel have been predicted
    h, w = image_shape
    output = torch.full((channels, h, w), torch.nan, device=device)
    counter = torch.zeros((channels, h, w), device=device)
    # create smoothing kernel, either uniform or gaussian to weight pixel prediction by position importance
    h_patch, w_patch = patches.shape[-2:]
    smoothing_kernel = kernel_smoothing(mode=patch_smoothing, size=(h_patch, w_patch)).to(device)
    # for each patch fill ouptut with values at corresponding original position of patch
    for c, patch in enumerate(patches.unbind()):
        patch = patch * smoothing_kernel
        output, counter = operator_fun(
            output, counter, patch, coordinates[c], smooth_kernel=smoothing_kernel
        )

    # if operator is average divide value by number of prediction/pixel
    if operator == "avg":
        output = output / counter

    return output
