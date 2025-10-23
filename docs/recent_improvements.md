# Recent Improvements to PIE Compiler

 

This document summarizes the recent improvements made to the PIE compiler, including bug fixes, new features, and enhancements.

 

## Table of Contents

 

1. [Bug Fixes](#bug-fixes)

2. [Dictionary Improvements](#dictionary-improvements)

3. [String Utilities](#string-utilities)

4. [Migration Guide](#migration-guide)

5. [Performance Notes](#performance-notes)

 

---

 

## Bug Fixes

 

### 1. Fixed LLVM Domination Error (String Literals in Conditionals)

 

**Issue**: Compiler failed with "Instruction does not dominate all uses!" when using string literals in output statements within conditional blocks.

 

**Root Cause**: String literal bitcast instructions were being cached and reused across different basic blocks, violating LLVM's domination rules.

 

**Solution**: Modified the code generator to cache global variables instead of bitcast instructions, creating fresh bitcasts for each use.

 

**Impact**: String literals can now be safely used in any control flow structure (if/else, loops, nested conditionals).

 

**Technical Details**: See [technical_notes.md](technical_notes.md) for in-depth explanation.

 

### 2. Fixed llvmlite Deprecation Warning

 

**Issue**: Compiler used deprecated `llvmlite.initialize()` function.

 

**Solution**: Removed the deprecated call as LLVM initialization is now handled automatically.

 

**Impact**: Clean compilation without deprecation warnings.

 

---

 

## Dictionary Improvements

 

### Overview

 

The PIE compiler now features an improved dictionary syntax with automatic type inference, making it much easier and more intuitive to work with key-value data structures.

 

### Before and After

 

#### Old Syntax (Still Supported)

 

```pie

// Old way - verbose and error-prone

dict person = dict_create();

dict_set(person, "name", new_string("John"));

dict_set(person, "age", new_int(30));

 

string name = dict_get_string(person, "name");

int age = dict_get_int(person, "age");

```

 

#### New Syntax (Recommended)

 

```pie

// New way - clean and intuitive

dict person = {"name": "John", "age": 30};

 

string name = dict_get(person, "name");

int age = dict_get(person, "age");

```

 

### Key Features

 

#### 1. Type Inference for dict_get()

 

The compiler automatically determines the return type based on the variable receiving the value:

 

```pie

dict data = {"count": 42, "price": 19.99, "name": "Product"};

 

int count = dict_get(data, "count");      // Returns int

float price = dict_get(data, "price");    // Returns float

string name = dict_get(data, "name");     // Returns string

```

 

**How it works:**

- During semantic analysis, the compiler tracks the expected type

- When visiting `dict_get()`, it uses this context to determine the return type

- During code generation, it calls the appropriate type-specific function

 

#### 2. Type Inference for dict_set()

 

The compiler automatically wraps values in the appropriate DictValue type:

 

```pie

dict person = {"name": "John"};

 

dict_set(person, "age", 30);           // Automatically wraps as int

dict_set(person, "score", 95.5);       // Automatically wraps as float

dict_set(person, "city", "Nairobi");   // Automatically wraps as string

```

 

**How it works:**

- During semantic analysis, the compiler determines the value type

- During code generation, it calls the appropriate wrapper function (`new_int`, `new_float`, `new_string`)

 

#### 3. Default Values for Missing Keys

 

When accessing non-existent keys, the compiler returns safe default values:

 

```pie

dict data = {"name": "John"};

 

int age = dict_get(data, "age");        // Returns 0

float score = dict_get(data, "score");  // Returns 0.0

string email = dict_get(data, "email"); // Returns ""

```

 

### Implementation Architecture

 

#### Semantic Analysis Layer

 

**File**: `src/frontend/semanticAnalysis.py`

 

**Key Changes:**

 

1. **Context Tracking**: Added `expected_type` attribute to track type context

   ```python

   self.expected_type = var_type_name

   expr_type = self.visit(node.initializer)

   self.expected_type = old_expected_type

   ```

 

2. **Special Handling for dict_get**:

   ```python

   if node.name == 'dict_get':

       expected = getattr(self, 'expected_type', None)

       if expected:

           node.inferred_return_type = expected

           return expected

   ```

 

3. **Special Handling for dict_set**:

   ```python

   if node.name == 'dict_set':

       value_type = self.visit(node.args[2])

       node.value_type = value_type

       return 'void'

   ```

 

#### Code Generation Layer

 

**File**: `src/backend/llvm_generator.py`

 

**Key Changes:**

 

1. **Type-Specific dict_get**:

   ```python

   if node.name == 'dict_get':

       inferred_type = getattr(node, 'inferred_return_type', None)

       if inferred_type == 'KEYWORD_INT':

           func = self.module.get_global("dict_get_int")

       elif inferred_type == 'KEYWORD_FLOAT':

           func = self.module.get_global("dict_get_float")

       elif inferred_type == 'KEYWORD_STRING':

           func = self.module.get_global("dict_get_string")

   ```

 

2. **Automatic Value Wrapping for dict_set**:

   ```python

   if node.name == 'dict_set':

       value_type = getattr(node, 'value_type', None)

       if value_type == 'KEYWORD_INT':

           new_int_func = self.module.get_global("new_int")

           dict_value = self.builder.call(new_int_func, [value_val])

   ```

 

### Usage Examples

 

#### Example 1: User Profile Management

 

```pie

int main() {

    dict user = {

        "username": "john_doe",

        "email": "john@example.com",

        "age": 28,

        "score": 95.5

    };

 

    // Read values

    string username = dict_get(user, "username");

    int age = dict_get(user, "age");

    float score = dict_get(user, "score");

 

    // Update values

    dict_set(user, "age", 29);

    dict_set(user, "score", 98.7);

 

    // Add new fields

    dict_set(user, "verified", 1);

 

    return 0;

}

```

 

#### Example 2: Configuration Management

 

```pie

int main() {

    dict config = {

        "app_name": "MyApp",

        "port": 8080,

        "debug": 1,

        "timeout": 30.5

    };

 

    string app_name = dict_get(config, "app_name");

    int port = dict_get(config, "port");

    int debug = dict_get(config, "debug");

 

    if (debug == 1) {

        output("Debug mode enabled", string);

    }

 

    // Update configuration

    dict_set(config, "port", 9000);

    dict_set(config, "debug", 0);

 

    return 0;

}

```

 

#### Example 3: Data Processing

 

```pie

int main() {

    dict product = {

        "id": 101,

        "name": "Laptop",

        "price": 999.99,

        "stock": 50

    };

 

    int stock = dict_get(product, "stock");

    if (stock > 0) {

        // Update stock

        int new_stock = stock - 1;

        dict_set(product, "stock", new_stock);

 

        // Calculate total with tax

        float price = dict_get(product, "price");

        float tax = price * 0.16;

        float total = price + tax;

 

        output("Total: ", string);

        output(total, float, 2);

    }

 

    return 0;

}

```

 

### Best Practices

 

#### 1. Use Local Variables in main()

 

For sequential operations, use local variables within a `main()` function:

 

```pie

// ✅ Good - local variables

int main() {

    dict data = {"value": 10};

    dict_set(data, "value", 20);

    int value = dict_get(data, "value");  // Gets 20

    return 0;

}

 

// ⚠️ Avoid - global variables without main()

dict data = {"value": 10};

dict_set(data, "value", 20);

int value = dict_get(data, "value");  // May get 10 due to initialization order

```

 

#### 2. Initialize Dictionaries with All Keys

 

```pie

// ✅ Good - clear structure

dict config = {

    "host": "localhost",

    "port": 8080,

    "debug": 0

};

 

// ⚠️ Less clear - adding keys later

dict config = {};

dict_set(config, "host", "localhost");

dict_set(config, "port", 8080);

```

 

#### 3. Check for Missing Keys

 

```pie

string email = dict_get(user, "email");

if (string_is_empty(email)) {

    output("Email not provided", string);

}

```

 

#### 4. Use Consistent Types

 

```pie

// ✅ Good - consistent types

dict scores = {"math": 95, "science": 87, "english": 92};

 

// ⚠️ Less clear - mixed unrelated types

dict mixed = {"name": "John", "age": 30, "score": 95.5};

```

 

---

 

## String Utilities

 

### Advanced String Functions

 

The compiler now includes 8 new advanced string manipulation functions:

 

1. **`string_to_upper(str)`** - Convert to uppercase

2. **`string_to_lower(str)`** - Convert to lowercase

3. **`string_trim(str)`** - Remove leading/trailing whitespace

4. **`string_substring(str, start, length)`** - Extract substring

5. **`string_index_of(haystack, needle)`** - Find substring position

6. **`string_replace_char(str, old, new)`** - Replace character

7. **`string_reverse(str)`** - Reverse string

8. **`string_count_char(str, ch)`** - Count character occurrences

 

**Documentation**: See [advanced_string_utilities.md](advanced_string_utilities.md)

 

### Existing String Functions

 

- `strlen(s)` - Get string length

- `strcmp(s1, s2)` - Compare strings

- `strcpy(dest, src)` - Copy string

- `strcat(dest, src)` - Concatenate strings

- `string_contains(haystack, needle)` - Check if contains substring

- `string_starts_with(str, prefix)` - Check if starts with prefix

- `string_ends_with(str, suffix)` - Check if ends with suffix

- `string_is_empty(str)` - Check if string is empty

 

---

 

## Migration Guide

 

### Migrating from Old Dictionary Syntax

 

#### Step 1: Update dict_get calls

 

```pie

// Old

string name = dict_get_string(person, "name");

int age = dict_get_int(person, "age");

float score = dict_get_float(person, "score");

 

// New

string name = dict_get(person, "name");

int age = dict_get(person, "age");

float score = dict_get(person, "score");

```

 

#### Step 2: Update dict_set calls

 

```pie

// Old

dict_set(person, "name", new_string("John"));

dict_set(person, "age", new_int(30));

dict_set(person, "score", new_float(95.5));

 

// New

dict_set(person, "name", "John");

dict_set(person, "age", 30);

dict_set(person, "score", 95.5);

```

 

#### Step 3: Wrap code in main() if needed

 

```pie

// Old (global scope)

dict data = {"value": 10};

dict_set(data, "value", 20);

int value = dict_get(data, "value");

 

// New (with main function)

int main() {

    dict data = {"value": 10};

    dict_set(data, "value", 20);

    int value = dict_get(data, "value");

    return 0;

}

```

 

### Backward Compatibility

 

All old syntax remains supported:

- `dict_create()` - Still works

- `dict_get_int()`, `dict_get_float()`, `dict_get_string()` - Still work

- `new_int()`, `new_float()`, `new_string()` - Still work

 

You can migrate gradually without breaking existing code.

 

---

 

## Performance Notes

 

### Dictionary Operations

 

- **Hash Table**: O(1) average lookup time

- **Type Inference**: No runtime overhead - resolved at compile time

- **Memory**: Each dictionary allocates a hash table structure

 

### String Operations

 

- **All functions**: Implemented in C for optimal performance

- **Time Complexity**: O(n) for most operations where n is string length

- **Memory**: Automatic allocation and cleanup

 

### Compilation

 

- **Type Inference**: Adds minimal compile time

- **Code Generation**: Generates efficient type-specific calls

- **Optimization**: LLVM optimizer handles redundant operations

 

---

 

## Testing

 

### Test Files

 

- `test_dict_improved.pie` - Comprehensive dictionary tests

- `test_dict_local.pie` - Local variable tests

- `test_string_utils.pie` - String utility tests

- `quickfox.pie` - Full language feature tests

 

### Running Tests

 

```bash

# Test improved dictionaries

python3 src/main.py test_dict_improved.pie && ./program

 

# Test string utilities

python3 src/main.py test_string_utils.pie && ./program

 

# Test all features

python3 src/main.py quickfox.pie && ./program

```

 

### Test Results

 

All tests pass successfully:

- ✅ Dictionary type inference

- ✅ Mixed type dictionaries

- ✅ Default values for missing keys

- ✅ String utilities

- ✅ Control flow with string literals

- ✅ Null checking

- ✅ Logical operators

 

---

 

## Future Enhancements

 

### Planned Dictionary Features

 

- Dictionary iteration (`dict_keys()`, `dict_values()`)

- Nested dictionaries

- Dictionary merging

- Dictionary size (`dict_size()`)

- Dictionary clearing (`dict_clear()`)

 

### Planned Regex Features

 

- Basic Kleene syntax support

- NFA-based matching

- Length constraints

- Character classes

- Pattern validation

 

---

 

## Summary

 

The recent improvements to the PIE compiler focus on:

 

1. **Developer Experience**: Simpler, more intuitive syntax

2. **Type Safety**: Compiler-enforced type correctness

3. **Reliability**: Fixed critical bugs in code generation

4. **Functionality**: Added powerful string manipulation tools

5. **Documentation**: Comprehensive guides and examples

 

These improvements make PIE a more productive and enjoyable language for developers while maintaining backward compatibility with existing code.

 

For detailed documentation on specific features:

- [Improved Dictionaries](improved_dictionaries.md)

- [Advanced String Utilities](advanced_string_utilities.md)

- [String Comparisons](string_comparisons.md)

- [Technical Notes](technical_notes.md)

