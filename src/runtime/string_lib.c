#include "string_lib.h"
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
