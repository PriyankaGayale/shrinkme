# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-03-20

### Added
- Initial release of Shrinkme
- Core SVD-based image compression using NumPy
- `compress_image()` function for SVD compression with configurable k values
- `load_image()` function for loading grayscale images
- `save_compressed_image()` function for saving compressed results
- `calculate_compression_metrics()` for detailed compression statistics
- Image visualization with `show_images()` side-by-side comparison
- `resize_image()` function for pre-compression resizing
- `resize_output()` function for post-compression resizing
- `parse_dimension_string()` utility for dimension string parsing
- `preserve_aspect_ratio()` utility for aspect ratio preservation
- `get_common_resolutions()` with preset dimensions (VGA, FHD, 4K, etc)
- Command-line interface via `shrinkme` command
- CLI support for compression with optional resizing and visualization
- Comprehensive documentation in README.md
- Full test suite with pytest
- Development dependencies configuration
- Package distribution via PyPI
- MIT License
- Contributing guidelines in CONTRIBUTING.md
- Code of Conduct
- Security policy
- GitHub Actions workflows for automated testing and deployment
- Example scripts for common use cases
- Detailed API documentation

### Features
- ✅ SVD-based compression using top-k singular values
- ✅ Flexible resizing before/after compression
- ✅ Dual interface (CLI + Python library)
- ✅ Compression metrics and statistics
- ✅ Visual comparison of original vs compressed
- ✅ Batch processing capability
- ✅ Cross-platform support (Windows, macOS, Linux)

## [Unreleased]

### Planned
- Support for colored (RGB) image compression
- GPU acceleration with CUDA/PyTorch
- Web interface for online compression
- Advanced filters and preprocessing
- Lossy vs lossless compression options
- Multi-threaded batch processing
- REST API server
- Docker containerization
- Comprehensive GUI application

---

For more details, see [https://github.com/akshayubale/shrinkme/releases](https://github.com/akshayubale/shrinkme/releases)
