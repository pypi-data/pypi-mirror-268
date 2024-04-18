# -*- coding: utf-8 -*-

"""general utilities and image preprocessing for Computer Vision tasks with Deep Learning using PyTorch."""

import random as rd
from pathlib import Path
from typing import Union

import numpy as np
import torch
import torchvision.transforms.functional as F
from PIL.Image import Image
from torch import Tensor
from torchvision.io import ImageReadMode, read_image

__version__ = "0.1.0"


def reproducibility(seed: int = 666, deterministic: bool = True) -> None:
    """Disable all accessible source of randomness.
    Be aware that it is not possible to have complete randomness using cuda.

    WARNING: disable cudnn benchmarking can lead to poor performances

    Args:
        seed (int): value of the seed.
        deterministic (bool): Use deterministic algorithm if True. Default True.
    """
    # set package seed
    rd.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    # make pytorch use deterministic algorithm
    if deterministic:
        torch.use_deterministic_algorithms(True)
    # disable convolutions benchmark
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = False


def end_reproducibility():
    """Remove torch reproducibility based on models and CUDA computations."""
    # reset seed
    rd.seed()
    np.random.seed()
    torch.seed()
    # set deterministic to False
    torch.use_deterministic_algorithms(False)
    # disable convolutions benchmark
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True


def save_image(image: Tensor, path: Union[str, Path]) -> Image:
    """Transform image in PIL format and save to given path."""
    if not isinstance(path, Path):
        path = Path(path)
    parent = path.parent
    Path(parent).mkdir(exist_ok=True, parents=True)
    image = image.to(torch.uint8)
    pil_image = F.to_pil_image(image)
    pil_image.save(path.as_posix())


def load_image(image_path: Union[str, Path]) -> Tensor:
    """Load image using torchvision.

    Args:
        image_path (str): Path to image.

    Returns:
        Tensor: Grayscale mask in torch Tensor.
    """
    if isinstance(image_path, Path):
        image_path = image_path.as_posix()
    return read_image(image_path, mode=ImageReadMode.RGB)


def load_mask(mask_path: str) -> Tensor:
    """Load mask in grayscale using torchvision & remove dummy channel dimesnion.

    Args:
        mask_path (str): Path to mask.

    Returns:
        Tensor: RGB image in torch Tensor.
    """
    if isinstance(mask_path, Path):
        mask_path = mask_path.as_posix()
    mask = read_image(mask_path, mode=ImageReadMode.GRAY)
    mask = mask.squeeze(0)
    return mask


def to_numpy(image: Tensor) -> np.ndarray:
    """Transform RGB image tensor to numpy array with channel permutation.

    Args:
        image (Tensor): RGB image tensor.
    Return:
        (np.ndarray): RGB numpy image.
    """

    image = image.permute(1, 2, 0).cpu().numpy()
    return image
