#include <stdio.h>
#include <string.h>

// The strict memory boundary for our pipeline
#define MAX_ALLOWED 256

// Traceability: Start at 1000 for a professional log appearance
static int request_id = 1000;

int main() {
    char buffer[MAX_ALLOWED];
    int current_id = request_id++; // Capture ID for this specific transaction

    // Listen to standard input (stdin) for incoming pipeline data
    if (fgets(buffer, MAX_ALLOWED, stdin) != NULL) {
        size_t len = strlen(buffer);

        // OVERFLOW DETECTION:
        if (len == MAX_ALLOWED - 1 && buffer[len - 1] != '\n') {
            
            // Output Traceable REJECTED JSON
            printf("{\n");
            printf("  \"request_id\": %d,\n", current_id);
            printf("  \"status\": \"REJECTED\",\n");
            printf("  \"reason\": \"BUFFER_OVERFLOW_ATTEMPT\",\n");
            printf("  \"max_allowed\": %d\n", MAX_ALLOWED);
            printf("}\n");
            
            return 1; 
        } 
        else {
            // Clean up the newline character
            if (len > 0 && buffer[len - 1] == '\n') {
                buffer[len - 1] = '\0';
                len--;
            }
            
            // Output Traceable ACCEPTED JSON
            printf("{\n");
            printf("  \"request_id\": %d,\n", current_id);
            printf("  \"status\": \"ACCEPTED\",\n");
            printf("  \"payload_length\": %zu,\n", len);
            printf("  \"max_allowed\": %d\n", MAX_ALLOWED);
            printf("}\n");
            
            return 0; 
        }
    }
    return 0;
} 
