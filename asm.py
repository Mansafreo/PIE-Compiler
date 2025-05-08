from ir import Parser, print_ast  # Import Parser and print_ast from ir.py

class IRGenerator:
    def __init__(self):
        self.instructions = []

    def generate(self, node):
        """Generate TAC instructions from the AST."""
        if not node or len(node) == 0:
            return  # Gracefully handle empty or None nodes

        print(f"Processing node: {node}")  # Debugging statement

        if node[0] == 'program':
            # Process the statement list
            for statement in node[1]:
                self.generate(statement)

        elif node[0] == 'declaration':
            # Variable declaration: type IDENTIFIER [= expression]
            if len(node) < 3:
                raise ValueError(f"Invalid declaration node: {node}")
            var_name = node[2]  # Variable name
            if len(node) > 3 and node[3] is not None:
                # If there's an initialization, generate code for it
                init_value = self.generate(node[3])
                self.instructions.append(f"{var_name} = {init_value}")
            else:
                # If no initialization, just declare the variable (optional in TAC)
                self.instructions.append(f"{var_name} = 0")  # Default initialization

        elif node[0] == 'assignment':
            # Assignment: IDENTIFIER = expression
            if len(node) < 3:
                raise ValueError(f"Invalid assignment node: {node}")
            var_name = node[1]
            expr_result = self.generate(node[2])
            self.instructions.append(f"{var_name} = {expr_result}")

        elif node[0] == 'binary_op':
            # Binary operation: left op right
            if len(node) < 4:
                raise ValueError(f"Invalid binary_op node: {node}")
            left = self.generate(node[2])
            right = self.generate(node[3])
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {left} {node[1]} {right}")
            return temp

        elif node[0] == 'if':
            # If statement: if (condition) then_label else_label
            if len(node) < 3:
                raise ValueError(f"Invalid if node: {node}")
            condition = self.generate(node[1])
            then_label = self.new_label()
            else_label = self.new_label()
            end_label = self.new_label()

            self.instructions.append(f"IF {condition} GOTO {then_label}")
            self.instructions.append(f"GOTO {else_label}")
            self.instructions.append(f"LABEL {then_label}")
            self.generate(node[2])  # Then block
            self.instructions.append(f"GOTO {end_label}")
            self.instructions.append(f"LABEL {else_label}")
            if len(node) > 3:
                self.generate(node[3])  # Else block
            self.instructions.append(f"LABEL {end_label}")

        elif node[0] == 'block':
            # Block statement
            for statement in node[1]:
                self.generate(statement)

        elif node[0] == 'primary':
            # Primary value (identifier or literal)
            if len(node) < 2:
                raise ValueError(f"Invalid primary node: {node}")
            return node[1]

        else:
            raise ValueError(f"Unknown AST node type: {node[0]}")

    def new_temp(self):
        """Generate a new temporary variable."""
        temp_name = f"t{len(self.instructions)}"
        return temp_name

    def new_label(self):
        """Generate a new label."""
        label_name = f"L{len(self.instructions)}"
        return label_name

    def get_instructions(self):
        """Return the generated TAC instructions."""
        return self.instructions


