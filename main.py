#!/opt/pie-compiler/.venv/bin/python3.12
import sys
import os
from parser import Parser, print_ast
from semanticAnalysis import SemanticAnalyzer
from ir_generator import IRGenerator
from llvmConverter import IRToLLVMConverter
import subprocess
def build_and_link(pie_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    runtime_path = os.path.join(script_dir, "runtime.c")
    
    # Get the directory where the .pie file is located
    pie_dir = os.path.dirname(os.path.abspath(pie_file_path))
    
    # Define output paths in the same directory as the .pie file
    output_ll = os.path.join(pie_dir, "output.ll")
    output_bc = os.path.join(pie_dir, "output.bc")
    output_o = os.path.join(pie_dir, "output.o")
    runtime_o = os.path.join(pie_dir, "runtime.o")
    program_exe = os.path.join(pie_dir, "program")
    
    try:
        # Compile the runtime functions to an object file
        subprocess.run(["clang", "-c", runtime_path, "-o", runtime_o], check=True)
        # Convert LLVM IR to bitcode
        subprocess.run(["llvm-as", output_ll, "-o", output_bc], check=True)
        # Generate native object file from bitcode
        subprocess.run(["llc", "-filetype=obj", output_bc, "-o", output_o], check=True)
        # Link everything together to create the executable
        subprocess.run(["clang", output_o, runtime_o, "-o", program_exe], check=True)
        print(f"Build and linking successful! Executable: {program_exe}")
    except subprocess.CalledProcessError as e:
        print(f"Error during build and linking process: {e}")
        raise

def main():
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename.pie>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".pie"):
        print("Error: Input file must have a .pie extension")
        sys.exit(1)
    
    # Create an instance of our parser
    parser = Parser()

    try:
        with open(filename, "r") as file:
            input_program = file.read()

        # Parse the program
        ast = parser.parse(input_program)
        print("Parsing successful!")
        print("AST:")
        print_ast(ast)  # Use prettier printing

        # Perform semantic analysis
        analyzer = SemanticAnalyzer(parser.symbol_table)
        is_valid = analyzer.analyze(ast)
        
        # Print semantic errors/warnings
        if analyzer.errors:
            print("\nSemantic Errors:")
            for error in analyzer.errors:
                print(f"  - {error}")
        
        if analyzer.warnings:
            print("\nSemantic Warnings:")
            for warning in analyzer.warnings:
                print(f"  - {warning}")
        
        if is_valid:
            print("\nProgram is semantically valid!")
            
            # Generate intermediate representation
            ir_gen = IRGenerator()
            ir_code = ir_gen.generate(ast, parser.symbol_table)
            
            print("\nIntermediate Representation (3-Address Code):")
            
            # Get the directory where the .pie file is located
            pie_dir = os.path.dirname(os.path.abspath(filename))
            
            # Save files in the same directory as the .pie file
            ir_output_path = os.path.join(pie_dir, "output.ir")
            llvm_output_path = os.path.join(pie_dir, "output.ll")

            # Save IR code to file in the .pie file directory
            with open(ir_output_path, "w") as ir_file:
                for instruction in ir_code:
                    ir_file.write(f"{instruction}\n")
            
            # Print IR code to console
            for instruction in ir_code:
                print(f"  {instruction}")

            # Translate the IR code to LLVM
            llvm_converter = IRToLLVMConverter()
            llvm_converter.convert_ir(ir_code)
            LLVMCODE = llvm_converter.finalize()

            # Save LLVM code to file in the .pie file directory
            with open(llvm_output_path, "w") as llvm_file:
                llvm_file.write(LLVMCODE)

            # Build and link the program (creates executable in the same directory)
            build_and_link(filename)

        else:
            print("\nProgram contains semantic errors!")
        
        # Print symbol table for demonstration
        print("\nSymbol Table:")
        for scope, symbols in parser.symbol_table.table.items():
            print(f"Scope {scope}:")
            for name, info in symbols.items():
                print(f"  {name}: {info}")
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()