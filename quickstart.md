# PIE Compiler - Quick Start Guide

 

Get started with the latest PIE compiler features in 5 minutes!

 

## Installation

 

```bash

# Install dependencies

pip install ply llvmlite

 

# Clone the repository

git clone https://github.com/Pie-Compiler/PIE-Compiler-V1-Python.git

cd PIE-Compiler-V1-Python

```

 

## Your First PIE Program

 

Create a file called `hello.pie`:

 

```pie

int main() {

    output("Hello, PIE!", string);

    return 0;

}

```

 

Compile and run:

 

```bash

python3 src/main.py hello.pie

./program

```

 

## New Feature: Improved Dictionaries

 

### Basic Usage

 

```pie

int main() {

    // Create a dictionary

    dict person = {"name": "Alice", "age": 25, "city": "NYC"};

 

    // Get values (type is automatically inferred!)

    string name = dict_get(person, "name");

    int age = dict_get(person, "age");

 

    output("Name: ", string);

    output(name, string);

    output("Age: ", string);

    output(age, int);

 

    return 0;

}

```

 

### Update Values

 

```pie

int main() {

    dict user = {"score": 100, "level": 1};

 

    // Update existing values

    dict_set(user, "score", 150);

    dict_set(user, "level", 2);

 

    // Add new values

    dict_set(user, "coins", 500);

 

    int score = dict_get(user, "score");

    output("Score: ", string);

    output(score, int);

 

    return 0;

}

```

 

### Mixed Types

 

```pie

int main() {

    dict config = {

        "app_name": "MyApp",

        "port": 8080,

        "debug": 1,

        "timeout": 30.5

    };

 

    string app = dict_get(config, "app_name");

    int port = dict_get(config, "port");

    int debug = dict_get(config, "debug");

 

    if (debug == 1) {

        output("Debug mode ON", string);

    }

 

    return 0;

}

```

 

## New Feature: String Utilities

 

### Case Conversion

 

```pie

int main() {

    string text = "Hello World";

 

    string upper = string_to_upper(text);

    string lower = string_to_lower(text);

 

    output(upper, string);  // HELLO WORLD

    output(lower, string);  // hello world

 

    return 0;

}

```

 

### String Manipulation

 

```pie

int main() {

    string text = "  Hello World  ";

 

    // Trim whitespace

    string trimmed = string_trim(text);

    output(trimmed, string);  // "Hello World"

 

    // Extract substring

    string sub = string_substring(trimmed, 0, 5);

    output(sub, string);  // "Hello"

 

    // Reverse string

    string reversed = string_reverse("PIE");

    output(reversed, string);  // "EIP"

 

    return 0;

}

```

 

### String Searching

 

```pie

int main() {

    string text = "The quick brown fox";

 

    // Find substring

    int index = string_index_of(text, "quick");

    output("Found at: ", string);

    output(index, int);  // 4

 

    // Count characters

    int count = string_count_char(text, 'o');

    output("Count of 'o': ", string);

    output(count, int);  // 2

 

    return 0;

}

```

 

### Character Operations

 

```pie

int main() {

    string filename = "my file.txt";

 

    // Replace spaces with underscores

    string safe = string_replace_char(filename, ' ', '_');

    output(safe, string);  // "my_file.txt"

 

    return 0;

}

```

 

## Complete Example: User Management

 

```pie

int main() {

    // Create user profile

    dict user = {

        "username": "alice",

        "email": "alice@example.com",

        "age": 25,

        "score": 0

    };

 

    // Display welcome message

    string username = dict_get(user, "username");

    string upper_name = string_to_upper(username);

 

    output("Welcome, ", string);

    output(upper_name, string);

    output("!", string);

 

    // Update user data

    dict_set(user, "score", 100);

    dict_set(user, "level", 1);

 

    // Display stats

    int score = dict_get(user, "score");

    int level = dict_get(user, "level");

 

    output("Score: ", string);

    output(score, int);

    output("Level: ", string);

    output(level, int);

 

    // Process email

    string email = dict_get(user, "email");

    int at_pos = string_index_of(email, "@");

 

    if (at_pos > 0) {

        string domain = string_substring(email, at_pos + 1, 20);

        output("Email domain: ", string);

        output(domain, string);

    }

 

    return 0;

}

```

 

