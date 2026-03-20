"""
Shrinkme - Image compression using Singular Value Decomposition (SVD).

A Python package that compresses images by decomposing pixel matrices
and reconstructing them with a subset of singular values, achieving significant
storage savings while preserving image quality.

Basic Usage:
    >>> from shrinkme import compress_image, load_image, save_compressed_image
    >>> img = load_image("sample.jpg")
    >>> compressed = compress_image(img, k=50)
    >>> save_compressed_image(compressed, "output.jpg")

CLI Usage:
    $ shrinkme compress --input image.jpg --k 50
    $ shrinkme compress --input image.jpg --k 50 --resize 800x600 --visualize

Author: Akshay Ubale
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Akshay Ubale"
__license__ = "MIT"

from .core import (
    load_image,
    compress_image,
    calculate_compression_metrics,
    show_images,
    print_metrics,
    save_compressed_image,
)
from .utils import (
    resize_image,
    resize_output,
    parse_dimension_string,
    get_common_resolutions,
    preserve_aspect_ratio,
)

__all__ = [
    "load_image",
    "compress_image",
    "calculate_compression_metrics",
    "show_images",
    "print_metrics",
    "save_compressed_image",
    "resize_image",
    "resize_output",
    "parse_dimension_string",
    "get_common_resolutions",
    "preserve_aspect_ratio",
]
