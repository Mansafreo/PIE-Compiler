#include "crypto_lib.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

// ============================================================================
// TYPE CONVERSION FUNCTIONS
// ============================================================================

/**
 * Convert string to integer
 * Returns 0 if conversion fails
 */
int string_to_int(const char* str) {
    if (!str) return 0;
    
    // Skip whitespace
    while (*str && isspace(*str)) str++;
    
    // Check for valid integer format
    int result = 0;
    int sign = 1;
    
    if (*str == '-') {
        sign = -1;
        str++;
    } else if (*str == '+') {
        str++;
    }
    
    // Convert digits
    while (*str && isdigit(*str)) {
        result = result * 10 + (*str - '0');
        str++;
    }
    
    return result * sign;
}

/**
 * Convert string to float
 * Returns 0.0 if conversion fails
 */
double string_to_float(const char* str) {
    if (!str) return 0.0;
    
    // Use standard library for float conversion
    char* endptr;
    double result = strtod(str, &endptr);
    
    // If no conversion was performed, return 0.0
    if (endptr == str) {
        return 0.0;
    }
    
    return result;
}

/**
 * Convert string to char (returns first character)
 * Returns '\0' if string is empty or null
 */
char string_to_char(const char* str) {
    if (!str || !*str) return '\0';
    return str[0];
}

/**
 * Convert char to int (returns ASCII value)
 */
int char_to_int(char c) {
    return (int)c;
}

/**
 * Convert int to char (takes value modulo 256)
 */
char int_to_char(int value) {
    return (char)(value % 256);
}

/**
 * Convert int to float
 */
double int_to_float(int value) {
    return (double)value;
}

/**
 * Convert float to int (truncates decimal part)
 */
int float_to_int(double value) {
    return (int)value;
}

// ============================================================================
// SIMPLE CRYPTOGRAPHY FUNCTIONS
// ============================================================================

/**
 * Caesar cipher - shifts each letter by the specified amount
 * Non-letter characters remain unchanged
 */
char* caesar_cipher(const char* text, int shift) {
    if (!text) return NULL;
    
    int len = strlen(text);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    // Normalize shift to 0-25 range
    shift = shift % 26;
    if (shift < 0) shift += 26;
    
    for (int i = 0; i < len; i++) {
        char c = text[i];
        
        if (c >= 'A' && c <= 'Z') {
            // Uppercase letter
            result[i] = 'A' + (c - 'A' + shift) % 26;
        } else if (c >= 'a' && c <= 'z') {
            // Lowercase letter
            result[i] = 'a' + (c - 'a' + shift) % 26;
        } else {
            // Non-letter character
            result[i] = c;
        }
    }
    
    result[len] = '\0';
    return result;
}

/**
 * Caesar decipher - shifts each letter backwards
 */
char* caesar_decipher(const char* text, int shift) {
    return caesar_cipher(text, -shift);
}

/**
 * ROT13 cipher - special case of Caesar cipher with shift 13
 */
char* rot13(const char* text) {
    return caesar_cipher(text, 13);
}

/**
 * Character shift - shifts all characters (including non-letters) by ASCII value
 * Wraps around at 256
 */
char* char_shift(const char* text, int shift) {
    if (!text) return NULL;
    
    int len = strlen(text);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (int i = 0; i < len; i++) {
        // Shift by ASCII value, wrapping around at 256
        int shifted = ((unsigned char)text[i] + shift) % 256;
        if (shifted < 0) shifted += 256;
        result[i] = (char)shifted;
    }
    
    result[len] = '\0';
    return result;
}

/**
 * Reverse string
 */
char* reverse_string(const char* text) {
    if (!text) return NULL;
    
    int len = strlen(text);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (int i = 0; i < len; i++) {
        result[i] = text[len - 1 - i];
    }
    
    result[len] = '\0';
    return result;
}

/**
 * XOR cipher - XORs each character with corresponding key character
 * Key repeats if shorter than text
 */
char* xor_cipher(const char* text, const char* key) {
    if (!text || !key) return NULL;
    
    int text_len = strlen(text);
    int key_len = strlen(key);
    
    if (key_len == 0) return NULL;
    
    char* result = (char*)malloc(text_len + 1);
    if (!result) return NULL;
    
    for (int i = 0; i < text_len; i++) {
        result[i] = text[i] ^ key[i % key_len];
    }
    
    result[text_len] = '\0';
    return result;
}
