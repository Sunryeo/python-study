firstNum = int(input("Input the first number: "))
secondNum = int(input("Input the second number: "))

start = 0
finish = 0

if firstNum > secondNum:
    start = secondNum+1
    finish = firstNum
else:
    start = firstNum+1
    finish = secondNum

count = 0
for i in range(start, finish):
    if count > 3:
        break
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}*{j}={i*j}")
        print()
        count += 1
    else:
        pass