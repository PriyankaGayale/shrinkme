"""
Core compression functionality using Singular Value Decomposition (SVD).

This module provides functions to compress images by decomposing pixel matrices
into singular values and reconstructing them with a subset of the most significant values.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from typing import Dict, Tuple, Optional


def load_image(path: str) -> np.ndarray:
    """
    Loads an image and converts it to a grayscale numpy matrix.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Grayscale image as a 2D numpy array with values 0-255.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image cannot be opened or processed.

    Example:
        >>> img = load_image("sample.jpg")
        >>> print(img.shape)
        (height, width)
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {path}")
        img = Image.open(path).convert("L")
        return np.array(img)
    except Exception as e:
        raise ValueError(f"Failed to load image from {path}: {str(e)}")


def compress_image(img_matrix: np.ndarray, k: int) -> np.ndarray:
    """
    Compress the image using Singular Value Decomposition (SVD).

    Decomposes the image matrix A into U @ Σ @ V^T and reconstructs using
    only the top k singular values, effectively reducing storage requirements.

    Args:
        img_matrix (np.ndarray): 2D grayscale image matrix (m x n).
        k (int): Number of singular values to keep. Must be > 0 and <= min(m, n).

    Returns:
        np.ndarray: Compressed image matrix with same shape as input.

    Raises:
        ValueError: If k is invalid or img_matrix is not 2D.

    Example:
        >>> img = load_image("sample.jpg")
        >>> compressed = compress_image(img, k=50)
        >>> print(compressed.shape)
        (height, width)

    Mathematical Background:
        For an m × n matrix A:
        A = U @ Σ @ V^T  (full decomposition)
        A_k ≈ U_k @ Σ_k @ V_k^T  (compressed with k components)

        Storage savings:
        - Original: m × n values
        - Compressed: k(m + n + 1) values
    """
    if not isinstance(img_matrix, np.ndarray) or img_matrix.ndim != 2:
        raise ValueError("img_matrix must be a 2D numpy array")

    m, n = img_matrix.shape
    if k <= 0 or k > min(m, n):
        raise ValueError(f"k must be between 1 and {min(m, n)}, got {k}")

    try:
        U, S, Vt = np.linalg.svd(img_matrix, full_matrices=False)

        U_k = U[:, :k]
        S_k = np.diag(S[:k])
        Vt_k = Vt[:k, :]

        compressed_matrix = U_k @ S_k @ Vt_k
        return compressed_matrix
    except Exception as e:
        raise ValueError(f"SVD compression failed: {str(e)}")


def calculate_compression_metrics(
    original_path: str, img_matrix: np.ndarray, k: int
) -> Dict[str, float]:
    """
    Calculate storage savings and compression metrics.

    Args:
        original_path (str): Path to the original image file.
        img_matrix (np.ndarray): Original image matrix (before compression).
        k (int): Number of singular values used in compression.

    Returns:
        dict: Dictionary containing:
            - file_size_bytes (int): Original file size in bytes
            - matrix_size (int): Total elements in original matrix (m × n)
            - compressed_matrix_size (int): Theoretical compressed size k(m+n+1)
            - compression_ratio (float): Original size / Compressed size
            - space_saved (float): Fraction of space saved (0-1)

    Example:
        >>> metrics = calculate_compression_metrics("sample.jpg", img, 50)
        >>> print(f"Ratio: {metrics['compression_ratio']:.2f}x")
        >>> print(f"Saved: {metrics['space_saved']*100:.1f}%")
    """
    try:
        original_file_size = os.path.getsize(original_path)
    except OSError:
        original_file_size = 0

    m, n = img_matrix.shape
    original_storage = m * n
    compressed_storage = k * (m + n + 1)

    compression_ratio = (
        original_storage / compressed_storage if compressed_storage > 0 else 0
    )
    space_saved = 1 - (compressed_storage / original_storage)

    return {
        "file_size_bytes": original_file_size,
        "matrix_size": original_storage,
        "compressed_matrix_size": compressed_storage,
        "compression_ratio": compression_ratio,
        "space_saved": space_saved,
    }


def show_images(original: np.ndarray, compressed: np.ndarray) -> None:
    """
    Display original and compressed images side by side.

    Args:
        original (np.ndarray): Original grayscale image matrix.
        compressed (np.ndarray): Compressed grayscale image matrix.

    Returns:
        None: Displays plot using matplotlib.

    Example:
        >>> img = load_image("sample.jpg")
        >>> compressed = compress_image(img, 50)
        >>> show_images(img, compressed)
    """
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Compressed Image")
    plt.imshow(compressed, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def print_metrics(metrics: Dict[str, float], k: int) -> None:
    """
    Print compression statistics in a formatted table.

    Args:
        metrics (dict): Output from calculate_compression_metrics().
        k (int): Number of singular values used (for display).

    Returns:
        None: Prints to stdout.

    Example:
        >>> metrics = calculate_compression_metrics("sample.jpg", img, 50)
        >>> print_metrics(metrics, k=50)
    """
    print("\n===== Compression Statistics =====\n")

    print(f"Singular values used (k): {k}")
    print(f"Original file size: {metrics['file_size_bytes'] / 1024:.2f} KB")

    print("\nMatrix Storage (conceptual representation)")
    print(f"Original matrix elements: {metrics['matrix_size']}")
    print(f"Compressed representation elements: {metrics['compressed_matrix_size']}")

    print(f"\nCompression ratio: {metrics['compression_ratio']:.2f}x")
    print(f"Space saved: {metrics['space_saved'] * 100:.2f}%")

    print("\n==================================\n")


def save_compressed_image(
    compressed_matrix: np.ndarray, output_path: str
) -> None:
    """
    Save compressed image matrix to file.

    Args:
        compressed_matrix (np.ndarray): Compressed image data.
        output_path (str): Path where to save the output image.

    Returns:
        None: Saves image to disk.

    Raises:
        ValueError: If the matrix cannot be converted to image format.

    Example:
        >>> compressed = compress_image(img, 50)
        >>> save_compressed_image(compressed, "output.jpg")
    """
    try:
        compressed_uint8 = np.clip(compressed_matrix, 0, 255).astype(np.uint8)
        img = Image.fromarray(compressed_uint8)
        img.save(output_path)
        print(f"Compressed image saved to {output_path}")
    except Exception as e:
        raise ValueError(f"Failed to save image: {str(e)}")
