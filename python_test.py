import sys

print("[INIT] Allocating 1GB of memory (250M integers)...")
num_elements = 250000000

# Python's way of allocating the array
data = [1] * num_elements

print("[READ] Iterating over memory...")
total = sum(data)

print("[SUCCESS] Python execution complete.")
