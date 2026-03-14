import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


def load_image(path):
    """
    Loads an image and converts it to a grayscale numpy matrix.
    """
    img = Image.open(path).convert("L")
    return np.array(img)


def compress_image(img_matrix, k):
    """
    Compress the image using Singular Value Decomposition (SVD)
    keeping only the top-k singular values.
    """

    U, S, Vt = np.linalg.svd(img_matrix, full_matrices=False)

    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]

    compressed_matrix = U_k @ S_k @ Vt_k

    return compressed_matrix


def calculate_compression_metrics(original_path, img_matrix, k):
    """
    Calculate storage savings and compression ratio.
    """

    # original file size
    original_file_size = os.path.getsize(original_path)

    # matrix storage approximation
    m, n = img_matrix.shape

    # original matrix storage
    original_storage = m * n

    # compressed storage
    compressed_storage = k * (m + n + 1)

    compression_ratio = original_storage / compressed_storage
    space_saved = 1 - (compressed_storage / original_storage)

    return {
        "file_size_bytes": original_file_size,
        "matrix_size": original_storage,
        "compressed_matrix_size": compressed_storage,
        "compression_ratio": compression_ratio,
        "space_saved": space_saved
    }


def show_images(original, compressed):
    """
    Display original and compressed images.
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

    plt.show()


def print_metrics(metrics, k):
    """
    Print compression statistics.
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


def main():

    image_path = "images/sample.jpg"

    img = load_image(image_path)

    k = int(input("Enter compression level (k): "))

    compressed_img = compress_image(img, k)

    metrics = calculate_compression_metrics(image_path, img, k)

    print_metrics(metrics, k)

    show_images(img, compressed_img)

    # Save compressed output
    compressed_uint8 = np.clip(compressed_img, 0, 255).astype(np.uint8)
    Image.fromarray(compressed_uint8).save("compressed_output.jpg")


if __name__ == "__main__":
    main()