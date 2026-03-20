"""
Utility functions for image resizing and preprocessing.

This module provides functions to resize images before or after compression,
supporting flexible dimension specifications and aspect ratio preservation.
"""

import numpy as np
from PIL import Image
from typing import Tuple, Optional


def resize_image(img_path: str, width: int, height: int) -> np.ndarray:
    """
    Resize an image from file and return as grayscale numpy array.

    Args:
        img_path (str): Path to the image file.
        width (int): Target width in pixels.
        height (int): Target height in pixels.

    Returns:
        np.ndarray: Resized grayscale image as 2D numpy array.

    Raises:
        ValueError: If dimensions are invalid or file cannot be opened.

    Example:
        >>> resized_img = resize_image("sample.jpg", 800, 600)
        >>> print(resized_img.shape)
        (600, 800)
    """
    if width <= 0 or height <= 0:
        raise ValueError(f"Dimensions must be positive, got {width}x{height}")

    try:
        img = Image.open(img_path).convert("L")
        img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
        return np.array(img_resized)
    except Exception as e:
        raise ValueError(f"Failed to resize image: {str(e)}")


def resize_output(
    compressed_matrix: np.ndarray, width: int, height: int
) -> np.ndarray:
    """
    Resize a compressed image matrix to specified dimensions.

    Args:
        compressed_matrix (np.ndarray): Compressed image as 2D numpy array.
        width (int): Target width in pixels.
        height (int): Target height in pixels.

    Returns:
        np.ndarray: Resized image array with shape (height, width).

    Raises:
        ValueError: If dimensions are invalid.

    Example:
        >>> resized_output = resize_output(compressed_img, 1024, 768)
        >>> print(resized_output.shape)
        (768, 1024)
    """
    if width <= 0 or height <= 0:
        raise ValueError(f"Dimensions must be positive, got {width}x{height}")

    try:
        # Clip values to valid range before converting to PIL Image
        data_uint8 = np.clip(compressed_matrix, 0, 255).astype(np.uint8)
        img = Image.fromarray(data_uint8)
        img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
        return np.array(img_resized)
    except Exception as e:
        raise ValueError(f"Failed to resize output: {str(e)}")


def parse_dimension_string(dim_str: str) -> Tuple[int, int]:
    """
    Parse dimension string in format 'WIDTHxHEIGHT' to tuple (width, height).

    Args:
        dim_str (str): Dimension string like '800x600' or '1920x1080'.

    Returns:
        tuple: (width, height) as integers.

    Raises:
        ValueError: If format is invalid or dimensions are not positive.

    Example:
        >>> width, height = parse_dimension_string("1024x768")
        >>> print(width, height)
        1024 768
    """
    try:
        parts = dim_str.split("x")
        if len(parts) != 2:
            raise ValueError(
                f"Invalid format. Use WIDTHxHEIGHT format, got '{dim_str}'"
            )
        width = int(parts[0])
        height = int(parts[1])
        if width <= 0 or height <= 0:
            raise ValueError(f"Dimensions must be positive, got {width}x{height}")
        return width, height
    except ValueError as e:
        raise ValueError(f"Failed to parse dimensions '{dim_str}': {str(e)}")


def get_common_resolutions() -> dict:
    """
    Return dictionary of common resolution presets.

    Returns:
        dict: Mapping of names to (width, height) tuples.

    Example:
        >>> resolutions = get_common_resolutions()
        >>> print(resolutions['VGA'])
        (640, 480)
    """
    return {
        "VGA": (640, 480),
        "SVGA": (800, 600),
        "XGA": (1024, 768),
        "WXGA": (1280, 800),
        "SXGA": (1280, 1024),
        "UXGA": (1600, 1200),
        "WUXGA": (1920, 1200),
        "FHD": (1920, 1080),
        "QHD": (2560, 1440),
        "4K": (3840, 2160),
    }


def preserve_aspect_ratio(
    original_width: int,
    original_height: int,
    target_width: int,
    target_height: int,
) -> Tuple[int, int]:
    """
    Calculate new dimensions while preserving aspect ratio.

    Fits the original image into the target dimensions while maintaining
    its aspect ratio (will be smaller than target in at least one dimension).

    Args:
        original_width (int): Original image width.
        original_height (int): Original image height.
        target_width (int): Target maximum width.
        target_height (int): Target maximum height.

    Returns:
        tuple: New (width, height) that preserves aspect ratio.

    Example:
        >>> new_w, new_h = preserve_aspect_ratio(1920, 1080, 800, 600)
        >>> print(new_w, new_h)
        800 450
    """
    aspect_ratio = original_width / original_height

    # Check if width is the limiting factor
    if target_width / target_height < aspect_ratio:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    return new_width, new_height
