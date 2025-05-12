import sys
from AST.tree import ASTNode

def gen_code(node):

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
        return f"// Program: {program_name}\nstart{var_list}{function_list}{main_block}\nstop\n"

    elif node.value == "main":
        if len(node.children) > 1 and node.children[1]:
            return gen_code(node.children[1])
        else:
            return ""
        
    elif node.value == "body":
        return "\n".join(gen_code(stmt) for stmt in node.children if stmt is not None)

    elif node.value == "Factor":
        if len(node.children) == 0:
            return ""
        primary = gen_code(node.children[0])
        if len(node.children) > 1 and node.children[1]:
            suffix_list = gen_code(node.children[1])
            if primary == "writeln":
                return f'\npushs "{suffix_list}"\nwrites\nwriteln'
        return primary

    elif node.value == "suffix list":
        if node.children and hasattr(node.children[0], 'value'):
            return gen_code(node.children[0])
        return ""

    elif node.value == "arg list":
        if node.children:
            return node.children[0] if isinstance(node.children[0], str) else gen_code(node.children[0])
        return ""

    elif node.value == "functionlist":
        return "\n".join(gen_code(func) for func in node.children if func is not None)

    else:
        print(f"Unhandled node type: {node.value}")
        return ""
