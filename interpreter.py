# interpreter.py

from minilang_parser import LetStatement, BinaryOp, Number, Variable, tokenize, parse_program

# Global environment for storing variables
env = {}

# Evaluate a list of AST statements
def evaluate(statements):
    result = None
    for stmt in statements:
        print(f"Evaluating statement: {stmt}")  # Debugging output
        result = eval_stmt(stmt)
    return result

# Evaluate a single statement
def eval_stmt(stmt):
    if isinstance(stmt, LetStatement):
        # Ensure correct evaluation of the right-hand side
        evaluated_value = eval_expr(stmt.value)
        print(f"Assigning {stmt.name} = {evaluated_value}")  # Debugging output
        env[stmt.name] = evaluated_value
    elif isinstance(stmt, BinaryOp):
        return eval_expr(stmt)
    elif isinstance(stmt, Number):
        return stmt.value
    elif isinstance(stmt, Variable):
        return env.get(stmt.name, 0)  # Default to 0 if variable is not found
    else:
        raise Exception(f"Unknown statement: {stmt}")

# Evaluate an expression
def eval_expr(expr):
    if isinstance(expr, Number):
        return expr.value
    elif isinstance(expr, Variable):
        return env.get(expr.name, 0)  # Default to 0 if variable is not found
    elif isinstance(expr, BinaryOp):
        left = eval_expr(expr.left)
        right = eval_expr(expr.right)
        if expr.op == '+':
            return left + right
        elif expr.op == '-':
            return left - right
        else:
            raise Exception(f"Unknown operator: {expr.op}")
    else:
        raise Exception(f"Unknown expression: {expr}")

# Example usage
code = 'let x = 5 + 3; let y = x + 2;'
tokens = tokenize(code)
print(f"Tokens: {tokens}")

# Parse tokens into AST
ast = parse_program(tokens)
print(f"AST: {ast}")  # Debugging output

# Evaluate the AST
result = evaluate(ast)

# Output final environment with variable values
print("Final Environment:", env)

# Optionally, print specific variable values (e.g., x and y)
print("x =", env.get('x'))
print("y =", env.get('y'))

