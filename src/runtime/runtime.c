#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _WIN32
    #include <windows.h>
#else
    #include <unistd.h>
#endif

// Input function for float (language 'float' mapped to double in LLVM)
void input_float(double *ptr) {
    if (scanf("%lf", ptr) != 1) {
        fprintf(stderr, "Error reading float input\n");
        *ptr = 0.0;
    }
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Input function for int
void input_int(int *ptr) {
    // Get the integer input
    if (scanf("%d", ptr) != 1) {
        fprintf(stderr, "Error reading integer input\n");
        *ptr = 0;
    }

    // Clear any remaining characters in the input buffer
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Input function for string
void input_string(char **ptr) {
    // Allocate a buffer for the input
    char *buffer = (char*)malloc(256);
    if (!buffer) {
        *ptr = NULL;
        return;
    }
    
    // Read a line of input (up to 255 characters)
    if (fgets(buffer, 256, stdin) != NULL) {
        // Remove the trailing newline if present
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len-1] == '\n') {
            buffer[len-1] = '\0';
        }
        *ptr = buffer;
    } else {
        // Error or EOF, set to empty string
        strcpy(buffer, "");
        *ptr = buffer;
    }
}

// Input function for char
void input_char(char *ptr) {
    // Clear any pending input
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    
    // Get the character input
    *ptr = getchar();
}

// Output function for float (double precision) with precision specifier
void output_float(double value, int precision) {
    if(precision < 0) precision = 0;
    if(precision > 12) precision = 12; // clamp to reasonable max
    char fmt[16];
    // Build format string like %.3f\n
    snprintf(fmt, sizeof(fmt), "%%.%df\n", precision);
    printf(fmt, value);
}

// Output function for int
void output_int(int value) {
    printf("%d\n", value);
}

// Output function for string
void output_string(const char *value) {
    if (value) {
        printf("%s\n", value);
    } else {
        printf("(null)\n");
    }
}

// Output function for char
void output_char(char value) {
    printf("%c\n", value);
}

// String concatenation
char* concat_strings(const char* s1, const char* s2) {
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    char* result = (char*)malloc(len1 + len2 + 1);
    if (result) {
        strcpy(result, s1);
        strcat(result, s2);
    }
    return result;
}

// Type-to-string conversion functions
char* int_to_string(int value) {
    // Allocate enough space for the string representation
    // Max int is 10 digits + sign + null terminator
    char* result = (char*)malloc(12);
    if (result) {
        snprintf(result, 12, "%d", value);
    }
    return result;
}

char* float_to_string(double value) {
    // Allocate enough space for the string representation
    char* result = (char*)malloc(32);
    if (result) {
        snprintf(result, 32, "%g", value);
    }
    return result;
}

char* char_to_string(char value) {
    // Allocate space for single char + null terminator
    char* result = (char*)malloc(2);
    if (result) {
        result[0] = value;
        result[1] = '\0';
    }
    return result;
}
// Exit function
void exit_program() {
    exit(0);
}

// Sleep function - sleeps for specified number of seconds
void pie_sleep(int seconds) {
    if (seconds > 0) {
        #ifdef _WIN32
            Sleep(seconds * 1000); // Windows uses milliseconds
        #else
            sleep(seconds); // Unix/Linux uses seconds
        #endif
    }
}
