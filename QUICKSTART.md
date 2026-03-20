# Shrinkme - Quick Start Guide

## 🚀 Installation

### On macOS/Linux/Windows

```bash
# Install globally (recommended)
pip install shrinkme

# Or install for current user only
pip install --user shrinkme
```

### Verify Installation

```bash
shrinkme --help
```

If `command not found`, try:
```bash
python3 -m shrinkme.cli --help
```

## 💡 Basic Usage

### Command Line (Easiest)

```bash
# Compress an image
shrinkme compress --input image.jpg --k 50

# With custom output
shrinkme compress --input image.jpg --k 50 --output compressed.jpg

# With resizing before compression
shrinkme compress --input image.jpg --k 50 --resize 800x600

# Show statistics
shrinkme compress --input image.jpg --k 50 --metrics

# All options
shrinkme compress --input image.jpg --k 50 --output result.jpg --resize 800x600 --visualize
```

### Python Code

```python
from shrinkme import load_image, compress_image, save_compressed_image

# Load
img = load_image("image.jpg")

# Compress
compressed = compress_image(img, k=50)

# Save
save_compressed_image(compressed, "output.jpg")
```

## 🎯 Common Tasks

### Compress with Different Quality Levels

```bash
# Aggressive (smallest file size)
shrinkme compress --input image.jpg --k 20

# Balanced (default)
shrinkme compress --input image.jpg --k 50

# High quality (minimal compression)
shrinkme compress --input image.jpg --k 100
```

### Resize Images

```bash
# Resize to 800x600 before compression
shrinkme compress --input large.jpg --k 50 --resize 800x600

# Resize output to exact dimensions
shrinkme compress --input image.jpg --k 50 --resize-output 1024x768
```

### Batch Process Multiple Images

```python
from pathlib import Path
from shrinkme import load_image, compress_image, save_compressed_image

output_dir = Path("compressed")
output_dir.mkdir(exist_ok=True)

for img_path in Path("images").glob("*.jpg"):
    img = load_image(str(img_path))
    compressed = compress_image(img, k=50)
    save_compressed_image(compressed, str(output_dir / img_path.name))
    print(f"✓ {img_path.name}")
```

## 📊 Understanding K Values

| K | Compression | File Size | Best For |
|----|-----------|-----------|----------|
| 10-20 | Very high (90%+ savings) | Tiny | Thumbnails |
| 30-50 | High (80%+ savings) | Small | Web images |
| 60-100 | Medium (50%+ savings) | Medium | Photos |
| 100+ | Low (<50% savings) | Large | Archival |

**Tip**: Start with k=50 and adjust based on results.

## ❓ Troubleshooting

### "command not found: shrinkme"

```bash
# Option 1: Update PATH
pipx ensurepath

# Option 2: Use python module
python3 -m shrinkme.cli compress --input image.jpg --k 50

# Option 3: Install in virtual environment
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# or: myenv\Scripts\activate (Windows)
pip install shrinkme
shrinkme --help
```

### "ModuleNotFoundError: No module named 'numpy'"

```bash
pip install shrinkme --upgrade
```

### "Input file not found"

```bash
# Make sure the path is correct
shrinkme compress --input ./images/photo.jpg --k 50

# Or use absolute path
shrinkme compress --input /full/path/to/image.jpg --k 50
```

## 📖 Documentation

- **Full API**: See [docs/API.md](docs/API.md)
- **Advanced Examples**: See [docs/EXAMPLES.md](docs/EXAMPLES.md)
- **Installation Guide**: See [docs/INSTALLATION.md](docs/INSTALLATION.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🔗 Getting Help

- **Issues**: GitHub Issues
- **Questions**: GitHub Discussions
- **Bug Reports**: See [SECURITY.md](SECURITY.md)

## ✨ What's Next?

1. **Try**: `shrinkme compress --input image.jpg --k 50`
2. **Experiment**: Test different k values
3. **Batch**: Process multiple images
4. **Integrate**: Use in your Python projects
5. **Share**: Let others know about shrinkme!

---

**That's it!** You're ready to start compressing images. 🎉
