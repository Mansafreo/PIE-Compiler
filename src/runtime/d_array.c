#include "d_array.h"
#include <stdlib.h>
#include <string.h>

DArrayInt* d_array_int_create() {
    DArrayInt* arr = (DArrayInt*)malloc(sizeof(DArrayInt));
    arr->data = (int*)malloc(sizeof(int) * 4); // Initial capacity of 4
    arr->size = 0;
    arr->capacity = 4;
    return arr;
}

void d_array_int_append(DArrayInt* arr, int value) {
    if (arr->size >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (int*)realloc(arr->data, sizeof(int) * arr->capacity);
    }
    arr->data[arr->size++] = value;
}

// Alias for append to match PIE language syntax
void d_array_int_push(DArrayInt* arr, int value) {
    d_array_int_append(arr, value);
}

int d_array_int_get(DArrayInt* arr, int index) {
    if (index >= arr->size) {
        // Error handling? For now, return 0
        return 0;
    }
    return arr->data[index];
}

void d_array_int_set(DArrayInt* arr, int index, int value) {
    if (index >= arr->size) {
        if (index >= arr->capacity) {
            size_t new_capacity = arr->capacity;
            while (index >= new_capacity) {
                new_capacity *= 2;
            }
            arr->data = (int*)realloc(arr->data, sizeof(int) * new_capacity);
            arr->capacity = new_capacity;
        }
        for (size_t i = arr->size; i < index; i++) {
            arr->data[i] = 0;
        }
        arr->size = index + 1;
    }
    arr->data[index] = value;
}

int d_array_int_size(DArrayInt* arr) {
    return arr->size;
}

void d_array_int_free(DArrayInt* arr) {
    if (arr) {
        free(arr->data);
        free(arr);
    }
}

int d_array_int_pop(DArrayInt* arr) {
    if (arr->size == 0) {
        return 0; // Or some error indicator
    }
    arr->size--;
    return arr->data[arr->size];
}

int d_array_int_contains(DArrayInt* arr, int value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return 1; // true
        }
    }
    return 0; // false
}

int d_array_int_indexof(DArrayInt* arr, int value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return i;
        }
    }
    return -1;
}

DArrayInt* d_array_int_concat(DArrayInt* arr1, DArrayInt* arr2) {
    DArrayInt* new_arr = d_array_int_create();
    for (size_t i = 0; i < arr1->size; i++) {
        d_array_int_append(new_arr, arr1->data[i]);
    }
    for (size_t i = 0; i < arr2->size; i++) {
        d_array_int_append(new_arr, arr2->data[i]);
    }
    return new_arr;
}

double d_array_int_avg(DArrayInt* arr) {
    if (arr->size == 0) {
        return 0.0;
    }
    long long sum = 0; // Use long long to avoid overflow
    for (size_t i = 0; i < arr->size; i++) {
        sum += arr->data[i];
    }
    return (double)sum / arr->size;
}

DArrayInt* d_array_int_copy(DArrayInt* arr) {
    if (!arr) return NULL;
    DArrayInt* new_arr = d_array_int_create();
    // Copy all elements
    for (size_t i = 0; i < arr->size; i++) {
        d_array_int_append(new_arr, arr->data[i]);
    }
    return new_arr;
}

// String array functions
DArrayString* d_array_string_create() {
    DArrayString* arr = (DArrayString*)malloc(sizeof(DArrayString));
    arr->data = (char**)malloc(sizeof(char*) * 4); // Initial capacity of 4
    arr->size = 0;
    arr->capacity = 4;
    return arr;
}

void d_array_string_append(DArrayString* arr, const char* value) {
    if (arr->size >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (char**)realloc(arr->data, sizeof(char*) * arr->capacity);
    }
    // Allocate memory for the string and copy it
    size_t len = strlen(value) + 1;
    arr->data[arr->size] = (char*)malloc(len);
    strcpy(arr->data[arr->size], value);
    arr->size++;
}

// Alias for append to match PIE language syntax
void d_array_string_push(DArrayString* arr, const char* value) {
    d_array_string_append(arr, value);
}

char* d_array_string_get(DArrayString* arr, int index) {
    if (index >= arr->size) {
        return NULL;
    }
    return arr->data[index];
}

