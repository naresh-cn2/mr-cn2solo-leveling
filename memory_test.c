#include <stdio.h>
#include <stdlib.h>

int main() {
    // 1GB = roughly 250,000,000 integers (4 bytes each)
    size_t num_elements = 250000000;
    size_t size = num_elements * sizeof(int);

    printf("[INIT] Allocating 1GB of virtual memory...\n");
    int *data = (int *)malloc(size);

    if (data == NULL) {
        printf("[ERROR] Memory allocation failed.\n");
        return 1;
    }

    printf("[COMMIT] Forcing Linux Page Faults (Writing to physical RAM)...\n");
    // THE FIX: Writing to the array forces Linux to give us actual physical silicon.
    for (size_t i = 0; i < num_elements; i++) {
        data[i] = 1; 
    }

    printf("[READ] Iterating over physical RAM...\n");
    volatile long long sum = 0; // volatile prevents compiler from skipping this loop
    for (size_t i = 0; i < num_elements; i++) {
        sum += data[i];
    }

    printf("[SUCCESS] 1GB physically written and read. Freeing memory.\n");
    free(data);

    return 0;
}
