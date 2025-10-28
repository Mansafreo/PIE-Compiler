#include "string_lib.h"
#include "d_array.h"
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// Basic string functions
int pie_strlen(const char* s) {
    return strlen(s);
}

int pie_strcmp(const char* s1, const char* s2) {
    return strcmp(s1, s2);
}

char* pie_strcpy(char* dest, const char* src) {
    return strcpy(dest, src);
}

char* pie_strcat(char* dest, const char* src) {
    return strcat(dest, src);
}

// Advanced string utilities

// Convert string to uppercase
char* string_to_upper(const char* str) {
    if (!str) return NULL;
    
    size_t len = strlen(str);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (size_t i = 0; i < len; i++) {
        result[i] = toupper((unsigned char)str[i]);
    }
    result[len] = '\0';
    
    return result;
}

// Convert string to lowercase
char* string_to_lower(const char* str) {
    if (!str) return NULL;
    
    size_t len = strlen(str);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (size_t i = 0; i < len; i++) {
        result[i] = tolower((unsigned char)str[i]);
    }
    result[len] = '\0';
    
    return result;
}

// Trim leading and trailing whitespace
char* string_trim(const char* str) {
    if (!str) return NULL;
    
    // Find first non-whitespace character
    while (*str && isspace((unsigned char)*str)) {
        str++;
    }
    
    if (*str == '\0') {
        char* result = (char*)malloc(1);
        if (result) result[0] = '\0';
        return result;
    }
    
    // Find last non-whitespace character
    const char* end = str + strlen(str) - 1;
    while (end > str && isspace((unsigned char)*end)) {
        end--;
    }
    
    size_t len = end - str + 1;
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    memcpy(result, str, len);
    result[len] = '\0';
    
    return result;
}

// Extract substring from start position with given length
char* string_substring(const char* str, int start, int length) {
    if (!str || start < 0 || length < 0) return NULL;
    
    size_t str_len = strlen(str);
    if ((size_t)start >= str_len) {
        char* result = (char*)malloc(1);
        if (result) result[0] = '\0';
        return result;
    }
    
    // Adjust length if it exceeds string bounds
    if ((size_t)(start + length) > str_len) {
        length = str_len - start;
    }
    
    char* result = (char*)malloc(length + 1);
    if (!result) return NULL;
    
    memcpy(result, str + start, length);
    result[length] = '\0';
    
    return result;
}

// Find index of first occurrence of needle in haystack
int string_index_of(const char* haystack, const char* needle) {
    if (!haystack || !needle) return -1;
    
    const char* pos = strstr(haystack, needle);
    if (!pos) return -1;
    
    return (int)(pos - haystack);
}

// Replace all occurrences of old_char with new_char
char* string_replace_char(const char* str, char old_char, char new_char) {
    if (!str) return NULL;
    
    size_t len = strlen(str);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (size_t i = 0; i < len; i++) {
        result[i] = (str[i] == old_char) ? new_char : str[i];
    }
    result[len] = '\0';
    
    return result;
}

// Reverse a string
char* string_reverse(const char* str) {
    if (!str) return NULL;
    
    size_t len = strlen(str);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (size_t i = 0; i < len; i++) {
        result[i] = str[len - 1 - i];
    }
    result[len] = '\0';
    
    return result;
}

// Count occurrences of a character in string
int string_count_char(const char* str, char ch) {
    if (!str) return 0;
    
    int count = 0;
    while (*str) {
        if (*str == ch) count++;
        str++;
    }
    
    return count;
}

// Get character at specific index
char string_char_at(const char* str, int index) {
    if (!str || index < 0) return '\0';
    
    size_t len = strlen(str);
    if ((size_t)index >= len) return '\0';
    
    return str[index];
}

// Split string by delimiter
// Returns array of strings and sets count to number of parts
// Caller must free the returned array and each string in it
char** string_split(const char* str, const char* delimiter, int* count) {
    if (!str || !delimiter || !count) {
        if (count) *count = 0;
        return NULL;
    }
    
    // Handle empty delimiter - return whole string
    if (delimiter[0] == '\0') {
        char** result = (char**)malloc(sizeof(char*));
        if (!result) {
            *count = 0;
            return NULL;
        }
        result[0] = (char*)malloc(strlen(str) + 1);
        if (!result[0]) {
            free(result);
            *count = 0;
            return NULL;
        }
        strcpy(result[0], str);
        *count = 1;
        return result;
    }
    
    // Count delimiters to determine array size
    int parts = 1;
    const char* temp = str;
    size_t delim_len = strlen(delimiter);
    
    while ((temp = strstr(temp, delimiter)) != NULL) {
        parts++;
        temp += delim_len;
    }
    
    // Allocate array for result
    char** result = (char**)malloc(parts * sizeof(char*));
    if (!result) {
        *count = 0;
        return NULL;
    }
    
    // Split the string
    int index = 0;
    const char* start = str;
    const char* end;
    
    while ((end = strstr(start, delimiter)) != NULL) {
        size_t part_len = end - start;
        result[index] = (char*)malloc(part_len + 1);
        if (!result[index]) {
            // Free previously allocated strings
            for (int i = 0; i < index; i++) {
                free(result[i]);
            }
            free(result);
            *count = 0;
            return NULL;
        }
        memcpy(result[index], start, part_len);
        result[index][part_len] = '\0';
        index++;
        start = end + delim_len;
    }
    
    // Add the last part
    size_t last_len = strlen(start);
    result[index] = (char*)malloc(last_len + 1);
    if (!result[index]) {
        for (int i = 0; i < index; i++) {
            free(result[i]);
        }
        free(result);
        *count = 0;
        return NULL;
    }
    strcpy(result[index], start);
    
    *count = parts;
    return result;
}

// Wrapper that returns DArrayString for easier use in PIE
DArrayString* string_split_to_array(const char* str, const char* delimiter) {
    if (!str || !delimiter) {
        return NULL;
    }
    
    int count = 0;
    char** parts = string_split(str, delimiter, &count);
    
    if (!parts) {
        return NULL;
    }
    
    // Create a DArrayString and populate it
    DArrayString* result = d_array_string_create();
    if (!result) {
        // Free the parts array
        for (int i = 0; i < count; i++) {
            free(parts[i]);
        }
        free(parts);
        return NULL;
    }
    
    // Add each part to the dynamic array
    for (int i = 0; i < count; i++) {
        d_array_string_append(result, parts[i]);
        free(parts[i]);  // Free the individual string after copying
    }
    free(parts);  // Free the array itself
    
    return result;
}
