import subprocess
import json

def validate_payload(payload: str):
    """
    High-speed C-Logic Bridge.
    Pipes Python data into the CN2 C-Guardian for metal-level validation.
    """
    # 1. Initialize the C-Binary process
    process = subprocess.Popen(
        ['./cn2_guardian'], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # 2. Pipe the Python payload into the C-Engine
    stdout, stderr = process.communicate(input=payload)

    # 3. Return the structured JSON audit log
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return {"status": "ERROR", "reason": "C_ENGINE_COMMUNICATION_FAILURE"}

# --- LIVE TEST SUITE ---
if __name__ == "__main__":
    print("--- TESTING PYTHON-TO-C BRIDGE ---")
    
    # Test 1: Safe Logic
    safe_test = validate_payload("user_id_123_auth_token")
    print(f"SAFE TEST: {safe_test['status']} (ID: {safe_test['request_id']})")

    # Test 2: Attack Logic
    attack_payload = "X" * 500
    attack_test = validate_payload(attack_payload)
    print(f"ATTACK TEST: {attack_test['status']} (Reason: {attack_test['reason']})")
