# 🧠 Neuro-Hardware Check (WSL2 Optimized)

A lightweight Python diagnostic tool designed for neuroimaging researchers to assess if their hardware can handle intensive MRI processing pipelines (e.g., FreeSurfer, fMRIPrep, FSL, AFNI).

## 🚀 Purpose
MRI processing is resource-heavy. This script evaluates:
- **RAM Capacity:** Checks if you have the 16GB-32GB+ required for high-res pipelines.
- **Disk I/O:** Benchmarks read/write speeds (crucial for 4D fMRI datasets).
- **GPU Availability:** Detects NVIDIA CUDA support for accelerated tools like `eddy_cuda` or `FastSurfer`.
- **WSL2 Verification:** Confirms if Windows Subsystem for Linux is correctly seeing your assigned resources.

Dependencies:
pip install -r requirements.txt


## 🛠️ Installation & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/neuro-hardware-check.git](https://github.com/yourusername/neuro-hardware-check.git)
   cd neuro-hardware-check