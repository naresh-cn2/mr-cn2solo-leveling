
## 🏎️ Hardware Benchmark: The Death Race (Acer Nitro 16)
Verified on Ryzen 7 / WSL2 Ubuntu:

| Metric | Subprocess Bridge | Direct C-Binding (.so) | Speedup |
| :--- | :--- | :--- | :--- |
| **Latency** | 664,000 ns / call | **244 ns / call** | **2,718x** |
| **Throughput** | ~1,500 req/sec | **~4,098,000 req/sec** | **Absolute** |

**Engineering Note:** The subprocess bridge is bottlenecked by OS context switching. The direct C-binding executes at the speed of raw RAM access.
