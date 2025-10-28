# PIE Programming Language

<div align="center">

**A Modern, C-like Programming Language with Advanced Features**

[Quick Start](#quick-start) • [Documentation](#documentation) • [Examples](#examples) • [Features](#features)

</div>

---

## Overview

PIE is a statically-typed, compiled programming language that combines the simplicity of C-style syntax with modern programming features. Built with LLVM, PIE offers excellent performance while providing high-level abstractions for common programming tasks.

### Key Features

- 🚀 **LLVM-Based Compilation** - Fast, optimized native code generation
- 📝 **C-Like Syntax** - Familiar and easy to learn for C/C++ programmers
- 🎯 **Static Typing** - Catch errors at compile-time with type safety
- 📚 **Rich Standard Library** - Math, strings, file I/O, networking, and more
- 🔄 **Dynamic Arrays** - Built-in support for growable arrays
- 📖 **Dictionaries** - Hash maps with automatic type inference
- 🔍 **Regular Expressions** - Pattern matching with Kleene syntax
- 🌐 **Network Support** - TCP sockets for network programming
- 📁 **File I/O** - Comprehensive file handling capabilities

## Quick Start

### Prerequisites

- **Python 3.x** (3.7 or higher recommended)
- **LLVM Tools** (llvm-as, llc, clang)
- **Python Packages**: 
  - `llvmlite` (0.45.1 or higher)
  - `ply` (3.11 or higher)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Pie-Compiler/PIE-Compiler-V1-Python.git
cd PIE-Compiler-V1-Python
```

2. **Set up Python virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install llvmlite ply
```

4. **Verify LLVM installation:**
```bash
llc --version
clang --version
```

### Your First PIE Program

Create a file named `hello.pie`:

```pie
// Simple hello world program
output("Hello, PIE!", string);

// Variables and arithmetic
int x = 10;
int y = 20;
int sum = x + y;
output("Sum: ", string);
output(sum, int);
```

### Compile and Run

```bash
# Compile the PIE source code
python3 src/main.py hello.pie

# Run the compiled program
./program
```

**Output:**
```
Hello, PIE!
Sum: 
30
```

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Language Reference](docs/language-reference.md)** - Complete language syntax and features
- **[Standard Library](docs/standard-library.md)** - All built-in functions and their usage
- **[Examples & Tutorials](docs/examples.md)** - Practical examples and sample programs
- **[Advanced Features](docs/advanced-features.md)** - Dictionaries, regex, networking, and more

### Quick Language Overview

#### Data Types
```pie
int x = 42;                    // 32-bit signed integer
float pi = 3.14159;            // Double-precision floating point
char letter = 'A';             // Single character
string name = "Alice";         // String (null-terminated)
bool isValid = true;           // Boolean (true/false)
dict person = {};              // Dictionary (hash map)
regex pattern = regex_compile("a+"); // Regular expression
file f = file_open("data.txt", "r"); // File handle
```

#### Control Flow
```pie
// If-else statements
if (x > 10) {
    output("Greater than 10", string);
} else {
    output("Less than or equal to 10", string);
}

// For loops with increment/decrement operators
for (int i = 0; i < 10; i++) {
    output(i, int);
}

// While loops
while (x > 0) {
    x--;
}

// Do-while loops
do {
    output(x, int);
    x++;
} while (x < 5);
```

#### Arrays
```pie
// Static arrays
int numbers[5] = [1, 2, 3, 4, 5];

// Dynamic arrays
int[] dynamic = [1, 2, 3];
arr_push(dynamic, 4);          // Add element
int size = arr_size(dynamic);  // Get size
int last = arr_pop(dynamic);   // Remove and return last element
```

#### Functions
```pie
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int result = fibonacci(10);
output(result, int);
```

## Examples

### Example 1: Temperature Converter
```pie
float celsius = 25.0;
float fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
output("Celsius: ", string);
output(celsius, float, 2);
output("Fahrenheit: ", string);
output(fahrenheit, float, 2);
```

### Example 2: Working with Dictionaries
```pie
dict student = {
    "name": "Alice",
    "age": 20,
    "grade": 95.5
};

string name = dict_get(student, "name");
int age = dict_get(student, "age");
float grade = dict_get(student, "grade");

output(name, string);
output(age, int);
output(grade, float, 2);
```

### Example 3: String Manipulation
```pie
string text = "  Hello World  ";
string trimmed = string_trim(text);
string upper = string_to_upper(trimmed);
string reversed = string_reverse(upper);

output(reversed, string);  // Outputs: DLROW OLLEH
```

See [docs/examples.md](docs/examples.md) for more comprehensive examples.

