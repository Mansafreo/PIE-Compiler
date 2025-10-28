# Parser using PLY (Python Lex-Yacc)
from ply import yacc
from frontend.lexer import Lexer, build_master_nfa, nfa_to_dfa, epsilon_closure
from ply.lex import LexToken  # Import LexToken from the correct module
from frontend.plyAdapter import PLYLexerAdapter  # Import the adapter for PLY
from frontend.symbol_table import SymbolTable  # Import the symbol table class
from frontend.ast import * # Import all the AST node classes
from frontend.types import canonicalize

# Parser class that integrates with our lexer
class Parser:
    def __init__(self):
        self.tokens = [
            'IDENTIFIER', 'INT_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL', 'CHAR_LITERAL',
            'KEYWORD_IF', 'KEYWORD_ELSE', 'KEYWORD_FOR', 'KEYWORD_WHILE', 'KEYWORD_DO',
            'KEYWORD_RETURN', 'KEYWORD_BREAK', 'KEYWORD_CONTINUE', 'KEYWORD_SWITCH', 'KEYWORD_CASE', 'KEYWORD_DEFAULT',
            'KEYWORD_INT', 'KEYWORD_FLOAT', 'KEYWORD_CHAR', 'KEYWORD_VOID', 'KEYWORD_FILE', 'KEYWORD_SOCKET', 'KEYWORD_DICT','KEYWORD_REGEX',
            'KEYWORD_STRING', 'KEYWORD_BOOL', 'KEYWORD_TRUE', 'KEYWORD_FALSE', 'KEYWORD_NULL', 'KEYWORD_EXIT', 'KEYWORD_ARRAY',
            'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
            'SEMICOLON', 'COMMA', 'DOT', 'COLON',
            'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD',
            'GT', 'LT', 'GEQ', 'LEQ', 'EQ', 'NEQ', 'AND', 'OR', 'ASSIGN',
            'SYSTEM_INPUT', 'SYSTEM_OUTPUT', 'SYSTEM_EXIT', 'SYSTEM_SLEEP', 'COMMENT',
            'SYSTEM_ARR_PUSH', 'SYSTEM_ARR_POP', 'SYSTEM_ARR_SIZE', 'SYSTEM_ARR_CONTAINS', 'SYSTEM_ARR_INDEXOF', 'SYSTEM_ARR_AVG'
        ]
        
        self.precedence = (
            ('left', 'OR'),
            ('left', 'AND'),
            ('left', 'EQ', 'NEQ'),
            ('left', 'GT', 'LT', 'GEQ', 'LEQ'),
            ('left', 'PLUS', 'MINUS'),
            ('left', 'MUL', 'DIV', 'MOD'),
            ('right', 'UMINUS'),  # Unary minus operator
            ('nonassoc', 'LOWER_THAN_ELSE'),  # To handle the dangling else
            ('nonassoc', 'KEYWORD_ELSE')
        )
        
        self.symbol_table = SymbolTable()
        self.prepopulate_symbol_table()
        self.lexer_instance = None
        self.parser = yacc.yacc(module=self)
        
    def prepopulate_symbol_table(self):
        math_functions = {
            "sqrt": {"return_type": "float", "params": [("float", "x")]},
            "pow": {"return_type": "float", "params": [("float", "base"), ("float", "exp")]},
            "sin": {"return_type": "float", "params": [("float", "x")]},
            "cos": {"return_type": "float", "params": [("float", "x")]},
            "tan": {"return_type": "float", "params": [("float", "x")]},
            "asin": {"return_type": "float", "params": [("float", "x")]},
            "acos": {"return_type": "float", "params": [("float", "x")]},
            "atan": {"return_type": "float", "params": [("float", "x")]},
            "log": {"return_type": "float", "params": [("float", "x")]},
            "log10": {"return_type": "float", "params": [("float", "x")]},
            "exp": {"return_type": "float", "params": [("float", "x")]},
            "floor": {"return_type": "float", "params": [("float", "x")]},
            "ceil": {"return_type": "float", "params": [("float", "x")]},
            "round": {"return_type": "float", "params": [("float", "x")]},
            "abs": {"return_type": "float", "params": [("float", "x")]},
            "abs_int": {"return_type": "int", "params": [("int", "x")]},
            "min": {"return_type": "float", "params": [("float", "a"), ("float", "b")]},
            "max": {"return_type": "float", "params": [("float", "a"), ("float", "b")]},
            "min_int": {"return_type": "int", "params": [("int", "a"), ("int", "b")]},
            "max_int": {"return_type": "int", "params": [("int", "a"), ("int", "b")]},
            "rand": {"return_type": "int", "params": []},
            "srand": {"return_type": "void", "params": [("int", "seed")]},
            "rand_range": {"return_type": "int", "params": [("int", "min"), ("int", "max")]},
            "pi": {"return_type": "float", "params": []},
            "e": {"return_type": "float", "params": []},
            "time": {"return_type": "int", "params": []},
        }
        for name, info in math_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        time_functions = {
            "time_now": {"return_type": "int", "params": []},
            "time_to_local": {"return_type": "string", "params": [("int", "timestamp")]},
        }
        for name, info in time_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        string_functions = {
            "strlen": {"return_type": "int", "params": [("string", "s")]},
            "strcmp": {"return_type": "int", "params": [("string", "s1"), ("string", "s2")]},
            "strcpy": {"return_type": "string", "params": [("string", "dest"), ("string", "src")]},
            "strcat": {"return_type": "string", "params": [("string", "dest"), ("string", "src")]},
            "concat_strings": {"return_type": "string", "params": [("string", "s1"), ("string", "s2")]},
            # Advanced string utilities
            "string_to_upper": {"return_type": "string", "params": [("string", "str")]},
            "string_to_lower": {"return_type": "string", "params": [("string", "str")]},
            "string_trim": {"return_type": "string", "params": [("string", "str")]},
            "string_substring": {"return_type": "string", "params": [("string", "str"), ("int", "start"), ("int", "length")]},
            "string_index_of": {"return_type": "int", "params": [("string", "haystack"), ("string", "needle")]},
            "string_replace_char": {"return_type": "string", "params": [("string", "str"), ("char", "old_char"), ("char", "new_char")]},
            "string_reverse": {"return_type": "string", "params": [("string", "str")]},
            "string_count_char": {"return_type": "int", "params": [("string", "str"), ("char", "ch")]},
        }
        for name, info in string_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        # I/O Functions
        io_functions = {
            "output_int": {"return_type": "void", "params": [("int", "value")]},
            "output_float": {"return_type": "void", "params": [("float", "value"), ("int", "precision")]},
            "output_string": {"return_type": "void", "params": [("string", "s")]},
            "output_char": {"return_type": "void", "params": [("char", "c")]},
            "input_int": {"return_type": "void", "params": [("int*", "value")]},
            "input_float": {"return_type": "void", "params": [("float*", "value")]},
            "input_string": {"return_type": "void", "params": [("string*", "s")]},
            "input_char": {"return_type": "void", "params": [("char*", "c")]},
        }
        for name, info in io_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        dict_functions = {
            "dict_create": {"return_type": "dict", "params": []},
            "dict_set": {"return_type": "void", "params": [("dict", "d"), ("string", "key"), ("void*", "value")]},
            "dict_get": {"return_type": "void*", "params": [("dict", "d"), ("string", "key")]},
            "dict_get_int": {"return_type": "int", "params": [("dict", "d"), ("string", "key")]},
            "dict_get_float": {"return_type": "float", "params": [("dict", "d"), ("string", "key")]},
            "dict_get_string": {"return_type": "string", "params": [("dict", "d"), ("string", "key")]},
            "dict_has_key": {"return_type": "int", "params": [("dict", "d"), ("string", "key")]},  # Check if key exists
            "dict_key_exists": {"return_type": "int", "params": [("dict", "d"), ("string", "key")]},  # PIE wrapper for key existence
            "dict_delete": {"return_type": "void", "params": [("dict", "d"), ("string", "key")]},
            "new_int": {"return_type": "void*", "params": [("int", "value")]},
            "new_float": {"return_type": "void*", "params": [("float", "value")]},
            "new_string": {"return_type": "void*", "params": [("string", "value")]},
            "is_variable_defined": {"return_type": "int", "params": [("void*", "variable")]},  # Check if variable is defined
            "is_variable_null": {"return_type": "int", "params": [("void*", "variable")]},  # Check if variable is null
            "string_contains": {"return_type": "int", "params": [("string", "haystack"), ("string", "needle")]},  # Check if string contains substring
            "string_starts_with": {"return_type": "int", "params": [("string", "str"), ("string", "prefix")]},  # Check if string starts with prefix
            "string_ends_with": {"return_type": "int", "params": [("string", "str"), ("string", "suffix")]},  # Check if string ends with suffix
            "string_is_empty": {"return_type": "int", "params": [("string", "str")]},  # Check if string is empty
        }
        for name, info in dict_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )
        # Regex functions

        regex_functions = {

            "regex_compile": {"return_type": "regex", "params": [("string", "pattern")]},

            "regex_match": {"return_type": "int", "params": [("regex", "pattern"), ("string", "str")]},

            "regex_free": {"return_type": "void", "params": [("regex", "pattern")]},

        }

        for name, info in regex_functions.items():

            param_types = [p[0] for p in info['params']]

            self.symbol_table.add_symbol(

                name,

                'function',

                return_type=info['return_type'],

                param_types=param_types,

                params=info['params']

            )

 

        d_array_string_functions = {
            "d_array_string_create": {"return_type": "d_array_string", "params": []},
            "d_array_string_append": {"return_type": "void", "params": [("d_array_string", "arr"), ("string", "value")]},
            "d_array_string_get": {"return_type": "string", "params": [("d_array_string", "arr"), ("int", "index")]},
            "d_array_string_set": {"return_type": "void", "params": [("d_array_string", "arr"), ("int", "index"), ("string", "value")]},
            "d_array_string_size": {"return_type": "int", "params": [("d_array_string", "arr")]},
            "d_array_string_free": {"return_type": "void", "params": [("d_array_string", "arr")]},
        }
        for name, info in d_array_string_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        d_array_functions = {
            "d_array_int_create": {"return_type": "d_array_int", "params": []},
            "d_array_int_append": {"return_type": "void", "params": [("d_array_int", "arr"), ("int", "value")]},
            "d_array_int_get": {"return_type": "int", "params": [("d_array_int", "arr"), ("int", "index")]},
            "d_array_int_set": {"return_type": "void", "params": [("d_array_int", "arr"), ("int", "index"), ("int", "value")]},
            "d_array_int_size": {"return_type": "int", "params": [("d_array_int", "arr")]},
            "d_array_int_free": {"return_type": "void", "params": [("d_array_int", "arr")]},
        }
        for name, info in d_array_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )
        net_functions = {
            "tcp_socket": {"return_type": "socket", "params": []},
            "tcp_connect": {"return_type": "int", "params": [("socket", "sockfd"), ("string", "host"), ("int", "port")]},
            "tcp_send": {"return_type": "int", "params": [("socket", "sockfd"), ("string", "data")]},
            "tcp_recv": {"return_type": "int", "params": [("socket", "sockfd"), ("string", "buffer"), ("int", "size")]},
            "tcp_close": {"return_type": "void", "params": [("socket", "sockfd")]},
        }
        for name, info in net_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

        file_functions = {
            "file_open": {"return_type": "file", "params": [("string", "filename"), ("string", "mode")]},
            "file_close": {"return_type": "void", "params": [("file", "file_handle")]},
            "file_write": {"return_type": "void", "params": [("file", "file_handle"), ("string", "content")]},
            "file_flush": {"return_type": "void", "params": [("file", "file_handle")]},
            "file_read": {"return_type": "void", "params": [("file", "file_handle"), ("string", "buffer"), ("int", "size")]},
            "file_read_all": {"return_type": "string", "params": [("file", "file_handle")]},
            "file_read_lines": {"return_type": "d_array_string", "params": [("file", "file_handle")]},
        }
        for name, info in file_functions.items():
            param_types = [p[0] for p in info['params']]
            self.symbol_table.add_symbol(
                name,
                'function',
                return_type=info['return_type'],
                param_types=param_types,
                params=info['params']
            )

    def setup_lexer(self):
        """Create and configure the lexer instance."""
        nfa_start = build_master_nfa()
        dfa_transitions, dfa_token = nfa_to_dfa(nfa_start)
        start_set = frozenset(epsilon_closure({nfa_start}))
        lexer = Lexer(dfa_transitions, dfa_token, start_set)
        lexer.symbol_table = self.symbol_table  # Pass symbol table
        return lexer
        
    def tokenize_input(self, input_text):
        """Tokenize the input text using our lexer."""
        if not self.lexer_instance:
            self.lexer_instance = self.setup_lexer()
        
        token_list = self.lexer_instance.tokenize(input_text)
        
        # Convert our lexer's token format to PLY's format
        ply_tokens = []
        for token_type, token_text in token_list:
            token = LexToken()  # Use LexToken from ply.lex
            token.type = token_type
            token.value = token_text
            token.lineno = 0  # You might want to track line numbers in your lexer
            token.lexpos = 0  # And character positions
            ply_tokens.append(token)
            
        return ply_tokens
    
    def parse(self, input_text):
        if not self.lexer_instance:
            self.lexer_instance = self.setup_lexer()
        
        # Get tokens from your custom lexer
        token_list = self.lexer_instance.tokenize(input_text)
        
        # Debug: Print tokens before conversion
        print("Raw tokens from lexer:")
        for token in token_list:
            print(f"  {token}")
        
        # Convert to PLY tokens
        ply_tokens = []
        for token in token_list:
            # Check if we're getting 2-tuples or 3-tuples
            if len(token) == 2:
                token_type, token_text = token
                line_num = 1  # Default line number
            else:
                token_type, token_text, line_num = token
                
            if token_type == "COMMENT":
                continue  # Skip comments
            
            # Create a token object
            tok = LexToken()
            tok.type = token_type
            tok.value = token_text
            tok.lineno = line_num
            tok.lexpos = 0
            ply_tokens.append(tok)
        
        # Create adapter
        lexer_adapter = PLYLexerAdapter(ply_tokens)
        
        # Parse with the adapter
        return self.parser.parse(lexer=lexer_adapter)
    
    # Grammar rules defined below
    
    def p_program(self, p):
        '''program : statement_list'''
        p[0] = Program(p[1])

    def p_function_definition(self, p):
        '''function_definition : type_specifier IDENTIFIER LPAREN params RPAREN block_statement'''
        function_name = p[2]
        return_type = p[1]
        params = p[4]
        body = p[6]
        p[0] = FunctionDefinition(return_type, function_name, params, body)

    def p_params(self, p):
        '''params : param_list
                  | empty'''
        if p[1] is None:
            p[0] = []
        else:
            p[0] = p[1]

    def p_param_list(self, p):
        '''param_list : param
                      | param_list COMMA param'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_param(self, p):
        '''param : type_specifier IDENTIFIER'''
        p[0] = Parameter(p[1], p[2])
    
    def p_statement_list(self, p):
        '''statement_list : statement
                         | statement_list statement'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]
    
    def p_statement(self, p):
        '''statement : declaration_statement
                    | assignment_statement
                    | if_statement
                    | while_statement
                    | do_while_statement
                    | for_statement
                    | switch_statement
                    | break_statement
                    | return_statement
                    | function_call_statement
                    | block_statement
                    | function_definition'''
        p[0] = p[1]

    def p_do_while_statement(self, p):
        '''do_while_statement : KEYWORD_DO statement KEYWORD_WHILE LPAREN expression RPAREN SEMICOLON'''
        p[0] = DoWhileStatement(p[2], p[5])

    def p_switch_statement(self, p):
        '''switch_statement : KEYWORD_SWITCH LPAREN expression RPAREN LBRACE case_list RBRACE'''
        p[0] = SwitchStatement(p[3], p[6])

    def p_case_list(self, p):
        '''case_list : case_clause
                     | case_list case_clause'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_case_clause(self, p):
        '''case_clause : KEYWORD_CASE expression COLON statement_list
                       | KEYWORD_DEFAULT COLON statement_list'''
        if len(p) == 5:
            p[0] = CaseClause(p[2], p[4])
        else:
            p[0] = CaseClause('default', p[3])

    def p_break_statement(self, p):
        '''break_statement : KEYWORD_BREAK SEMICOLON'''
        p[0] = BreakStatement()
    
    def p_declaration_statement(self, p):
        '''declaration_statement : type_specifier IDENTIFIER SEMICOLON
                                | type_specifier IDENTIFIER ASSIGN expression SEMICOLON
                                | type_specifier IDENTIFIER LBRACKET expression RBRACKET SEMICOLON
                                | type_specifier IDENTIFIER LBRACKET expression RBRACKET ASSIGN initializer_list SEMICOLON
                                | type_specifier IDENTIFIER LBRACKET RBRACKET ASSIGN initializer_list SEMICOLON
                                | type_specifier IDENTIFIER LBRACKET RBRACKET ASSIGN expression SEMICOLON
                                | type_specifier IDENTIFIER LBRACKET RBRACKET SEMICOLON'''
        # Simple variable decl
        if len(p) == 4:
            p[0] = Declaration(p[1], p[2])
        # Simple variable with initializer
        elif len(p) == 6 and p[3] == '=':
            p[0] = Declaration(p[1], p[2], p[4])
        # Static array with size, no initializer: type id [ expr ] ;
        elif len(p) == 7 and p[3] == '[' and p[5] == ']':
            p[0] = ArrayDeclaration(p[1], p[2], size=p[4])
        # Static array with size and initializer: type id [ expr ] = init ;
        elif len(p) == 9 and p[3] == '[' and p[5] == ']' and p[6] == '=':
            p[0] = ArrayDeclaration(p[1], p[2], size=p[4], initializer=p[7], is_dynamic=False)
        # Dynamic array with initializer: type id [ ] = init ; (can be initializer_list or expression)
        elif len(p) == 8 and p[3] == '[' and p[4] == ']' and p[5] == '=':
            p[0] = ArrayDeclaration(p[1], p[2], initializer=p[6], is_dynamic=True)
        # Empty dynamic array: type id [ ] ;
        elif len(p) == 6 and p[3] == '[' and p[4] == ']':
            p[0] = ArrayDeclaration(p[1], p[2], initializer=None, is_dynamic=True)
    
    def p_type_specifier(self, p):
        '''type_specifier : primitive_type
                         | array_type'''
        p[0] = p[1]

    def p_primitive_type(self, p):
        '''primitive_type : KEYWORD_INT
                          | KEYWORD_FLOAT
                          | KEYWORD_CHAR
                          | KEYWORD_VOID
                          | KEYWORD_STRING
                          | KEYWORD_BOOL
                          | KEYWORD_FILE
                          | KEYWORD_SOCKET
                          | KEYWORD_DICT
                          | KEYWORD_REGEX
                          | KEYWORD_ARRAY'''
        base = canonicalize(p[1])
        p[0] = TypeSpecifier(base)

    def p_array_type(self, p):
        'array_type : primitive_type LBRACKET RBRACKET'
        p[0] = TypeSpecifier(p[1].type_name, is_array=True)
    
    def p_assignment_statement(self, p):
        '''assignment_statement : left_hand_side ASSIGN expression SEMICOLON'''
        p[0] = Assignment(p[1], p[3])
    
    def p_left_hand_side(self, p):
        '''left_hand_side : IDENTIFIER
                         | subscript_access'''
        if isinstance(p[1], str):
            p[0] = Identifier(p[1])
        else:
            p[0] = p[1]

    def p_assignment_statement_no_semi(self, p):
        '''assignment_statement_no_semi : left_hand_side ASSIGN expression'''
        p[0] = Assignment(p[1], p[3])
    
    def p_if_statement(self, p):
        '''if_statement : KEYWORD_IF LPAREN expression RPAREN statement %prec LOWER_THAN_ELSE
                        | KEYWORD_IF LPAREN expression RPAREN statement KEYWORD_ELSE statement'''
        if len(p) == 6:
            p[0] = IfStatement(p[3], p[5])
        else:
            p[0] = IfStatement(p[3], p[5], p[7])
    
    def p_while_statement(self, p):
        '''while_statement : KEYWORD_WHILE LPAREN expression RPAREN statement'''
        p[0] = WhileStatement(p[3], p[5])
    
    def p_for_statement(self, p):
        '''for_statement : KEYWORD_FOR LPAREN for_init expression_opt SEMICOLON expression_opt RPAREN statement'''
        p[0] = ForStatement(p[3], p[4], p[6], p[8])

    def p_for_init(self, p):
        '''for_init : assignment_statement_no_semi SEMICOLON
                    | declaration_statement
                    | SEMICOLON'''
        if len(p) == 2 and p[1] == ';':
            p[0] = None  # Empty initialization
        elif len(p) == 3:
            p[0] = p[1]  # assignment with semicolon
        else:
            p[0] = p[1]  # declaration with its own semicolon

    def p_expression_statement(self, p):
        '''expression_statement : expression SEMICOLON
                               | SEMICOLON'''
        if len(p) == 2:
            p[0] = None  # Empty expression
        else:
            p[0] = p[1]

    def p_expression_opt(self, p):
        '''expression_opt : expression
                         | assignment_statement_no_semi
                         | increment_decrement
                         | empty'''
        p[0] = p[1]
    
    def p_increment_decrement(self, p):
        '''increment_decrement : IDENTIFIER PLUS PLUS
                              | IDENTIFIER MINUS MINUS'''
        # Convert i++ to i = i + 1 and i-- to i = i - 1
        identifier = Identifier(p[1])
        if p[2] == '+':
            # i++ becomes i = i + 1
            p[0] = Assignment(identifier, BinaryOp('+', identifier, Primary('1')))
        else:
            # i-- becomes i = i - 1
            p[0] = Assignment(identifier, BinaryOp('-', identifier, Primary('1')))

    def p_empty(self, p):
        'empty :'
        p[0] = None
    
    def p_return_statement(self, p):
        '''return_statement : KEYWORD_RETURN SEMICOLON
                           | KEYWORD_RETURN expression SEMICOLON'''
        if len(p) == 3:
            p[0] = ReturnStatement()
        else:
            p[0] = ReturnStatement(p[2])
    
    def p_function_call_statement(self, p):
        '''function_call_statement : function_call SEMICOLON'''
        p[0] = FunctionCallStatement(p[1])
    
    def p_function_call(self, p):
        '''function_call : IDENTIFIER LPAREN argument_list RPAREN
                        | IDENTIFIER LPAREN RPAREN
                        | SYSTEM_INPUT LPAREN IDENTIFIER COMMA type_specifier RPAREN
                        | SYSTEM_OUTPUT LPAREN expression COMMA type_specifier RPAREN
                        | SYSTEM_OUTPUT LPAREN expression COMMA type_specifier COMMA expression RPAREN
                        | KEYWORD_EXIT LPAREN RPAREN
                        | SYSTEM_SLEEP LPAREN expression RPAREN
                        | SYSTEM_ARR_PUSH LPAREN expression COMMA expression RPAREN
                        | SYSTEM_ARR_POP LPAREN expression RPAREN
                        | SYSTEM_ARR_SIZE LPAREN expression RPAREN
                        | SYSTEM_ARR_CONTAINS LPAREN expression COMMA expression RPAREN
                        | SYSTEM_ARR_INDEXOF LPAREN expression COMMA expression RPAREN
                        | SYSTEM_ARR_AVG LPAREN expression RPAREN
                        | SYSTEM_ARR_AVG LPAREN expression COMMA expression RPAREN'''
        slice_type = p.slice[1].type
        if slice_type == 'SYSTEM_INPUT':
            p[0] = SystemInput(Identifier(p[3]), p[5])
        elif slice_type == 'SYSTEM_OUTPUT':
            precision = p[7] if len(p) > 7 and p.slice[-2].type != 'RPAREN' else None
            p[0] = SystemOutput(p[3], p[5], precision)
        elif slice_type == 'KEYWORD_EXIT':
            p[0] = SystemExit()
        elif slice_type == 'SYSTEM_SLEEP':
            p[0] = SystemSleep(p[3])
        elif slice_type == 'SYSTEM_ARR_PUSH':
            p[0] = ArrayPush(p[3], p[5])
        elif slice_type == 'SYSTEM_ARR_POP':
            p[0] = ArrayPop(p[3])
        elif slice_type == 'SYSTEM_ARR_SIZE':
            p[0] = ArraySize(p[3])
        elif slice_type == 'SYSTEM_ARR_CONTAINS':
            p[0] = ArrayContains(p[3], p[5])
        elif slice_type == 'SYSTEM_ARR_INDEXOF':
            p[0] = ArrayIndexOf(p[3], p[5])
        elif slice_type == 'SYSTEM_ARR_AVG':
            if len(p) == 5:
                p[0] = ArrayAvg(p[3])
            else:
                p[0] = ArrayAvg(p[3], p[5])
        elif slice_type == 'IDENTIFIER':
            args = p[3] if len(p) == 5 else []
            p[0] = FunctionCall(p[1], args)
    
    def p_argument_list(self, p):
        '''argument_list : expression
                        | argument_list COMMA expression'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_block_statement(self, p):
        '''block_statement : LBRACE RBRACE
                          | LBRACE statement_list RBRACE'''
        if len(p) == 3:
            p[0] = Block([])
        else:
            p[0] = Block(p[2])
    
    def p_initializer_list(self, p):
        'initializer_list : LBRACKET expression_list_opt RBRACKET'
        p[0] = InitializerList(p[2])

    def p_expression_list_opt(self, p):
        '''expression_list_opt : expression_list
                               | empty'''
        if p[1] is None:
            p[0] = []
        else:
            p[0] = p[1]

    def p_expression_list(self, p):
        '''expression_list : expression
                           | expression_list COMMA expression'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_expression(self, p):
        '''expression : logical_expression
                      | initializer_list'''
        p[0] = p[1]
    
    def p_logical_expression(self, p):
        '''logical_expression : equality_expression
                             | logical_expression AND equality_expression
                             | logical_expression OR equality_expression'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = BinaryOp(p[2], p[1], p[3])
    
    def p_equality_expression(self, p):
        '''equality_expression : relational_expression
                               | equality_expression EQ relational_expression
                               | equality_expression NEQ relational_expression'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = BinaryOp(p[2], p[1], p[3])
    
    def p_relational_expression(self, p):
        '''relational_expression : additive_expression
                                | relational_expression GT additive_expression
                                | relational_expression LT additive_expression
                                | relational_expression GEQ additive_expression
                                | relational_expression LEQ additive_expression'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = BinaryOp(p[2], p[1], p[3])
    
    def p_additive_expression(self, p):
        '''additive_expression : multiplicative_expression
                              | additive_expression PLUS multiplicative_expression
                              | additive_expression MINUS multiplicative_expression'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = BinaryOp(p[2], p[1], p[3])
    
    def p_multiplicative_expression(self, p):
        '''multiplicative_expression : unary_expression
                                    | multiplicative_expression MUL unary_expression
                                    | multiplicative_expression DIV unary_expression
                                    | multiplicative_expression MOD unary_expression'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = BinaryOp(p[2], p[1], p[3])
    
    def p_unary_expression(self, p):
        '''unary_expression : primary_expression
                           | MINUS unary_expression %prec UMINUS'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = UnaryOp(p[1], p[2])
    
    def p_primary_expression(self, p):
        '''primary_expression : IDENTIFIER
                             | INT_LITERAL
                             | FLOAT_LITERAL
                             | STRING_LITERAL
                             | CHAR_LITERAL
                             | KEYWORD_TRUE
                             | KEYWORD_FALSE
                             | KEYWORD_NULL
                             | LPAREN expression RPAREN
                             | function_call
                             | subscript_access
                             | dictionary_literal'''
        if len(p) == 4: # Parenthesized expression
            p[0] = p[2]
        elif isinstance(p[1], Node): # Already a node (function_call, etc.)
            p[0] = p[1]
        else:
            # Check if it's an identifier token or a literal token
            if p.slice[1].type == 'IDENTIFIER':
                p[0] = Identifier(p[1])
            else: # It's a literal
                p[0] = Primary(p[1])


    def p_dictionary_literal(self, p):
        '''dictionary_literal : LBRACE key_value_list_opt RBRACE'''
        p[0] = DictionaryLiteral(p[2])

    def p_key_value_list_opt(self, p):
        '''key_value_list_opt : key_value_list
                              | empty'''
        if p[1] is None:
            p[0] = []
        else:
            p[0] = p[1]

    def p_key_value_list(self, p):
        '''key_value_list : key_value
                          | key_value_list COMMA key_value'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_key_value(self, p):
        '''key_value : expression COLON expression'''
        p[0] = (p[1], p[3]) # Keep as tuple for DictionaryLiteral

    def p_subscript_access(self, p):
        '''subscript_access : IDENTIFIER LBRACKET expression RBRACKET'''
        p[0] = SubscriptAccess(p[1], p[3])
    
    def p_error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, token='{p.value}', type={p.type}")
        else:
            print("Syntax error at EOF")

def print_ast(node, indent=0):
    """Pretty-prints the class-based AST."""
    indent_str = "  " * indent
    if not isinstance(node, Node):
        if isinstance(node, list):
            for item in node:
                print_ast(item, indent)
        else:
            print(f"{indent_str}{node}")
        return

    print(f"{indent_str}{node.__class__.__name__}")
    for attr, value in node.__dict__.items():
        if value is None:
            continue
        print(f"{indent_str}  {attr}:")
        if isinstance(value, list):
            for item in value:
                print_ast(item, indent + 2)
        elif isinstance(value, Node):
            print_ast(value, indent + 2)
        else:
            print(f"{indent_str}    {value}")
