# Shrinkme - SVD-Based Image Compression

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/shrinkme.svg)](https://badge.fury.io/py/shrinkme)
[![Tests](https://github.com/PriyankaGayale/shrinkme/workflows/tests/badge.svg)](https://github.com/PriyankaGayale/shrinkme/actions)

Compress images intelligently using **Singular Value Decomposition (SVD)**, a mathematical technique that reduces file size while maintaining visual quality. Perfect for batch processing, thumbnail generation, or optimizing image storage.

## 🚀 Features

- **SVD-Based Compression**: Uses mathematical decomposition to analyze and compress images
- **Flexible Resizing**: Resize images before or after compression to fit your needs
- **Dual Interface**: Use as a Python library or command-line tool
- **Detailed Metrics**: Get compression ratios, storage savings, and file size statistics
- **Visual Comparison**: Preview original vs. compressed images side-by-side
- **Batch Processing**: Easily compress multiple images programmatically
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📦 Installation

### Via pip (Recommended)

```bash
pip install shrinkme
```

### From source

```bash
git clone https://github.com/PriyankaGayale/shrinkme.git
cd shrinkme
pip install -e .
```

## 🎯 Quick Start

### Command Line

```bash
# Basic compression
shrinkme compress --input image.jpg --k 50

# Compress with resizing
shrinkme compress --input image.jpg --k 50 --resize 800x600

# Compress and visualize
shrinkme compress --input image.jpg --k 50 --visualize

# Save to custom output path
shrinkme compress --input image.jpg --k 50 --output result.jpg
```

### Python Library

```python
from shrinkme import load_image, compress_image, save_compressed_image

# Load image
img = load_image("image.jpg")

# Compress with k=50 singular values
compressed = compress_image(img, k=50)

# Save result
save_compressed_image(compressed, "output.jpg")
```

## 📚 Usage Examples

### Basic Compression

```python
from shrinkme import load_image, compress_image, save_compressed_image, print_metrics, calculate_compression_metrics

img = load_image("sample.jpg")
compressed = compress_image(img, k=50)
metrics = calculate_compression_metrics("sample.jpg", img, k=50)
print_metrics(metrics, k=50)
save_compressed_image(compressed, "compressed.jpg")
```

### Compression with Resizing

```python
from shrinkme import resize_image, compress_image, resize_output, save_compressed_image

# Resize before compression
img = resize_image("sample.jpg", width=800, height=600)
compressed = compress_image(img, k=40)
save_compressed_image(compressed, "result.jpg")

# Or resize after compression
img = load_image("sample.jpg")
compressed = compress_image(img, k=50)
resized = resize_output(compressed, width=1024, height=768)
save_compressed_image(resized, "result.jpg")
```

### Batch Processing

```python
from pathlib import Path
from shrinkme import load_image, compress_image, save_compressed_image

image_dir = Path("images/")
for img_path in image_dir.glob("*.jpg"):
    img = load_image(str(img_path))
    compressed = compress_image(img, k=50)
    output_path = f"compressed/{img_path.name}"
    save_compressed_image(compressed, output_path)
    print(f"✓ Processed {img_path.name}")
```

### Finding Optimal K Value

```python
from shrinkme import load_image, compress_image, calculate_compression_metrics

img = load_image("image.jpg")

for k in [20, 40, 60, 80, 100]:
    compressed = compress_image(img, k)
    metrics = calculate_compression_metrics("image.jpg", img, k)
    ratio = metrics["compression_ratio"]
    saved = metrics["space_saved"] * 100
    print(f"k={k}: {ratio:.2f}x compression, {saved:.1f}% space saved")
```

## 🔧 API Reference

See [docs/API.md](docs/API.md) for complete function documentation.

### Core Functions

- `load_image(path)` - Load image and convert to grayscale matrix
- `compress_image(img_matrix, k)` - Compress using SVD with k singular values
- `calculate_compression_metrics(path, img_matrix, k)` - Get compression statistics
- `save_compressed_image(matrix, output_path)` - Save compressed image to file
- `show_images(original, compressed)` - Display before/after comparison

### Utility Functions

- `resize_image(path, width, height)` - Resize image before compression
- `resize_output(matrix, width, height)` - Resize after compression
- `parse_dimension_string(dim_str)` - Parse "WIDTHxHEIGHT" format
- `preserve_aspect_ratio(...)` - Calculate dimensions preserving aspect ratio

## 📖 How It Works

### Mathematical Background

Shrinkme uses **Singular Value Decomposition (SVD)** to compress images:

1. **Convert image to matrix**: Each pixel is a value (0-255)
2. **Decompose matrix**: A = U × Σ × V^T
3. **Keep top k singular values**: Only use most significant components
4. **Reconstruct image**: A_k ≈ U_k × Σ_k × V_k^T

**Storage Savings:**
- Original: `m × n` values
- Compressed: `k(m + n + 1)` values

**Example**: A 512×512 image with k=50:
- Original: 262,144 values
- Compressed: 51,250 values
- **Compression ratio: 5.1x**
- **Space saved: 80.4%**

### Why SVD for Images?

Natural images contain redundant information (similar colors in large areas). SVD exploits this by keeping only the most important information (highest singular values) and discarding the rest.

## 🎮 CLI Commands

```bash
shrinkme compress --help
```

**Options:**
- `--input, -i` (required): Path to input image
- `--k, -k` (required): Number of singular values to keep
- `--output, -o`: Save path (default: compressed_output.jpg)
- `--resize, -r`: Resize input to WIDTHxHEIGHT before compression
- `--resize-output`: Resize output to WIDTHxHEIGHT after compression
- `--visualize, -v`: Show before/after comparison
- `--metrics, -m`: Display compression statistics (default: true)

## 📋 Requirements

- Python 3.8 or higher
- numpy >= 1.21.0
- Pillow >= 8.0.0
- matplotlib >= 3.3.0 (for visualization)

## 🧪 Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=shrinkme
```

## 🚧 Development

### Setup Development Environment

```bash
git clone https://github.com/PriyankaGayale/shrinkme.git
cd shrinkme
pip install -e ".[dev]"
```

### Code Style

```bash
# Format code
black shrinkme/

# Check style
flake8 shrinkme/

# Sort imports
isort shrinkme/
```

### Building Distribution Package

```bash
pip install build twine

# Build
python -m build

# Test upload
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [NumPy](https://numpy.org/) for efficient matrix operations
- Image processing with [Pillow](https://python-pillow.org/)
- Visualization using [Matplotlib](https://matplotlib.org/)

## 📞 Support & Feedback

- **Issues**: [GitHub Issues](https://github.com/PriyankaGayale/shrinkme/issues)
- **Discussions**: [GitHub Discussions](https://github.com/PriyankaGayale/shrinkme/discussions)
- **Security**: See [SECURITY.md](SECURITY.md) for vulnerability reporting

## 💡 Tips & Tricks

### Choosing the Right K Value

| K Value | Use Case |
|---------|----------|
| 10-20 | Aggressive compression, thumbnails |
| 30-50 | Balanced quality/compression |
| 60-100 | High quality, web images |
| 100+ | Minimal compression, archival |

### Performance Tips

1. **Resize first**: Smaller images compress faster
2. **Batch process**: Use loops for efficiency
3. **Experiment**: Test different k values to find sweet spot