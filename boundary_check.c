#include <stddef.h>

#define MAX_ALLOWED 256

/**
 * CN2 Boundary Guardian v1.1 - Hardened API
 * No strlen() usage. Length is enforced by the caller.
 */
int validate_guardian(const char* input_payload, size_t input_len) {
    if (!input_payload) return -2; // ERROR: Null Pointer

    // Metal-Level Boundary Enforcement
    if (input_len >= MAX_ALLOWED) {
        return -1; // REJECTED: Overflow detected
    }

    return (int)input_len; // ACCEPTED: Returns safe byte count
}
