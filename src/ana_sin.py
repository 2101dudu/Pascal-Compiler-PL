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


def p_arrayindexes(p):
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
    MainSectionListElem : Func OptionalSemiColon
    """


def p_mainsectionlistelem_atrib(p):
    """
    MainSectionListElem : Atrib OptionalSemiColon
    """


def p_mainsectionlistelem_forstatement(p):
    """
    MainSectionListElem : FORStatement OptionalSemiColon
    """


def p_mainsectionlistelem_ifstatement(p):
    """
    MainSectionListElem : IFStatement OptionalSemiColon
    """


def p_mainsectionlistelem_whilestatement(p):
    """
    MainSectionListElem : WHILEStatement OptionalSemiColon
    """


def p_func_id(p):
    """
    Func : id '(' ArgsList ')'
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


def p_arg_wrapper(p):
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
    FORStatement : FOR Atrib TO NumExp DO FORBody
    """


def p_forbody_forstatement(p):
    """
    FORBody : FORStatement
    """


def p_forbody_begin(p):
    """
    FORBody : BEGIN MainSectionList END OptionalSemiColon
    """


def p_forbody_mainsectionlistelem(p):
    """
    FORBody : MainSectionListElem
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN MainSectionListElem ELSE MainSectionListElem
    """


def p_ifstatement_if_single(p):
    """
    IFStatement : IF Condition THEN MainSectionListElem
    """


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
    WHILEBody : BEGIN MainSectionList END OptionalSemiColon
    """


def p_whilebody_mainsectionlistelem(p):
    """
    WHILEBody : MainSectionListElem
    """


def p_condition_wrapper(p):
    """
    Condition : '(' Condition ')'
    """


def p_condition_logicexp(p):
    """
    Condition : LogicExp
    """


def p_atrib_id(p):
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


def p_numterm_numterm_mod(p):
    """
    NumTerm : NumTerm MOD NumFactor
    """


def p_numterm_numfactor(p):
    """
    NumTerm : NumFactor
    """


def p_numfactor_numexp(p):
    """
    NumFactor : '(' NumExp ')'
    """


def p_numfactor_num(p):
    """
    NumFactor : num
    """


def p_numfactor_arrayelem(p):
    """
    NumFactor : ArrayElem
    """


def p_numfactor_id(p):
    """
    NumFactor : id
    """


def p_comparationsymbol_gt(p):
    """
    ComparationSymbol : '>'
    """


def p_comparationsymbol_lt(p):
    """
    ComparationSymbol : '<'
    """


def p_comparationsymbol_eq(p):
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


def p_booleanfactor_wrapper(p):
    """
    BooleanFactor : '(' Exp ')'
    """


def p_booleanfactor_boolean(p):
    """
    BooleanFactor : boolean
    """


def p_booleanfactor_num(p):
    """
    BooleanFactor : num
    """


def p_booleanfactor_arrayelem(p):
    """
    BooleanFactor : ArrayElem
    """


def p_booleanfactor_id(p):
    """
    BooleanFactor : id
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


def p_logicfactor_logicexp(p):
    """
    LogicFactor : '(' LogicExp ')'
    """


def p_logicfactor_booleanexp(p):
    """
    LogicFactor : BooleanExp
    """


def p_optionalsemicolon_single(p):
    """
    OptionalSemiColon : ';'
    """


def p_optionalsemicolon_empty(p):
    """
    OptionalSemiColon :
    """


def p_arrayelem_id(p):
    """
    ArrayElem : id '[' id ']'
    """


def p_error(p):
    parser.success = False
    if p:
        print(f"Syntax error at '{p.value}', line {
              p.lineno}, position {p.lexpos}")
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
