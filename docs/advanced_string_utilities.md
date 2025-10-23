# Advanced String Utilities in PIE

The PIE compiler provides a comprehensive set of advanced string manipulation functions that make text processing easy and efficient.

## Table of Contents

1. [Case Conversion](#case-conversion)
2. [String Trimming](#string-trimming)
3. [Substring Operations](#substring-operations)
4. [String Searching](#string-searching)
5. [Character Operations](#character-operations)
6. [String Reversal](#string-reversal)
7. [Character Counting](#character-counting)
8. [Complete Examples](#complete-examples)

## Case Conversion

### `string_to_upper(str)`
Converts all characters in a string to uppercase.

**Parameters:**
- `str` (string): The string to convert

**Returns:** A new string with all characters in uppercase

**Example:**
```pie
string text = "Hello World";
string upper = string_to_upper(text);
output(upper, string);  // Output: HELLO WORLD
```

### `string_to_lower(str)`
Converts all characters in a string to lowercase.

**Parameters:**
- `str` (string): The string to convert

**Returns:** A new string with all characters in lowercase

**Example:**
```pie
string text = "Hello World";
string lower = string_to_lower(text);
output(lower, string);  // Output: hello world
```

**Use Cases:**
- Case-insensitive comparisons
- Normalizing user input
- Formatting output
- Data processing

## String Trimming

### `string_trim(str)`
Removes leading and trailing whitespace from a string.

**Parameters:**
- `str` (string): The string to trim

**Returns:** A new string with whitespace removed from both ends

**Example:**
```pie
string padded = "   hello world   ";
string trimmed = string_trim(padded);
output(trimmed, string);  // Output: "hello world"
```

**Use Cases:**
- Cleaning user input
- Processing file data
- Removing extra spaces from text
- Data validation

## Substring Operations

### `string_substring(str, start, length)`
Extracts a portion of a string starting at a specific position.

**Parameters:**
- `str` (string): The source string
- `start` (int): Starting position (0-based index)
- `length` (int): Number of characters to extract

**Returns:** A new string containing the extracted substring

**Example:**
```pie
string text = "The quick brown fox";
string sub = string_substring(text, 4, 5);
output(sub, string);  // Output: "quick"

// Extract from position 10 with length 5
string sub2 = string_substring(text, 10, 5);
output(sub2, string);  // Output: "brown"
```

**Use Cases:**
- Parsing structured data
- Extracting specific fields
- Text processing
- String manipulation

## String Searching

### `string_index_of(haystack, needle)`
Finds the first occurrence of a substring within a string.

**Parameters:**
- `haystack` (string): The string to search in
- `needle` (string): The substring to search for

**Returns:** The index of the first occurrence, or -1 if not found

**Example:**
```pie
string text = "The quick brown fox";
int index = string_index_of(text, "quick");
output(index, int);  // Output: 4

int not_found = string_index_of(text, "lazy");
output(not_found, int);  // Output: -1
```

**Use Cases:**
- Finding patterns in text
- Validating string content
- Text parsing
- Search functionality

## Character Operations

### `string_replace_char(str, old_char, new_char)`
Replaces all occurrences of a character with another character.

**Parameters:**
- `str` (string): The source string
- `old_char` (char): The character to replace
- `new_char` (char): The replacement character

**Returns:** A new string with all occurrences replaced

**Example:**
```pie
string text = "hello world";
string replaced = string_replace_char(text, ' ', '_');
output(replaced, string);  // Output: "hello_world"

// Replace vowels
string text2 = "hello";
string replaced2 = string_replace_char(text2, 'e', 'a');
output(replaced2, string);  // Output: "hallo"
```

**Use Cases:**
- Formatting strings
- Character substitution
- Data cleaning
- Text normalization

## String Reversal

### `string_reverse(str)`
Reverses the order of characters in a string.

**Parameters:**
- `str` (string): The string to reverse

**Returns:** A new string with characters in reverse order

**Example:**
```pie
string text = "PIE";
string reversed = string_reverse(text);
output(reversed, string);  // Output: "EIP"

string palindrome = "racecar";
string rev = string_reverse(palindrome);
output(rev, string);  // Output: "racecar"
```

**Use Cases:**
- Palindrome checking
- String manipulation puzzles
- Data transformation
- Text effects

## Character Counting

### `string_count_char(str, ch)`
Counts the number of occurrences of a specific character in a string.

**Parameters:**
- `str` (string): The string to search
- `ch` (char): The character to count

**Returns:** The number of times the character appears

**Example:**
```pie
string text = "hello world";
int count_l = string_count_char(text, 'l');
output(count_l, int);  // Output: 3

int count_o = string_count_char(text, 'o');
output(count_o, int);  // Output: 2
```

**Use Cases:**
- Character frequency analysis
- Validation (e.g., counting special characters)
- Text statistics
- Data analysis

## Complete Examples

### Example 1: Text Normalization
```pie
// Normalize user input
string user_input = "  HELLO WORLD  ";

// Trim whitespace
string trimmed = string_trim(user_input);

// Convert to lowercase
string normalized = string_to_lower(trimmed);

output("Normalized: ", string);
output(normalized, string);  // Output: "hello world"
```

### Example 2: Password Validation
```pie
string password = "MyP@ssw0rd";

// Count special characters
int special_count = string_count_char(password, '@');
special_count = special_count + string_count_char(password, '#');
special_count = special_count + string_count_char(password, '$');

// Check length
int length = strlen(password);

if (length >= 8 && special_count > 0) {
    output("Password is valid", string);
} else {
    output("Password is invalid", string);
}
```

### Example 3: Text Processing
```pie
string text = "The Quick Brown Fox";

// Convert to lowercase
string lower = string_to_lower(text);

// Replace spaces with underscores
string formatted = string_replace_char(lower, ' ', '_');

output("Formatted: ", string);
output(formatted, string);  // Output: "the_quick_brown_fox"
```

### Example 4: String Analysis
```pie
string sentence = "Hello World";

// Count specific characters
int space_count = string_count_char(sentence, ' ');
int l_count = string_count_char(sentence, 'l');

output("Spaces: ", string);
output(space_count, int);  // Output: 1

output("Letter 'l': ", string);
output(l_count, int);  // Output: 3

// Find substring
int index = string_index_of(sentence, "World");
output("Index of 'World': ", string);
output(index, int);  // Output: 6
```

### Example 5: Data Extraction
```pie
string data = "Name:John,Age:30,City:NYC";

// Find positions
int name_start = string_index_of(data, "Name:") + 5;
int age_start = string_index_of(data, "Age:") + 4;

// Extract name (assuming fixed format)
string name = string_substring(data, name_start, 4);
output("Name: ", string);
output(name, string);  // Output: "John"
```

### Example 6: Palindrome Checker
```pie
string word = "racecar";
string reversed = string_reverse(word);

int cmp = strcmp(word, reversed);
if (cmp == 0) {
    output("It's a palindrome!", string);
} else {
    output("Not a palindrome", string);
}
```

## Memory Management

All string utility functions that return strings allocate new memory for the result. The PIE runtime handles memory management automatically, but be aware that:

- Each function call creates a new string
- Original strings are not modified
- Memory is managed by the runtime

## Performance Considerations

- **Case conversion**: O(n) where n is string length
- **Trimming**: O(n) where n is string length
- **Substring**: O(m) where m is the substring length
- **Index search**: O(n*m) where n is haystack length, m is needle length
- **Character replacement**: O(n) where n is string length
- **Reversal**: O(n) where n is string length
- **Character counting**: O(n) where n is string length

## Best Practices

### 1. Chain Operations Efficiently
```pie
// Good: Chain operations
string text = "  HELLO WORLD  ";
string result = string_to_lower(string_trim(text));

// Avoid: Unnecessary intermediate variables
string temp1 = string_trim(text);
string temp2 = string_to_lower(temp1);
```

### 2. Validate Input
```pie
string input = "user input";

// Check if string is empty before processing
int is_empty = string_is_empty(input);
if (is_empty == 0) {
    string processed = string_trim(input);
    // Process the string
}
```

### 3. Use Appropriate Functions
```pie
// Good: Use string_index_of for searching
int pos = string_index_of(text, "pattern");
if (pos != -1) {
    // Pattern found
}

// Good: Use string_contains for existence check
int exists = string_contains(text, "pattern");
if (exists == 1) {
    // Pattern exists
}
```

### 4. Handle Edge Cases
```pie
string text = "short";
int start = 10;
int length = 5;

// string_substring handles out-of-bounds gracefully
string sub = string_substring(text, start, length);
// Returns empty string if start is beyond string length
```

## Summary

The advanced string utilities in PIE provide:

✅ **Comprehensive text manipulation** - Case conversion, trimming, substring extraction  
✅ **Powerful search capabilities** - Find substrings and character positions  
✅ **Character-level operations** - Replace, count, and analyze characters  
✅ **Efficient implementations** - Optimized C implementations for performance  
✅ **Safe memory handling** - Automatic memory management  
✅ **Edge case handling** - Graceful handling of invalid inputs  

These utilities make PIE an excellent choice for text processing, data parsing, and string manipulation tasks.