void d_array_string_set(DArrayString* arr, int index, const char* value) {
    if (index >= arr->size) {
        if (index >= arr->capacity) {
            size_t new_capacity = arr->capacity;
            while (index >= new_capacity) {
                new_capacity *= 2;
            }
            arr->data = (char**)realloc(arr->data, sizeof(char*) * new_capacity);
            arr->capacity = new_capacity;
        }
        for (size_t i = arr->size; i < index; i++) {
            arr->data[i] = NULL;
        }
        arr->size = index + 1;
    }
    if (arr->data[index]) {
        free(arr->data[index]);
    }
    size_t len = strlen(value) + 1;
    arr->data[index] = (char*)malloc(len);
    strcpy(arr->data[index], value);
}

int d_array_string_size(DArrayString* arr) {
    return arr->size;
}

void d_array_string_free(DArrayString* arr) {
    if (arr) {
        for (size_t i = 0; i < arr->size; i++) {
            if (arr->data[i]) {
                free(arr->data[i]);
            }
        }
        free(arr->data);
        free(arr);
    }
}

char* d_array_string_pop(DArrayString* arr) {
    if (arr->size == 0) {
        return NULL;
    }
    arr->size--;
    return arr->data[arr->size];
}

int d_array_string_contains(DArrayString* arr, const char* value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] != NULL && strcmp(arr->data[i], value) == 0) {
            return 1; // true
        }
    }
    return 0; // false
}

int d_array_string_indexof(DArrayString* arr, const char* value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] != NULL && strcmp(arr->data[i], value) == 0) {
            return i;
        }
    }
    return -1;
}

DArrayString* d_array_string_concat(DArrayString* arr1, DArrayString* arr2) {
    DArrayString* new_arr = d_array_string_create();
    for (size_t i = 0; i < arr1->size; i++) {
        d_array_string_append(new_arr, arr1->data[i]);
    }
    for (size_t i = 0; i < arr2->size; i++) {
        d_array_string_append(new_arr, arr2->data[i]);
    }
    return new_arr;
}

DArrayString* d_array_string_copy(DArrayString* arr) {
    if (!arr) return NULL;
    DArrayString* new_arr = d_array_string_create();
    // Copy all elements
    for (size_t i = 0; i < arr->size; i++) {
        d_array_string_append(new_arr, arr->data[i]);
    }
    return new_arr;
}

DArrayFloat* d_array_float_create() {
    DArrayFloat* arr = (DArrayFloat*)malloc(sizeof(DArrayFloat));
    arr->data = (double*)malloc(sizeof(double) * 4); // Initial capacity of 4
    arr->size = 0;
    arr->capacity = 4;
    return arr;
}

void d_array_float_append(DArrayFloat* arr, double value) {
    if (arr->size >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (double*)realloc(arr->data, sizeof(double) * arr->capacity);
    }
    arr->data[arr->size++] = value;
}

// Alias for append to match PIE language syntax
void d_array_float_push(DArrayFloat* arr, double value) {
    d_array_float_append(arr, value);
}

double d_array_float_get(DArrayFloat* arr, int index) {
    if (index >= arr->size) {
        return 0.0;
    }
    return arr->data[index];
}

void d_array_float_set(DArrayFloat* arr, int index, double value) {
    if (index >= arr->size) {
        if (index >= arr->capacity) {
            size_t new_capacity = arr->capacity;
            while (index >= new_capacity) {
                new_capacity *= 2;
            }
            arr->data = (double*)realloc(arr->data, sizeof(double) * new_capacity);
            arr->capacity = new_capacity;
        }
        for (size_t i = arr->size; i < index; i++) {
            arr->data[i] = 0.0;
        }
        arr->size = index + 1;
    }
    arr->data[index] = value;
}

int d_array_float_size(DArrayFloat* arr) {
    return arr->size;
}

void d_array_float_free(DArrayFloat* arr) {
    if (arr) {
        free(arr->data);
        free(arr);
    }
}

double d_array_float_pop(DArrayFloat* arr) {
    if (arr->size == 0) {
        return 0.0;
    }
    arr->size--;
    return arr->data[arr->size];
}

int d_array_float_contains(DArrayFloat* arr, double value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return 1;
        }
    }
    return 0;
}

int d_array_float_indexof(DArrayFloat* arr, double value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return i;
        }
    }
    return -1;
}

DArrayFloat* d_array_float_concat(DArrayFloat* arr1, DArrayFloat* arr2) {
    DArrayFloat* new_arr = d_array_float_create();
    for (size_t i = 0; i < arr1->size; i++) {
        d_array_float_append(new_arr, arr1->data[i]);
    }
    for (size_t i = 0; i < arr2->size; i++) {
        d_array_float_append(new_arr, arr2->data[i]);
    }
    return new_arr;
}

