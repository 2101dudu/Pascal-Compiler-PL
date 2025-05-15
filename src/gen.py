import sys
from AST.tree import ASTNode

vars_dic = {}
while_id = 0
for_id = 0
if_id = 0

op_map = {
            "GT": "sup",
            "LT": "inf",
            "EQ": "equal",
            "NE": "nequal",
            "GE": "supeq",
            "LE": "infeq",
}

def gen_code(node : ASTNode) -> str:
    

    if node is None:
        return ""
    
    if isinstance(node, (str, int, float, bool)):
        return str(node)

    if not hasattr(node, 'value') or not hasattr(node, 'children'):
                raise ValueError(f"Expected an ASTNode, got {type(node)} instead", node)

    #print(node)

    if node.value == "program":
        program_name = gen_code(node.children[0])
        var_list = gen_code(node.children[1]) if len(node.children) > 1 and node.children[1] else ""
        function_list = gen_code(node.children[2]) if len(node.children) > 2 and node.children[2] else ""
        main_block = gen_code(node.children[3]) if len(node.children) > 3 and node.children[3] else ""
        return f"// Program: {program_name}{var_list}{function_list}\nstart{main_block}\nstop"

    ########## MAIN ##########
    elif node.value == "main":
        varsec = ""
        body = ""   
        if len(node.children) > 0 and node.children[0]:
            varsec = gen_code(node.children[0])
        if len(node.children) > 1 and node.children[1]:
            body = gen_code(node.children[1])
        return f"{varsec}{body}"
        
    elif node.value == "body":
        return "".join(gen_code(stmt) for stmt in node.children if stmt is not None)
    
    ########## FUNCTIONS ##########
    elif node.value == "functionlist":
        return "\n".join(gen_code(func) for func in node.children if func is not None)

    ########## VAR ##########
    elif node.value == "varsection":
        lines = []
        current_index = len(vars_dic)
        for var_decl in node.children:
            if var_decl.value == "var":
                var_ids_node = var_decl.children[0]
                var_type = var_decl.children[1]

                var_names = [gen_code(child) for child in var_ids_node.children]
                for i, var_name in enumerate(var_names):
                    vars_dic[var_name] = {
                        "index": current_index + i,
                        "type": var_type
                    }

                if isinstance(var_type, str):
                    lines.append(f"pushn {len(var_names)}")
        
        res = "\n".join(lines)
        return f"\n{res}"
    
    ########## IF ##########

    elif node.value == "if":
        global if_id
        label_else = f"ELSE{if_id}"
        label_end = f"ENDIF{if_id}"
        if_id += 1
        condition_child = gen_code(node.children[0])
        then_child = gen_code(node.children[1])
        else_child = gen_code(node.children[2]) if len(node.children) > 2 and node.children[2] else ""


        lines = []
        lines.append(condition_child)
        lines.append(f"\njz {label_else}")
        lines.append(then_child)
        lines.append(f"\njump {label_end}")
        lines.append(f"\n{label_else}:")
        
        if else_child:
            lines.append(else_child)
        lines.append(f"\n{label_end}:")
        

        return "".join(lines)
        
    ########## WHILE ##########
    elif node.value == "for":
        atrib = gen_code(node.children[0])
        
        global for_id
        
        label_for = f"FOR{for_id}"
        label_end = f"ENDFOR{for_id}"
        for_id += 1

        var_name = node.children[0].children[0].children[0] # FOR -> ATRIB -> VAR -> Var name
        var_index = vars_dic[var_name]["index"]

        for_to = node.children[1]
        
        expr = gen_code(node.children[2])
        expr_index = None
        if expr in vars_dic: # check if expr is a variable
            expr_index = vars_dic[expr]["index"]
            expr_string = f"\npushg {expr_index}"
        else: # check if expr is a literal
            if vars_dic[var_name]["type"] == "integer":
                expr_string = f"\npushi {expr}"
            if vars_dic[var_name]["type"] == "string":
                expr_string = f'\npushs "{expr}"'

        body = gen_code(node.children[3])

        cond = ""
        if for_to == "to": 
            cond = "inf"
        else:
            cond = "sup"
        
        lines = []
        lines.append(f"\n{label_for}:")
        lines.append(f"\npushg {var_index}")
        lines.append(f"\npushi {expr_index}")
        lines.append(f"\n{cond}")
        lines.append(f"\njz {label_end}")
        lines.append(body)
        lines.append(f"\npushg {var_index}")
        lines.append(f"\npushi 1")
        if cond == "inf":
            lines.append("\nadd")
        else:
            lines.append("\nsub")
        lines.append(f"\nstoreg {var_index}")
        lines.append(f"\njump {label_for}")
        lines.append(f"\n{label_end}:")

        return "".join(lines)

        

    ########## CONDITION ##########
    elif node.value in {"GT", "LT", "EQ", "NE", "GE", "LE"}:
        left = node.children[0]
        right = node.children[1]

        left_code = gen_code(left) if isinstance(left, ASTNode) else f"\npushg {vars_dic[left]['index']}"
        right_code = gen_code(right) if isinstance(right, ASTNode) else f"\npushg {vars_dic[right]['index']}"

        return f"{left_code}{right_code}\n{op_map[node.value]}"
    
    ########## OTHER ##########
    elif node.value == "Atrib":
        var_node = node.children[0]
        expr = node.children[1]

        var_name = var_node.children[0]
        var_index = vars_dic[var_name]["index"]

        var_array = var_node.children[1] if len(var_node.children) > 1 else None
        

        if var_array:
            # handle arrays
            return ""
        else: 
            expr_code = ""
            if expr in vars_dic:
                expr_index = vars_dic[expr]["index"]
                expr_code = f"\npushg {expr_index}"
            else:
                if vars_dic[var_name]["type"] == "integer":
                    expr_code = f"\npushi {expr}"
                if vars_dic[var_name]["type"] == "string":
                    expr_code = f'\npushs "{expr}"'
            
            return f"{expr_code}\nstoreg {var_index}"


    elif node.value == "Factor":
        if len(node.children) == 0:
            return ""
        
        primary = node.children[0]  # Ex: "writeln", "readln"
        suffix_node = node.children[1] if len(node.children) > 1 else None

        if isinstance(primary, str) and suffix_node and suffix_node.value == "suffix list":
            args = []
            list_nodes = [child for child in suffix_node.children]
            if len(list_nodes) == 1 and list_nodes[0].value == "arg list":
                args = list_nodes[0].children
                lines = []
                ## WRITELN ##
                if primary.lower() == "writeln":
                    for arg in args:
                        if isinstance(arg, ASTNode):
                            arg_code = gen_code(arg)
                            lines.append(arg_code)
                            lines.append("writes")
                        elif arg in vars_dic:  # write de variável
                            var_info = vars_dic[arg]
                            lines.append(f"pushg {var_info['index']}")
                            if var_info["type"].lower() == "integer":
                                lines.append("writei")
                            else:
                                lines.append("writes")
                        else:  # write de literal
                            lines.append(f'pushs "{arg}"')
                            lines.append("writes")
                    lines.append("writeln")
                    return "\n" + "\n".join(lines)
                
                ## WRITE ##
                elif primary.lower() == "write":
                    for arg in args:
                        if isinstance(arg, ASTNode):
                            arg_code = gen_code(arg)
                            lines.append(arg_code)
                            lines.append("writes")
                        elif arg in vars_dic:  # write de variável
                            var_info = vars_dic[arg]
                            lines.append(f"pushg {var_info['index']}")
                            if var_info["type"].lower() == "integer":
                                lines.append("writei")
                            else:
                                lines.append("writes")
                        else:  # write de literal
                            lines.append(f'pushs "{arg}"')
                            lines.append("writes")
                    return "\n" + "\n".join(lines)
                ## READLN ##
                elif primary.lower() == "readln":

                    for arg in args:
                        if arg in vars_dic:
                            var_info = vars_dic[arg]
                            lines.append("read")
                            if var_info["type"].lower() == "integer":
                                lines.append("atoi")
                            lines.append(f"storeg {var_info['index']}")
                            lines.append("writeln")
                    return "\n" + "\n".join(lines)
            # ELSE ARRAY
        return primary

    
    else:
        print(f"Unhandled node type: {node.value}")
        return ""
