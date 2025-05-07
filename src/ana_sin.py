import sys
import ply.yacc as yacc
from ana_lex import tokens
from ana_lex import literals
from gen import gen_code


def p_program_program(p):
    """
    Program : PROGRAM id ';' OptionalVarList FunctionList Main
    """


def p_optionalvarlist_varsection(p):
    """
    OptionalVarList : VarSection
    """


def p_optionalvarlist(p):
    """
    OptionalVarList :
    """


def p_functionlist_functionlist(p):
    """
    FunctionList : FunctionList FunctionListElem
    """


def p_functionlist_functionlistelem(p):
    """
    FunctionList : FunctionListElem
    """


def p_functionlist_empty(p):
    """
    FunctionList :
    """


def p_functionlistelem_function(p):
    """
    FunctionListElem : FUNCTION FuncDefinition ':' id ';' OptionalVarList FunctionBody
    """


def p_functionlistelem_procedure(p):
    """
    FunctionListElem : PROCEDURE FuncDefinition ';' OptionalVarList FunctionBody
    """


def p_funcdefinition_id(p):
    """
    FuncDefinition : id Parameters
    """


def p_parameters_(p):
    """
    Parameters : '(' PairList ')'
    """


def p_parameters_empty(p):
    """
    Parameters :
    """


def p_pairlist_pairlist(p):
    """
    PairList : PairList ';' PairListElem
    """


def p_pairlist_pairlistelem(p):
    """
    PairList : PairListElem
    """


def p_pairlist_empty(p):
    """
    PairList :
    """


def p_pairlistelem_id(p):
    """
    PairListElem : id ':' id
    """


def p_functionbody_begin(p):
    """
    FunctionBody : BEGIN Body OptionalSemiColon END ';'
    """


def p_main_varsection(p):
    """
    Main : OptionalVarList MainSection
    """


def p_varsection_var(p):
    """
    VarSection : VAR VarsList
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
    VarsListElem : VarsListElemIDs ':' VarType ';'
    """


def p_vartype_id(p):
    """
    VarType : id
    """


def p_vartype_array(p):
    """
    VarType : ARRAY ArrayIndexes OF id
    """


def p_arrayindexes_(p):
    """
    ArrayIndexes : '[' num '.' '.' num ']'
    """


def p_arrayindexes_empty(p):
    """
    ArrayIndexes :
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
    MainSection : BEGIN Body OptionalSemiColon END '.' 
    """


def p_body_body(p):
    """
    Body : Body ';' BodyElem
    """


def p_body_bodyelem(p):
    """
    Body : BodyElem
    """


def p_bodyelem_factor(p):
    """
    BodyElem : Factor
    """


def p_bodyelem_atrib(p):
    """
    BodyElem : Atrib
    """


def p_bodyelem_forstatement(p):
    """
    BodyElem : FORStatement
    """


def p_bodyelem_ifstatement(p):
    """
    BodyElem : IFStatement
    """


def p_bodyelem_whilestatement(p):
    """
    BodyElem : WHILEStatement
    """


def p_argslist_argslist(p):
    """
    ArgsList : ArgsList ',' Arg
    """


def p_argslist_arg(p):
    """
    ArgsList : Arg
    """


def p_argslist_empty(p):
    """
    ArgsList :
    """


def p_arg_(p):
    """
    Arg : '(' Arg ')'
    """

def p_arg_exp(p):
    """
    Arg : Exp
    """


def p_forstatement_for(p):
    """
    FORStatement : FOR Atrib FORTo Exp DO FORBody
    """


def p_forto_to(p):
    """
    FORTo : TO
    """


def p_forto_downto(p):
    """
    FORTo : DOWNTO
    """

def p_forbody_begin(p):
    """
    FORBody : BEGIN Body OptionalSemiColon END
    """


def p_forbody_bodyelem(p):
    """
    FORBody : BodyElem
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN IFBody IFStatementCont
    """


def p_ifstatementcont_else(p):
    """
    IFStatementCont : ELSE IFBody
    """

def p_ifstatementcont_empty(p):
    """
    IFStatementCont : 
    """

def p_ifbody_begin(p):
    """
    IFBody : BEGIN Body OptionalSemiColon END
    """

