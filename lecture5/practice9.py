inputNumber = input("Input a number: ")
length = len(inputNumber)

count = 0
for i, digit in enumerate(inputNumber, start=0):
    if count > length:
        break
    else:
        count += 1
        requiredZero = (length-1) - i
        print(f"1{'0'*requiredZero} digit: {digit}")