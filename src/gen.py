import sys
from AST.tree import ASTNode

vars_dic = {}

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
        return f"// Program: {program_name}{var_list}\nstart{function_list}{main_block}\nstop\n"

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
    
    ########## Other ##########
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

                if primary.lower() == "writeln":
                    lines = []
                    for arg in args:
                        if arg in vars_dic: # write de um valor do dicionário
                            index = vars_dic[arg]["index"]
                            # continuar ............
                        else: # write de um valor literal
                            
                            lines.append(f'pushs "{arg}"')
                        lines.append("writes")
                    lines.append("writeln")
                    return "\n" + "\n".join(lines)

                elif primary.lower() == "write":
                    lines = []
                    for arg in args:
                        if arg in vars_dic: # write dic
                            index = vars_dic[arg]["index"]
                            # continuar ............
                        else: # write literal
                            lines.append(f'pushs "{arg}"')
                        lines.append("writes")
                    return "\n" + "\n".join(lines)

                elif primary.lower() == "readln":
                    lines = []
                    for arg in args:
                        if arg in vars_dic:
                            var_info = vars_dic[arg]
                            lines.append("read")
                            if var_info["type"].lower() == "integer":
                                lines.append("atoi")
                            lines.append(f"storeg {var_info['index']}")
                            lines.append("writeln")
                    return "\n" + "\n".join(lines)

        return primary

    
    else:
        print(f"Unhandled node type: {node.value}")
        return ""
