#ifndef TIME_LIB_H
#define TIME_LIB_H

// Returns the current time as a Unix timestamp (seconds since epoch)
int pie_time_now();

// Converts a Unix timestamp to a local time string (e.g., "HH:MM:SS")
char* pie_time_to_local(int timestamp);

#endif // TIME_LIB_H
