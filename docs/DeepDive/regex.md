# PIE Regex Quick Reference

 

## Basic Syntax

```pie

// Declare a regex pattern

regex pattern_name = regex_compile("pattern_string");

 

// Match a string against the pattern

int result = regex_match(pattern_name, test_string);

// Returns 1 if match, 0 if no match

```

## Operators

 

| Operator | Description | Example | Matches |

|----------|-------------|---------|---------|

| `a` | Literal | `"a"` | `"a"` |

| `.` | Concatenation | `"a.b"` | `"ab"` |

| `\|` | OR (alternation) | `"a\|b"` | `"a"` or `"b"` |

| `*` | Kleene star (0 or more) | `"a*"` | `""`, `"a"`, `"aa"`, ... |

| `+` | Positive closure (1 or more) | `"a+"` | `"a"`, `"aa"`, `"aaa"`, ... |

| `()` | Grouping | `"(a\|b).c"` | `"ac"` or `"bc"` |

 

## Length Constraints

 

| Constraint | Description | Example | Matches |

|------------|-------------|---------|---------|

| `:n` | Exactly n characters | `"a+:3"` | `"aaa"` only |

| `>n` | More than n characters | `"a+>2"` | `"aaa"`, `"aaaa"`, ... |

| `<n` | Fewer than n characters | `"a+<5"` | `"a"`, `"aa"`, `"aaa"`, `"aaaa"` |

| `>n<m` | Between n and m (exclusive) | `"a+>2<6"` | `"aaa"`, `"aaaa"`, `"aaaaa"` |

 

## Common Patterns

 

### Digits

```pie

regex digit = regex_compile("0|1|2|3|4|5|6|7|8|9");

```

 

### Letters

```pie

regex letter = regex_compile("a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z");

```

 

### Alphanumeric

```pie

regex alnum = regex_compile("(a|b|c|...|z|0|1|2|...|9)+");

```

 

### Email (Simplified)

```pie

regex email = regex_compile("(a|b|c|...|z|0|1|2|...|9)+.@.(a|b|c|...|z)+>8");

```

 

### Phone Number (10 digits)

```pie

regex phone = regex_compile("(0|1|2|3|4|5|6|7|8|9)+:10");

```

 

### Password (8+ characters)

```pie

regex password = regex_compile("(a|b|c|...|z|A|B|C|...|Z|0|1|2|...|9)+>7");

```

 

## Quick Examples

 

### Example 1: Validate Input

```pie

int main() {

    regex pattern = regex_compile("a+");

    string input = "aaa";

 

    if (regex_match(pattern, input) == 1) {

        output("Valid input", string);

    } else {

        output("Invalid input", string);

    }

 

    return 0;

}

```

 

### Example 2: Multiple Patterns

```pie

int main() {

    regex vowel = regex_compile("a|e|i|o|u");

    regex consonant = regex_compile("b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z");

 

    string ch = "a";

 

    if (regex_match(vowel, ch) == 1) {

        output("It's a vowel", string);

    } else if (regex_match(consonant, ch) == 1) {

        output("It's a consonant", string);

    }

 

    return 0;

}

```

 

### Example 3: Length Validation

```pie

int main() {

    regex username = regex_compile("(a|b|c|...|z|0|1|2|...|9)+>2<21");

 

    string user = "john123";

 

    if (regex_match(username, user) == 1) {

        output("Username valid", string);

    } else {

        output("Username must be 3-20 characters", string);

    }

 

    return 0;

}

```

 

## Tips

 

1. **Use parentheses** for grouping: `(a|b).c` not `a|b.c`

2. **Test patterns** with simple strings first

3. **Length constraints** are checked after pattern matching

4. **Exact match only** - pattern must match entire string

5. **Case sensitive** - `a` does not match `A`

 

## Common Mistakes

 

### ❌ Wrong

```pie

regex pattern = regex_compile("a|b.c");  // Matches "a" OR "bc"

```

 

### ✅ Correct

```pie

regex pattern = regex_compile("(a|b).c");  // Matches "ac" OR "bc"

```

 

### ❌ Wrong

```pie

regex pattern = regex_compile("a*:0");  // Contradictory: 0 or more, but exactly 0

```

 

### ✅ Correct

```pie

regex pattern = regex_compile("a*");  // 0 or more 'a's

```

 

## Operator Precedence

 

1. **Parentheses** `()`

2. **Quantifiers** `*`, `+`

3. **Concatenation** `.`

4. **OR** `|`

5. **Length Constraints** `:`, `>`, `<`

 

## See Also

 

- [Full Regex Specification](regex_specification.md)

- [Regex Examples](../test_regex.pie)

- [PIE Documentation](README.md)