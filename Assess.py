import psutil
import platform
import subprocess
import shutil

def get_size(bytes, suffix="B"):
    """Scale bytes to its proper format (e.g., MB, GB)."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def check_gpu():
    """Check for NVIDIA GPU using nvidia-smi."""
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total,memory.free', '--format=csv,noheader'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "NVIDIA GPU found, but nvidia-smi failed."
    except FileNotFoundError:
        return "No NVIDIA GPU detected (or nvidia-smi not in PATH)."

def run_diagnostics():
    print("="*50)
    print("🧠 MRI PROCESSING HARDWARE DIAGNOSTICS 🧠")
    print("="*50)

    # 1. CPU Information
    print("\n--- Processor (CPU) ---")
    print(f"Processor: {platform.processor()}")
    print(f"Physical cores (Fast parallel processing): {psutil.cpu_count(logical=False)}")
    print(f"Total threads (Hyperthreading): {psutil.cpu_count(logical=True)}")
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        print(f"Max Frequency: {cpu_freq.max:.2f}Mhz")

    # 2. Memory (RAM) Information
    print("\n--- Memory (RAM) ---")
    svmem = psutil.virtual_memory()
    print(f"Total RAM: {get_size(svmem.total)}")
    print(f"Available RAM: {get_size(svmem.available)}")
    
    # 3. GPU Information
    print("\n--- Graphics Processing Unit (GPU) ---")
    print(check_gpu())

    # 4. Storage Information
    print("\n--- Storage (Disk) ---")
    # Getting stats for the primary drive (where the script is run)
    total, used, free = shutil.disk_usage("/")
    print(f"Total Disk Space: {get_size(total)}")
    print(f"Free Disk Space: {get_size(free)}")
    
    print("\n" + "="*50)
    print("📊 NEUROIMAGING CAPABILITY ASSESSMENT 📊")
    print("="*50)
    
    # Simple Heuristics for MRI Processing
    ram_gb = svmem.total / (1024**3)
    cores = psutil.cpu_count(logical=False)
    
    if ram_gb >= 30 and cores >= 8:
        print("✅ Heavy Workloads: Capable of running fMRIPrep, FreeSurfer recon-all (parallelized), and handling large 4D datasets.")
    elif ram_gb >= 15:
        print("⚠️ Medium Workloads: Can run standard structural processing (SPM, FSL). Watch out for memory errors on large fMRI datasets or intensive Nipype workflows.")
    else:
        print("❌ Light Workloads Only: Limited to basic image viewing, single-subject lightweight preprocessing, or cropping. Consider upgrading RAM.")

if __name__ == "__main__":
    run_diagnostics()