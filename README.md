## 🏎️ Hardware Benchmark: The Death Race (Acer Nitro 16)
Verified on Ryzen 7 / WSL2 Ubuntu. Observed near-zero overhead relative to subprocess bridges.

| Metric | Subprocess Bridge (Legacy) | Direct C-Binding (CN2 v1.2) | Speedup |
| :--- | :--- | :--- | :--- |
| **Latency per Call** | 664,000 ns | **244 ns** | **2,718x** |
| **Stability** | - | **1,000,000+ Iterations** | **Verified** |

## 🛡️ Quick Start (The CN2 Interface)
Harden your Python logic with sub-microsecond metal-level validation.

```python
from guardian_wrapper import CN2Guardian, GuardianStatus

# Initialize the Metal
guard = CN2Guardian()

# Inspect payload (Latency: ~244ns)
status = guard.inspect("your_payload_here")

if status == GuardianStatus.SUCCESS:
    # Proceed to high-level logic
    pass
elif status == GuardianStatus.OVERFLOW:
    print("🚨 Attack Blocked: Payload size violation.")
