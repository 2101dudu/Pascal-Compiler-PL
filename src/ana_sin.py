import sys
import ply.yacc as yacc
from ana_lex import tokens
from ana_lex import literals
from gen import gen_code


def p_program_program(p):
    """
    Program : PROGRAM id ';' ProgramBody
    """


def p_programbody_varsection(p):
    """
    ProgramBody : VarSection MainSection
    """


def p_varsection_var(p):
    """
    VarSection : VAR VarsList
    """


def p_varsection_empty(p):
    """
    VarSection :
    """


def p_varslist_varslist(p):
    """
    VarsList : VarsList VarsListElem
    """


def p_varslist_varslistelem(p):
    """
    VarsList : VarsListElem
    """


def p_varslistelem_varslistelemids(p):
    """
    VarsListElem : VarsListElemIDs ':' INTEGER ';'
    """


def p_varslistelemids_varslistelemids(p):
    """
    VarsListElemIDs : VarsListElemIDs ',' id
    """


def p_varslistelemids_id(p):
    """
    VarsListElemIDs : id
    """


def p_mainsection_begin(p):
    """
    MainSection : BEGIN MainSectionList END '.'
    """


def p_mainsectionlist_mainsectionlist(p):
    """
    MainSectionList : MainSectionList MainSectionListElem
    """


def p_mainsectionlist_mainsectionlistelem(p):
    """
    MainSectionList : MainSectionListElem
    """


def p_mainsectionlistelem_func(p):
    """
    MainSectionListElem : Func
    """


def p_mainsectionlistelem_ifstatementwrapper(p):
    """
    MainSectionListElem : IFStatementWrapper
    """


def p_func_funcname(p):
    """
    Func : FuncName '(' ArgsList ')' OptionalSemiColon
    """


def p_funcname_write(p):
    """
    FuncName : WRITE
    """


def p_funcname_readln(p):
    """
    FuncName : READLN
    """


def p_funcname_writeln(p):
    """
    FuncName : WRITELN
    """


def p_argslist_argslist(p):
    """
    ArgsList : ArgsList ',' Arg
    """


def p_argslist_single(p):
    """
    ArgsList : Arg
    """


def p_argslist_empty(p):
    """
    ArgsList :
    """


def p_arg_string(p):
    """
    Arg : string
    """


def p_arg_id(p):
    """
    Arg : id
    """


def p_ifstatementwrapper_ifstatement(p):
    """
    IFStatementWrapper : IFStatement OptionalSemiColon
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Expression THEN Statement ELSE Statement
    """


def p_ifstatement_if_single(p):
    """
    IFStatement : IF Expression THEN Statement
    """


def p_statement_ifstatement(p):
    """
    Statement : IFStatement
    """


def p_statement_operation(p):
    """
    Statement : Operation
    """


def p_expression_id(p):
    """
    Expression : id ComparationSymbol id
    """


def p_comparationsymbol_gt(p):
    """
    ComparationSymbol : '>'
    """


def p_comparationsymbol_lt(p):
    """
    ComparationSymbol : '<'
    """


def p_operation_atrib(p):
    """
    Operation : Atrib
    """


def p_atrib_id(p):
    """
    Atrib : id ':' '=' id
    """


def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : ';'
    """


def p_optionalsemicolon_empty(p):
    """
    OptionalSemiColon :
    """


def p_error(p):
    parser.success = False
    if p:
        print(f"Syntax error at '{p.value}', line {
              p.lineno}, position {p.lexpos}")
    else:
        print("Syntax error at end of input")


parser = yacc.yacc()

texto = sys.stdin.read()
parser.success = True
parser.parse(texto)

if parser.success:
    print(f"Texto válido.\n")
else:
    print("Texto inválido...")
