# Directly Coded Lexer Example Using NFA to DFA Conversion 
# ---------------------------- 
# NFA State Data Structure 
# ---------------------------- 
class NFAState: 
    def __init__(self): 
        self.transitions = {}         # transitions on symbols: {symbol: [state, ...]} 
        self.epsilon_transitions = [] # transitions on epsilon (None) 
        self.is_accepting = False     # indicates whether this state is accepting 
        self.token_type = None        # token type if state is accepting 
 
def add_epsilon_transition(from_state, to_state): 
    from_state.epsilon_transitions.append(to_state) 

def build_literal_nfa(literal):
    start = NFAState()
    current = start
    for ch in literal:
        next_state = NFAState()
        current.transitions.setdefault(ch, []).append(next_state)
        current = next_state
    return start, current
# ---------------------------- 
# Thompson's Construction Functions 
# ---------------------------- 
def literal_nfa(char): 
    """Creates an NFA fragment for a literal character.""" 
    start = NFAState() 
    accept = NFAState() 
    start.transitions[char] = [accept] 
    accept.is_accepting = True 
    return start, accept 
 
def concatenate_nfa(nfa1, nfa2): 
    """Concatenates two NFA fragments.""" 
    nfa1_accept = nfa1[1] 
    nfa2_start = nfa2[0] 
    nfa1_accept.is_accepting = False 
    add_epsilon_transition(nfa1_accept, nfa2_start) 
    return nfa1[0], nfa2[1] 
 
def alternate_nfa(nfa1, nfa2): 
    """Creates an NFA that recognizes either nfa1 or nfa2.""" 
    start = NFAState() 
    accept = NFAState() 
    add_epsilon_transition(start, nfa1[0]) 
    add_epsilon_transition(start, nfa2[0]) 
    nfa1[1].is_accepting = False 
    nfa2[1].is_accepting = False 
    add_epsilon_transition(nfa1[1], accept) 
    add_epsilon_transition(nfa2[1], accept) 
    accept.is_accepting = True 
    return start, accept 
 
def kleene_star_nfa(nfa): 
    """Applies the Kleene star to an NFA fragment.""" 
    start = NFAState() 
    accept = NFAState() 
    add_epsilon_transition(start, nfa[0]) 
    add_epsilon_transition(start, accept) 
    nfa[1].is_accepting = False 
    add_epsilon_transition(nfa[1], nfa[0]) 
    add_epsilon_transition(nfa[1], accept) 
    accept.is_accepting = True 
    return start, accept 
 
# ---------------------------- 
# NFA to DFA Conversion (Subset Construction) 
# ---------------------------- 
def epsilon_closure(states): 
    """Returns the epsilon closure of a set of NFA states.""" 
    stack = list(states) 
    closure = set(states) 
    while stack: 
        state = stack.pop() 
        for next_state in state.epsilon_transitions: 
            if next_state not in closure: 
                closure.add(next_state) 
                stack.append(next_state) 
    return closure 
 
def move(states, symbol): 
    """Returns the set of states reachable on a given symbol.""" 
    result = set() 
    for state in states: 
        if symbol in state.transitions: 
            result.update(state.transitions[symbol]) 
    return result 
 
def get_alphabet(state_set): 
    """Extracts the set of input symbols from a set of NFA states.""" 
    symbols = set() 
    for state in state_set: 
        symbols.update(state.transitions.keys()) 
    return symbols 
 
def nfa_to_dfa(nfa_start):
    """
    Converts an NFA into a DFA using the subset construction method.
    Returns:
      - dfa_transitions: dict mapping DFA states (frozensets) to
        transitions { symbol: next DFA state }
      - dfa_token: dict mapping DFA state to token type (if accepting)
    """
    dfa_transitions = {}
    dfa_token = {}

    start_set = epsilon_closure({nfa_start})
    start_dfa = frozenset(start_set)
    unmarked_states = [start_dfa]
    dfa_transitions[start_dfa] = {}

    for state in start_set:
        if state.is_accepting:
            # Prioritize keywords over identifiers
            if start_dfa not in dfa_token or state.token_type.startswith("KEYWORD") or state.token_type.startswith("SYSTEM"):
                dfa_token[start_dfa] = state.token_type

    while unmarked_states:
        current = unmarked_states.pop()
        dfa_transitions[current] = {}
        symbols = get_alphabet(current)
        for symbol in symbols:
            next_states = epsilon_closure(move(current, symbol))
            if not next_states:
                continue
            next_dfa = frozenset(next_states)
            dfa_transitions[current][symbol] = next_dfa
            if next_dfa not in dfa_transitions:
                unmarked_states.append(next_dfa)
                for state in next_dfa:
                    if state.is_accepting:
                        # Prioritize keywords over identifiers
                        if next_dfa not in dfa_token or state.token_type.startswith("KEYWORD") or state.token_type.startswith("SYSTEM"):
                            dfa_token[next_dfa] = state.token_type
    return dfa_transitions, dfa_token
