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
    FunctionBody : BEGIN Body END ';'
    """


def p_main_varsection(p):
    """
    Main : OptionalVarList MainSection
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
    MainSection : BEGIN Body END '.'
    """


def p_body_body(p):
    """
    Body : Body BodyElem
    """


def p_body_bodyelem(p):
    """
    Body : BodyElem
    """


def p_bodyelem_func(p):
    """
    BodyElem : Func OptionalSemiColon
    """


def p_bodyelem_atrib(p):
    """
    BodyElem : Atrib OptionalSemiColon
    """


def p_bodyelem_forstatement(p):
    """
    BodyElem : FORStatement OptionalSemiColon
    """


def p_bodyelem_ifstatement(p):
    """
    BodyElem : IFStatement OptionalSemiColon
    """


def p_bodyelem_whilestatement(p):
    """
    BodyElem : WHILEStatement OptionalSemiColon
    """


def p_func_id(p):
    """
    Func : id ArgSection
    """

def p_argsection(p):
    """
    ArgSection : '(' ArgsList ')'
    """

def p_argsection_empty(p):
    """
    ArgSection :
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


def p_arg_string(p):
    """
    Arg : string
    """


def p_arg_exp(p):
    """
    Arg : Exp
    """


def p_forstatement_for(p):
    """
    FORStatement : FOR Atrib FORTo NumExp DO FORBody
    """


def p_forto_to(p):
    """
    FORTo : TO
    """


def p_forto_downto(p):
    """
    FORTo : DOWNTO
    """


def p_forbody_forstatement(p): ## Necessário?
    """
    FORBody : FORStatement
    """


def p_forbody_begin(p):
    """
    FORBody : BEGIN Body END OptionalSemiColon
    """


def p_forbody_bodyelem(p):
    """
    FORBody : BodyElem
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN IFBody ELSE IFBody
    """


def p_ifstatement_if_single(p):
    """
    IFStatement : IF Condition THEN IFBody
    """

################## Exatamente igual ao FORBody (mentemos?)
def p_ifbody_begin(p):
    """
    IFBody : BEGIN Body END OptionalSemiColon
    """

def p_ifbody_bodyelem(p):
    """
    IFBody : BodyElem
    """
##########################################################

def p_whilestatement_while(p):
    """
    WHILEStatement : WHILE Condition DO WHILEBody
    """


def p_whilebody_whilestatement(p):
    """
    WHILEBody : WHILEStatement
    """


def p_whilebody_begin(p):
    """
    WHILEBody : BEGIN Body END OptionalSemiColon
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
    Condition : LogicExp
    """


def p_atrib_idwrapper(p):
    """
    Atrib : IDWrapper ':' '=' Exp
    """


def p_idwrapper_(p):
    """
    IDWrapper : '(' IDWrapper ')'
    """


def p_idwrapper_arrayelem(p):
    """
    IDWrapper : ArrayElem
    """


def p_idwrapper_id(p):
    """
    IDWrapper : id
    """


def p_exp_numexp(p):
    """
    Exp : NumExp
    """


def p_exp_booleanexp(p):
    """
    Exp : BooleanExp
    """


def p_exp_logicexp(p):
    """
    Exp : LogicExp
    """


def p_numexp_numexp_add(p):
    """
    NumExp : NumExp '+' NumTerm
    """


def p_numexp_numexp_sub(p):
    """
    NumExp : NumExp '-' NumTerm
    """


def p_numexp_numterm(p):
    """
    NumExp : NumTerm
    """


def p_numterm_numterm_mul(p):
    """
    NumTerm : NumTerm '*' NumFactor
    """


def p_numterm_numterm_div(p):
    """
    NumTerm : NumTerm '/' NumFactor
    """


def p_numterm_numterm_whole_div(p):
    """
    NumTerm : NumTerm DIV NumFactor
    """


def p_numterm_numterm(p):
    """
    NumTerm : NumTerm MOD NumFactor
    """


def p_numterm_numfactor(p):
    """
    NumTerm : NumFactor
    """


def p_numfactor_(p):
    """
    NumFactor : '(' NumExp ')'
    """


def p_numfactor_primary(p):
    """
    NumFactor : Primary
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


def p_booleanexp_booleanexp(p):
    """
    BooleanExp : BooleanExp ComparationSymbol BooleanExp
    """


def p_booleanexp_booleanfactor(p):
    """
    BooleanExp : BooleanFactor
    """


def p_booleanfactor_(p):
    """
    BooleanFactor : '(' Exp ')'
    """


def p_booleanfactor_boolean(p):
    """
    BooleanFactor : boolean
    """


def p_booleanfactor_string(p):
    """
    BooleanFactor : string
    """

def p_booleanfactor_primary(p):
    """
    BooleanFactor : Primary
    """


def p_logicexp_logicexp(p):
    """
    LogicExp : LogicExp OR LogicTerm
    """


def p_logicexp_logicterm(p):
    """
    LogicExp : LogicTerm
    """


def p_logicterm_logicterm(p):
    """
    LogicTerm : LogicTerm AND LogicNot
    """


def p_logicterm_logicnot(p):
    """
    LogicTerm : LogicNot
    """


def p_logicnot_not(p):
    """
    LogicNot : NOT LogicFactor
    """


def p_logicnot_logicfactor(p):
    """
    LogicNot : LogicFactor
    """


def p_logicfactor_(p):
    """
    LogicFactor : '(' LogicExp ')'
    """


def p_logicfactor_booleanexp(p):
    """
    LogicFactor : BooleanExp
    """


def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : ';'
    """


def p_optionalsemicolon_empty(p):
    """
    OptionalSemiColon :
    """


def p_arrayelem_id(p):
    """
    ArrayElem : id '[' Exp ']'
    """

def p_primary_num(p):
    """
    Primary : num
    """

def p_primary_id(p):
    """
    Primary : id
    """

def p_primary_func(p):
    """
    Primary : Func
    """

def p_primary_arrayelem(p):
    """
    Primary : ArrayElem
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
