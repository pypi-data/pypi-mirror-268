from typing import List, Tuple

import torchvision.transforms.v2 as T
from torch import Tensor
from torchvision.tv_tensors import Image, Mask


class Augmentation:
    """Wrap torchvision transforms into one class and apply transformation to images & masks"""

    def __init__(self, augmentations: List[T.Transform] = []):
        """Generate Augmentation instance with list of transformations.

        Args:
            augmentations (List[T.Transform], optional): List of torchvision v2 transforms. Defaults to [].
        """
        # Make the compose of all the augmentations
        self.transform = T.Compose(augmentations)

    def __call__(
        self, image: Tensor, mask: Tensor
    ) -> Tuple[Tensor, Tensor]:
        """Apply intern transfomrations to image & mask and return augmented pair.

        Args:
            image (Tensor): RGB tensor image.
            mask (Tensor): Tensor mask.

        Returns:
            Tuple[Tensor, Tensor]: Pair of augmented image & mask.
        """
        # send image é mask to TVTensors
        image = Image(image)
        mask = Mask(mask)
        # apply augmentation
        augmented_image, augmented_mask = self.transform(image, mask)

        return augmented_image, augmented_mask

class Scaling(Augmentation):
    """Child class of Augmentation only for scaling size of image & mask.
    Use to fix size of data in trainning. Process only cropping & padding, not resize.
    """

    def __init__(self, size):
        super().__init__(augmentations=[T.RandomCrop(size=size, pad_if_needed=True)])