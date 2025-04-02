def gen_code(parsed):
    if parsed[0] == "program":
        stmt = parsed[2]  
        return f"""start\n   {gen_code(stmt)}stop"""

    elif parsed[0] == "writeln":
        string = parsed[1]
        return f'pushs "{string}"\nwrites\nwriteln\n'