def p_ifbody_bodyelem(p):
    """
    IFBody : BodyElem
    """

def p_whilestatement_while(p):
    """
    WHILEStatement : WHILE Condition DO WHILEBody
    """


def p_whilebody_begin(p):
    """
    WHILEBody : BEGIN Body OptionalSemiColon END
    """


def p_whilebody_bodyelem(p):
    """
    WHILEBody : BodyElem
    """


def p_condition_(p):
    """
    Condition : '(' Condition ')'
    """


def p_condition_logicexp(p):
    """
    Condition : Exp
    """


def p_atrib_suffixlistarray(p):
    """
    Atrib : id SuffixListArray ':' '=' Exp
    """


def p_comparationsymbol_gt(p):
    """
    ComparationSymbol : '>'
    """


def p_comparationsymbol_lt(p):
    """
    ComparationSymbol : '<'
    """


def p_comparationsymbol_e(p):
    """
    ComparationSymbol : '='
    """


def p_comparationsymbol_gte(p):
    """
    ComparationSymbol : '>' '='
    """


def p_comparationsymbol_lte(p):
    """
    ComparationSymbol : '<' '='
    """

def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : ';'
    """


def p_optionalsemicolon_empty(p):
    """
    OptionalSemiColon :
    """

def p_factor_primary(p):
    """
    Factor : Primary SuffixList
    """
def p_suffixlist_suffixlist(p):
    """
    SuffixList : SuffixList Suffix
    """

def p_suffixlist_(p):
    """
    SuffixList : 
    """

def p_suffix_(p):
    """
    Suffix : '(' ArgsList ')'
    """

def p_suffix_exp(p):
    """
    Suffix : '[' Exp ']'
    """

def p_suffixlistarray_arr(p):
    """
    SuffixListArray : '[' Exp ']' SuffixListArray
    """

def p_suffixlistarray_(p):
    """
    SuffixListArray : 
    """

def p_primary_num(p):
    """
    Primary : num
    """

def p_primary_string(p):
    """
    Primary : string
    """

def p_primary_boolean(p):
    """
    Primary : boolean
    """

def p_primary_id(p):
    """
    Primary : id
    """
    
def p_primary_exp(p):
    """
    Primary : '(' Exp ')'
    """

def p_termop_plus(p):
    """
    TermOp : '+'
    """

def p_termop_minus(p):
    """
    TermOp : '-'
    """

def p_factorop_mult(p):
    """
    FactorOp : '*'
    """

def p_factorop_div(p):
    """
    FactorOp : '/'
    """

def p_factorop_int_div(p):
    """
    FactorOp : DIV
    """

def p_factorop_mod(p):
    """
    FactorOp : MOD
    """

def p_exp_orexp(p):
    """
    Exp : OrExp
    """

def p_orexp_orexp(p):
    """
    OrExp : OrExp OR AndExp
    """

def p_orexp_andexp(p):
    """
    OrExp : AndExp
    """

def p_andexp_andexp(p):
    """
    AndExp : AndExp AND RelExp
    """

def p_andexp_relexp(p):
    """
    AndExp : RelExp
    """

def p_relexp_addexp_comp(p):
    """
    RelExp : AddExp ComparationSymbol AddExp
    """

def p_relexp_addexp(p):
    """
    RelExp : AddExp
    """

def p_addexp_addexp(p):
    """
    AddExp : AddExp TermOp MulExp
    """

def p_addexp_mulexp(p):
    """
    AddExp : MulExp
    """

def p_mulexp_mulexp(p):
    """
    MulExp : MulExp FactorOp Unary
    """

def p_mulexp_unary(p):
    """
    MulExp : Unary
    """

def p_unary_not(p):
    """
    Unary : NOT Unary
    """

def p_unary_primary(p):
    """
    Unary : Factor
    """


def p_error(p):
    parser.success = False
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}, position {p.lexpos}")
    else:
        print("Syntax error at end of input")
    print("Erro de sintaxe!")


parser = yacc.yacc()

texto = sys.stdin.read()
parser.success = True
parser.parse(texto)

if parser.success:
    print(f"Texto válido.\n")
else:
    print("Texto inválido...")
