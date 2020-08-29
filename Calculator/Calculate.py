def Calculate():

    def calculate():
        global stack
        global label
        result = 0
        operand2 = Decimal(stack.pop())
        operation = stack.pop()
        operand1 = Decimal(stack.pop())

        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2
        label.configure(text=str(result))
