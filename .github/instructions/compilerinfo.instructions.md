---
applyTo: '**'
---
This folder contains a custom compiler for a programming language called PIE. The compiler is in python and uses libraries like LLVMLITE to produce LLVM IR that can then be coverted to machine code along with the pre-compiled runtime C files that contain implementations for various inbuilt functions and utilities. The code must run in the python venv that has the dependencies installed. The language files have a .pie extension. The syntax does not require the entry point of the program to be named main, any function can be called to start execution. The runtime files are in the runtime folder. The compiler is invoked from the command line as follows:

```bash
python3 ./src/main.py <source_file.pie> 
```
The compiler prodeces the AST, performs semantic analysis and then generates LLVM IR code which is saved in a .ll file. This file is then be compiled to an executable which can be run to see the output of the program. The program can be run as follows:

```bash
./program
```

The compiler is in the src folder. The main files of interest are:
- main.py : The entry point for the compiler
- lexer.py : The lexer that tokenizes the source code
- parser.py : The parser that generates the AST
- semantic_analyzer.py : Performs semantic analysis on the AST
- llvm_generator.py : Generates LLVM IR from the AST

The runtime folder contains C files that implement various inbuilt functions and utilities that the PIE language provides. These files are compiled along with the generated LLVM IR to produce the final executable.