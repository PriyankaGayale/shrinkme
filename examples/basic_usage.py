#!/usr/bin/env python
"""
Basic usage example of shrinkme library.

This script demonstrates the simplest way to compress an image.
"""

from pathlib import Path
from shrinkme import load_image, compress_image, save_compressed_image, calculate_compression_metrics, print_metrics

# Specify your image path
image_path = "images/sample.jpg"

# Check if the image exists
if not Path(image_path).exists():
    print(f"Error: Image not found at {image_path}")
    print("Please place a JPEG image in the images/ directory")
    exit(1)

# Load image
print("Loading image...")
img = load_image(image_path)
print(f"Image shape: {img.shape}")

# Compress with k=50
k_value = 50
print(f"\nCompressing with k={k_value}...")
compressed = compress_image(img, k=k_value)

# Calculate metrics
print("\nCalculating metrics...")
metrics = calculate_compression_metrics(image_path, img, k=k_value)
print_metrics(metrics, k=k_value)

# Save result
output_path = "compressed_output.jpg"
print(f"\nSaving compressed image to {output_path}...")
save_compressed_image(compressed, output_path)

print(f"✓ Successfully saved to {output_path}")
