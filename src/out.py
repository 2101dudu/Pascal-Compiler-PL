def p_program_program(p):
    """
    Program : PROGRAM id ';' OptionalVarList FunctionList Main
    """

def p_optionalvarlist_varsection(p):
    """
    OptionalVarList : VarSection
    """

def p_optionalvarlist_(p):
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

def p_functionlist_(p):
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

def p_parameters_(p):
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

def p_pairlist_(p):
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

def p_main_optionalvarlist(p):
    """
    Main : OptionalVarList MainSection
    """

def p_varsection_var(p):
    """
    VarSection : VAR VarsList
    """

def p_varsection_(p):
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

def p_arrayindexes_(p):
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

def p_bodyelem_factor(p):
    """
    BodyElem : Factor OptionalSemiColon
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

def p_argslist_argslist(p):
    """
    ArgsList : ArgsList ',' Arg
    """

def p_argslist_arg(p):
    """
    ArgsList : Arg
    """

def p_argslist_(p):
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

def p_forbody_forstatement(p):
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

def p_ifstatement_if(p):
    """
    IFStatement : IF Condition THEN IFBody
    """

def p_ifbody_begin(p):
    """
    IFBody : BEGIN Body END OptionalSemiColon
    """

def p_ifbody_bodyelem(p):
    """
    IFBody : BodyElem
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

def p_idwrapper_factor(p):
    """
    IDWrapper : Factor
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

def p_comparationsymbol_(p):
    """
    ComparationSymbol : '>' '='
    """

def p_comparationsymbol_(p):
    """
    ComparationSymbol : '<' '='
    """

def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : ';'
    """

def p_optionalsemicolon_(p):
    """
    OptionalSemiColon : 
    """

def p_factor_primary(p):
    """
    Factor : Primary SuffixList
    """

def p_suffix_(p):
    """
    Suffix : '(' ArgsList ')'
    """

def p_suffix_(p):
    """
    Suffix : '[' Exp ']'
    """

def p_suffixlist_suffixlist(p):
    """
    SuffixList : SuffixList Suffix
    """

def p_suffixlist_(p):
    """
    SuffixList : 
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

def p_primary_(p):
    """
    Primary : '(' Exp ')'
    """

def p_termop_(p):
    """
    TermOp : '+'
    """

def p_termop_(p):
    """
    TermOp : '-'
    """

def p_factorop_(p):
    """
    FactorOp : '*'
    """

def p_factorop_(p):
    """
    FactorOp : '/'
    """

def p_factorop_div(p):
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

def p_relexp_addexp(p):
    """
    RelExp : AddExp
    """

def p_relexp_addexp(p):
    """
    RelExp : AddExp ComparationSymbol AddExp
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
    Unary : Primary SuffixList
    """