# ---------------------------- 
# Lexer Class Using the DFA 
# ---------------------------- 
class Lexer: 
    def __init__(self, dfa_transitions, dfa_token, start_state): 
        self.dfa = dfa_transitions      # DFA transition table 
        self.token_map = dfa_token      # Mapping from DFA state to token type 
        self.start_state = start_state  # DFA start state 
 
    def tokenize(self, input_string): 
        pos = 0 
        tokens = [] 
        current_line = 1  # Track line number
        
        while pos < len(input_string): 
            # Track newlines
            if input_string[pos] == '\n':
                current_line += 1
                pos += 1
                continue
                
            if input_string[pos].isspace(): 
                pos += 1 
                continue 
            current_state = self.start_state 
            last_accepting = None 
            last_accepting_pos = pos 
            current_pos = pos 
            while current_pos < len(input_string): 
                symbol = input_string[current_pos] 
                if symbol in self.dfa[current_state]: 
                    current_state = self.dfa[current_state][symbol] 
                    current_pos += 1 
                    if current_state in self.token_map: 
                        last_accepting = current_state 
                        last_accepting_pos = current_pos 
                else: 
                    break 
            if last_accepting is None: 
                raise Exception(f"Lexical error at position {pos}, unrecognized character: '{input_string[pos]}'") 
            token_text = input_string[pos:last_accepting_pos] 
            token_type = self.token_map[last_accepting] 
            tokens.append((token_type, token_text, current_line)) 
            pos = last_accepting_pos 
        return tokens 
 
# ---------------------------- 
# Building the Master NFA 
# ---------------------------- 
def create_int_literal_nfa():
    int_start = NFAState()
    int_accept = NFAState()
    for d in "0123456789":
        int_start.transitions.setdefault(d, []).append(int_accept)
        int_accept.transitions.setdefault(d, []).append(int_accept)
    int_accept.is_accepting = True
    return int_start, int_accept

def create_float_literal_nfa():
    float_start = NFAState()
    float_digits = NFAState()
    float_point = NFAState()
    float_fraction = NFAState()

    # First part: digits
    for d in "0123456789":
        float_start.transitions.setdefault(d, []).append(float_digits)
        float_digits.transitions.setdefault(d, []).append(float_digits)

    # Decimal point
    float_digits.transitions.setdefault('.', []).append(float_point)

    # Fractional part (optional)
    for d in "0123456789":
        float_point.transitions.setdefault(d, []).append(float_fraction)
        float_fraction.transitions.setdefault(d, []).append(float_fraction)

    # Both decimal point and fractional part are accepting
    float_point.is_accepting = True
    float_fraction.is_accepting = True

    return float_start, float_fraction

