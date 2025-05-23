import sys
from AST.tree import ASTNode

vars_dic = {}
while_id = 0
for_id = 0
if_id = 0

op_map = {
            "GT": "sup",
            "GTE": "supeq",
            "LT": "inf",
            "LTE": "infeq",
            "EQ": "equal",
            "NE": "nequal",
            "GE": "supeq",
            "LE": "infeq",
}

def gen_code(node : ASTNode) -> str:
    

    if node is None:
        return ""
    
    if isinstance(node, int):
        return f"\npushi {node}"
    
    if isinstance(node, str):
        if node in ["true", "false"]:
            return "\npushi 1" if node == "true" else "\npushi 0"

        if node in vars_dic:
            var_info = vars_dic[node]
            return f"\npushg {var_info['index']}"
        else:
            return f'\npushs "{node}"\nchrcode'

    if isinstance(node, float):
        return f"\npushf {node}"

    if not hasattr(node, 'value') or not hasattr(node, 'children'):
                raise ValueError(f"Expected an ASTNode, got {type(node)} instead", node)

    #print(node)

    if node.value == "program":
        program_name = node.children[0]
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

                var_names = [str(child) for child in var_ids_node.children]
                for var_name in var_names:
                    if isinstance(var_type, ASTNode) and var_type.value == "array":
                        array_indexes = var_type.children[0]
                        size = array_indexes.children[1] - array_indexes.children[0] + 1

                        vars_dic[var_name] = {
                            "index": current_index,
                            "type": var_type,
                            "size": size,
                            "start_index": array_indexes.children[0],
                            "type_array": str(var_type.children[1])
                        }
                        current_index += size
                    else:   
                        vars_dic[var_name] = {
                            "index": current_index,
                            "type": var_type
                        }
                        current_index += 1

                if isinstance(var_type, str):
                    lines.append(f"pushn {len(var_names)}")
                elif isinstance(var_type, ASTNode) and var_type.value == "array":
                    lines.append(f"pushn {len(var_names) * vars_dic[var_name]['size']}")
        
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
    elif node.value == "while":
        global while_id

        label_while = f"WHILE{while_id}"
        label_end = f"ENDWHILE{while_id}"
        while_id += 1

        condition_child = gen_code(node.children[0])
        body_child = gen_code(node.children[1])

        lines = []
        lines.append(f"\n{label_while}:")
        lines.append(condition_child)
        lines.append(f"\njz {label_end}")
        lines.append(body_child)
        lines.append(f"\njump {label_while}")
        lines.append(f"\n{label_end}:")

        return "".join(lines)


    ########## FOR ##########
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

        body = gen_code(node.children[3])

        cond = ""
        if for_to == "to": 
            cond = "infeq"
        else:
            cond = "supeq"
        
        lines = []
        lines.append(atrib)
        lines.append(f"\n{label_for}:")
        lines.append(f"\npushg {var_index}")
        lines.append(f"{expr}")
        lines.append(f"\n{cond}")
        lines.append(f"\njz {label_end}")
        lines.append(body)
        lines.append(f"\npushg {var_index}")
        lines.append(f"\npushi 1")
        if cond == "infeq":
            lines.append("\nadd")
        else:
            lines.append("\nsub")
        lines.append(f"\nstoreg {var_index}")
        lines.append(f"\njump {label_for}")
        lines.append(f"\n{label_end}:")

        return "".join(lines)

        

    ########## COMPARATION ##########
    elif node.value in op_map:
        left = node.children[0]
        right = node.children[1]

        left_code = gen_code(left)
        right_code = gen_code(right)

        return f"{left_code}{right_code}\n{op_map[node.value]}"
    
    elif node.value in {"AND", "OR", "NOT"}:
        left = node.children[0]
        right = node.children[1] if len(node.children) > 1 else None
        
        if node.value == "AND":
            left_code = gen_code(left)
            right_code = gen_code(right)
            return f"{left_code}{right_code}\nand"
        elif node.value == "OR":
            left_code = gen_code(left)
            right_code = gen_code(right)
            return f"{left_code}{right_code}\nor"
        elif node.value == "NOT":
            left_code = gen_code(left)
            return f"{left_code}\nnot"
    
    ########## OTHER ##########
    elif node.value == "Atrib":
        var_node = node.children[0]
        expr = gen_code(node.children[1])

        var_name = var_node.children[0]
        var_index = vars_dic[var_name]["index"]

        var_array = var_node.children[1] if len(var_node.children) > 1 else None
        

        if var_array:
            # handle arrays
            var_info = vars_dic[var_name]
            arr_index = var_array.children[0]
            if isinstance(arr_index, str):
                if arr_index in vars_dic:
                    arr_index = vars_dic[arr_index]["index"]

                return f"\npushgp\npushi {var_info['index']}\npushg {arr_index}\npushi {var_info['start_index']}\nsub\nadd{expr}\nstoren"
            
            elif isinstance(arr_index, int):
                return f"\npushgp\npushg {var_info['index'] + (arr_index - var_info['start_index'])}\n{expr}\nstoren"

        else: 
            return f"{expr}\nstoreg {var_index}"

    elif node.value in {"+", "-", "*", "/"}:
        left = node.children[0]
        right = node.children[1]

        left_code = gen_code(left)
        right_code = gen_code(right)

        if node.value == "+":
            return f"{left_code}{right_code}\nadd"
        elif node.value == "-":
            return f"{left_code}{right_code}\nsub"
        elif node.value == "*":
            return f"{left_code}{right_code}\nmul"
        elif node.value == "/":
            return f"{left_code}{right_code}\nfdiv" # for real division
        
    elif node.value in {"div", "mod"}:
        left = node.children[0]
        right = node.children[1]

        left_code = gen_code(left)
        right_code = gen_code(right)

        if node.value == "div":
            return f"{left_code}{right_code}\ndiv"
        elif node.value == "mod":
            return f"{left_code}{right_code}\nmod"


    elif node.value == "Factor":
        if len(node.children) == 0:
            return ""
        
        primary = node.children[0]  # Ex: "writeln", "readln"
        suffix_node = node.children[1] if len(node.children) > 1 else None

        if isinstance(primary, str) and suffix_node and suffix_node.value == "suffix list":
            args = []
            list_nodes = [child for child in suffix_node.children]
            if len(list_nodes) == 1 and isinstance(list_nodes[0], ASTNode) and list_nodes[0].value == "arg list":
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

                        # arrays
                        elif isinstance(arg, ASTNode) and arg.value == "Factor":
                            var_info = vars_dic[arg.children[0]]
                            
                            #TODO: allow multiple dimensions
                            arr_index = arg.children[1].children[0]
                            if isinstance(arr_index, str):
                                if arr_index in vars_dic:
                                    arr_index = vars_dic[arr_index]["index"]

                                lines.append(f"pushgp\npushi {var_info['index']}\npushg {arr_index}\npushi {var_info['start_index']}\nsub\nadd")
                            elif isinstance(arr_index, int):
                                lines.append(f"pushgp\npushg {var_info['index'] + (arr_index - var_info['start_index'])}")

                            lines.append("read")
                            if var_info["type_array"].lower() == "integer":
                                lines.append("atoi")
                            
                            lines.append("storen")                            

                    return "\n" + "\n".join(lines)
                elif primary.lower() == "length":
                    for arg in args:
                        if isinstance(arg, str):
                            arg_code = gen_code(arg)
                            return f"{arg_code}\nstrlen"
                
                else:
                    print(f"Unhandled function call: {primary}")
                    return ""
            # handle arrays
            else:
                #TODO: allow multiple dimensions

                var_info = vars_dic[primary]
                arr_index = list_nodes.pop()
                if isinstance(arr_index, str):
                    if arr_index in vars_dic:
                        arr_index = vars_dic[arr_index]["index"]

                    if var_info["type"] == "array":
                        return f"\npushgp\npushi {var_info['index']}\npushg {arr_index}\npushi {var_info['start_index']}\nsub\nadd\nloadn"
                    elif var_info["type"] == "string":
                        return f"\npushg {var_info['index']}\npushg {arr_index}\npushi 1\nsub\ncharat"
                        
                elif isinstance(arr_index, int):
                    if var_info["type"] == "array":
                        return f"\npushgp\npushg {var_info['index'] + (arr_index - var_info['start_index'])}\nloadn"
                    elif var_info["type"] == "string":
                        f"\npushg {var_info['index']}\npushi {arr_index}\npushi 1\nsub\ncharat"
                
        return primary

    
    else:
        print(f"Unhandled node type: {node.value}")
        return ""
