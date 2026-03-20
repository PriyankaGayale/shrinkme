"""
Setup configuration for shrinkme package.

This file specifies package metadata, dependencies, and distribution information
for building and publishing the shrinkme package to PyPI.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shrinkme",
    version="0.1.0",
    author="Akshay Ubale",
    author_email="your.email@example.com",
    description="Compress images using Singular Value Decomposition (SVD)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akshayubale/shrinkme",
    project_urls={
        "Bug Tracker": "https://github.com/iakshayubale/shrinkme/issues",
        "Documentation": "https://github.com/iakshayubale/shrinkme/blob/main/docs",
        "Source Code": "https://github.com/akshayubale/shrinkme",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "Pillow>=8.0.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.12.0",
            "flake8>=3.9.0",
            "black>=21.0",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "shrinkme=shrinkme.cli:main",
        ],
    },
    include_package_data=True,
    keywords="image-compression svd singular-value-decomposition compression",
    zip_safe=False,
)
