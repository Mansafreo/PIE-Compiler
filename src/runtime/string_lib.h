#ifndef STRING_LIB_H
#define STRING_LIB_H

#include <stddef.h>

// Basic string functions
int pie_strlen(const char* s);
int pie_strcmp(const char* s1, const char* s2);
char* pie_strcpy(char* dest, const char* src);
char* pie_strcat(char* dest, const char* src);

// Advanced string utilities
char* string_to_upper(const char* str);
char* string_to_lower(const char* str);
char* string_trim(const char* str);
char* string_substring(const char* str, int start, int length);
int string_index_of(const char* haystack, const char* needle);
char* string_replace_char(const char* str, char old_char, char new_char);
char* string_reverse(const char* str);
int string_count_char(const char* str, char ch);

#endif // STRING_LIB_H
