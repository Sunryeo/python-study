firstNum = int(input("Input the first number: "))
secondNum = int(input("Input the second number: "))
firstDigit = firstNum % 10
secondDigit = secondNum % 10

if firstNum + secondNum > 100:
    print("범위 초과!")
elif firstDigit + secondDigit > 10:
    print("받아 올림 됨!")
else:
    print("받아 올려지지 않음.")