# PIE Standard Library Reference

Complete reference for all built-in functions and utilities in the PIE programming language.

## Table of Contents

1. [Input/Output Functions](#inputoutput-functions)
2. [Math Library](#math-library)
3. [String Functions](#string-functions)
4. [Array Functions](#array-functions)
5. [Dictionary Functions](#dictionary-functions)
6. [Regular Expression Functions](#regular-expression-functions)
7. [File I/O Functions](#file-io-functions)
8. [Network Functions](#network-functions)
9. [Time Functions](#time-functions)
10. [System Functions](#system-functions)

---

## Input/Output Functions

### input()

Read user input and store it in a variable.

**Syntax:**
```pie
input(variable, type);
```

**Parameters:**
- `variable` - The variable to store the input
- `type` - The data type to read (`int`, `float`, `string`, `char`)

**Examples:**
```pie
int age;
input(age, int);

float temperature;
input(temperature, float);

string name;
input(name, string);

char grade;
input(grade, char);
```

**Notes:**
- For strings, reads up to 255 characters or until newline
- Automatically clears input buffer after reading
- Sets default values on error (0 for numbers, "" for strings)

---

### output()

Print a value to the console.

**Syntax:**
```pie
output(value, type);
output(value, float, precision);  // For float with precision
```

**Parameters:**
- `value` - The value to output
- `type` - The data type (`int`, `float`, `string`, `char`, `bool`)
- `precision` - (Optional) Number of decimal places for floats (0-12)

**Examples:**
```pie
// Basic output
output(42, int);
output("Hello, World!", string);
output('A', char);
output(true, bool);

// Float with precision
float pi = 3.14159265;
output(pi, float, 2);    // Outputs: 3.14
output(pi, float, 5);    // Outputs: 3.14159
```

**Notes:**
- Automatically adds a newline after output
- Float precision defaults to full precision if not specified
- Precision is clamped to 0-12 range

---

## Math Library

### Basic Math Functions

#### sqrt()

Calculate the square root of a number.

**Syntax:**
```pie
float sqrt(float x);
```

**Example:**
```pie
float result = sqrt(16.0);    // 4.0
float result2 = sqrt(2.0);    // 1.414...
```

---

#### pow()

Raise a number to a power.

**Syntax:**
```pie
float pow(float base, float exponent);
```

**Example:**
```pie
float result = pow(2.0, 8.0);   // 256.0
float result2 = pow(10.0, 3.0); // 1000.0
```

---

#### abs()

Get the absolute value of a float.

**Syntax:**
```pie
float abs(float x);
```

**Example:**
```pie
float result = abs(-5.5);   // 5.5
float result2 = abs(3.2);   // 3.2
```

---

#### abs_int()

Get the absolute value of an integer.

**Syntax:**
```pie
int abs_int(int x);
```

**Example:**
```pie
int result = abs_int(-10);   // 10
int result2 = abs_int(5);    // 5
```

---

### Trigonometric Functions

#### sin()

Calculate the sine of an angle (in radians).

**Syntax:**
```pie
float sin(float x);
```

**Example:**
```pie
float result = sin(0.0);      // 0.0
float result2 = sin(1.5708);  // ~1.0 (π/2)
```

---

#### cos()

Calculate the cosine of an angle (in radians).

**Syntax:**
```pie
float cos(float x);
```

**Example:**
```pie
float result = cos(0.0);      // 1.0
float result2 = cos(3.1416);  // ~-1.0 (π)
```

---

#### tan()

Calculate the tangent of an angle (in radians).

**Syntax:**
```pie
float tan(float x);
```

**Example:**
```pie
float result = tan(0.0);      // 0.0
float result2 = tan(0.7854);  // ~1.0 (π/4)
```

---

#### asin()

Calculate the arcsine (inverse sine) of a value.

**Syntax:**
```pie
float asin(float x);
```

**Example:**
```pie
float result = asin(0.0);   // 0.0
float result2 = asin(1.0);  // ~1.5708 (π/2)
```

---

#### acos()

Calculate the arccosine (inverse cosine) of a value.

**Syntax:**
```pie
float acos(float x);
```

**Example:**
```pie
float result = acos(1.0);   // 0.0
float result2 = acos(-1.0); // ~3.1416 (π)
```

---

#### atan()

Calculate the arctangent (inverse tangent) of a value.

**Syntax:**
```pie
float atan(float x);
```

**Example:**
```pie
float result = atan(0.0);   // 0.0
float result2 = atan(1.0);  // ~0.7854 (π/4)
```

---

### Logarithmic and Exponential Functions

#### log()

Calculate the natural logarithm (base e).

**Syntax:**
```pie
float log(float x);
```

**Example:**
```pie
float result = log(2.7183);  // ~1.0 (ln(e))
float result2 = log(10.0);   // ~2.3026
```

---

#### log10()

Calculate the base-10 logarithm.

**Syntax:**
```pie
float log10(float x);
```

**Example:**
```pie
float result = log10(10.0);   // 1.0
float result2 = log10(100.0); // 2.0
```

---

#### exp()

Calculate e raised to a power.

**Syntax:**
```pie
float exp(float x);
```

**Example:**
```pie
float result = exp(0.0);   // 1.0
float result2 = exp(1.0);  // ~2.7183 (e)
```

---

### Rounding Functions

#### floor()

Round down to the nearest integer.

**Syntax:**
```pie
float floor(float x);
```

**Example:**
```pie
float result = floor(3.7);   // 3.0
float result2 = floor(-2.3); // -3.0
```

---

#### ceil()

Round up to the nearest integer.

**Syntax:**
```pie
float ceil(float x);
```

**Example:**
```pie
float result = ceil(3.2);   // 4.0
float result2 = ceil(-2.7); // -2.0
```

---

#### round()

Round to the nearest integer.

**Syntax:**
```pie
float round(float x);
```

**Example:**
```pie
float result = round(3.5);   // 4.0
float result2 = round(3.4);  // 3.0
float result3 = round(-2.6); // -3.0
```

---

### Min/Max Functions

#### min()

Return the smaller of two float values.

**Syntax:**
```pie
float min(float a, float b);
```

**Example:**
```pie
float result = min(5.5, 3.2);   // 3.2
float result2 = min(-1.0, 2.0); // -1.0
```

---

#### max()

Return the larger of two float values.

**Syntax:**
```pie
float max(float a, float b);
```

**Example:**
```pie
float result = max(5.5, 3.2);   // 5.5
float result2 = max(-1.0, 2.0); // 2.0
```

---

#### min_int()

Return the smaller of two integer values.

**Syntax:**
```pie
int min_int(int a, int b);
```

**Example:**
```pie
int result = min_int(10, 5);    // 5
int result2 = min_int(-3, 2);   // -3
```

---

#### max_int()

Return the larger of two integer values.

**Syntax:**
```pie
int max_int(int a, int b);
```

**Example:**
```pie
int result = max_int(10, 5);    // 10
int result2 = max_int(-3, 2);   // 2
```

---

### Random Number Functions

#### rand()

Generate a random integer.

**Syntax:**
```pie
int rand();
```

**Example:**
```pie
int random = rand();
output(random, int);
```

**Notes:**
- Returns a pseudo-random integer
- Use `srand()` to seed the generator

---

#### srand()

Seed the random number generator.

**Syntax:**
```pie
void srand(int seed);
```

**Example:**
```pie
// Seed with current time for better randomness
int currentTime = time_now();
srand(currentTime);

int random = rand();
```

---

#### rand_range()

Generate a random integer within a range.

**Syntax:**
```pie
int rand_range(int min, int max);
```

**Example:**
```pie
int dice = rand_range(1, 6);     // Random number from 1 to 6
int percent = rand_range(0, 100); // Random number from 0 to 100
```

---

### Mathematical Constants

#### pi()

Get the value of π (pi).

**Syntax:**
```pie
float pi();
```

**Example:**
```pie
float pi_value = pi();  // 3.14159265358979323846
float circumference = 2.0 * pi() * radius;
```

---

#### e()

Get the value of e (Euler's number).

**Syntax:**
```pie
float e();
```

**Example:**
```pie
float e_value = e();  // 2.71828182845904523536
```

---

## String Functions

### Basic String Functions

#### strlen()

Get the length of a string.

**Syntax:**
```pie
int strlen(string s);
```

**Example:**
```pie
int len = strlen("Hello");       // 5
int len2 = strlen("PIE Language"); // 12
```

---

#### strcmp()

Compare two strings.

**Syntax:**
```pie
int strcmp(string s1, string s2);
```

**Returns:**
- `0` if strings are equal
- `< 0` if s1 < s2
- `> 0` if s1 > s2

**Example:**
```pie
int result = strcmp("apple", "apple");  // 0
int result2 = strcmp("apple", "banana"); // < 0
int result3 = strcmp("zebra", "apple");  // > 0
```

---

#### strcpy()

Copy a string.

**Syntax:**
```pie
string strcpy(string dest, string src);
```

**Example:**
```pie
string original = "Hello";
string copy = strcpy("", original);
```

---

#### strcat()

Concatenate two strings.

**Syntax:**
```pie
string strcat(string dest, string src);
```

**Example:**
```pie
string result = strcat("Hello, ", "World!");  // "Hello, World!"
```

**Note:** PIE also supports the `+` operator for string concatenation:
```pie
string result = "Hello, " + "World!";
```

---

### Case Conversion Functions

#### string_to_upper()

Convert string to uppercase.

**Syntax:**
```pie
string string_to_upper(string str);
```

**Example:**
```pie
string upper = string_to_upper("hello world");  // "HELLO WORLD"
string upper2 = string_to_upper("PIE 123!");    // "PIE 123!"
```

---

#### string_to_lower()

Convert string to lowercase.

**Syntax:**
```pie
string string_to_lower(string str);
```

**Example:**
```pie
string lower = string_to_lower("HELLO WORLD");  // "hello world"
string lower2 = string_to_lower("PIE 123!");    // "pie 123!"
```

---

### String Manipulation Functions

#### string_trim()

Remove leading and trailing whitespace.

**Syntax:**
```pie
string string_trim(string str);
```

**Example:**
```pie
string trimmed = string_trim("   hello   ");    // "hello"
string trimmed2 = string_trim("\t  world \n");  // "world"
```

---

#### string_substring()

Extract a substring.

**Syntax:**
```pie
string string_substring(string str, int start, int length);
```

**Parameters:**
- `str` - The source string
- `start` - Starting index (0-based)
- `length` - Number of characters to extract

**Example:**
```pie
string sub = string_substring("Hello World", 0, 5);    // "Hello"
string sub2 = string_substring("Hello World", 6, 5);   // "World"
string sub3 = string_substring("PIE Language", 0, 3);  // "PIE"
```

---

#### string_reverse()

Reverse a string.

**Syntax:**
```pie
string string_reverse(string str);
```

**Example:**
```pie
string reversed = string_reverse("Hello");  // "olleH"
string reversed2 = string_reverse("PIE");   // "EIP"
```

---

#### string_replace_char()

Replace all occurrences of a character.

**Syntax:**
```pie
string string_replace_char(string str, char old_char, char new_char);
```

**Example:**
```pie
string replaced = string_replace_char("hello world", ' ', '_');
// "hello_world"

string replaced2 = string_replace_char("foo-bar-baz", '-', '.');
// "foo.bar.baz"
```

---

### String Search Functions

#### string_index_of()

Find the index of the first occurrence of a substring.

**Syntax:**
```pie
int string_index_of(string haystack, string needle);
```

**Returns:**
- Index of first occurrence (0-based)
- `-1` if not found

**Example:**
```pie
int index = string_index_of("Hello World", "World");  // 6
int index2 = string_index_of("Hello World", "o");     // 4
int index3 = string_index_of("Hello World", "xyz");   // -1
```

---

#### string_count_char()

Count occurrences of a character.

**Syntax:**
```pie
int string_count_char(string str, char ch);
```

**Example:**
```pie
int count = string_count_char("hello world", 'l');  // 3
int count2 = string_count_char("Mississippi", 's'); // 4
int count3 = string_count_char("PIE", 'x');        // 0
```

---

#### string_contains()

Check if a string contains a substring.

**Syntax:**
```pie
int string_contains(string haystack, string needle);
```

**Returns:**
- `1` if substring is found
- `0` if not found

**Example:**
```pie
int result = string_contains("Hello World", "World");  // 1
int result2 = string_contains("Hello World", "xyz");   // 0
```

---

#### string_starts_with()

Check if a string starts with a prefix.

**Syntax:**
```pie
int string_starts_with(string str, string prefix);
```

**Returns:**
- `1` if string starts with prefix
- `0` otherwise

**Example:**
```pie
int result = string_starts_with("Hello World", "Hello");  // 1
int result2 = string_starts_with("Hello World", "World"); // 0
```

---

#### string_ends_with()

Check if a string ends with a suffix.

**Syntax:**
```pie
int string_ends_with(string str, string suffix);
```

**Returns:**
- `1` if string ends with suffix
- `0` otherwise

**Example:**
```pie
int result = string_ends_with("Hello World", "World");  // 1
int result2 = string_ends_with("Hello World", "Hello"); // 0
```

---

#### string_is_empty()

Check if a string is empty.

**Syntax:**
```pie
int string_is_empty(string str);
```

**Returns:**
- `1` if string is empty or null
- `0` otherwise

**Example:**
```pie
int result = string_is_empty("");         // 1
int result2 = string_is_empty("Hello");   // 0
```

---

## Array Functions

### arr_push()

Add an element to the end of a dynamic array.

**Syntax:**
```pie
void arr_push(array, value);
```

**Example:**
```pie
int[] numbers = [1, 2, 3];
arr_push(numbers, 4);
arr_push(numbers, 5);
// numbers is now {1, 2, 3, 4, 5}
```

**Note:** Only works with dynamic arrays (`type[]`), not static arrays.

---

### arr_pop()

Remove and return the last element from a dynamic array.

**Syntax:**
```pie
type arr_pop(array);
```

**Example:**
```pie
int[] numbers = [1, 2, 3, 4, 5];
int last = arr_pop(numbers);  // 5
int prev = arr_pop(numbers);  // 4
// numbers is now {1, 2, 3}
```

---

### arr_size()

Get the size of an array.

**Syntax:**
```pie
int arr_size(array);
```

**Example:**
```pie
int[] numbers = [1, 2, 3, 4, 5];
int size = arr_size(numbers);  // 5

string[] names = ["Alice", "Bob"];
int count = arr_size(names);   // 2
```

---

### arr_contains()

Check if an array contains a value.

**Syntax:**
```pie
int arr_contains(array, value);
```

**Returns:**
- `1` if value is found
- `0` if not found

**Example:**
```pie
int[] numbers = [10, 20, 30, 40];
int found = arr_contains(numbers, 30);   // 1
int notFound = arr_contains(numbers, 99); // 0
```

---

### arr_indexof()

Find the index of a value in an array.

**Syntax:**
```pie
int arr_indexof(array, value);
```

**Returns:**
- Index of first occurrence (0-based)
- `-1` if not found

**Example:**
```pie
int[] numbers = [10, 20, 30, 40, 30];
int index = arr_indexof(numbers, 30);   // 2 (first occurrence)
int notFound = arr_indexof(numbers, 99); // -1
```

---

### arr_avg()

Calculate the average of numeric array elements.

**Syntax:**
```pie
float arr_avg(array);
float arr_avg(array, count);  // Average of first N elements
```

**Example:**
```pie
int[] numbers = [10, 20, 30, 40, 50];
float average = arr_avg(numbers);  // 30.0

// Average of first 3 elements
float partial = arr_avg(numbers, 3);  // 20.0 (avg of 10, 20, 30)
```

---

## Dictionary Functions

### dict_create()

Create a new empty dictionary.

**Syntax:**
```pie
dict dict_create();
```

**Example:**
```pie
dict myDict = dict_create();
```

**Note:** You can also use the literal syntax:
```pie
dict myDict = {};
```

---

### dict_set()

Set a key-value pair in a dictionary.

**Syntax:**
```pie
void dict_set(dict d, string key, value);
```

**Example:**
```pie
dict person = {};
dict_set(person, "name", "Alice");
dict_set(person, "age", 25);
dict_set(person, "score", 95.5);
```

**Note:** Type is automatically inferred. No need for `new_int()`, `new_float()`, etc.

---

### dict_get()

Get a value from a dictionary.

**Syntax:**
```pie
type dict_get(dict d, string key);
```

**Example:**
```pie
dict person = {"name": "Alice", "age": 25, "score": 95.5};

string name = dict_get(person, "name");    // "Alice"
int age = dict_get(person, "age");         // 25
float score = dict_get(person, "score");   // 95.5
```

**Note:** Return type is automatically inferred from the receiving variable.

---

### dict_has_key() / dict_key_exists()

Check if a dictionary contains a key.

**Syntax:**
```pie
int dict_has_key(dict d, string key);
int dict_key_exists(dict d, string key);  // Alias
```

**Returns:**
- `1` if key exists
- `0` if key doesn't exist

**Example:**
```pie
dict person = {"name": "Alice", "age": 25};

int hasName = dict_has_key(person, "name");    // 1
int hasEmail = dict_has_key(person, "email");  // 0
```

---

### dict_delete()

Remove a key-value pair from a dictionary.

**Syntax:**
```pie
void dict_delete(dict d, string key);
```

**Example:**
```pie
dict person = {"name": "Alice", "age": 25, "temp": "value"};
dict_delete(person, "temp");
// person now only has "name" and "age"
```

---

## Type Conversion Functions

### string_to_int()

Convert a string to an integer.

**Syntax:**
```pie
int string_to_int(string str);
```

**Returns:** Integer value, or 0 if invalid

**Example:**
```pie
string num = "42";
int value = string_to_int(num);  // 42
```

---

### string_to_float()

Convert a string to a float.

**Syntax:**
```pie
float string_to_float(string str);
```

**Returns:** Float value, or 0.0 if invalid

---

### string_to_char()

Get the first character of a string.

**Syntax:**
```pie
char string_to_char(string str);
```

**Returns:** First character, or '\0' if empty

---

### char_to_int()

Get ASCII value of a character.

**Syntax:**
```pie
int char_to_int(char c);
```

**Returns:** ASCII value (0-255)

**Example:**
```pie
char letter = 'A';
int ascii = char_to_int(letter);  // 65
```

---

### int_to_char()

Convert integer to character.

**Syntax:**
```pie
char int_to_char(int value);
```

**Returns:** Character with given ASCII value (mod 256)

---

### int_to_float()

Convert integer to float.

**Syntax:**
```pie
float int_to_float(int value);
```

---

### float_to_int()

Convert float to integer (truncates).

**Syntax:**
```pie
int float_to_int(float value);
```

**Returns:** Integer part of the float

---

## Cryptography Functions

### caesar_cipher()

Encrypt text using Caesar cipher.

**Syntax:**
```pie
string caesar_cipher(string text, int shift);
```

**Example:**
```pie
string encrypted = caesar_cipher("Hello", 3);  // "Khoor"
```

---

### caesar_decipher()

Decrypt Caesar cipher text.

**Syntax:**
```pie
string caesar_decipher(string text, int shift);
```

---

### rot13()

Apply ROT13 encoding (symmetric).

**Syntax:**
```pie
string rot13(string text);
```

**Example:**
```pie
string encoded = rot13("Secret");
string decoded = rot13(encoded);  // Back to "Secret"
```

---

### char_shift()

Shift all characters by ASCII value.

**Syntax:**
```pie
string char_shift(string text, int shift);
```

**Example:**
```pie
string alien = char_shift("Hello", 3);  // Shifts all chars
string earth = char_shift(alien, -3);   // "Hello"
```

---

### reverse_string()

Reverse a string.

**Syntax:**
```pie
string reverse_string(string text);
```

---

### xor_cipher()

XOR cipher with repeating key.

**Syntax:**
```pie
string xor_cipher(string text, string key);
```

**Note:** XOR is its own inverse - use same function to decrypt.

---

## Regular Expression Functions

### regex_compile()

Compile a regular expression pattern.

**Syntax:**
```pie
regex regex_compile(string pattern);
```

**Parameters:**
- `pattern` - Regex pattern using Kleene syntax

**Example:**
```pie
regex digit = regex_compile("0|1|2|3|4|5|6|7|8|9");
regex phone = regex_compile("(0|1|2|3|4|5|6|7|8|9)+:10");  // Exactly 10 digits
regex letter = regex_compile("a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z");
```

**Pattern Syntax:**
- Literals: `a`, `b`, `1`, etc.
- Concatenation: `.` (e.g., `a.b` matches "ab")
- OR: `|` (e.g., `a|b` matches "a" or "b")
- Kleene Star: `*` (zero or more)
- Positive Closure: `+` (one or more)
- Exact length: `:n` (e.g., `a+:3` matches exactly 3 a's)
- Min length: `>n` (e.g., `a+>2` matches 3+ a's)
- Max length: `<n` (e.g., `a+<5` matches up to 4 a's)
- Range: `>n<m` (e.g., `a+>2<6` matches 3-5 a's)

---

### regex_match()

Match a string against a compiled regex pattern.

**Syntax:**
```pie
int regex_match(regex pattern, string str);
```

**Returns:**
- `1` if string matches the pattern
- `0` if no match

**Example:**
```pie
regex digit_pattern = regex_compile("0|1|2|3|4|5|6|7|8|9");
int match1 = regex_match(digit_pattern, "5");  // 1
int match2 = regex_match(digit_pattern, "a");  // 0

regex four_digits = regex_compile("(0|1|2|3|4|5|6|7|8|9)+:4");
int match3 = regex_match(four_digits, "1234");  // 1
int match4 = regex_match(four_digits, "123");   // 0
```

---

### regex_free()

Free memory used by a compiled regex pattern.

**Syntax:**
```pie
void regex_free(regex pattern);
```

**Example:**
```pie
regex pattern = regex_compile("a+.b*");
// Use pattern...
regex_free(pattern);
```

---

## File I/O Functions

### file_open()

Open a file for reading or writing.

**Syntax:**
```pie
file file_open(string filename, string mode);
```

**Parameters:**
- `filename` - Path to the file
- `mode` - Open mode: `"r"` (read), `"w"` (write), `"a"` (append)

**Example:**
```pie
file f = file_open("data.txt", "w");
file r = file_open("input.txt", "r");
file a = file_open("log.txt", "a");
```

---

### file_close()

Close an open file.

**Syntax:**
```pie
void file_close(file handle);
```

**Example:**
```pie
file f = file_open("data.txt", "w");
file_write(f, "Hello");
file_close(f);
```

---

### file_write()

Write a string to a file.

**Syntax:**
```pie
void file_write(file handle, string content);
```

**Example:**
```pie
file f = file_open("output.txt", "w");
file_write(f, "Hello, World!");
file_write(f, "Second line");
file_close(f);
```

---

### file_read_all()

Read entire file contents as a string.

**Syntax:**
```pie
string file_read_all(file handle);
```

**Example:**
```pie
file f = file_open("data.txt", "r");
string content = file_read_all(f);
output(content, string);
file_close(f);
```

---

### file_flush()

Flush the file buffer to disk.

**Syntax:**
```pie
void file_flush(file handle);
```

**Example:**
```pie
file f = file_open("log.txt", "a");
file_write(f, "Log entry");
file_flush(f);  // Ensure data is written
file_close(f);
```

---

## Network Functions

### tcp_socket()

Create a TCP socket.

**Syntax:**
```pie
socket tcp_socket();
```

**Example:**
```pie
socket sock = tcp_socket();
```

---

### tcp_connect()

Connect to a remote host.

**Syntax:**
```pie
int tcp_connect(socket sock, string host, int port);
```

**Returns:**
- `0` on success
- `-1` on failure

**Example:**
```pie
socket sock = tcp_socket();
int result = tcp_connect(sock, "example.com", 80);
if (result == 0) {
    output("Connected!", string);
}
```

---

### tcp_send()

Send data over a socket.

**Syntax:**
```pie
int tcp_send(socket sock, string data);
```

**Returns:**
- Number of bytes sent
- `-1` on error

**Example:**
```pie
int sent = tcp_send(sock, "GET / HTTP/1.1\r\n");
```

---

### tcp_recv()

Receive data from a socket.

**Syntax:**
```pie
int tcp_recv(socket sock, string buffer, int size);
```

**Returns:**
- Number of bytes received
- `-1` on error

**Example:**
```pie
string buffer = "";
int received = tcp_recv(sock, buffer, 1024);
```

---

### tcp_close()

Close a socket connection.

**Syntax:**
```pie
void tcp_close(socket sock);
```

**Example:**
```pie
tcp_close(sock);
```

---

## Time Functions

### time_now()

Get the current Unix timestamp.

**Syntax:**
```pie
int time_now();
```

**Returns:**
- Current time as seconds since epoch (January 1, 1970)

**Example:**
```pie
int timestamp = time_now();
output(timestamp, int);

// Seed random number generator
srand(time_now());
```

---

### time_to_local()

Convert Unix timestamp to local time string.

**Syntax:**
```pie
string time_to_local(int timestamp);
```

**Returns:**
- Formatted time string (e.g., "14:30:45")

**Example:**
```pie
int now = time_now();
string timeStr = time_to_local(now);
output(timeStr, string);
```

---

## System Functions

### exit()

Exit the program immediately.

**Syntax:**
```pie
void exit();
```

**Example:**
```pie
if (errorCondition) {
    output("Fatal error!", string);
    exit();
}
```

---

### sleep()

Pause program execution for a specified duration.

**Syntax:**
```pie
void sleep(int milliseconds);
```

**Parameters:**
- `milliseconds` - Duration to sleep in milliseconds

**Example:**
```pie
output("Starting...", string);
sleep(1000);  // Wait 1 second
output("Done!", string);

// Countdown
for (int i = 5; i > 0; i--) {
    output(i, int);
    sleep(1000);
}
output("Blast off!", string);
```

---

## Helper Functions

### is_variable_defined()

Check if a variable is defined (non-null pointer check).

**Syntax:**
```pie
int is_variable_defined(void* variable);
```

**Returns:**
- `1` if variable is defined
- `0` if null

---

### is_variable_null()

Check if a variable is null.

**Syntax:**
```pie
int is_variable_null(void* variable);
```

**Returns:**
- `1` if variable is null
- `0` if defined

---

## Function Categories Summary

### Input/Output
- `input()` - Read user input
- `output()` - Print to console

### Math (28 functions)
- Basic: `sqrt()`, `pow()`, `abs()`, `abs_int()`
- Trig: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
- Log/Exp: `log()`, `log10()`, `exp()`
- Rounding: `floor()`, `ceil()`, `round()`
- Min/Max: `min()`, `max()`, `min_int()`, `max_int()`
- Random: `rand()`, `srand()`, `rand_range()`
- Constants: `pi()`, `e()`

### Strings (18 functions)
- Basic: `strlen()`, `strcmp()`, `strcpy()`, `strcat()`
- Case: `string_to_upper()`, `string_to_lower()`
- Manipulation: `string_trim()`, `string_substring()`, `string_reverse()`, `string_replace_char()`
- Search: `string_index_of()`, `string_count_char()`, `string_contains()`, `string_starts_with()`, `string_ends_with()`, `string_is_empty()`

### Arrays (6 functions)
- `arr_push()`, `arr_pop()`, `arr_size()`
- `arr_contains()`, `arr_indexof()`, `arr_avg()`

### Dictionaries (5 functions)
- `dict_create()`, `dict_set()`, `dict_get()`
- `dict_has_key()`, `dict_delete()`

### Regular Expressions (3 functions)
- `regex_compile()`, `regex_match()`, `regex_free()`

### File I/O (5 functions)
- `file_open()`, `file_close()`, `file_write()`
- `file_read_all()`, `file_flush()`

### Networking (5 functions)
- `tcp_socket()`, `tcp_connect()`, `tcp_send()`
- `tcp_recv()`, `tcp_close()`

### Time (2 functions)
- `time_now()`, `time_to_local()`

### System (2 functions)
- `exit()`, `sleep()`

---

## See Also

- [Language Reference](language-reference.md) - Complete language syntax
- [Advanced Features](advanced-features.md) - In-depth guides for complex features
- [Examples](examples.md) - Sample programs and tutorials
