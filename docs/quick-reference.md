# PIE Language Quick Reference

Fast reference guide for PIE programming language syntax and features.

## Data Types

```pie
int x = 42;              // 32-bit integer
float pi = 3.14;         // 64-bit float
char c = 'A';            // Single character
string s = "Hello";      // String
bool b = true;           // Boolean
dict d = {};             // Dictionary
regex r = regex_compile("a+"); // Regex
file f = file_open("f.txt", "r"); // File handle
int numbers[]=[1,2,3] //array -> [datatype] [identifier]
```

## Operators

```pie
// Arithmetic
+ - * / %

// Comparison
== != < > <= >=

// Logical
&& ||

// Assignment
=

// Increment/Decrement
++ --

// String Concatenation
+
```

## Control Flow

```pie
// If-else
if (condition) { } else { }
if (condition) {} else if(condifion){} else {}

// While
while (condition) { }

// Do-while
do { } while (condition);

// For
for (init; condition; update) { }

// Switch
switch (expr) {
    case value: break;
    default:
}

// Break/Continue
break; continue;
```

## Arrays

```pie
// Static
int nums[5] = [1, 2, 3, 4, 5];

// Dynamic
int[] arr = [1, 2, 3];
arr_push(arr, 4);
int val = arr_pop(arr);
int size = arr_size(arr);
int exists = arr_contains(arr, 2);
int idx = arr_indexof(arr, 3);
float avg = arr_avg(arr);
```

## Dictionaries

```pie
dict d = {"key": "value", "num": 42};
dict_set(d, "new", "data");
string val = dict_get(d, "key");
int exists = dict_has_key(d, "key");
dict_delete(d, "key");
```

## Functions

```pie
int add(int a, int b) {
    return a + b;
}
```

## I/O

```pie
// Input
input(variable, type);

// Output
output(value, type);
output(value, float, precision);
```

## Math

```pie
sqrt(x)   pow(x,y)   abs(x)
sin(x)    cos(x)     tan(x)
floor(x)  ceil(x)    round(x)
min(a,b)  max(a,b)   rand()
pi()      e()
```

## Strings

```pie
strlen(s)
strcmp(s1, s2)
string_to_upper(s)
string_to_lower(s)
string_trim(s)
string_substring(s, start, len)
string_index_of(haystack, needle)
string_reverse(s)
string_contains(haystack, needle)
string_starts_with(s, prefix)
string_ends_with(s, suffix)
```

## Type Conversions

```pie
// String conversions
int string_to_int(s)
float string_to_float(s)
char string_to_char(s)

// Character conversions
int char_to_int(c)      // ASCII value
char int_to_char(n)     // From ASCII

// Numeric conversions
float int_to_float(n)
int float_to_int(f)     // Truncates
```

## Cryptography & Encoding

```pie
// Caesar cipher
string caesar_cipher(text, shift)
string caesar_decipher(text, shift)
string rot13(text)

// Character operations
string char_shift(text, shift)    // All chars
string reverse_string(text)
string xor_cipher(text, key)      // Repeating key
```

**Note:** These are for education/obfuscation only, not secure encryption.

## File I/O

```pie
file f = file_open("file.txt", "r"); // or "w", "a"
file_write(f, "content");
string content = file_read_all(f);
file_flush(f);
file_close(f);
```

## Regular Expressions

```pie
regex r = regex_compile("pattern");
int match = regex_match(r, "string");
regex_free(r);

// Pattern syntax
// Literals: a, b, 1, 2
// Concat: a.b
// OR: a|b
// Star: a*
// Plus: a+
// Exact: a+:3
// Min: a+>2
// Max: a+<5
// Range: a+>2<6
```

## Network

```pie
socket s = tcp_socket();
tcp_connect(s, "host", port);
tcp_send(s, "data");
tcp_recv(s, buffer, size);
tcp_close(s);
```

## Time

```pie
int now = time_now();
string timeStr = time_to_local(timestamp);
```

## System

```pie
exit();
sleep(milliseconds);
```

## Comments

```pie
// Single line

/*
 * Multi-line
 */
```

## Compilation

```bash
# Compile
python3 src/main.py program.pie

# Run
./program
```
