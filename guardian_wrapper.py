import ctypes
from enum import IntEnum
from pathlib import Path

# Map the C-Enum exactly so Python understands the metal's language
class GuardianStatus(IntEnum):
    SUCCESS = 0
    OVERFLOW = -1
    NULL_PTR = -2

class CN2Guardian:
    def __init__(self):
        # Self-locating library logic
        lib_path = Path(__file__).parent / "libguardian.so"
        self._lib = ctypes.CDLL(str(lib_path))
        self._lib.validate_guardian.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
        self._lib.validate_guardian.restype = ctypes.c_int

    def inspect(self, data: str) -> GuardianStatus:
        """High-speed boundary inspection."""
        if data is None:
            return GuardianStatus.NULL_PTR
        
        # Convert to bytes for the C engine
        b_data = data.encode('utf-8')
        result = self._lib.validate_guardian(b_data, len(b_data))
        
        # Convert the raw integer back into a readable Status Name
        return GuardianStatus(result)

# --- THE PROOF ---
if __name__ == "__main__":
    gate = CN2Guardian()
    
    # Test 1: Normal Data
    print(f"Normal Check: {gate.inspect('hello_world').name}")
    
    # Test 2: Attack Data
    print(f"Attack Check: {gate.inspect('X' * 500).name}")
