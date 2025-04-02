import sys
import ply.yacc as yacc
from lexer import tokens
from gen import gen_code


def p_Program(p):
    "Program : PROGRAM id ';' BEGIN Statement END '.'"
    p[0] = ("program", p[2], p[5])


def p_Statement_writeln(p):
    "Statement : WRITELN '(' string ')' ';'"
    p[0] = ("writeln", p[3])


def p_error(p):
    parser.success = False
    print("Erro de sintaxe!")


parser = yacc.yacc()

text = sys.stdin.read()
parser.success = True
parsed = parser.parse(text)

if parser.success:
    print(f"Texto válido.\n{text}")
    print(gen_code(parsed))
else:
    print("Texto inválido...")
