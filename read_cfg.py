# read_cfg.py

# Define the grammar with more detail on lexical tokens and expressions
grammar = {
    'S': ['let_stmt', 'expr_stmt', 'func_stmt', 'if_stmt'],
    'let_stmt': ['let id = expression'],
    'expr_stmt': ['expression'],
    'func_stmt': ['fn id ( params ) { statement* }'],
    'if_stmt': ['if expression { statement* } else { statement* }'],
    'expression': ['number', 'id', 'binary_op', 'call_expr'],
    'binary_op': ['expression + expression', 'expression - expression'],
    'call_expr': ['id ( expression* )'],
    'id': '[a-zA-Z_][a-zA-Z0-9_]*',  # Regular expression for identifiers
    'number': '[0-9]+',  # Regular expression for numbers
}

# Helper function to print the grammar
def print_grammar():
    for non_terminal, rules in grammar.items():
        print(f'{non_terminal} -> {", ".join(rules)}')

