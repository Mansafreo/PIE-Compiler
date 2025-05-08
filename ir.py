from parser import Parser, print_ast  # Import the Parser and print_ast function

class IRGenerator:
    def __init__(self):
        self.instructions = []  # List to store TAC instructions
        self.temp_count = 0     # Counter for temporary variables
        self.label_count = 0    # Counter for labels

    def new_temp(self):
        """Generate a new temporary variable."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        """Generate a new label."""
        self.label_count += 1
        return f"L{self.label_count}"

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

    def print_instructions(self):
        """Print the generated TAC instructions."""
        for instr in self.instructions:
            print(instr)

    def get_instructions(self):
        """Return the generated TAC instructions."""
        return self.instructions

# Main function to integrate parsing and IR generation
def main():
    # Create an instance of the parser
    parser = Parser()

    # Example program
    with open("test2.pie", "r") as file:
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

        # Print the generated TAC
        print("\nThree-Address Code (TAC):")
        ir_gen.print_instructions()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
