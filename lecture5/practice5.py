firstNum = int(input("Input a first number: "))
secondNum = int(input("Input a second number: "))
thirdNum = int(input("Input a third number: "))

first = 0
second = 0
third = 0
# a/b, b/c, c/a

# 1>2
if firstNum > secondNum:
    third = firstNum
    # 1>3
    if firstNum > thirdNum:
        # 2>3
        if secondNum > thirdNum:
            second = secondNum
            first = thirdNum
        # 3>2
        else:
            second = thirdNum
            first = secondNum
    # 3>1
    else:
        third = thirdNum
        second = firstNum
        first = secondNum
# 2>3
elif secondNum > thirdNum:
    third = secondNum
    # 2>1
    if secondNum > firstNum:
        # 1>3
        if firstNum > thirdNum:
            second = firstNum
            first = thirdNum
        # 3>1
        else:
            second = thirdNum
            first = firstNum
    # 3>2
    else:
        third = thirdNum
        second = secondNum
        first = firstNum
# 3>1
elif thirdNum > firstNum:
    third = thirdNum
    # 3>2
    if thirdNum > secondNum:
        # 1>2
        if firstNum > secondNum:
            second = firstNum
            first = secondNum
        # 2>1
        else:
            second = secondNum
            first = firstNum
    # 2>3
    else:
        third = secondNum
        second = thirdNum
        first = firstNum

print(f"오름차순 정렬: {first} {second} {third}")
