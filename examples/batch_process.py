#!/usr/bin/env python
"""
Batch processing example for shrinkme.

Compress multiple images in a directory at once.
"""

from pathlib import Path
from shrinkme import load_image, compress_image, save_compressed_image, calculate_compression_metrics

# Configuration
input_directory = Path("images")
output_directory = Path("compressed_images")
k_value = 50

# Create output directory if it doesn't exist
output_directory.mkdir(exist_ok=True)

# Find all JPG files in input directory
image_files = list(input_directory.glob("*.jpg")) + list(input_directory.glob("*.jpeg"))

if not image_files:
    print(f"No JPEG images found in {input_directory}")
    exit(1)

print(f"Found {len(image_files)} images to process\n")

# Process each image
processed = 0
total_original_size = 0
total_compressed_size = 0

for img_path in sorted(image_files):
    try:
        # Load image
        img = load_image(str(img_path))
        
        # Compress
        compressed = compress_image(img, k=k_value)
        
        # Calculate metrics
        metrics = calculate_compression_metrics(str(img_path), img, k=k_value)
        total_original_size += metrics["matrix_size"]
        total_compressed_size += metrics["compressed_matrix_size"]
        
        # Save
        output_path = output_directory / f"{img_path.stem}_compressed.jpg"
        save_compressed_image(compressed, str(output_path))
        
        ratio = metrics["compression_ratio"]
        saved = metrics["space_saved"] * 100
        print(f"✓ {img_path.name}: {ratio:.2f}x compression, {saved:.1f}% saved")
        
        processed += 1
        
    except Exception as e:
        print(f"✗ {img_path.name}: {e}")

# Summary
print(f"\n{'='*50}")
print(f"Batch Processing Complete")
print(f"{'='*50}")
print(f"Processed: {processed}/{len(image_files)} images")
print(f"Output directory: {output_directory.absolute()}")

if processed > 0:
    overall_ratio = total_original_size / total_compressed_size if total_compressed_size > 0 else 0
    overall_saved = (1 - total_compressed_size / total_original_size) * 100 if total_original_size > 0 else 0
    print(f"Overall compression: {overall_ratio:.2f}x")
    print(f"Total space saved: {overall_saved:.1f}%")
