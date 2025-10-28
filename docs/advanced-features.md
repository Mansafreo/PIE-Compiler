# PIE Advanced Features Guide

In-depth documentation for advanced features in the PIE programming language.

## Table of Contents

1. [Dynamic Arrays](#dynamic-arrays)
2. [Dictionaries](#dictionaries)
3. [Regular Expressions](#regular-expressions)
4. [File I/O](#file-io)
5. [Network Programming](#network-programming)
6. [Type Conversions](#type-conversions)
7. [Cryptography & Encoding](#cryptography--encoding)
8. [Memory Management](#memory-management)
9. [Best Practices](#best-practices)

---

## Dynamic Arrays

### Overview

PIE supports both static and dynamic arrays. Dynamic arrays can grow and shrink at runtime, making them more flexible than static arrays.

### Creating Dynamic Arrays

```pie
// Empty dynamic array
int numbers[] = [];

// Dynamic array with initial values
int scores[] = [85, 92, 78, 95];
string names[] = ["Alice", "Bob", "Charlie"];
float grades[] = [3.5, 3.8, 3.2];
```

### Array Declaration Syntax

```pie
// Static array - fixed size
int staticArray[10];
string staticNames[5] = ["A", "B", "C", "D", "E"];

// Dynamic array - growable
int dynamicArray[];
string dynamicNames[] = ["Alice", "Bob"];
```

**Key Differences:**

| Feature | Static Array | Dynamic Array |
|---------|--------------|---------------|
| Declaration | `type[size]` | `type[]` |
| Size | Fixed at compile time | Can grow/shrink at runtime |
| Push/Pop | ❌ Not supported | ✅ Supported |
| Memory | Stack allocated | Heap allocated |

### Dynamic Array Operations

#### Adding Elements

```pie
int numbers[] = [1, 2, 3];

// Add single element
arr_push(numbers, 4);
arr_push(numbers, 5);
// numbers is now {1, 2, 3, 4, 5}

// Add multiple elements in a loop
for (int i = 6; i <= 10; i++) {
    arr_push(numbers, i);
}
```

#### Removing Elements

```pie
int[] numbers = [1, 2, 3, 4, 5];

// Remove and get last element
int last = arr_pop(numbers);  // Returns 5
int prev = arr_pop(numbers);  // Returns 4
// numbers is now {1, 2, 3}
```

#### Querying Arrays

```pie
int numbers[] = [10, 20, 30, 40, 50];

// Get size
int size = arr_size(numbers);  // 5

// Check if value exists
int exists = arr_contains(numbers, 30);  // 1 (true)
int missing = arr_contains(numbers, 99); // 0 (false)

// Find index of value
int index = arr_indexof(numbers, 40);    // 3
int notFound = arr_indexof(numbers, 99); // -1

// Calculate average
float avg = arr_avg(numbers);  // 30.0
```

### Practical Examples

#### Building an Array from Input

```pie
int scores[] = [];
int count;

output("How many scores? ", string);
input(count, int);

for (int i = 0; i < count; i++) {
    int score;
    output("Enter score ", string);
    output(i + 1, int);
    output(": ", string);
    input(score, int);
    arr_push(scores, score);
}

// Display statistics
output("Total scores: ", string);
output(arr_size(scores), int);
output("Average: ", string);
output(arr_avg(scores), float, 2);
```

#### Filtering an Array

```pie
int numbers[] = [15, 32, 8, 47, 23, 91, 12, 56];
int evenNumbers[] = [];

// Filter even numbers
for (int i = 0; i < arr_size(numbers); i++) {
    if (numbers[i] % 2 == 0) {
        arr_push(evenNumbers, numbers[i]);
    }
}

output("Even numbers:", string);
for (int i = 0; i < arr_size(evenNumbers); i++) {
    output(evenNumbers[i], int);
}
```

#### Stack Implementation

```pie
// Stack using dynamic array
int stack[] = [];

// Push operations
arr_push(stack, 10);
arr_push(stack, 20);
arr_push(stack, 30);

output("Stack size: ", string);
output(arr_size(stack), int);  // 3

// Pop operations
int top = arr_pop(stack);  // 30
int next = arr_pop(stack); // 20

output("Remaining size: ", string);
output(arr_size(stack), int);  // 1
```

---

## Dictionaries

### Overview

Dictionaries (hash maps) in PIE provide key-value storage with string keys. PIE features **automatic type inference** for dictionary operations, making them intuitive to use.

### Creating Dictionaries

```pie
// Empty dictionary
dict empty = {};

// Dictionary with initial values
dict person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "salary": 75000.50
};

// Mixed types are supported
dict config = {
    "app_name": "PIE App",
    "version": 1,
    "debug": 1,
    "timeout": 30.5
};
```

### Type Inference

PIE automatically infers types for dictionary operations:

#### Setting Values

```pie
dict data = {};

// Type is automatically inferred from the value
dict_set(data, "count", 42);        // int
dict_set(data, "price", 19.99);     // float
dict_set(data, "title", "Book");    // string
```

**Old way (still supported):**
```pie
dict_set(data, "count", new_int(42));
dict_set(data, "price", new_float(19.99));
```

**New way (recommended):**
```pie
dict_set(data, "count", 42);
dict_set(data, "price", 19.99);
```

#### Getting Values

```pie
dict person = {"name": "Bob", "age": 25, "score": 95.5};

// Type is inferred from the receiving variable
string name = dict_get(person, "name");    // Returns string
int age = dict_get(person, "age");         // Returns int
float score = dict_get(person, "score");   // Returns float
```

### Dictionary Operations

#### Adding and Updating

```pie
dict user = {"username": "alice", "role": "admin"};

// Add new key
dict_set(user, "email", "alice@example.com");
dict_set(user, "login_count", 5);

// Update existing key
dict_set(user, "role", "superadmin");
dict_set(user, "login_count", 6);
```

#### Checking Keys

```pie
dict user = {"username": "alice", "role": "admin"};

// Check if key exists
if (dict_has_key(user, "email") == 1) {
    output("Email is set", string);
} else {
    output("Email not found", string);
}

// Alternative function name
if (dict_key_exists(user, "username") == 1) {
    string username = dict_get(user, "username");
    output("Username: " + username, string);
}
```

#### Deleting Keys

```pie
dict data = {"temp": 100, "name": "Test", "count": 5};

// Remove temporary data
dict_delete(data, "temp");

// temp key no longer exists
if (dict_has_key(data, "temp") == 0) {
    output("Temp data removed", string);
}
```

### Practical Examples

#### User Profile Management

```pie
dict profile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 28,
    "premium": 1
};

// Display profile
string username = dict_get(profile, "username");
string email = dict_get(profile, "email");
int age = dict_get(profile, "age");
int premium = dict_get(profile, "premium");

output("=== User Profile ===", string);
output("Username: " + username, string);
output("Email: " + email, string);
output("Age: ", string);
output(age, int);

if (premium == 1) {
    output("Account Type: Premium", string);
} else {
    output("Account Type: Free", string);
}

// Update profile
dict_set(profile, "age", 29);
dict_set(profile, "last_login", "2024-10-24");
```

#### Configuration System

```pie
dict appConfig = {
    "app_name": "MyApp",
    "version": 1,
    "max_connections": 100,
    "timeout": 30.5,
    "debug_mode": 1
};

// Read configuration
string appName = dict_get(appConfig, "app_name");
int version = dict_get(appConfig, "version");
int maxConn = dict_get(appConfig, "max_connections");
float timeout = dict_get(appConfig, "timeout");
int debug = dict_get(appConfig, "debug_mode");

output("Application: " + appName, string);
output("Version: ", string);
output(version, int);
output("Max Connections: ", string);
output(maxConn, int);
output("Timeout: ", string);
output(timeout, float, 1);

if (debug == 1) {
    output("[DEBUG] Debug mode enabled", string);
}
```

#### Database Record Simulation

```pie
// Simulate database record
dict record = {
    "id": 1001,
    "name": "Product A",
    "price": 29.99,
    "stock": 150,
    "category": "Electronics"
};

// Process order
int orderQty = 5;
int currentStock = dict_get(record, "stock");

if (currentStock >= orderQty) {
    int newStock = currentStock - orderQty;
    dict_set(record, "stock", newStock);
    
    output("Order processed", string);
    output("Remaining stock: ", string);
    output(newStock, int);
} else {
    output("Insufficient stock", string);
}
```

### Default Values for Missing Keys

When retrieving a non-existent key, PIE returns default values:

```pie
dict data = {"name": "Alice"};

// Missing keys return defaults
int missing_int = dict_get(data, "age");        // 0
float missing_float = dict_get(data, "score");  // 0.0
string missing_str = dict_get(data, "email");   // ""

// Always check if key exists for critical data
if (dict_has_key(data, "age") == 1) {
    int age = dict_get(data, "age");
} else {
    output("Age not set", string);
}
```

---

## Regular Expressions

### Overview

PIE includes a built-in regular expression engine using Kleene syntax with NFA-based matching. This provides powerful pattern matching capabilities.

### Regex Syntax

#### Basic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| Literal | Match specific character | `a` matches "a" |
| `.` | Concatenation | `a.b` matches "ab" |
| `|` | OR (alternation) | `a|b` matches "a" or "b" |
| `*` | Kleene star (0 or more) | `a*` matches "", "a", "aa", ... |
| `+` | Positive closure (1 or more) | `a+` matches "a", "aa", ... |
| `()` | Grouping | `(a|b).c` matches "ac" or "bc" |

#### Length Constraints

| Constraint | Description | Example |
|------------|-------------|---------|
| `:n` | Exactly n occurrences | `a+:3` matches "aaa" |
| `>n` | More than n occurrences | `a+>2` matches "aaa", "aaaa", ... |
| `<n` | Fewer than n occurrences | `a+<5` matches "a" to "aaaa" |
| `>n<m` | Between n and m occurrences | `a+>2<6` matches "aaa" to "aaaaa" |

### Using Regular Expressions

#### Compile and Match

```pie
// Compile a pattern
regex pattern = regex_compile("a+.b*");

// Match strings
int match1 = regex_match(pattern, "aabb");   // 1 (match)
int match2 = regex_match(pattern, "a");      // 1 (match)
int match3 = regex_match(pattern, "b");      // 0 (no match)

// Free pattern when done
regex_free(pattern);
```

### Practical Patterns

#### Email Validation (Simplified)

```pie
// Pattern: one or more letters, @, one or more letters
regex email = regex_compile("(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+.@.(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+");

int valid1 = regex_match(email, "user@example");  // 1
int valid2 = regex_match(email, "invalid");       // 0
int valid3 = regex_match(email, "test@site");     // 1
```

#### Phone Number Validation

```pie
// Exactly 10 digits
regex phone = regex_compile("(0|1|2|3|4|5|6|7|8|9)+:10");

string number1 = "1234567890";
string number2 = "123456789";

if (regex_match(phone, number1) == 1) {
    output("Valid phone: " + number1, string);
}

if (regex_match(phone, number2) == 0) {
    output("Invalid phone: " + number2, string);
}
```

#### Password Strength

```pie
// At least 8 characters (letters and digits)
regex password = regex_compile("(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|0|1|2|3|4|5|6|7|8|9)+>7");

string pass1 = "secret123";   // 9 chars - valid
string pass2 = "short";       // 5 chars - invalid

if (regex_match(password, pass1) == 1) {
    output("Password accepted", string);
}

if (regex_match(password, pass2) == 0) {
    output("Password too short", string);
}
```

#### Username Validation

```pie
// 3-20 characters (letters and digits)
regex username = regex_compile("(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|0|1|2|3|4|5|6|7|8|9)+>2<21");

string user1 = "john_doe";  // 8 chars - valid
string user2 = "ab";        // 2 chars - invalid
string user3 = "verylongusernamethatexceedslimit";  // Too long - invalid

if (regex_match(username, user1) == 1) {
    output("Username valid: " + user1, string);
}
```

#### Input Validation Example

```pie
// Note: For simplicity, using just a few letters. In practice, list all needed characters.
regex emailPattern = regex_compile("(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+.@.(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+>5");

string userEmail;
output("Enter email: ", string);
input(userEmail, string);

if (regex_match(emailPattern, userEmail) == 1) {
    output("Email format is valid", string);
} else {
    output("Invalid email format", string);
}

regex_free(emailPattern);
```

### Pattern Building Tips

1. **Start simple:** Build patterns incrementally
   ```pie
   // Start with: a+
   // Add OR: (a|b)+
   // Add concatenation: (a|b)+.c
   // Add length: (a|b)+.c>5
   ```

2. **Use grouping for clarity:**
   ```pie
   // Clear: (a|b).(c|d)
   // Confusing: a|b.c|d
   ```

3. **Test patterns thoroughly:**
   ```pie
   regex pattern = regex_compile("your_pattern");
   
   // Test multiple cases
   output("Test 1: ", string);
   output(regex_match(pattern, "test1"), int);
   output("Test 2: ", string);
   output(regex_match(pattern, "test2"), int);
   ```

---

## File I/O

### Overview

PIE provides comprehensive file I/O capabilities for reading and writing text files.

### File Modes

| Mode | Description | Creates if Missing | Overwrites |
|------|-------------|-------------------|------------|
| `"r"` | Read only | ❌ No | N/A |
| `"w"` | Write only | ✅ Yes | ✅ Yes |
| `"a"` | Append | ✅ Yes | ❌ No |

### Basic File Operations

#### Writing to a File

```pie
file f = file_open("output.txt", "w");

if (f != null) {
    file_write(f, "Line 1: Hello, World!");
    file_write(f, "Line 2: PIE language");
    file_write(f, "Line 3: File I/O");
    file_close(f);
    output("File written successfully", string);
}
```

#### Reading from a File

```pie
file f = file_open("output.txt", "r");

if (f != null) {
    string content = file_read_all(f);
    file_close(f);
    
    output("File contents:", string);
    output(content, string);
}
```

#### Appending to a File

```pie
file log = file_open("log.txt", "a");

if (log != null) {
    int timestamp = time_now();
    string timeStr = time_to_local(timestamp);
    
    file_write(log, "[" + timeStr + "] Event occurred");
    file_close(log);
}
```

### Practical Examples

#### Data Export

```pie
// Export student grades to file
string[] names = ["Alice", "Bob", "Charlie"];
float[] grades = [95.5, 87.3, 91.2];

file f = file_open("grades.txt", "w");

file_write(f, "=== Student Grades ===");

for (int i = 0; i < arr_size(names); i++) {
    string line = names[i] + ": ";
    file_write(f, line);
    // Note: file_write only accepts strings
    // Convert numbers to strings if needed
}

file_close(f);
output("Grades exported to grades.txt", string);
```

#### Log System

```pie
void writeLog(string message) {
    file log = file_open("app.log", "a");
    
    int timestamp = time_now();
    string timeStr = time_to_local(timestamp);
    
    string entry = "[" + timeStr + "] " + message;
    file_write(log, entry);
    file_flush(log);  // Ensure data is written
    file_close(log);
}

// Usage
writeLog("Application started");
writeLog("Processing data");
writeLog("Task completed");
```

#### Configuration File

```pie
// Write configuration
file config = file_open("config.txt", "w");
file_write(config, "app_name=MyApp");
file_write(config, "version=1");
file_write(config, "debug=true");
file_close(config);

// Read configuration
file configRead = file_open("config.txt", "r");
string configData = file_read_all(configRead);
file_close(configRead);

output("Configuration:", string);
output(configData, string);
```

### Error Handling

Always check if file operations succeed:

```pie
file f = file_open("data.txt", "r");

if (f == null) {
    output("Error: Cannot open file", string);
    exit();
}

string content = file_read_all(f);
file_close(f);
```

### Best Practices

1. **Always close files**
   ```pie
   file f = file_open("file.txt", "w");
   file_write(f, "data");
   file_close(f);  // Important!
   ```

2. **Use flush for critical data**
   ```pie
   file log = file_open("important.log", "a");
   file_write(log, "Critical event");
   file_flush(log);  // Ensure it's written immediately
   file_close(log);
   ```

3. **Check file handles**
   ```pie
   file f = file_open("file.txt", "r");
   if (f != null) {
       // Safe to use
   }
   ```

---

## Network Programming

### Overview

PIE provides TCP socket support for network programming.

### Basic Socket Operations

#### Creating a Client

```pie
// Create socket
socket sock = tcp_socket();

// Connect to server
int connected = tcp_connect(sock, "example.com", 80);

if (connected == 0) {
    output("Connected!", string);
    
    // Send HTTP request
    tcp_send(sock, "GET / HTTP/1.1\r\n");
    tcp_send(sock, "Host: example.com\r\n");
    tcp_send(sock, "\r\n");
    
    // Receive response
    string buffer = "";
    int received = tcp_recv(sock, buffer, 1024);
    
    if (received > 0) {
        output("Response:", string);
        output(buffer, string);
    }
    
    tcp_close(sock);
} else {
    output("Connection failed", string);
}
```

### Practical Example: Simple HTTP Client

```pie
socket httpClient = tcp_socket();

string host = "httpbin.org";
int port = 80;

if (tcp_connect(httpClient, host, port) == 0) {
    output("Connected to " + host, string);
    
    // Send HTTP GET request
    tcp_send(httpClient, "GET /get HTTP/1.1\r\n");
    tcp_send(httpClient, "Host: httpbin.org\r\n");
    tcp_send(httpClient, "Connection: close\r\n");
    tcp_send(httpClient, "\r\n");
    
    // Receive response
    string response = "";
    int bytes = tcp_recv(httpClient, response, 2048);
    
    output("Received bytes: ", string);
    output(bytes, int);
    output("Response:", string);
    output(response, string);
    
    tcp_close(httpClient);
} else {
    output("Failed to connect", string);
}
```

---

## Type Conversions

### Overview

PIE provides a comprehensive set of type conversion functions to convert between different data types. These functions handle edge cases gracefully and provide predictable behavior.

### String Conversions

#### string_to_int()

Convert a string to an integer.

**Syntax:**
```pie
int string_to_int(string str);
```

**Returns:**
- Integer value parsed from the string
- `0` if the string is invalid or empty

**Example:**
```pie
string num_str = "42";
int num = string_to_int(num_str);
output(num, int);  // 42

string negative = "-123";
int neg_num = string_to_int(negative);
output(neg_num, int);  // -123

string invalid = "abc";
int zero = string_to_int(invalid);
output(zero, int);  // 0
```

**Behavior:**
- Skips leading whitespace
- Handles positive and negative numbers
- Stops parsing at first non-digit character
- Returns 0 for invalid input

---

#### string_to_float()

Convert a string to a floating-point number.

**Syntax:**
```pie
float string_to_float(string str);
```

**Returns:**
- Float value parsed from the string
- `0.0` if the string is invalid

**Example:**
```pie
string pi_str = "3.14159";
float pi = string_to_float(pi_str);
output(pi, float, 5);  // 3.14159

string scientific = "1.5e10";
float big = string_to_float(scientific);
output(big, float, 2);  // 15000000000.00
```

---

#### string_to_char()

Get the first character of a string.

**Syntax:**
```pie
char string_to_char(string str);
```

**Returns:**
- First character of the string
- `'\0'` (null character) if string is empty

**Example:**
```pie
string word = "Hello";
char first = string_to_char(word);
output(first, char);  // H

string empty = "";
char null_char = string_to_char(empty);
// Returns '\0'
```

---

### Character Conversions

#### char_to_int()

Get the ASCII value of a character.

**Syntax:**
```pie
int char_to_int(char c);
```

**Returns:**
- ASCII value of the character (0-255)

**Example:**
```pie
char letter = 'A';
int ascii = char_to_int(letter);
output(ascii, int);  // 65

char newline = '\n';
int nl_code = char_to_int(newline);
output(nl_code, int);  // 10
```

**Use Cases:**
- Character arithmetic
- Case conversion logic
- Character validation
- Custom encoding schemes

---

#### int_to_char()

Convert an integer to a character.

**Syntax:**
```pie
char int_to_char(int value);
```

**Returns:**
- Character with the given ASCII value
- Value is taken modulo 256

**Example:**
```pie
int code = 65;
char letter = int_to_char(code);
output(letter, char);  // A

int wrap = 321;  // > 255
char wrapped = int_to_char(wrap);
// 321 % 256 = 65, so outputs 'A'
```

---

### Numeric Conversions

#### int_to_float()

Convert an integer to a floating-point number.

**Syntax:**
```pie
float int_to_float(int value);
```

**Example:**
```pie
int whole = 42;
float decimal = int_to_float(whole);
output(decimal, float, 2);  // 42.00

// Useful for division
int a = 5;
int b = 2;
float result = int_to_float(a) / int_to_float(b);
output(result, float, 2);  // 2.50
```

---

#### float_to_int()

Convert a float to an integer (truncates decimal part).

**Syntax:**
```pie
int float_to_int(float value);
```

**Returns:**
- Integer part of the float (truncated, not rounded)

**Example:**
```pie
float pi = 3.14159;
int truncated = float_to_int(pi);
output(truncated, int);  // 3

float negative = -2.99;
int neg_trunc = float_to_int(negative);
output(neg_trunc, int);  // -2
```

**Note:** This function truncates (rounds toward zero), not rounds to nearest integer. For rounding, use the `round()` math function first.

---

### Type Conversion Best Practices

1. **Validate Before Converting**
   ```pie
   string input = "123abc";
   int num = string_to_int(input);
   // num will be 123 (stops at 'a')
   // Better to validate first if you need strict parsing
   ```

2. **Handle Edge Cases**
   ```pie
   string user_input = "";
   int value = string_to_int(user_input);
   if (value == 0) {
       // Could be actual zero or invalid input
       // Check the original string if distinction matters
   }
   ```

3. **Use for Data Format Conversion**
   ```pie
   // Reading CSV data
   string age_str = "25";
   string gpa_str = "3.75";
   
   int age = string_to_int(age_str);
   float gpa = string_to_float(gpa_str);
   ```

---

## Cryptography & Encoding

### Overview

PIE provides simple cryptographic and encoding functions suitable for learning, obfuscation, and basic text transformations. These are **not** cryptographically secure and should not be used for serious security applications.

**Security Warning:** The crypto functions in PIE are for educational purposes and simple text obfuscation only. For real security needs, use established cryptographic libraries.

---

### Caesar Cipher

#### caesar_cipher()

Encrypt text using the Caesar cipher (shift cipher).

**Syntax:**
```pie
string caesar_cipher(string text, int shift);
```

**Parameters:**
- `text` - The text to encrypt
- `shift` - Number of positions to shift (can be negative)

**Returns:**
- Encrypted text

**Behavior:**
- Only letters (A-Z, a-z) are shifted
- Numbers, spaces, and punctuation remain unchanged
- Case is preserved
- Shift wraps around the alphabet

**Example:**
```pie
string message = "Hello World";
string encrypted = caesar_cipher(message, 3);
output(encrypted, string);  // "Khoor Zruog"

string encrypted_neg = caesar_cipher(message, -3);
output(encrypted_neg, string);  // "Ebiil Tloia"

// Large shifts wrap around
string wrapped = caesar_cipher("XYZ", 5);
output(wrapped, string);  // "CDE"
```

---

#### caesar_decipher()

Decrypt Caesar cipher text.

**Syntax:**
```pie
string caesar_decipher(string text, int shift);
```

**Example:**
```pie
string encrypted = "Khoor Zruog";
string decrypted = caesar_decipher(encrypted, 3);
output(decrypted, string);  // "Hello World"
```

**Note:** `caesar_decipher(text, n)` is equivalent to `caesar_cipher(text, -n)`.

---

#### rot13()

Apply ROT13 encoding (Caesar cipher with shift 13).

**Syntax:**
```pie
string rot13(string text);
```

**Returns:**
- ROT13 encoded text

**Properties:**
- ROT13 is its own inverse: `rot13(rot13(text)) == text`
- Often used for hiding spoilers or puzzle solutions
- Symmetric: encoding and decoding use the same function

**Example:**
```pie
string original = "SECRET MESSAGE";
string encoded = rot13(original);
output(encoded, string);  // "FRPERG ZRFFNTR"

string decoded = rot13(encoded);
output(decoded, string);  // "SECRET MESSAGE"
```

---

### Character Manipulation

#### char_shift()

Shift all characters by their ASCII values (not just letters).

**Syntax:**
```pie
string char_shift(string text, int shift);
```

**Parameters:**
- `text` - Text to transform
- `shift` - Number of ASCII positions to shift

**Returns:**
- Transformed text

**Behavior:**
- Shifts **all** characters, including spaces, numbers, and punctuation
- Wraps around at ASCII value 256
- Can use negative shifts to decrypt

**Example:**
```pie
string earthling = "Greetings from Earth!";
string alienling = char_shift(earthling, 3);
output(alienling, string);  // "Juhhwlqjv#iurp#Hduwk$"

// Decrypt by shifting back
string decoded = char_shift(alienling, -3);
output(decoded, string);  // "Greetings from Earth!"
```

**Use Cases:**
- Simple text obfuscation
- "Alien language" converters
- Basic encoding for non-security purposes
- Teaching encryption concepts

---

#### reverse_string()

Reverse the characters in a string.

**Syntax:**
```pie
string reverse_string(string text);
```

**Example:**
```pie
string forward = "Hello";
string backward = reverse_string(forward);
output(backward, string);  // "olleH"

string palindrome = "racecar";
string reversed = reverse_string(palindrome);
output(reversed, string);  // "racecar" (same!)
```

---

#### xor_cipher()

Encrypt text using XOR cipher with a repeating key.

**Syntax:**
```pie
string xor_cipher(string text, string key);
```

**Parameters:**
- `text` - Text to encrypt/decrypt
- `key` - Encryption key (repeats if shorter than text)

**Returns:**
- Encrypted or decrypted text

**Properties:**
- XOR cipher is its own inverse: `xor_cipher(xor_cipher(text, key), key) == text`
- Same function for encryption and decryption
- Key repeats if shorter than the text

**Example:**
```pie
string message = "Secret";
string key = "KEY";
string encrypted = xor_cipher(message, key);

// To decrypt, XOR again with the same key
string decrypted = xor_cipher(encrypted, key);
output(decrypted, string);  // "Secret"
```

**Warning:** XOR cipher with a short key is weak encryption. Never use for sensitive data.

---

### Practical Examples

#### Example 1: Simple Password Obfuscation

```pie
string obfuscate_password(string password) {
    // Combine multiple transformations
    string step1 = char_shift(password, 7);
    string step2 = reverse_string(step1);
    string step3 = rot13(step2);
    return step3;
}

string deobfuscate_password(string obfuscated) {
    // Reverse the operations in opposite order
    string step1 = rot13(obfuscated);
    string step2 = reverse_string(step1);
    string step3 = char_shift(step2, -7);
    return step3;
}

string original = "MyPassword123";
string hidden = obfuscate_password(original);
string restored = deobfuscate_password(hidden);
output(restored, string);  // "MyPassword123"
```

#### Example 2: Message Encoder/Decoder

```pie
int main() {
    output("=== Message Encoder ===", string);
    
    string message = "Attack at dawn";
    int shift = 13;
    
    output("Original: " + message, string);
    
    // Encode
    string encoded = caesar_cipher(message, shift);
    output("Encoded: " + encoded, string);
    
    // Decode
    string decoded = caesar_decipher(encoded, shift);
    output("Decoded: " + decoded, string);
    
    return 0;
}
```

#### Example 3: Data Type Converter

```pie
// Convert string data to appropriate types
string process_csv_line(string line) {
    // Assume format: "name,age,gpa"
    // In a real application, you'd parse the commas
    
    string name = "Alice";
    string age_str = "20";
    string gpa_str = "3.75";
    
    int age = string_to_int(age_str);
    float gpa = string_to_float(gpa_str);
    
    output("Name: " + name, string);
    output("Age: ", string);
    output(age, int);
    output("GPA: ", string);
    output(gpa, float, 2);
    
    return name;
}
```

---

### Security Considerations

1. **Not Cryptographically Secure**
   - These functions are for learning and simple obfuscation only
   - Do not use for passwords, sensitive data, or security-critical applications

2. **Recommended Use Cases**
   - Educational projects
   - Simple text games
   - Basic obfuscation
   - Teaching encryption concepts
   - Puzzle creation

3. **Not Recommended**
   - Password storage
   - Sensitive user data
   - Financial information
   - Anything requiring real security

---

## Memory Management

### Overview

PIE handles memory management automatically for most operations:

- **Stack Memory:** Local variables, function parameters
- **Heap Memory:** Dynamic arrays, dictionaries, strings

### Dynamic Array Memory

Dynamic arrays are automatically managed:

```pie
int numbers[] = [1, 2, 3];
arr_push(numbers, 4);  // Automatically resizes if needed
arr_pop(numbers);      // Memory is managed automatically
```

### Dictionary Memory

Dictionaries are heap-allocated and managed:

```pie
dict data = {};
dict_set(data, "key", "value");  // Memory allocated automatically
dict_delete(data, "key");        // Memory freed automatically
```

### String Memory

Strings are automatically managed:

```pie
string s1 = "Hello";
string s2 = string_to_upper(s1);  // New string allocated
string s3 = s1 + s2;              // Concatenation allocates new string
```

---

## Best Practices

### Code Organization

1. **Use functions for modularity**
   ```pie
   float calculateTotal(float[] prices) {
       float total = 0.0;
       for (int i = 0; i < arr_size(prices); i++) {
           total = total + prices[i];
       }
       return total;
   }
   ```

2. **Group related data in dictionaries**
   ```pie
   dict createUser(string name, int age) {
       dict user = {};
       dict_set(user, "name", name);
       dict_set(user, "age", age);
       dict_set(user, "created", time_now());
       return user;
   }
   ```

### Error Handling

1. **Validate input**
   ```pie
   int age;
   input(age, int);
   
   if (age < 0 || age > 150) {
       output("Invalid age", string);
       exit();
   }
   ```

2. **Check array bounds**
   ```pie
   int index = 5;
   if (index >= 0 && index < arr_size(numbers)) {
       int value = numbers[index];
   }
   ```

3. **Verify file operations**
   ```pie
   file f = file_open("data.txt", "r");
   if (f == null) {
       output("Cannot open file", string);
       return;
   }
   ```

### Performance Tips

1. **Minimize array resizing**
   ```pie
   // If you know the size, preallocate
   int large[] = [];
   for (int i = 0; i < 1000; i++) {
       arr_push(large, i);  // May resize multiple times
   }
   ```

2. **Reuse regex patterns**
   ```pie
   regex emailPattern = regex_compile("pattern");
   
   // Use pattern multiple times
   for (int i = 0; i < count; i++) {
       int valid = regex_match(emailPattern, emails[i]);
   }
   
   regex_free(emailPattern);  // Free once when done
   ```

3. **Close resources promptly**
   ```pie
   file f = file_open("file.txt", "r");
   string content = file_read_all(f);
   file_close(f);  // Close immediately after use
   ```

---

## See Also

- [Language Reference](language-reference.md) - Complete syntax guide
- [Standard Library](standard-library.md) - All built-in functions
- [Examples](examples.md) - Sample programs and tutorials