class X86AssemblyGenerator:
    def __init__(self):
        self.instructions = []  # List to store x86 assembly instructions
        self.temp_map = {}      # Map TAC temp variables to x86 registers or memory
        self.label_map = {}     # Map TAC labels to x86 labels
        self.registers = ['eax', 'ebx', 'ecx', 'edx']  # Available registers
        self.used_registers = set()

    def allocate_register(self, temp):
        """Allocate a register or memory for a TAC temp variable."""
        if temp in self.temp_map:
            return self.temp_map[temp]
        if len(self.used_registers) < len(self.registers):
            reg = next(r for r in self.registers if r not in self.used_registers)
            self.used_registers.add(reg)
            self.temp_map[temp] = reg
            return reg
        # If no registers are available, spill to memory
        mem = f"[{temp}]"
        self.temp_map[temp] = mem
        return mem

    def free_register(self, temp):
        """Free a register or memory used by a TAC temp variable."""
        if temp in self.temp_map:
            reg = self.temp_map[temp]
            if reg in self.registers:
                self.used_registers.discard(reg)
            del self.temp_map[temp]

    def generate(self, tac_instructions):
        """Generate x86 assembly from TAC instructions."""
        for instr in tac_instructions:
            parts = instr.split()
            if "=" in instr and len(parts) == 5:  # Binary operation: t1 = t2 + t3
                dest = self.allocate_register(parts[0])
                src1 = self.allocate_register(parts[2])
                src2 = self.allocate_register(parts[4])
                op = parts[3]
                if op == "+":
                    self.instructions.append(f"mov {dest}, {src1}")
                    self.instructions.append(f"add {dest}, {src2}")
                elif op == "-":
                    self.instructions.append(f"mov {dest}, {src1}")
                    self.instructions.append(f"sub {dest}, {src2}")
                elif op == "*":
                    self.instructions.append(f"mov {dest}, {src1}")
                    self.instructions.append(f"imul {dest}, {src2}")
                elif op == "/":
                    self.instructions.append(f"mov eax, {src1}")
                    self.instructions.append(f"cdq")  # Sign extend eax into edx:eax
                    self.instructions.append(f"idiv {src2}")
                    self.instructions.append(f"mov {dest}, eax")
                self.free_register(parts[2])
                self.free_register(parts[4])

            elif "=" in instr and len(parts) == 3:  # Assignment: t1 = t2
                dest = self.allocate_register(parts[0])
                src = self.allocate_register(parts[2])
                self.instructions.append(f"mov {dest}, {src}")
                self.free_register(parts[2])

            elif instr.startswith("IF"):  # Conditional jump: IF t1 < t2 GOTO L1
                condition = parts[1]
                src1 = self.allocate_register(parts[2])
                src2 = self.allocate_register(parts[4])
                label = parts[6]
                self.instructions.append(f"cmp {src1}, {src2}")
                if condition == "<":
                    self.instructions.append(f"jl {label}")
                elif condition == "<=":
                    self.instructions.append(f"jle {label}")
                elif condition == ">":
                    self.instructions.append(f"jg {label}")
                elif condition == ">=":
                    self.instructions.append(f"jge {label}")
                elif condition == "==":
                    self.instructions.append(f"je {label}")
                elif condition == "!=":
                    self.instructions.append(f"jne {label}")
                self.free_register(parts[2])
                self.free_register(parts[4])

            elif instr.startswith("LABEL"):  # Label: LABEL L1
                label = parts[1]
                self.instructions.append(f"{label}:")

            elif instr.startswith("GOTO"):  # Unconditional jump: GOTO L1
                label = parts[1]
                self.instructions.append(f"jmp {label}")

            elif instr.startswith("RETURN"):  # Return: RETURN t1
                if len(parts) > 1:
                    src = self.allocate_register(parts[1])
                    self.instructions.append(f"mov eax, {src}")
                    self.free_register(parts[1])
                self.instructions.append("ret")

    def print_instructions(self):
        """Print the generated x86 assembly instructions."""
        for instr in self.instructions:
            print(instr)

    def save_to_file(self, filename):
        """Save the generated x86 assembly instructions to a file."""
        with open(filename, "w") as file:
            for instr in self.instructions:
                file.write(instr + "\n")


def main():
    # Create an instance of the parser
    parser = Parser()

    # Example program
    with open("test3.pie", "r") as file:
        input_program = file.read()

    try:
        # Parse the program to generate the AST
        ast = parser.parse(input_program)
        print("Parsing successful!")
        print("AST:")
        print_ast(ast)

        # Generate IR
        ir_gen = IRGenerator()
        ir_gen.generate(ast)

        # Get TAC instructions
        tac_instructions = ir_gen.get_instructions()

        # Generate x86 assembly
        asm_gen = X86AssemblyGenerator()
        asm_gen.generate(tac_instructions)

        # Print the generated x86 assembly
        print("\nGenerated x86 Assembly:")
        asm_gen.print_instructions()

        # Save the x86 assembly to a file
        output_file = "output.asm"
        asm_gen.save_to_file(output_file)
        print(f"\nThe x86 assembly has been saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()