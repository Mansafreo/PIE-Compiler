#ifndef D_ARRAY_H
#define D_ARRAY_H

#include <stddef.h>

typedef struct {
    int* data;
    size_t size;
    size_t capacity;
} DArrayInt;

DArrayInt* d_array_int_create();
void d_array_int_append(DArrayInt* arr, int value);
void d_array_int_push(DArrayInt* arr, int value);  // Alias for append
int d_array_int_get(DArrayInt* arr, int index);
void d_array_int_set(DArrayInt* arr, int index, int value);
int d_array_int_size(DArrayInt* arr);
void d_array_int_free(DArrayInt* arr);
int d_array_int_pop(DArrayInt* arr);
int d_array_int_contains(DArrayInt* arr, int value);
int d_array_int_indexof(DArrayInt* arr, int value);
DArrayInt* d_array_int_concat(DArrayInt* arr1, DArrayInt* arr2);
double d_array_int_avg(DArrayInt* arr);
DArrayInt* d_array_int_copy(DArrayInt* arr);


typedef struct {
    char** data;
    size_t size;
    size_t capacity;
} DArrayString;

DArrayString* d_array_string_create();
void d_array_string_append(DArrayString* arr, const char* value);
void d_array_string_push(DArrayString* arr, const char* value);  // Alias for append
char* d_array_string_get(DArrayString* arr, int index);
void d_array_string_set(DArrayString* arr, int index, const char* value);
int d_array_string_size(DArrayString* arr);
void d_array_string_free(DArrayString* arr);
char* d_array_string_pop(DArrayString* arr);
int d_array_string_contains(DArrayString* arr, const char* value);
int d_array_string_indexof(DArrayString* arr, const char* value);
DArrayString* d_array_string_concat(DArrayString* arr1, DArrayString* arr2);
DArrayString* d_array_string_copy(DArrayString* arr);

typedef struct {
    char* data;
    size_t size;
    size_t capacity;
} DArrayChar;

DArrayChar* d_array_char_create();
void d_array_char_append(DArrayChar* arr, char value);
char d_array_char_get(DArrayChar* arr, int index);
void d_array_char_set(DArrayChar* arr, int index, char value);
int d_array_char_size(DArrayChar* arr);
void d_array_char_free(DArrayChar* arr);
char d_array_char_pop(DArrayChar* arr);
int d_array_char_contains(DArrayChar* arr, char value);
int d_array_char_indexof(DArrayChar* arr, char value);
DArrayChar* d_array_char_concat(DArrayChar* arr1, DArrayChar* arr2);
DArrayChar* d_array_char_copy(DArrayChar* arr);

typedef struct {
    double* data;
    size_t size;
    size_t capacity;
} DArrayFloat;

DArrayFloat* d_array_float_create();
void d_array_float_append(DArrayFloat* arr, double value);
void d_array_float_push(DArrayFloat* arr, double value);  // Alias for append
double d_array_float_get(DArrayFloat* arr, int index);
void d_array_float_set(DArrayFloat* arr, int index, double value);
int d_array_float_size(DArrayFloat* arr);
void d_array_float_free(DArrayFloat* arr);
double d_array_float_pop(DArrayFloat* arr);
int d_array_float_contains(DArrayFloat* arr, double value);
int d_array_float_indexof(DArrayFloat* arr, double value);
DArrayFloat* d_array_float_concat(DArrayFloat* arr1, DArrayFloat* arr2);
double d_array_float_avg(DArrayFloat* arr);
DArrayFloat* d_array_float_copy(DArrayFloat* arr);

void print_int_array(DArrayInt* arr);
void print_string_array(DArrayString* arr);
void print_float_array(DArrayFloat* arr);
void print_char_array(DArrayChar* arr);

#endif // D_ARRAY_H
