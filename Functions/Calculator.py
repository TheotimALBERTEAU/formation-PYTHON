def Calculator(txt: str) -> int:
    operators = ["+", "-", "/", "*"]
    operator = ""
    operandes = []
    for i in txt:
        if i in operators:
            operator = i
            operandes = txt.split(i)
    if operator == '+':
        return int(operandes[0]) + int(operandes[1])
    elif operator == '-':
        return int(operandes[0]) - int(operandes[1])
    elif operator == '*':
        return int(operandes[0]) * int(operandes[1])
    else:
        return int(operandes[0]) / int(operandes[1])
