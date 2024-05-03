def sum_func1():
    num1, num2 = map(int, input("Input two numbers: ").split())
    op = input("Input operator: ")

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '/':
        print(num1 // num2)
    elif op == '*':
        print(num1 * num2)


def sum_func2(num1: int, num2: int, op: str):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '/':
        print(num1 // num2)
    elif op == '*':
        print(num1 * num2)


def sum_func3() -> int:
    num1, num2 = map(int, input("Input two numbers: ").split())
    op = input("Input operator: ")
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '/':
        result = num1 // num2
    elif op == '*':
        result = num1 * num2
    else:
        result = None

    return result


def sum_func4(num1: int, num2: int, op: str) -> int:
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '/':
        result = num1 // num2
    elif op == '*':
        result = num1 * num2
    else:
        result = None

    return result
