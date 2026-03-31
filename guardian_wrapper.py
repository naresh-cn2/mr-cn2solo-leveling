import ctypes
from enum import IntEnum
from pathlib import Path

class GuardianStatus(IntEnum):
    SUCCESS = 0
    OVERFLOW = -1
    NULL_PTR = -2

class CN2Guardian:
    def __init__(self):
        lib_path = Path(__file__).parent / "libguardian.so"
        self._lib = ctypes.CDLL(str(lib_path))
        self._lib.validate_guardian.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
        self._lib.validate_guardian.restype = ctypes.c_int

    def inspect(self, data: str) -> GuardianStatus:
        if data is None:
            return GuardianStatus.NULL_PTR
        b_data = data.encode('utf-8')
        result = self._lib.validate_guardian(b_data, len(b_data))
        return GuardianStatus(result)

if __name__ == "__main__":
    guard = CN2Guardian()
    print(f"Normal Check: {guard.inspect('safe_data').name}")
    print(f"Attack Check: {guard.inspect('A' * 500).name}")