def build_master_nfa():
    master_start = NFAState()

    # Identifiers: [A-Za-z_][A-Za-z0-9_]* (Add this first)
    id_start = NFAState()
    id_accept = NFAState()
    for ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
        id_start.transitions.setdefault(ch, []).append(id_accept)
    for ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
        id_accept.transitions.setdefault(ch, []).append(id_accept)
    id_accept.is_accepting = True
    id_accept.token_type = "IDENTIFIER"
    add_epsilon_transition(master_start, id_start)

    # Keywords (Add this after identifiers)
    keywords = {
        "do": "KEYWORD_DO",
        "if": "KEYWORD_IF",
        "else": "KEYWORD_ELSE",
        "for": "KEYWORD_FOR",
        "while": "KEYWORD_WHILE",
        "return": "KEYWORD_RETURN",
        "break": "KEYWORD_BREAK",
        "regex": "KEYWORD_REGEX",
        "continue": "KEYWORD_CONTINUE",
        "switch": "KEYWORD_SWITCH",
        "case": "KEYWORD_CASE",
        "default": "KEYWORD_DEFAULT",
        "exit": "KEYWORD_EXIT",
        "int": "KEYWORD_INT",
        "float": "KEYWORD_FLOAT",
        "file": "KEYWORD_FILE",
        "socket": "KEYWORD_SOCKET",
        "dict": "KEYWORD_DICT",
        "char": "KEYWORD_CHAR",
        "void": "KEYWORD_VOID",
        "null": "KEYWORD_NULL",
        "string": "KEYWORD_STRING",
        "bool": "KEYWORD_BOOL",
        "boolean": "KEYWORD_BOOL",  # Add this line
        "true": "KEYWORD_TRUE",
        "false": "KEYWORD_FALSE",
        "array": "KEYWORD_ARRAY"
    }
    for word, token_name in keywords.items():
        nfa_start, nfa_end = build_literal_nfa(word)
        nfa_end.is_accepting = True
        nfa_end.token_type = token_name
        add_epsilon_transition(master_start, nfa_start)

    # Integer literal pattern
    int_nfa = create_int_literal_nfa()
    int_nfa[1].token_type = "INT_LITERAL"
    add_epsilon_transition(master_start, int_nfa[0])

    # Float literal pattern
    float_nfa = create_float_literal_nfa()
    float_nfa[1].token_type = "FLOAT_LITERAL"
    add_epsilon_transition(master_start, float_nfa[0])

    # String literal: "..."
    string_start = NFAState()
    string_body = NFAState()
    string_end = NFAState()
    
    # Opening quote
    string_start.transitions.setdefault('"', []).append(string_body)
    
    # String content (any char except quote or newline)
    for ch in range(128):
        if ch != ord('"') and ch != ord('\n'):
            string_body.transitions.setdefault(chr(ch), []).append(string_body)
    
    # Closing quote
    string_body.transitions.setdefault('"', []).append(string_end)
    
    string_end.is_accepting = True
    string_end.token_type = "STRING_LITERAL"
    add_epsilon_transition(master_start, string_start)

    #char literal: 'a' or '\n' or '\t' or '\\' or any other char
    char_start = NFAState()
    char_body = NFAState()
    char_end = NFAState()

    # Opening quote
    char_start.transitions.setdefault("'", []).append(char_body)


    # String content (any char except quote or newline)
    for ch in range(128):
        if ch != ord("'") and ch != ord('\n') and ch != ord('\\'):
            char_body.transitions.setdefault(chr(ch), []).append(char_body)
        elif ch == ord("\\"):
            char_body.transitions.setdefault("\\", []).append(char_body)


    # Closing quote
    char_body.transitions.setdefault("'", []).append(char_end)


    char_end.is_accepting = True
    char_end.token_type = "CHAR_LITERAL"
    add_epsilon_transition(master_start, char_start)


   


    # Punctuation
    punctuations = {
        '(': "LPAREN", ')': "RPAREN",
        '{': "LBRACE", '}': "RBRACE",
        '[': "LBRACKET", ']': "RBRACKET",
        ';': "SEMICOLON", ',': "COMMA", ':': "COLON"
    }
    for p, token_name in punctuations.items():
        start, end = build_literal_nfa(p)
        end.is_accepting = True
        end.token_type = token_name
        add_epsilon_transition(master_start, start)
    
    # Operators (Simple)
    simple_operators = {
        '+': "PLUS", '-': "MINUS", '*': "MUL", '/': "DIV", 
        '%': "MOD", '.': "DOT", '>': "GT", '<': "LT"
    }
    for op, token_name in simple_operators.items():
        start, end = build_literal_nfa(op)
        end.is_accepting = True
        end.token_type = token_name
        add_epsilon_transition(master_start, start)

    # Operators (Complex - multi-character)
    complex_operators = {
        '==': "EQ", '!=': "NEQ", '>=': "GEQ", '<=': "LEQ",
        '&&': "AND", '||': "OR", '=': "ASSIGN"
    }
    for op, token_name in complex_operators.items():
        start, end = build_literal_nfa(op)
        end.is_accepting = True
        end.token_type = token_name
        add_epsilon_transition(master_start, start)

    # System functions
    system_functions = {
        "input": "SYSTEM_INPUT",
        "output": "SYSTEM_OUTPUT",
        "exit": "SYSTEM_EXIT",
        "sleep": "SYSTEM_SLEEP",
        "arr_push": "SYSTEM_ARR_PUSH",
        "arr_pop": "SYSTEM_ARR_POP",
        "arr_size": "SYSTEM_ARR_SIZE",
        "arr_contains": "SYSTEM_ARR_CONTAINS",
        "arr_indexof": "SYSTEM_ARR_INDEXOF",
        "arr_avg": "SYSTEM_ARR_AVG",
    }
    for func, token_name in system_functions.items():
        nfa_start, nfa_end = build_literal_nfa(func)
        nfa_end.is_accepting = True
        nfa_end.token_type = token_name
        add_epsilon_transition(master_start, nfa_start)

    # Single-line comments (// style)
    single_comment_start = NFAState()
    single_comment_middle = NFAState()
    single_comment_end = NFAState()
    
    # First slash
    single_comment_start.transitions.setdefault('/', []).append(single_comment_middle)
    
    # Second slash
    single_comment_middle.transitions.setdefault('/', []).append(single_comment_end)
    
    # Any character until newline
    for ch in range(128):  # ASCII characters
        if ch != ord('\n'):
            single_comment_end.transitions.setdefault(chr(ch), []).append(single_comment_end)
    
    single_comment_end.is_accepting = True
    single_comment_end.token_type = "COMMENT"
    add_epsilon_transition(master_start, single_comment_start)
    
    # Multi-line comments (/* ... */ style)
    multi_comment_start = NFAState()
    multi_comment_middle = NFAState()
    multi_comment_body = NFAState()
    multi_comment_star = NFAState()
    multi_comment_end = NFAState()
    
    # First slash
    multi_comment_start.transitions.setdefault('/', []).append(multi_comment_middle)
    
    # Star
    multi_comment_middle.transitions.setdefault('*', []).append(multi_comment_body)
    
    # Any character within comment
    for ch in range(128):
        if ch != ord('*'):
            multi_comment_body.transitions.setdefault(chr(ch), []).append(multi_comment_body)
        else:
            multi_comment_body.transitions.setdefault('*', []).append(multi_comment_star)
    
    # After star, if not slash, go back to body
    for ch in range(128):
        if ch != ord('/'):
            multi_comment_star.transitions.setdefault(chr(ch), []).append(multi_comment_body)
        else:
            multi_comment_star.transitions.setdefault('/', []).append(multi_comment_end)
    
    multi_comment_end.is_accepting = True
    multi_comment_end.token_type = "COMMENT"
    add_epsilon_transition(master_start, multi_comment_start)
    
    # DO NOT include a catch-all for unrecognized characters
    # Instead, the lexer will throw an error when it encounters unrecognized input

    return master_start
 
# ---------------------------- 
# Main Function 
# ---------------------------- 
def main(): 
    # Build the master NFA. 
    nfa_start = build_master_nfa() 
    # Convert the NFA into a DFA. 
    dfa_transitions, dfa_token = nfa_to_dfa(nfa_start) 
    start_set = frozenset(epsilon_closure({nfa_start})) 
    # Create the Lexer instance. 
    lexer = Lexer(dfa_transitions, dfa_token, start_set) 
    
    # Test with a sample program
#     test_program = """int x=5;
# if(x>5){
#     output("It is greater than 5",string)
# }"""
    
    # try:
    #     with open("test11.pie", "r") as file: 
    #         input_program = file.read()

    #     tokens = lexer.tokenize(input_program)
    #     print("Tokens:")
    #     for token_type, token_text in tokens:
    #         print(f"{token_type:20} : '{token_text}'")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # Uncomment to test with file input
    with open("test11.pie", "r") as file: 
        input_program = file.read()
    tokens = lexer.tokenize(input_program) 
    print("Tokens:") 
    for token_type, token_text, line_number in tokens:
       print(f"{token_type:20} : '{token_text}' (Line {line_number})")
 
if __name__ == "__main__": 
    main()