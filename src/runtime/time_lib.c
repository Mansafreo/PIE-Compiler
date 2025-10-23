#include "time_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Returns the current time as a Unix timestamp (seconds since epoch)
int pie_time_now() {
    return (int)time(NULL);
}

// Converts a Unix timestamp to a local time string (e.g., "HH:MM:SS")
char* pie_time_to_local(int timestamp) {
    time_t time_val = (time_t)timestamp;
    struct tm *info;
    info = localtime(&time_val);

    // Allocate memory for the formatted time string
    char* buffer = (char*) malloc(9 * sizeof(char));
    if (buffer == NULL) {
        return NULL; // Memory allocation failed
    }

    // Format the time into "HH:MM:SS"
    strftime(buffer, 9, "%H:%M:%S", info);

    return buffer;
}
