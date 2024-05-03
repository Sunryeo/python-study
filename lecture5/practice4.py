# 0: exit, 1: +, 2: -, 3: *, 4: /
inputOperator = int(input("Input a number: \n(0: exit, 1: +, 2: -, 3: *, 4: /)"))
is_operator = True

if inputOperator == 0:
    is_operator = False
if inputOperator > 4:
    is_operator = False
    print("Wrong number was input!")

if is_operator:
    firstNum = int(input("Input the first number: "))
    secondNum = int(input("Input the second number: "))
    if inputOperator == 1:
        print(f"{firstNum} + {secondNum} = {firstNum+secondNum}")
    elif inputOperator == 2:
        print(f"{firstNum} - {secondNum} = {firstNum-secondNum}")
    elif inputOperator == 3:
        print(f"{firstNum} * {secondNum} = {firstNum*secondNum}")
    elif inputOperator == 4:
        print(f"{firstNum} / {secondNum} = {firstNum/secondNum}")