# PIE Language Reference

Complete reference documentation for the PIE programming language.

## Table of Contents

1. [Lexical Elements](#lexical-elements)
2. [Data Types](#data-types)
3. [Variables and Declarations](#variables-and-declarations)
4. [Operators](#operators)
5. [Expressions](#expressions)
6. [Statements](#statements)
7. [Control Flow](#control-flow)
8. [Functions](#functions)
9. [Arrays](#arrays)
10. [Comments](#comments)

---

## 1. Lexical Elements

### Identifiers

Identifiers are names used for variables, functions, and other user-defined entities.

**Rules:**
- Must start with a letter (`a-z`, `A-Z`) or underscore (`_`)
- Can contain letters, digits (`0-9`), and underscores
- Case-sensitive

**Examples:**
```pie
int myVariable;
float _privateValue;
string userName123;
```

**Reserved Keywords:**
```
int       float     char      string    bool      boolean
void      file      socket    dict      regex     array
if        else      for       while     do        switch
case      default   break     continue  return    exit
true      false     null
```

### Literals

#### Integer Literals
```pie
int decimal = 42;
int negative = -100;
int zero = 0;
```

#### Floating-Point Literals
```pie
float pi = 3.14159;
float scientific = 2.5;
float decimal_only = 123.0;
```

#### Character Literals
```pie
char letter = 'A';
char digit = '9';
char newline = '\n';
char tab = '\t';
char backslash = '\\';
```

**Escape Sequences:**
- `\n` - Newline
- `\t` - Tab
- `\\` - Backslash
- `\'` - Single quote

#### String Literals
```pie
string greeting = "Hello, World!";
string empty = "";
string multiWord = "This is a sentence.";
```

**Note:** Strings are enclosed in double quotes (`"`) and are null-terminated.

#### Boolean Literals
```pie
bool isTrue = true;
bool isFalse = false;
```

#### Null Literal
```pie
string empty = null;
```

---

## 2. Data Types

### Primitive Types

| Type | Size | Range/Description |
|------|------|-------------------|
| `int` | 32-bit | Signed integer: -2,147,483,648 to 2,147,483,647 |
| `float` | 64-bit | Double-precision floating point |
| `char` | 8-bit | Single character (ASCII) |
| `bool` or `boolean` | 1-bit | `true` or `false` |
| `string` | pointer | Null-terminated character string |

### Complex Types

| Type | Description |
|------|-------------|
| `file` | File handle for I/O operations |
| `socket` | Network socket handle |
| `dict` | Hash map with string keys and mixed-type values |
| `regex` | Compiled regular expression pattern |

### Array Types

Arrays can be declared with or without explicit sizes:

```pie
// Static array - fixed size
int staticArray[10];

// Dynamic array - growable
int[] dynamicArray;
```

**Array Type Notation:**
- `type[size]` - Static array with fixed size
- `type[]` - Dynamic array

---

## 3. Variables and Declarations

### Simple Variable Declaration

```pie
// Declaration only
int x;
float y;
char c;
string s;

// Declaration with initialization
int age = 25;
float price = 19.99;
char grade = 'A';
string name = "Alice";
bool isActive = true;
```

### Array Declaration

#### Static Arrays

```pie
// Declaration with size
int numbers[5];

// Declaration with size and initializer
int values[5] = [1, 2, 3, 4, 5];

// Declaration with initializer (size inferred)
string names[] = ["Alice", "Bob", "Charlie"];
```

#### Dynamic Arrays

```pie
// Empty dynamic array
int[] dynamicArray;

// Dynamic array with initializer
int[] numbers = [1, 2, 3, 4, 5];
float[] scores = [95.5, 87.3, 91.2];
string[] words = ["hello", "world"];
```

### Dictionary Declaration

```pie
// Empty dictionary
dict empty = {};

// Dictionary with initial values
dict person = {
    "name": "John",
    "age": 30,
    "score": 95.5
};
```

### Scope

Variables have block scope:

```pie
int global = 10;  // Global scope

int main() {
    int local = 20;  // Function scope
    
    if (local > 0) {
        int nested = 30;  // Block scope
        // nested is only visible here
    }
    // nested is not accessible here
    
    return 0;
}
```

---

## 4. Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulo (remainder) | `a % b` |

**Examples:**
```pie
int sum = 10 + 5;        // 15
int diff = 10 - 5;       // 5
int product = 10 * 5;    // 50
int quotient = 10 / 5;   // 2
int remainder = 10 % 3;  // 1
```

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `<` | Less than | `a < b` |
| `>` | Greater than | `a > b` |
| `<=` | Less than or equal | `a <= b` |
| `>=` | Greater than or equal | `a >= b` |

**Examples:**
```pie
bool isEqual = (10 == 10);     // true
bool notEqual = (10 != 5);     // true
bool lessThan = (5 < 10);      // true
bool greaterThan = (10 > 5);   // true
```

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&&` | Logical AND | `a && b` |
| `||` | Logical OR | `a || b` |

**Examples:**
```pie
bool result1 = (true && false);   // false
bool result2 = (true || false);   // true
bool complex = (x > 0 && x < 10); // true if x is between 0 and 10
```

### Assignment Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Assignment | `a = b` |

**Examples:**
```pie
int x = 10;
x = 20;  // x is now 20

string name = "Alice";
name = "Bob";  // name is now "Bob"
```

### Increment and Decrement Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `++` | Increment by 1 | `i++` |
| `--` | Decrement by 1 | `i--` |

**Examples:**
```pie
int count = 0;
count++;  // count is now 1
count++;  // count is now 2
count--;  // count is now 1

// Common use in loops
for (int i = 0; i < 10; i++) {
    output(i, int);
}
```

**Note:** Currently only postfix increment/decrement is supported (`i++`, `i--`).

### Unary Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `-` | Unary minus (negation) | `-x` |

**Examples:**
```pie
int positive = 10;
int negative = -positive;  // -10
```

### String Concatenation Operator

The `+` operator concatenates strings:

```pie
string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;  // "John Doe"
```

### Operator Precedence

From highest to lowest:

1. Unary operators: `-` (unary minus)
2. Multiplicative: `*`, `/`, `%`
3. Additive: `+`, `-`
4. Relational: `<`, `>`, `<=`, `>=`
5. Equality: `==`, `!=`
6. Logical AND: `&&`
7. Logical OR: `||`
8. Assignment: `=`

**Use parentheses to override precedence:**
```pie
int result = (2 + 3) * 4;  // 20, not 14
```

---

## 5. Expressions

### Primary Expressions

```pie
// Literals
42
3.14
'A'
"Hello"
true
false
null

// Identifiers
myVariable
userName

// Parenthesized expressions
(x + y)
(a > b && c < d)

// Function calls
sqrt(16.0)
strlen("Hello")

// Array subscripts
numbers[0]
names[i]
```

### Binary Expressions

```pie
// Arithmetic
a + b
x * y
total / count

// Comparison
age > 18
score >= 90

// Logical
isValid && isActive
hasPermission || isAdmin
```

### Type Compatibility

PIE is statically typed. Type checking is performed at compile time:

```pie
int x = 10;
float y = 3.14;

// Valid: compatible types
int z = x + 5;

// Invalid: type mismatch
int result = x + y;  // Error: cannot mix int and float
```

**String Comparison:**

Strings can be compared using all comparison operators:

```pie
string password = "secret123";

// String-to-string comparison
if (password == "admin") {
    output("Match!", string);
}

// String-to-integer comparison (uses string length)
if (password < 8) {
    output("Password too short", string);
}
```

---

## 6. Statements

### Expression Statements

Any expression followed by a semicolon:

```pie
x = 10;
output("Hello", string);
arr_push(myArray, 5);
```

### Declaration Statements

```pie
int age = 25;
string name = "Alice";
float[] scores = [95.5, 87.3];
```

### Block Statements

Group multiple statements:

```pie
{
    int x = 10;
    int y = 20;
    output(x + y, int);
}
```

### Empty Statement

```pie
;  // Empty statement (does nothing)
```

---

## 7. Control Flow

### If Statement

```pie
// Simple if
if (condition) {
    // statements
}

// If-else
if (condition) {
    // statements
} else {
    // statements
}

// Nested if-else
if (score >= 90) {
    output("A", string);
} else if (score >= 80) {
    output("B", string);
} else if (score >= 70) {
    output("C", string);
} else {
    output("F", string);
}
```

### While Loop

```pie
while (condition) {
    // statements
}

// Example
int count = 0;
while (count < 10) {
    output(count, int);
    count++;
}
```

### Do-While Loop

Execute at least once, then check condition:

```pie
do {
    // statements
} while (condition);

// Example
int x = 0;
do {
    output(x, int);
    x++;
} while (x < 5);
```

### For Loop

```pie
for (initialization; condition; update) {
    // statements
}

// Example
for (int i = 0; i < 10; i++) {
    output(i, int);
}

// Can use multiple variables
for (int i = 0, j = 10; i < j; i++, j--) {
    output(i, int);
    output(j, int);
}
```

**For Loop Components:**
- **Initialization**: Executed once before the loop (can be declaration or assignment)
- **Condition**: Checked before each iteration
- **Update**: Executed after each iteration

### Switch Statement

```pie
switch (expression) {
    case value1:
        // statements
        break;
    case value2:
        // statements
        break;
    default:
        // statements
}

// Example
int day = 3;
switch (day) {
    case 1:
        output("Monday", string);
        break;
    case 2:
        output("Tuesday", string);
        break;
    case 3:
        output("Wednesday", string);
        break;
    default:
        output("Other day", string);
}
```

### Break Statement

Exit the current loop or switch:

```pie
while (true) {
    if (condition) {
        break;  // Exit the loop
    }
}

for (int i = 0; i < 100; i++) {
    if (i == 50) {
        break;  // Stop at 50
    }
}
```

### Continue Statement

Skip to the next iteration:

```pie
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;  // Skip even numbers
    }
    output(i, int);  // Only odd numbers printed
}
```

### Return Statement

Exit a function and optionally return a value:

```pie
int add(int a, int b) {
    return a + b;
}

void printMessage() {
    output("Hello", string);
    return;  // Optional for void functions
}
```

---

## 8. Functions

### Function Definition

```pie
<return_type> <function_name>(<parameters>) {
    <function_body>
}
```

**Examples:**

```pie
// Function with no parameters
int getConstant() {
    return 42;
}

// Function with parameters
int add(int a, int b) {
    return a + b;
}

// Function with multiple parameters
float calculateArea(float width, float height) {
    return width * height;
}

// Void function (no return value)
void printGreeting(string name) {
    output("Hello, " + name, string);
}
```

### Function Calls

```pie
int result = add(10, 20);
float area = calculateArea(5.0, 10.0);
printGreeting("Alice");
int constant = getConstant();
```

### Recursion

Functions can call themselves:

```pie
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### Parameter Passing

All parameters are passed by value:

```pie
void modifyValue(int x) {
    x = 100;  // Only modifies the local copy
}

int main() {
    int value = 10;
    modifyValue(value);
    // value is still 10
    return 0;
}
```

### Program Entry Point

PIE programs can be written in two ways:

**1. Global Statements (No Main Function):**
```pie
// Statements at global scope
output("Hello", string);
int x = 10;
output(x, int);
```

**2. Explicit Main Function:**
```pie
int main() {
    output("Hello", string);
    return 0;
}
```

Both approaches are valid. Global statements are automatically wrapped in a `main()` function by the compiler.

---

## 9. Arrays

### Array Declaration and Initialization

#### Static Arrays

```pie
// Declaration with fixed size
int numbers[10];

// With initializer
int values[5] = [1, 2, 3, 4, 5];

// Size inferred from initializer
string names[] = ["Alice", "Bob", "Charlie"];
```

#### Dynamic Arrays

```pie
// Empty dynamic array
int[] dynamicArray;

// With initializer
int[] numbers = [1, 2, 3, 4, 5];
float[] scores = [95.5, 87.3, 91.2];
string[] words = ["hello", "world"];
```

### Array Access

```pie
int[] numbers = [10, 20, 30, 40, 50];

// Read element
int first = numbers[0];   // 10
int third = numbers[2];   // 30

// Write element
numbers[0] = 100;
numbers[2] = 300;
```

### Array Functions

PIE provides built-in functions for array manipulation:

```pie
int[] numbers = [1, 2, 3];

// Add element (dynamic arrays only)
arr_push(numbers, 4);

// Remove and return last element
int last = arr_pop(numbers);

// Get array size
int size = arr_size(numbers);

// Check if array contains value
int exists = arr_contains(numbers, 2);  // Returns 1 if found

// Find index of value
int index = arr_indexof(numbers, 3);    // Returns index or -1

// Calculate average
float avg = arr_avg(numbers);
```

**Note:** `arr_push` and `arr_pop` only work with dynamic arrays (`int[]`).

### Printing Arrays

```pie
int[] numbers = [1, 2, 3, 4, 5];

// Print each element
for (int i = 0; i < arr_size(numbers); i++) {
    output(numbers[i], int);
}
```
The inbuilt output function also supports printing arrays

```pie
int[] numbers = [1, 2, 3, 4, 5];
output(numbers, array)
---

## 10. Comments

### Single-Line Comments

```pie
// This is a single-line comment
int x = 10;  // Comment after code
```

### Multi-Line Comments

```pie
/*
 * This is a multi-line comment
 * It can span multiple lines
 */
int y = 20;

/* Another multi-line comment */
```

---

## Type Conversion

### Implicit Conversion

PIE does not perform implicit type conversion. All type conversions must be explicit or handled through function calls.

### String-to-Integer Comparison

When comparing a string to an integer, PIE uses the string's length:

```pie
string password = "secret";

if (password < 8) {
    output("Password must be at least 8 characters", string);
}
// This compares strlen(password) < 8
```

---

## Best Practices

1. **Use meaningful variable names:**
   ```pie
   int studentCount;  // Good
   int sc;           // Avoid
   ```

2. **Initialize variables when declaring:**
   ```pie
   int count = 0;    // Good
   int count;        // Avoid (uninitialized)
   ```

3. **Use const for fixed values (if available):**
   ```pie
   float PI = 3.14159;
   ```

4. **Add comments to explain complex logic:**
   ```pie
   // Calculate factorial using recursion
   int factorial(int n) {
       if (n <= 1) {
           return 1;
       }
       return n * factorial(n - 1);
   }
   ```

5. **Use appropriate data types:**
   ```pie
   float price = 19.99;  // Use float for decimals
   int count = 5;        // Use int for whole numbers
   ```

---

## Error Messages

PIE provides helpful error messages during compilation:

- **Undefined variable:** "Undefined variable: 'variableName'"
- **Type mismatch:** "Type mismatch: Cannot assign float to int variable"
- **Undeclared function:** "Undeclared function: 'functionName'"
- **Array index must be integer:** "Array index must be an integer"

Always read error messages carefully as they indicate the location and nature of the problem.

---

## See Also

- [Standard Library](standard-library.md) - Built-in functions and utilities
- [Advanced Features](advanced-features.md) - Dictionaries, regex, file I/O
- [Examples](examples.md) - Sample programs and tutorials
