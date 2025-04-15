# ast_nodes.py

class Number:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Number({self.value})"

class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Variable({self.name})"

class BinaryOp:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"BinaryOp({self.left}, {self.operator}, {self.right})"

class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"LetStatement(name={self.name}, value={self.value})"

class FunctionDef:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f"FunctionDef(name={self.name}, params={self.params}, body={self.body})"

class CallExpr:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __repr__(self):
        return f"CallExpr(name={self.name}, args={self.args})"

class IfExpr:
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        return f"IfExpr(condition={self.condition}, then_branch={self.then_branch}, else_branch={self.else_branch})"