## Features

### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `&&` (AND), `||` (OR)
- **Assignment**: `=`
- **Increment/Decrement**: `++`, `--`
- **String Concatenation**: `+`

### Standard Library Highlights

#### Math Functions
```pie
float result = sqrt(16.0);      // Square root
float power = pow(2.0, 8.0);    // Power function
float angle = sin(1.57);        // Trigonometric functions
int random = rand();            // Random number
```

#### String Functions
```pie
int len = strlen("Hello");                          // String length
string upper = string_to_upper("hello");            // Convert to uppercase
string sub = string_substring("Hello", 0, 4);       // Extract substring
int idx = string_index_of("Hello World", "World");  // Find substring
```

#### Type Conversions
```pie
int num = string_to_int("42");              // String to integer
float pi = string_to_float("3.14");         // String to float
char first = string_to_char("Hello");       // First char of string
int ascii = char_to_int('A');               // Get ASCII value (65)
char letter = int_to_char(65);              // ASCII to char ('A')
float f = int_to_float(42);                 // Int to float
int i = float_to_int(3.99);                 // Float to int (truncates to 3)
```

#### Cryptography & Encoding (Educational)
```pie
// Caesar cipher - shifts letters only
string encrypted = caesar_cipher("HELLO", 3);      // "KHOOR"
string decrypted = caesar_decipher("KHOOR", 3);    // "HELLO"

// ROT13 - symmetric encoding
string encoded = rot13("SECRET");                   // "FRPERG"
string decoded = rot13(encoded);                    // "SECRET"

// Character shift - shifts all characters
string alien = char_shift("Hello!", 5);            // "Mjqqt&"
string earth = char_shift(alien, -5);              // "Hello!"

// String manipulation
string reversed = reverse_string("HELLO");          // "OLLEH"
string xor_enc = xor_cipher("text", "key");        // XOR encryption
```

**Note:** Crypto functions are for education and simple obfuscation only, not secure encryption.

#### Array Functions
```pie
arr_push(array, value);         // Add element to dynamic array
int val = arr_pop(array);       // Remove and return last element
int size = arr_size(array);     // Get array size
int exists = arr_contains(array, value);  // Check if value exists
int index = arr_indexof(array, value);    // Find index of value
float avg = arr_avg(array);     // Calculate average
```

#### Regular Expressions
```pie
// Compile pattern with explicit OR operators for each character
regex email_pattern = regex_compile("(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+.@.(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)+");
int is_match = regex_match(email_pattern, "user@example");
```

#### File I/O
```pie
file f = file_open("data.txt", "w");
file_write(f, "Hello, File!");
file_close(f);

file r = file_open("data.txt", "r");
string content = file_read_all(r);
file_close(r);
```

## Project Structure

```
PIE-Compiler-V1-Python/
├── src/
│   ├── main.py                 # Compiler entry point
│   ├── frontend/               # Lexer, parser, semantic analysis
│   │   ├── lexer.py           # NFA/DFA-based tokenization
│   │   ├── parser.py          # PLY-based parser
│   │   ├── semanticAnalysis.py
│   │   └── symbol_table.py
│   ├── backend/               # LLVM code generation
│   │   └── llvm_generator.py
│   └── runtime/               # C runtime library
│       ├── runtime.c          # I/O functions
│       ├── math_lib.c         # Math functions
│       ├── string_lib.c       # String utilities
│       ├── d_array.c          # Dynamic array implementation
│       ├── dict_lib.c         # Dictionary implementation
│       ├── regex_lib.c        # Regex engine
│       ├── file_lib.c         # File I/O
│       ├── net_lib.c          # Network functions
│       └── time_lib.c         # Time functions
├── docs/                      # Documentation
├── README.md                  # This file
└── CHANGELOG.md              # Version history and updates
```

## Compiler Usage

### Basic Compilation
```bash
python3 src/main.py <source_file.pie>
```

The compiler performs these steps:
1. **Lexical Analysis** - Tokenizes the source code
2. **Parsing** - Generates Abstract Syntax Tree (AST)
3. **Semantic Analysis** - Type checking and validation
4. **Code Generation** - Produces LLVM IR
5. **Linking** - Links with runtime library
6. **Output** - Creates executable binary `./program`

### Compiler Output

The compiler generates several intermediate files:
- `output.ll` - LLVM IR (human-readable)
- `output.bc` - LLVM bitcode (binary)
- `program` - Final executable

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is open source. See LICENSE file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history and updates.

---

<div align="center">

**Happy Coding with PIE! 🥧**

Made with ❤️ by the PIE Compiler Team

</div>
