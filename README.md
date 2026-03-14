# NumPy Image Compression using SVD

This project demonstrates how Singular Value Decomposition (SVD) can compress images using NumPy.

## How it works

1. Convert image to grayscale matrix
2. Apply SVD
3. Keep top k singular values
4. Reconstruct image

## Example

Original vs Compressed Image

## Run

pip install -r requirements.txt

python compress.py

3️⃣ Architecture Design
System Architecture
User
  │
  ▼
Main Controller
  │
  ├── Image Loader
  │
  ├── SVD Compression Engine
  │
  ├── Compression Metrics Analyzer
  │
  └── Visualization Module
4️⃣ Module Responsibilities
1. Image Loader

Function:

load_image()

Responsibilities:

read image file

convert to grayscale

transform to NumPy matrix

Example matrix representation:

[
 [120 122 125 ...]
 [118 119 123 ...]
 ...
]

Each value = pixel intensity (0–255)

2. Compression Engine

Function:

compress_image()

Core operation:

A = U Σ Vᵀ

Where:

A  = original image matrix
U  = left singular vectors
Σ  = singular values
Vᵀ = right singular vectors

Instead of storing full matrix:

A ≈ U_k Σ_k V_kᵀ

We keep only top k singular values.

5️⃣ Deep Mathematical Explanation

For an image matrix:

A ∈ R^(m × n)

SVD decomposes it into:

A = U Σ Vᵀ

Where:

U = m × m
Σ = m × n
Vᵀ = n × n

But we only keep:

U_k = m × k
Σ_k = k × k
V_kᵀ = k × n

Reconstruction:

A_k = U_k Σ_k V_kᵀ
6️⃣ Why Compression Works

Natural images contain redundant information.

Example:

Large areas like sky, walls, skin tones have similar pixel values.

This means the matrix has low effective rank.

Thus:

Top singular values capture most information

Small singular values represent noise or minor details.

7️⃣ Storage Analysis

Original storage:

m × n

Compressed storage:

k(m + n + 1)

Example:

Image: 512 × 512
Original = 262144 values

If:

k = 40

Compressed storage:

40(512 + 512 + 1)
≈ 40920

Compression ratio:

262144 / 40920 ≈ 6.4x
8️⃣ Computational Complexity

SVD complexity:

O(mn²)

For large images:

~ millions of operations

NumPy uses optimized LAPACK routines, making it very fast.

9️⃣ Real World Applications

SVD compression is used in:

Image processing

photo compression

noise reduction

Recommender systems

Netflix recommendation algorithm

Natural language processing

Latent Semantic Analysis

Signal processing

audio compression

🔟 Limitations

SVD compression has tradeoffs:

Advantage	Limitation
mathematically elegant	computationally expensive
good theoretical compression	not optimal for storage
preserves structure	slower than JPEG

That's why JPEG uses DCT instead of SVD.