import abc

class Node(abc.ABC):
    """Base class for all AST nodes."""
    def accept(self, visitor):
        method_name = f'visit_{self.__class__.__name__.lower()}'
        return visitor(self, method_name)

# Generic Wrappers
class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

# Statements
class Statement(Node):
    """Base class for all statement nodes."""
    pass

class Declaration(Statement):
    def __init__(self, var_type, identifier, initializer=None):
        self.var_type = var_type
        self.identifier = identifier
        self.initializer = initializer

class ArrayDeclaration(Declaration):
    def __init__(self, var_type, identifier, size=None, initializer=None, is_dynamic=False):
        super().__init__(var_type, identifier, initializer)
        self.size = size
        self.is_dynamic = is_dynamic

class Assignment(Statement):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class IfStatement(Statement):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class DoWhileStatement(Statement):
    def __init__(self, body, condition):
        self.body = body
        self.condition = condition

class ForStatement(Statement):
    def __init__(self, initializer, condition, update, body):
        self.initializer = initializer
        self.condition = condition
        self.update = update
        self.body = body

class SwitchStatement(Statement):
    def __init__(self, expression, cases):
        self.expression = expression
        self.cases = cases

class CaseClause(Node):
    def __init__(self, value, statements):
        self.value = value  # Can be an expression or 'default'
        self.statements = statements

class BreakStatement(Statement):
    pass

class ReturnStatement(Statement):
    def __init__(self, value=None):
        self.value = value

class FunctionDefinition(Statement):
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body

class Parameter(Node):
    def __init__(self, param_type, name):
        self.param_type = param_type
        self.name = name

# Expressions
class Expression(Node):
    """Base class for all expression nodes."""
    pass

class BinaryOp(Expression):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        self.result_type = None # To be filled in by semantic analysis

class UnaryOp(Expression):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class Primary(Expression):
    def __init__(self, value):
        self.value = value

class FunctionCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class FunctionCallStatement(Statement):
    def __init__(self, function_call):
        self.function_call = function_call


class SubscriptAccess(Expression):
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.element_type = None # To be filled in by semantic analysis

class InitializerList(Expression):
    def __init__(self, values):
        self.values = values

class DictionaryLiteral(Expression):
    def __init__(self, pairs):
        self.pairs = pairs # List of (key_expr, value_expr) tuples

class SafeDictionaryAccess(Expression):
    def __init__(self, dict_name, key, default_value=None):
        self.dict_name = dict_name
        self.key = key
        self.default_value = default_value  # Optional default value if key doesn't exist

# System Calls (can be treated as specific function calls)
class SystemInput(FunctionCall):
    def __init__(self, variable, input_type):
        super().__init__('input', [variable, input_type])
        self.variable = variable
        self.input_type = input_type

class SystemOutput(FunctionCall):
    def __init__(self, expression, output_type, precision=None):
        super().__init__('output', [expression, output_type, precision])
        self.expression = expression
        self.output_type = output_type
        self.precision = precision

class SystemExit(FunctionCall):
    def __init__(self):
        super().__init__('exit', [])

class SystemSleep(FunctionCall):
    def __init__(self, duration):
        super().__init__('sleep', [duration])
        self.duration = duration

# Array Functions
class ArrayPush(FunctionCall):
    def __init__(self, array, value):
        super().__init__('arr_push', [array, value])
        self.array = array
        self.value = value

class ArrayPop(FunctionCall):
    def __init__(self, array):
        super().__init__('arr_pop', [array])
        self.array = array

class ArraySize(FunctionCall):
    def __init__(self, array):
        super().__init__('arr_size', [array])
        self.array = array

class ArrayContains(FunctionCall):
    def __init__(self, array, value):
        super().__init__('arr_contains', [array, value])
        self.array = array
        self.value = value

class ArrayIndexOf(FunctionCall):
    def __init__(self, array, value):
        super().__init__('arr_indexof', [array, value])
        self.array = array
        self.value = value

class ArrayAvg(FunctionCall):
    def __init__(self, array, precision=None):
        super().__init__('arr_avg', [array, precision])
        self.array = array
        self.precision = precision

# TypeSpecifier Node
class TypeSpecifier(Node):
    def __init__(self, type_name, is_array=False):
        self.type_name = type_name
        self.is_array = is_array

class Identifier(Node):
    def __init__(self, name):
        self.name = name
