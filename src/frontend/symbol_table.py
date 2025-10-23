from frontend.types import TypeInfo, canonicalize

# Symbol Table Implementation
class SymbolTable:
    def __init__(self):
        # Main table structure: { scope_id: { symbol_name: symbol_info } }
        self.table = {}
        
        # Stack to track nested scopes
        self.scope_stack = [0]  # Start with global scope (0)
        
        # Current active scope
        self.current_scope = 0
        
        # Next available scope ID
        self.next_scope = 1
    
    def enter_scope(self):
        """Create a new scope and make it the current scope."""
        self.scope_stack.append(self.next_scope)
        self.current_scope = self.next_scope
        self.next_scope += 1
        return self.current_scope
    
    def exit_scope(self):
        """Exit the current scope and return to the previous scope."""
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
            self.current_scope = self.scope_stack[-1]
        return self.current_scope
    
    def add_symbol(self, name, type_info, line_num=None, is_initialized=False, **kwargs):
        """Add a symbol to the current scope. type_info can be a TypeInfo or string for legacy."""
        if self.current_scope not in self.table:
            self.table[self.current_scope] = {}
        if isinstance(type_info, str):
            symbol_info = {'type': type_info}
        elif isinstance(type_info, TypeInfo):
            symbol_info = {'type': 'array' if type_info.kind == 'array' else type_info.base,
                           'typeinfo': type_info,
                           'element_type': type_info.base if type_info.kind == 'array' else None,
                           'is_dynamic': type_info.is_dynamic,
                           'size': type_info.size}
        else:
            symbol_info = {'type': str(type_info)}
        symbol_info.update({'line': line_num, 'initialized': is_initialized})
        symbol_info.update(kwargs)
        self.table[self.current_scope][name] = symbol_info
        return symbol_info

    def get_array_info(self, name):
        sym = self.lookup_symbol(name)
        if not sym:
            return None
        ti = sym.get('typeinfo')
        if ti and ti.kind == 'array':
            return ti
        if sym.get('type') == 'array':
            return TypeInfo(sym.get('element_type'), is_dynamic=sym.get('is_dynamic', False), is_array=not sym.get('is_dynamic', False), size=sym.get('size'))
        return None
    
    def lookup_symbol(self, name):
        """Look up a symbol in the current scope and parent scopes."""
        # Search from current scope up through parent scopes
        for scope in reversed(self.scope_stack):
            if scope in self.table and name in self.table[scope]:
                return self.table[scope][name]
        return None
    
    def lookup_function(self, name):
        """Looks up a function in the symbol table."""
        # Functions are typically in the global scope
        if 0 in self.table and name in self.table[0]:
            symbol = self.table[0][name]
            if symbol['type'] == 'function':
                return symbol
        return None

    def lookup_symbol_current_scope(self, name):
        """Look up a symbol in ONLY the current scope."""
        if self.current_scope in self.table and name in self.table[self.current_scope]:
            return self.table[self.current_scope][name]
        return None
    
    def update_symbol(self, name, **updates):
        """Update a symbol's information."""
        symbol = self.lookup_symbol(name)
        if symbol:
            for key, value in updates.items():
                symbol[key] = value
            return True
        return False
        
    def __str__(self):
        """String representation of the symbol table for debugging."""
        result = []
        for scope, symbols in self.table.items():
            result.append(f"Scope {scope}:")
            for name, info in symbols.items():
                if info['type'] == 'function':
                    params = ", ".join(f"{p['type']} {p['name']}" for p in info.get('params', []))
                    result.append(f"  {info.get('return_type')} {name}({params})")
                else:
                    result.append(f"  {name}: {info}")
        return "\n".join(result)