double d_array_float_avg(DArrayFloat* arr) {
    if (arr->size == 0) {
        return 0.0;
    }
    double sum = 0; // Use double for sum to maintain precision
    for (size_t i = 0; i < arr->size; i++) {
        sum += arr->data[i];
    }
    return sum / arr->size;
}

DArrayFloat* d_array_float_copy(DArrayFloat* arr) {
    if (!arr) return NULL;
    DArrayFloat* new_arr = d_array_float_create();
    // Copy all elements
    for (size_t i = 0; i < arr->size; i++) {
        d_array_float_append(new_arr, arr->data[i]);
    }
    return new_arr;
}

#include <stdio.h>

void print_int_array(DArrayInt* arr) {
    if (!arr) return;
    for (size_t i = 0; i < arr->size; i++) {
        printf("[%zu]: %d\n", i, arr->data[i]);
    }
}

void print_string_array(DArrayString* arr) {
    if (!arr) return;
    for (size_t i = 0; i < arr->size; i++) {
        printf("[%zu]: \"%s\"\n", i, arr->data[i] ? arr->data[i] : "null");
    }
}

void print_float_array(DArrayFloat* arr) {
    if (!arr) return;
    for (size_t i = 0; i < arr->size; i++) {
        printf("[%zu]: %f\n", i, arr->data[i]);
    }
}

DArrayChar* d_array_char_create() {
    DArrayChar* arr = (DArrayChar*)malloc(sizeof(DArrayChar));
    arr->data = (char*)malloc(sizeof(char) * 4);
    arr->size = 0;
    arr->capacity = 4;
    return arr;
}

void d_array_char_append(DArrayChar* arr, char value) {
    if (arr->size >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (char*)realloc(arr->data, sizeof(char) * arr->capacity);
    }
    arr->data[arr->size++] = value;
}

char d_array_char_get(DArrayChar* arr, int index) {
    if (index >= arr->size) {
        return '\0';
    }
    return arr->data[index];
}

void d_array_char_set(DArrayChar* arr, int index, char value) {
    if (index >= arr->size) {
        if (index >= arr->capacity) {
            size_t new_capacity = arr->capacity;
            while (index >= new_capacity) {
                new_capacity *= 2;
            }
            arr->data = (char*)realloc(arr->data, sizeof(char) * new_capacity);
            arr->capacity = new_capacity;
        }
        for (size_t i = arr->size; i < index; i++) {
            arr->data[i] = '\0';
        }
        arr->size = index + 1;
    }
    arr->data[index] = value;
}

int d_array_char_size(DArrayChar* arr) {
    return arr->size;
}

void d_array_char_free(DArrayChar* arr) {
    if (arr) {
        free(arr->data);
        free(arr);
    }
}

char d_array_char_pop(DArrayChar* arr) {
    if (arr->size == 0) {
        return '\0';
    }
    arr->size--;
    return arr->data[arr->size];
}

int d_array_char_contains(DArrayChar* arr, char value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return 1;
        }
    }
    return 0;
}

int d_array_char_indexof(DArrayChar* arr, char value) {
    for (size_t i = 0; i < arr->size; i++) {
        if (arr->data[i] == value) {
            return i;
        }
    }
    return -1;
}

DArrayChar* d_array_char_concat(DArrayChar* arr1, DArrayChar* arr2) {
    DArrayChar* new_arr = d_array_char_create();
    for (size_t i = 0; i < arr1->size; i++) {
        d_array_char_append(new_arr, arr1->data[i]);
    }
    for (size_t i = 0; i < arr2->size; i++) {
        d_array_char_append(new_arr, arr2->data[i]);
    }
    return new_arr;
}

DArrayChar* d_array_char_copy(DArrayChar* arr) {
    if (!arr) return NULL;
    DArrayChar* new_arr = d_array_char_create();
    // Copy all elements
    for (size_t i = 0; i < arr->size; i++) {
        d_array_char_append(new_arr, arr->data[i]);
    }
    return new_arr;
}

void print_char_array(DArrayChar* arr) {
    if (!arr) return;
    for (size_t i = 0; i < arr->size; i++) {
        printf("[%zu]: '%c'\n", i, arr->data[i]);
    }
}
