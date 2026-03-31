import ctypes
import subprocess
import time
import os

# Load the Metal
lib = ctypes.CDLL(os.path.abspath("./libguardian.so"))
lib.validate_guardian.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
lib.validate_guardian.restype = ctypes.c_int

def run_benchmarks():
    payload = "user_auth_token_safe"
    byte_payload = payload.encode('utf-8')
    
    print("--- 🏎️ PERFORMANCE DEATH RACE ---")
    
    # Test 1: Subprocess (The slow way)
    iters_sub = 100
    start = time.time()
    for _ in range(iters_sub):
        p = subprocess.Popen(['./cn2_guardian'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        p.communicate(input=payload)
    sub_total = time.time() - start

    # Test 2: C-Binding (The fast way)
    iters_ct = 1_000_000
    start = time.time()
    for _ in range(iters_ct):
        lib.validate_guardian(byte_payload, len(byte_payload))
    ct_total = time.time() - start

    # Math
    sub_lat = sub_total / iters_sub
    ct_lat = ct_total / iters_ct
    
    print(f"Subprocess Latency: {sub_lat:.6f} sec/call")
    print(f"C-Binding Latency:  {ct_lat:.9f} sec/call")
    print(f"\n🚀 SPEEDUP: {sub_lat / ct_lat:,.1f}x FASTER")

if __name__ == "__main__":
    run_benchmarks()
