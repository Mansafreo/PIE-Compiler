# PIE Language Documentation

Complete documentation for the PIE programming language.

## Documentation Structure

### 📚 Core Documentation

1. **[Language Reference](language-reference.md)**
   - Complete syntax guide
   - Data types and variables
   - Operators and expressions
   - Control flow statements
   - Functions and scope
   - Comments and conventions

2. **[Standard Library](standard-library.md)**
   - Input/Output functions
   - Math library (28 functions)
   - String functions (18 functions)
   - Array functions (6 functions)
   - Dictionary functions (5 functions)
   - Regular expression functions
   - File I/O functions
   - Network functions
   - Time functions
   - System functions

3. **[Examples & Tutorials](examples.md)**
   - Getting started
   - Basic programs
   - Control flow examples
   - Functions and recursion
   - Array operations
   - String processing
   - Dictionary usage
   - File I/O examples
   - Complete sample programs

4. **[Advanced Features](advanced-features.md)**
   - Dynamic arrays in-depth
   - Dictionary type inference
   - Regular expressions with Kleene syntax
   - File I/O best practices
   - Network programming
   - Memory management
   - Performance tips

5. **[Quick Reference](quick-reference.md)**
   - Syntax cheat sheet
   - Quick lookup for common operations
   - One-page reference guide

## Getting Started

### New to PIE?

1. Start with the main [README](../README.md) for installation and setup
2. Read the [Language Reference](language-reference.md) to understand the syntax
3. Work through [Examples & Tutorials](examples.md) to learn by doing
4. Explore [Advanced Features](advanced-features.md) for complex topics

### Quick Lookup

- Need a function? → [Standard Library](standard-library.md)
- Forgot syntax? → [Quick Reference](quick-reference.md)
- Want examples? → [Examples & Tutorials](examples.md)

## Language Features

### ✅ Supported Features

- ✅ Static typing with compile-time type checking
- ✅ C-like syntax (familiar to C/C++/Java developers)
- ✅ Functions with recursion support
- ✅ Static and dynamic arrays
- ✅ Hash map dictionaries with automatic type inference
- ✅ Regular expressions with Kleene syntax
- ✅ File I/O operations
- ✅ TCP network sockets
- ✅ Comprehensive math library
- ✅ Rich string manipulation functions
- ✅ Increment/decrement operators (`++`, `--`)
- ✅ Multiple loop types (for, while, do-while)
- ✅ Switch-case statements
- ✅ Comments (single-line and multi-line)

### 📊 Standard Library Statistics

- **Total Functions:** 75+
- **Math Functions:** 28
- **String Functions:** 18
- **Array Functions:** 6
- **Dictionary Functions:** 5
- **File I/O:** 5
- **Network:** 5
- **Time:** 2
- **System:** 2
- **Regex:** 3

## Documentation Conventions

### Code Examples

All code examples are complete and runnable unless otherwise noted:

```pie
// This is a complete example
int x = 10;
output(x, int);
```

### Function Signatures

Functions are documented with their full signatures:

```pie
float sqrt(float x);  // Returns square root of x
```

### Return Values

- `1` / `0` - Boolean true/false (for functions returning int as boolean)
- `-1` - Common error indicator
- `null` - Null pointer/uninitialized value

## Version Information

This documentation corresponds to PIE Compiler V1 (Python implementation).

**Compiler:**
- LLVM-based code generation
- Python 3.x frontend
- C runtime library

**Dependencies:**
- Python 3.7+
- llvmlite 0.45.1+
- ply 3.11+
- LLVM tools (llc, clang)

## Contributing to Documentation

Found an error or want to improve the documentation?

1. Check existing examples for style consistency
2. Test all code examples before submitting
3. Use clear, concise language
4. Include practical examples where possible

## Additional Resources

- **[CHANGELOG.md](../CHANGELOG.md)** - Version history and updates
- **[README.md](../README.md)** - Project overview and quick start

## Community and Support

For questions, issues, or contributions:

- GitHub Repository: PIE-Compiler-V1-Python
- Issues: Report bugs or request features
- Discussions: Ask questions and share projects

---

**Last Updated:** October 2024  
**Documentation Version:** 1.0

Happy coding with PIE! 🥧
