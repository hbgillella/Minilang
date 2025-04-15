# minilang_parser.py

import re

class Number:
    def __init__(self, value):
        self.value = int(value)
    def __repr__(self):
        return f"Number({self.value})"

class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Variable('{self.name}')"

class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    def __repr__(self):
        return f"BinaryOp('{self.op}', {self.left}, {self.right})"

class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"LetStatement('{self.name}', {self.value})"

def tokenize(code):
    tokens = []
    token_specification = [
        ('ID',             r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('NUMBER',         r'\d+'),
        ('ASSIGN',         r'='),
        ('PLUS',           r'\+'),
        ('MINUS',          r'-'),
        ('SEMICOLON',      r';'),
        ('WHITESPACE',     r'\s+'),
        ('MISMATCH',       r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'WHITESPACE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        else:
            tokens.append((kind, value))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def peek(self):
        try:
            next_token = self.tokens.__next__()
            self.tokens = iter([next_token] + list(self.tokens))
            return next_token
        except StopIteration:
            return None

    def consume(self, token_type):
        if self.current_token and self.current_token[0] == token_type:
            value = self.current_token[1]
            self.advance()
            return value
        elif self.current_token:
            raise SyntaxError(f"Expected {token_type}, but got {self.current_token[0]}: '{self.current_token[1]}'")
        else:
            raise SyntaxError(f"Expected {token_type}, but reached end of input")

    def parse_program(self):
        statements = []
        while self.current_token is not None:
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            elif self.current_token is not None:
                raise SyntaxError(f"Unexpected token at top level: {self.current_token}")
            else:
                break
        return statements

    def parse_statement(self):
        if self.current_token and self.current_token[0] == 'ID' and self.current_token[1] == 'let':
            return self.parse_let_statement()
        elif self.current_token is not None:
            raise SyntaxError(f"Unexpected token at the beginning of a statement: {self.current_token}")
        return None # If it's not a 'let' statement, we're done with this statement

    def parse_let_statement(self):
        self.consume('ID') # Consume 'let'
        name = self.consume('ID')
        self.consume('ASSIGN')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return LetStatement(name, value)

    def parse_expression(self):
        return self.parse_additive_expression()

    def parse_additive_expression(self):
        left = self.parse_term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            op_type, op_value = self.current_token
            self.advance()
            right = self.parse_term()
            left = BinaryOp(op_value, left, right)
        return left

    def parse_term(self):
        if self.current_token and self.current_token[0] == 'NUMBER':
            return Number(self.consume('NUMBER'))
        elif self.current_token and self.current_token[0] == 'ID':
            return Variable(self.consume('ID'))
        else:
            raise SyntaxError(f"Unexpected token in expression: {self.current_token}")

def parse_program(tokens):
    parser = Parser(tokens)
    return parser.parse_program()

if __name__ == '__main__':
    code = 'let x = 5 + 3; let y = x + 2;'
    tokens = tokenize(code)
    print(f"Tokens: {tokens}")
    parser = Parser(tokens)
    ast = parser.parse_program()
    print(f"AST: {ast}")