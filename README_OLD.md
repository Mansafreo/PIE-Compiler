# PIE Compiler

A compiler for the PIE programming language, supporting parsing, semantic analysis, intermediate representation (IR) generation, and LLVM-based code generation.

## 1. Basic Language Structure

PIE is a C-like language that supports both global statements and user-defined functions. You can write programs in two ways:

1. **Global statements only**: Write your code directly at the top level. The compiler will automatically wrap these statements in a `main()` function.
2. **Explicit main function**: Define your own `main()` function if you prefer traditional C-style structure.

**Data Types:**
- `int` - 32-bit signed integers
- `float` - Double-precision floating point numbers  
- `char` - Single characters
- `string` - Null-terminated character strings
- `boolean` (or `bool`) - Boolean values (`true`/`false`)
- `file` - File handles for I/O operations
- `socket` - Network socket handles
- `dict` - Hash map dictionaries with string keys

**Comments:**
- Single line: `// comment text`
- Multi-line: `/* comment text */`

## 2. Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `%`  
**Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`  
**Logical:** `&&` (and), `||` (or)  
**Assignment:** `=`  
**String concatenation:** `+` (for strings)

## 3. Control Flow Statements

**Conditional Statements:**
```pie
if (condition) {
    // statements
} else {
    // statements
}
```

**Loops:**
```pie
// For loop
for (initialization; condition; update) {
    // statements
}

// While loop  
while (condition) {
    // statements
}
```

**Control keywords:** `break`, `continue`, `return`

## 4. Variable Declarations

**Basic declarations:**
```pie
int x;              // Declaration only
int y = 5;          // Declaration with initialization
float pi = 3.14159; // Float initialization
char grade = 'A';   // Character initialization
string name = "Alice"; // String initialization
boolean isValid = true; // Boolean initialization
```

**Global variables:**
Variables declared outside functions are global and initialized at program startup.

## 5. Arrays

**Static Arrays:**
```pie
// Declaration with size
int numbers[10];

// Declaration with initializer list (size inferred)
string names[] = {"Alice", "Bob", "Charlie"};

// Array access
numbers[0] = 42;
string first = names[0];
```

**Dynamic Arrays:**
```pie
int[] dynamicArray = {1, 2, 3, 4, 5};
// Dynamic arrays use runtime library functions for manipulation
```

## 6. User-Defined Functions

Functions can be defined with type-safe parameters and return types.

**Syntax:**
```pie
<return_type> <function_name>(<parameter_list>) {
    <function_body>
}
```

**Example:**
```pie
int add(int a, int b) {
    return a + b;
}
```

## 7. Dictionaries

PIE supports dictionaries (hash maps) with string keys and **automatic type inference**.

**Syntax:**
```pie
// Create dictionary with mixed types
dict person = {"name": "John Doe", "age": 30, "city": "New York"};

// Get values - type is automatically inferred
string name = dict_get(person, "name");
int age = dict_get(person, "age");

// Set values - type is automatically inferred
dict_set(person, "age", 31);
```

## 8. String Operations

**String concatenation:**
```pie
string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;
output(fullName, string); // Outputs: John Doe
```

**String Comparisons:**
PIE supports all standard comparison operators for strings (`==`, `!=`, `<`, `>`, `<=`, `>=`). It also supports automatic string-to-integer comparison using string length.
```pie
string password = "secret123";

// Check if password is too short
if(password < 8){
    output("Password must be at least 8 characters", string);
}
```

## 9. Regular Expressions
PIE supports **regular expressions** with Kleene syntax and NFA-based matching.
**Basic Usage:**
```pie
// Compile a regex pattern
regex pattern = regex_compile("a+.b*");

// Match strings against the pattern
int result = regex_match(pattern, "aabb");
if (result == 1) {
    output("Match found!", string);
}
```

## 10. Standard Library

PIE includes a comprehensive standard library for common operations.

#### System I/O Functions
```pie
// Input functions - read values from user
input(variable, type);    // Reads input and stores in variable

// Output functions - print values to console  
output(value, type);         // Basic output
output(value, float, precision); // Float output with precision control

// Program control
exit();                      // Exit the program
```

#### Math Library Functions
```pie
float sqrt(float x);          // Square root
float pow(float base, float exp); // Power function  
float sin(float x);           // Sine function
float cos(float x);           // Cosine function
float floor(float x);         // Floor function
float ceil(float x);          // Ceiling function
int rand();                   // Random number generator
```

#### File I/O Library
```pie
file file_open(string filename, string mode); // Open file
void file_close(file handle);                 // Close file
void file_write(file handle, string content); // Write to file
string file_read_all(file handle);           // Read entire file
string file_read_line(file handle);          // Read single line
void file_flush(file handle);                // Flush file buffer
```

#### String Utility Functions
```pie
// Case conversion
string string_to_upper(string str);     // Convert to uppercase
string string_to_lower(string str);     // Convert to lowercase

// String manipulation
string string_trim(string str);         // Remove leading/trailing whitespace
string string_substring(string str, int start, int length); // Extract substring
string string_reverse(string str);      // Reverse string

// String searching
int string_index_of(string haystack, string needle); // Find substring position
int string_contains(string haystack, string needle); // Check if contains substring
int string_starts_with(string str, string prefix);   // Check if starts with prefix
int string_ends_with(string str, string suffix);     // Check if ends with suffix
```

#### Network Library
```pie
socket tcp_socket();                           // Create TCP socket
int tcp_connect(socket sock, string host, int port); // Connect to host
int tcp_send(socket sock, string data);       // Send data
int tcp_recv(socket sock, string buffer, int size);  // Receive data
void tcp_close(socket sock);                  // Close socket
```

## How to Run the Compiler

### Prerequisites

- Python 3.x
- `ply` (`pip install ply`)
- `llvmlite` (`pip install llvmlite`)
- Clang and LLVM tools (`llvm-as`, `llc`)

### Steps

1. **Write your PIE program** (e.g., `test.pie`).
2. **Run the compiler:** `python3 src/main.py test.pie`
3. **Run your program:** `./program`