## Tips and Best Practices

 

### 1. Always Use main() Function

 

```pie

// ✅ Good

int main() {

    dict data = {"value": 10};

    dict_set(data, "value", 20);

    int value = dict_get(data, "value");

    return 0;

}

 

// ⚠️ Avoid (global scope has initialization order issues)

dict data = {"value": 10};

dict_set(data, "value", 20);

int value = dict_get(data, "value");

```

 

### 2. Check for Missing Keys

 

```pie

int main() {

    dict data = {"name": "John"};

 

    string email = dict_get(data, "email");

    if (string_is_empty(email)) {

        output("Email not found", string);

    }

 

    return 0;

}

```

 

### 3. Use Descriptive Keys

 

```pie

// ✅ Good

dict user = {"first_name": "John", "last_name": "Doe"};

 

// ⚠️ Avoid

dict user = {"fn": "John", "ln": "Doe"};

```

 

### 4. Initialize Dictionaries with All Keys

 

```pie

// ✅ Good - clear structure

dict config = {

    "host": "localhost",

    "port": 8080,

    "debug": 0

};

 

// ⚠️ Less clear

dict config = {};

dict_set(config, "host", "localhost");

dict_set(config, "port", 8080);

```

 

## Common Patterns

 

### Configuration Management

 

```pie

int main() {

    dict config = {

        "app_name": "MyApp",

        "version": "1.0",

        "port": 8080,

        "debug": 1

    };

 

    string app = dict_get(config, "app_name");

    string version = dict_get(config, "version");

    int port = dict_get(config, "port");

 

    output(app, string);

    output(" v", string);

    output(version, string);

    output(" running on port ", string);

    output(port, int);

 

    return 0;

}

```

 

### Data Validation

 

```pie

int main() {

    string username = "john_doe";

    string password = "secret123";

 

    // Validate username length

    if (username < 3 || username > 20) {

        output("Username must be 3-20 characters", string);

        return 1;

    }

 

    // Validate password

    if (password < 8) {

        output("Password too short", string);

        return 1;

    }

 

    // Check for special characters

    int has_underscore = string_count_char(username, '_');

    if (has_underscore > 0) {

        output("Username contains underscore", string);

    }

 

    output("Validation passed!", string);

    return 0;

}

```

 

### Text Processing

 

```pie

int main() {

    string input = "  Hello World  ";

 

    // Clean and normalize

    string cleaned = string_trim(input);

    string lower = string_to_lower(cleaned);

    string safe = string_replace_char(lower, ' ', '_');

 

    output("Processed: ", string);

    output(safe, string);  // "hello_world"

 

    return 0;

}

```

 

## Running Tests

 

```bash

# Test improved dictionaries

python3 src/main.py test_dict_improved.pie && ./program

 

# Test string utilities

python3 src/main.py test_string_utils.pie && ./program

 

# Test all features

python3 src/main.py quickfox.pie && ./program

```

 

## Documentation

 

- **[Complete Documentation](docs/README.md)** - Full language reference

- **[Improved Dictionaries](docs/improved_dictionaries.md)** - Dictionary guide

- **[String Utilities](docs/advanced_string_utilities.md)** - String functions

- **[Recent Improvements](docs/recent_improvements.md)** - What's new

 

## Getting Help

 

- Check the [documentation](docs/)

- Look at [example programs](testFiles/)

- Read the [CHANGELOG](CHANGELOG.md)

- Review [technical notes](docs/technical_notes.md)

 

## Next Steps

 

1. Try the examples above

2. Read the [improved dictionaries guide](docs/improved_dictionaries.md)

3. Explore [string utilities](docs/advanced_string_utilities.md)

4. Build your own PIE programs!

 

---

 

**Happy Coding with PIE! 🥧**