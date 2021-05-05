def nums(a, b, num): #Редач осторожно. Придушу если сломается
    if num == "+":
        print(int(a) + b)
    elif num == "-":
        print(int(a) - b)
    elif num == "*":
        print(int(a) * b)
    elif num == "/":
        print(int(a) / b)
    elif num == "%":
        print(int(a) % b)
    elif num == "**":
        print(int(a) ** b)