# Type Checking Helper
class TypeChecker:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.numeric = {'KEYWORD_INT','KEYWORD_FLOAT','int','float'}

    def _normalize_type(self, type_name):
        if type_name is None:
            return None
        if isinstance(type_name, TypeInfo):
            if type_name.kind == 'array':
                return 'array'
            return 'KEYWORD_'+type_name.base.upper()
        # Keep legacy KEYWORD_ forms
        if type_name.startswith('KEYWORD_'):
            return type_name
        base = canonicalize(type_name)
        mapping = {
            'int':'KEYWORD_INT','float':'KEYWORD_FLOAT','char':'KEYWORD_CHAR','string':'KEYWORD_STRING','bool':'KEYWORD_BOOL','void':'KEYWORD_VOID','file':'KEYWORD_FILE','socket':'KEYWORD_SOCKET','dict':'KEYWORD_DICT','null':'KEYWORD_NULL'
        }
        return mapping.get(base, type_name)

    def is_compatible(self, target_type, source_type):
        t = self._normalize_type(target_type)
        s = self._normalize_type(source_type)
        if not t or not s:
            return False
        if s == 'KEYWORD_NULL' and t in ['KEYWORD_STRING','KEYWORD_FILE','KEYWORD_SOCKET']:
            return True
        if t == s:
            return True
        if t == 'KEYWORD_FLOAT' and s == 'KEYWORD_INT':
            return True
        return False

    def check_binary_op(self, op, left_type, right_type):
        l = self._normalize_type(left_type)
        r = self._normalize_type(right_type)
        if not l or not r:
            return None
        if op in ['PLUS','MINUS','MUL','DIV','MOD']:
            if op=='PLUS' and l=='KEYWORD_STRING' and r=='KEYWORD_STRING':
                return 'KEYWORD_STRING'
            # Allow string concatenation with any type (auto-convert to string)
            if op=='PLUS' and (l=='KEYWORD_STRING' or r=='KEYWORD_STRING'):
                return 'KEYWORD_STRING'
            if l in ['KEYWORD_INT','KEYWORD_FLOAT'] and r in ['KEYWORD_INT','KEYWORD_FLOAT']:
                if op=='DIV':
                    return 'KEYWORD_FLOAT'
                if l=='KEYWORD_FLOAT' or r=='KEYWORD_FLOAT':
                    return 'KEYWORD_FLOAT'
                return 'KEYWORD_INT'
            return None
        if op in ['LT','GT','LEQ','GEQ']:
            if l in ['KEYWORD_INT','KEYWORD_FLOAT'] and r in ['KEYWORD_INT','KEYWORD_FLOAT']:
                return 'KEYWORD_BOOL'
            # Add support for string comparisons
            if l == 'KEYWORD_STRING' and r == 'KEYWORD_STRING':
                return 'KEYWORD_BOOL'
            # Add support for string length comparisons (string < int, int < string)
            if (l == 'KEYWORD_STRING' and r in ['KEYWORD_INT', 'KEYWORD_FLOAT']) or \
               (r == 'KEYWORD_STRING' and l in ['KEYWORD_INT', 'KEYWORD_FLOAT']):
                return 'KEYWORD_BOOL'
            return None
        if op in ['EQ','NEQ']:
            if l==r:
                return 'KEYWORD_BOOL'
            if {l,r} <= {'KEYWORD_INT','KEYWORD_FLOAT'}:
                return 'KEYWORD_BOOL'
            if 'KEYWORD_NULL' in [l,r]:
                return 'KEYWORD_BOOL'
            # Add support for string equality comparisons
            if l == 'KEYWORD_STRING' and r == 'KEYWORD_STRING':
                return 'KEYWORD_BOOL'
            return None
        if op in ['AND','OR']:
            if l=='KEYWORD_BOOL' and r=='KEYWORD_BOOL':
                return 'KEYWORD_BOOL'
            return None
        return None

# Usage Example
def test_symbol_table():
    symbol_table = SymbolTable()
    
    # Add some symbols in global scope
    symbol_table.add_symbol("x", "KEYWORD_INT", line_num=1, is_initialized=True)
    symbol_table.add_symbol("y", "KEYWORD_FLOAT", line_num=2)
    
    # Enter a new scope (e.g., inside a function or block)
    symbol_table.enter_scope()
    
    # Add symbols in the new scope
    symbol_table.add_symbol("z", "KEYWORD_STRING", line_num=3)
    symbol_table.add_symbol("x", "KEYWORD_BOOL", line_num=4)  # Shadows global "x"
    
    # Look up symbols
    print("Looking up 'x' (should find local scope's bool):", symbol_table.lookup_symbol("x"))
    print("Looking up 'y' (should find global scope's float):", symbol_table.lookup_symbol("y"))
    print("Looking up 'z' (should find local scope's string):", symbol_table.lookup_symbol("z"))
    
    # Exit back to global scope
    symbol_table.exit_scope()
    
    # Now "x" should refer to the global int
    print("After exiting scope, looking up 'x':", symbol_table.lookup_symbol("x"))
    
    # "z" is no longer visible
    print("After exiting scope, looking up 'z':", symbol_table.lookup_symbol("z"))
    
    # Test function table
    symbol_table.add_symbol("calculateArea", "function", return_type="KEYWORD_FLOAT", params=[{'type': 'KEYWORD_FLOAT', 'name': 'width'}, {'type': 'KEYWORD_FLOAT', 'name': 'height'}])
    symbol_table.add_symbol("main", "function", return_type="KEYWORD_INT", params=[])
    
    print("\nSymbol Table with Functions:")
    print(symbol_table)
    
    # Test type checker
    type_checker = TypeChecker(symbol_table)
    print("\nType compatibility checks:")
    print("int + float =", type_checker.check_binary_op("PLUS", "KEYWORD_INT", "KEYWORD_FLOAT"))
    print("bool && bool =", type_checker.check_binary_op("AND", "KEYWORD_BOOL", "KEYWORD_BOOL"))
    print("int > float =", type_checker.check_binary_op("GT", "KEYWORD_INT", "KEYWORD_FLOAT"))
    print("string + int =", type_checker.check_binary_op("PLUS", "KEYWORD_STRING", "KEYWORD_INT"))

if __name__ == "__main__":
    test_symbol_table()