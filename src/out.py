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


def p_varsection_dontforgettoremove(p):
    """
    VarSection : DONTFORGETTOREMOVE
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
    VarsListElem : VarsListElemIDs ':' id ';'
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


def p_func_id(p):
    """
    Func : id '(' ArgsList ')'
    """


def p_argslist_argslist(p):
    """
    ArgsList : ArgsList ',' Arg
    """


def p_argslist_arg(p):
    """
    ArgsList : Arg
    """


def p_argslist_dontforgettoremove(p):
    """
    ArgsList : DONTFORGETTOREMOVE
    """


def p_arg_string(p):
    """
    Arg : string
    """


def p_arg_id(p):
    """
    Arg : id
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN Statement ELSE Statement
    """


def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN Statement
    """


def p_statement_ifstatement(p):
    """
    Statement : IFStatement
    """


def p_statement_operation(p):
    """
    Statement : Operation
    """


def p_condition_id(p):
    """
    Condition : id ComparationSymbol id
    """


def p_comparationsymbol_(p):
    """
    ComparationSymbol : '>'
    """


def p_comparationsymbol_(p):
    """
    ComparationSymbol : '<'
    """


def p_comparationsymbol_(p):
    """
    ComparationSymbol : '='
    """


def p_operation_atrib(p):
    """
    Operation : Atrib
    """


def p_atrib_id(p):
    """
    Atrib : id ':' '=' Val
    """


def p_exp_exp(p):
    """
    Exp : Exp '+' Term
    """


def p_exp_exp(p):
    """
    Exp : Exp '-' Term
    """


def p_exp_term(p):
    """
    Exp : Term
    """


def p_term_term(p):
    """
    Term : Term '*' Factor
    """


def p_term_term(p):
    """
    Term : Term '/' Factor
    """


def p_term_factor(p):
    """
    Term : Factor
    """


def p_factor_exp(p):
    """
    Factor : Exp
    """


def p_factor_num(p):
    """
    Factor : num
    """


def p_factor_id(p):
    """
    Factor : id
    """


def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : ';'
    """


def p_optionalsemicolon_dontforgettoremove(p):
    """
    OptionalSemiColon : DONTFORGETTOREMOVE
    """


def p_forstatement_for(p):
    """
    FORStatement : FOR Atrib TO id DO FORBody
    """


def p_forbody_forstatement(p):
    """
    FORBody : FORStatement
    """


def p_forbody_begin(p):
    """
    FORBody : BEGIN MainSectionList END ';'
    """


def p_forbody_mainsectionlistelem(p):
    """
    FORBody : MainSectionListElem
    """
