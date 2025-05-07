import ply.lex as lex

literals = ['(', ')', ';', '.', ',', ':',
            '{', '}', '>', '<', '=', '*', '+', '-', '[', ']']

tokens = (
    'PROGRAM', 'VAR', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'FOR', 'TO', 'DO', 'WHILE', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'ARRAY', 'OF', 'DOWNTO', 'FUNCTION', 'PROCEDURE',
    'id', 'string', 'num', 'boolean'
)


def t_PROGRAM(t):
    r'program'
    return t


def t_FUNCTION(t):
    r'function'
    return t


def t_PROCEDURE(t):
    r'procedure'
    return t


def t_VAR(t):
    r'var'
    return t


def t_BEGIN(t):
    r'begin'
    return t


def t_END(t):
    r'end'
    return t


def t_IF(t):
    r'if'
    return t


def t_THEN(t):
    r'then'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_FOR(t):
    r'for'
    return t


def t_TO(t):
    r'to'
    return t


def t_DOWNTO(t):
    r'downto'
    return t


def t_DO(t):
    r'do'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_DIV(t):
    r'div'
    return t


def t_MOD(t):
    r'mod'
    return t


def t_AND(t):
    r'and'
    return t


def t_OR(t):
    r'or'
    return t


def t_NOT(t):
    r'not'
    return t


def t_ARRAY(t):
    r'array'
    return t


def t_OF(t):
    r'of'
    return t


def t_string(t):
    r'\'[^\']*?\''
    t.value = t.value[1:-1]
    return t


def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_boolean(t):
    r'true|false'
    return t


def t_id(t):
    r'[a-zA-Z_]\w*'
    return t


t_ignore = ' \t\n\r'
t_ignore_COMMENT = r'{.*}'


def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()
