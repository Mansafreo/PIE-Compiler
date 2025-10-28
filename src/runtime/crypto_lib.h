#ifndef CRYPTO_LIB_H
#define CRYPTO_LIB_H

// Type conversion functions
int string_to_int(const char* str);
double string_to_float(const char* str);
char string_to_char(const char* str);
int char_to_int(char c);
char int_to_char(int value);
double int_to_float(int value);
int float_to_int(double value);

// Simple crypto/encoding functions
char* caesar_cipher(const char* text, int shift);
char* caesar_decipher(const char* text, int shift);
char* rot13(const char* text);
char* char_shift(const char* text, int shift);
char* reverse_string(const char* text);
char* xor_cipher(const char* text, const char* key);

#endif // CRYPTO_LIB_H
