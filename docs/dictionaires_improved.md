# Improved Dictionary Support in PIE

 

## Overview

 

PIE now features an improved dictionary syntax that makes working with key-value pairs more intuitive and developer-friendly. The new syntax uses type inference to automatically determine value types, eliminating the need for explicit type-specific getter functions.

 

## Table of Contents

 

1. [Dictionary Declaration](#dictionary-declaration)

2. [Setting Values](#setting-values)

3. [Getting Values](#getting-values)

4. [Type Inference](#type-inference)

5. [Complete Examples](#complete-examples)

6. [Migration Guide](#migration-guide)

 

## Dictionary Declaration

 

### Syntax

 

```pie

dict variable_name = {"key1": value1, "key2": value2, ...};

```

 

### Examples

 

```pie

// Person dictionary with mixed types

dict person = {"name": "John Doe", "age": 30, "city": "New York"};

 

// Configuration dictionary

dict config = {"debug": 1, "timeout": 30.5, "host": "localhost"};

 

// Empty dictionary

dict empty = {};

```

 

**Key Points:**

- All keys are strings (enclosed in quotes)

- Values can be: `int`, `float`, or `string`

- Mixed types are supported in the same dictionary

- Dictionary initialization is done at declaration time

 

## Setting Values

 

### Syntax

 

```pie

dict_set(dict_name, key, value);

```

 

### Parameters

- `dict_name`: The dictionary variable

- `key`: String literal or string variable (key name)

- `value`: The value to store (int, float, or string)

 

### Examples

 

```pie

dict person = {"name": "John Doe", "age": 30};

 

// Update existing key

dict_set(person, "age", 31);

 

// Add new key

dict_set(person, "city", "Nairobi");

 

// Update with variable

string new_city = "London";

dict_set(person, "city", new_city);

 

// Set numeric values

dict_set(person, "salary", 50000);

dict_set(person, "rating", 4.5);

```

 

**Key Points:**

- Type is automatically inferred from the value

- Overwrites existing keys

- Creates new keys if they don't exist

- No need for type-specific functions (no more `new_int()`, `new_string()`, etc.)

 

## Getting Values

 

### Syntax

 

```pie

type variable = dict_get(dict_name, key);

```

 

### Parameters

- `dict_name`: The dictionary variable

- `key`: String literal or string variable (key name)

 

### Return Values

- Returns the value associated with the key

- Returns default value if key not found:

  - `0` for int

  - `0.0` for float

  - `""` (empty string) for string

  - `null` for undefined keys

 

### Examples

 

```pie

dict person = {"name": "John Doe", "age": 30, "city": "New York"};

 

// Get values with type inference

int age = dict_get(person, "age");           // Returns 30

string name = dict_get(person, "name");      // Returns "John Doe"

string city = dict_get(person, "city");      // Returns "New York"

 

// Get non-existent key (returns default)

int salary = dict_get(person, "salary");     // Returns 0

string email = dict_get(person, "email");    // Returns ""

 

// Use in expressions

int next_year = dict_get(person, "age") + 1;

output("Age next year: ", string);

output(next_year, int);

```

 

**Key Points:**

- Type is inferred from the variable declaration

- No need for `dict_get_int()`, `dict_get_string()`, etc.

- Safe defaults for missing keys

- Can be used directly in expressions

 

## Type Inference

 

### How It Works

 

The compiler uses the **symbol table** to determine the expected type of the value:

 

1. **At dict_get()**: The type of the variable receiving the value determines what type to retrieve

2. **At dict_set()**: The type of the value being stored is automatically detected

 

### Type Inference Examples

 

```pie

dict data = {"count": 42, "price": 19.99, "name": "Product"};

 

// Compiler infers int because 'count' is declared as int

int count = dict_get(data, "count");

 

// Compiler infers float because 'price' is declared as float

float price = dict_get(data, "price");

 

// Compiler infers string because 'name' is declared as string

string name = dict_get(data, "name");

 

// Type mismatch handling

int wrong = dict_get(data, "price");  // Gets 19.99 but converts to int (19)

```

 

### Type Safety

 

```pie

dict person = {"age": 30};

 

// Correct type

int age = dict_get(person, "age");        // ✅ Works correctly

 

// Type conversion (automatic)

float age_float = dict_get(person, "age"); // ✅ Converts 30 to 30.0

 

// Wrong type (returns default)

string age_str = dict_get(person, "age");  // ⚠️ Returns "" (empty string)

```

 

## Complete Examples

 

### Example 1: User Profile Management

 

```pie

// Create user profile

dict user = {

    "username": "john_doe",

    "email": "john@example.com",

    "age": 28,

    "score": 95.5

};

 

// Display user info

string username = dict_get(user, "username");

string email = dict_get(user, "email");

int age = dict_get(user, "age");

float score = dict_get(user, "score");

 

output("Username: ", string);

output(username, string);

output("Email: ", string);

output(email, string);

output("Age: ", string);

output(age, int);

output("Score: ", string);

output(score, float, 2);

 

// Update user info

dict_set(user, "age", 29);

dict_set(user, "email", "john.doe@newdomain.com");

dict_set(user, "score", 98.7);

 

// Add new fields

dict_set(user, "city", "Nairobi");

dict_set(user, "verified", 1);

```

 

### Example 2: Configuration Management

 

```pie

// Application configuration

dict config = {

    "app_name": "MyApp",

    "version": "1.0",

    "port": 8080,

    "debug": 1,

    "timeout": 30.5

};

 

// Read configuration

string app_name = dict_get(config, "app_name");

int port = dict_get(config, "port");

int debug = dict_get(config, "debug");

float timeout = dict_get(config, "timeout");

 

output("Starting ", string);

output(app_name, string);

output(" on port ", string);

output(port, int);

 

if (debug == 1) {

    output("Debug mode enabled", string);

}

 

// Update configuration

dict_set(config, "port", 9000);

dict_set(config, "debug", 0);

```

 

### Example 3: Data Processing

 

```pie

// Product inventory

dict product = {

    "id": 101,

    "name": "Laptop",

    "price": 999.99,

    "stock": 50

};

 

// Process order

int stock = dict_get(product, "stock");

if (stock > 0) {

    output("Product available", string);

 

    // Update stock

    int new_stock = stock - 1;

    dict_set(product, "stock", new_stock);

 

    // Calculate total

    float price = dict_get(product, "price");

    float tax = price * 0.16;

    float total = price + tax;

 

    output("Price: ", string);

    output(price, float, 2);

    output("Tax: ", string);

    output(tax, float, 2);

    output("Total: ", string);

    output(total, float, 2);

} else {

    output("Product out of stock", string);

}

```

 

### Example 4: Dynamic Key Access

 

```pie

dict settings = {

    "theme": "dark",

    "language": "en",

    "notifications": 1

};

 

// Dynamic key access

string key = "theme";

string theme = dict_get(settings, key);

output("Current theme: ", string);

output(theme, string);

 

// Update with dynamic key

string new_theme = "light";

dict_set(settings, key, new_theme);

```

 

## Migration Guide

 

### Old Syntax vs New Syntax

 

#### Old Syntax (Still Supported)

 

```pie

// Old way - explicit type functions

dict person = dict_create();

dict_set(person, "name", new_string("John"));

dict_set(person, "age", new_int(30));

 

string name = dict_get_string(person, "name");

int age = dict_get_int(person, "age");

```

 

#### New Syntax (Recommended)

 

```pie

// New way - type inference

dict person = {"name": "John", "age": 30};

 

string name = dict_get(person, "name");

int age = dict_get(person, "age");

```

 

### Benefits of New Syntax

 

1. **Less Verbose**: No need for `new_int()`, `new_string()`, etc.

2. **More Readable**: Clear and intuitive syntax

3. **Type Safe**: Compiler handles type inference

4. **Fewer Errors**: Less boilerplate means fewer mistakes

5. **Familiar**: Similar to JavaScript, Python, and other modern languages

 

### Backward Compatibility

 

The old syntax is still supported for backward compatibility:

- `dict_create()` - Create empty dictionary

- `new_int()`, `new_float()`, `new_string()` - Create typed values

- `dict_get_int()`, `dict_get_float()`, `dict_get_string()` - Type-specific getters

 

However, the new syntax is recommended for all new code.

 

## Best Practices

 

### 1. Use Descriptive Keys

 

```pie

// Good

dict user = {"first_name": "John", "last_name": "Doe"};

 

// Avoid

dict user = {"fn": "John", "ln": "Doe"};

```

 

### 2. Initialize with All Keys

 

```pie

// Good - all keys defined upfront

dict config = {

    "host": "localhost",

    "port": 8080,

    "debug": 0

};

 

// Avoid - adding keys later makes structure unclear

dict config = {};

dict_set(config, "host", "localhost");

dict_set(config, "port", 8080);

```

 

### 3. Check for Missing Keys

 

```pie

dict data = {"name": "John"};

 

// Check if key exists

string email = dict_get(data, "email");

if (string_is_empty(email)) {

    output("Email not provided", string);

}

```

 

### 4. Use Consistent Types

 

```pie

// Good - consistent value types

dict scores = {"math": 95, "science": 87, "english": 92};

 

// Avoid - mixing unrelated types

dict mixed = {"name": "John", "age": 30, "score": 95.5};  // OK but less clear

```

 

## Performance Considerations

 

- **Hash Table**: Dictionaries use hash tables for O(1) average lookup time

- **Memory**: Each dictionary allocates memory for the hash table structure

- **Type Inference**: No runtime overhead - types are resolved at compile time

- **String Keys**: Keys are stored as strings and hashed for fast lookup

 

## Limitations

 

1. **Keys Must Be Strings**: Only string keys are supported

2. **Value Types**: Only int, float, and string values are supported

3. **No Nested Dictionaries**: Dictionaries cannot contain other dictionaries (yet)

4. **No Iteration**: No built-in way to iterate over dictionary keys (yet)

 

## Future Enhancements

 

Planned features for future releases:

- Dictionary iteration (`dict_keys()`, `dict_values()`)

- Nested dictionaries

- Dictionary merging

- Key existence checking (`dict_has_key()`)

- Dictionary size (`dict_size()`)

- Dictionary clearing (`dict_clear()`)

 

## Summary

 

The improved dictionary syntax makes PIE more developer-friendly:

 

✅ **Intuitive syntax** - Similar to modern languages  

✅ **Type inference** - Automatic type detection  

✅ **Less boilerplate** - No explicit type wrappers  

✅ **Type safe** - Compiler-enforced types  

✅ **Backward compatible** - Old syntax still works  

 

This makes PIE an excellent choice for applications that need key-value data structures!

