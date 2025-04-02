import ply.lex as lex

literals = ['(', ')', ';', '.']

tokens = (
    'PROGRAM', 'BEGIN', 'END', 'WRITELN',
    'id', 'string'
)

def t_PROGRAM(t):
    r'program'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_END(t):
    r'end'
    return t

def t_WRITELN(t):
    r'writeln'
    return t

def t_string(t):
    r'\'[^\']*?\''
    t.value = t.value[1:-1]
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t  

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
