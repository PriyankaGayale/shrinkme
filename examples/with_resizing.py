#!/usr/bin/env python
"""
Compression with resizing example for shrinkme.

Demonstrates how to resize images before and/or after compression.
"""

from pathlib import Path
from shrinkme import (
    load_image,
    resize_image,
    compress_image,
    resize_output,
    save_compressed_image,
    calculate_compression_metrics,
    parse_dimension_string,
)

image_path = "images/sample.jpg"
k_value = 50

# Check if image exists
if not Path(image_path).exists():
    print(f"Error: Image not found at {image_path}")
    exit(1)

print("=" * 50)
print("Example 1: Resize BEFORE Compression")
print("=" * 50)

# Pre-compression resizing (faster processing)
print(f"Loading and resizing image to 800x600...")
img_resized_input = resize_image(image_path, width=800, height=600)
print(f"Resized image shape: {img_resized_input.shape}")

compressed_1 = compress_image(img_resized_input, k=k_value)
metrics_1 = calculate_compression_metrics(image_path, img_resized_input, k=k_value)

save_compressed_image(compressed_1, "example1_resized_input.jpg")
print(f"✓ Saved: example1_resized_input.jpg")
print(f"  Compression ratio: {metrics_1['compression_ratio']:.2f}x")
print(f"  Space saved: {metrics_1['space_saved']*100:.1f}%")

print("\n" + "=" * 50)
print("Example 2: Resize AFTER Compression")
print("=" * 50)

# Post-compression resizing (exact output dimensions)
print(f"Loading image...")
img = load_image(image_path)
print(f"Original shape: {img.shape}")

print(f"Compressing with k={k_value}...")
compressed = compress_image(img, k=k_value)

print(f"Resizing output to 1024x768...")
resized_output = resize_output(compressed, width=1024, height=768)
print(f"Final shape: {resized_output.shape}")

save_compressed_image(resized_output, "example2_resized_output.jpg")
print(f"✓ Saved: example2_resized_output.jpg")

print("\n" + "=" * 50)
print("Example 3: Parse Dimension String and Resize")
print("=" * 50)

# Using parse_dimension_string for flexible dimension input
dimension_strings = ["800x600", "1920x1080", "640x480"]

for dim_str in dimension_strings:
    width, height = parse_dimension_string(dim_str)
    print(f"\nResizing to {dim_str} ({width}x{height})...")
    
    img = load_image(image_path)
    resized = resize_image(image_path, width, height)
    compressed = compress_image(resized, k=k_value)
    
    output_file = f"example3_{dim_str.replace('x', '_')}.jpg"
    save_compressed_image(compressed, output_file)
    print(f"✓ Saved: {output_file}")

print("\n" + "=" * 50)
print("Example 4: Batch Resizing with Different Aspect Ratios")
print("=" * 50)

from shrinkme import preserve_aspect_ratio

# Original image dimensions (you would get these from the actual image)
original_width = 1920
original_height = 1080

targets = [
    ("mobile", 480, 360),
    ("tablet", 1024, 768),
    ("desktop", 1600, 1200),
]

img = load_image(image_path)

for name, target_w, target_h in targets:
    # Preserve aspect ratio while fitting to target
    new_w, new_h = preserve_aspect_ratio(original_width, original_height, target_w, target_h)
    
    print(f"\n{name.upper()} ({target_w}x{target_h}):")
    print(f"  Calculated dimensions: {new_w}x{new_h}")
    
    resized = resize_image(image_path, new_w, new_h)
    compressed = compress_image(resized, k=k_value)
    
    output_file = f"example4_{name}.jpg"
    save_compressed_image(compressed, output_file)
    print(f"  ✓ Saved: {output_file}")

print("\n" + "=" * 50)
print("All examples completed successfully!")
print("=" * 50)
