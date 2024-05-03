# together
# numbers = list(range(2, 101, 2))
# first_five = numbers[:5]
# last_seven = numbers[-7:]
#
# print(first_five)
# print(last_seven)

# practice1
# evenNumList = list(range(2, 101, 2))
# inputNum = map(int, input("Input 4 numbers: "))
# inputList = list(inputNum)
# minNum = inputList[0] if inputList[0] < inputList[1] else inputList[1]
# maxNum = inputList[1] if inputList[1] > inputList[0] else inputList[0]
#
# print(evenNumList[minNum:maxNum])
#
# minusMinNum = inputList[2] if inputList[2] > inputList[3] else inputList[3]
# minusMaxNum = inputList[3] if inputList[3] < inputList[2] else inputList[2]
#
# print(-minusMinNum, -minusMaxNum)
# print(evenNumList[-minusMinNum:-minusMaxNum])

# practice2
# setList = []
# print(f"Initial list: {setList}")
#
# for _ in range(0, 3):
#     inputNum = int(input("Input a number: "))
#     setList.append(inputNum)
#     print(f"Current List: {setList}")

# practice3
# list_ = []
# while True:
#     action = int(input("1) Add 2) Remove 3) Exit: "))
#     print(f"Current List: {list_}")
#
#     if action == 1:
#         list_.append(int(input("Input a number: ")))
#     elif action == 2:
#         list_.remove(int(input("What element do you want to remove?: ")))
#     elif action == 3:
#         exit()
#
#     print(f"Modified list: {list_}")

# practice 4
prime_list = []
num = int(input("Input a number: "))
for i in range(2, num+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        prime_list.append(i)

print(f"Prime numbers are {prime_list}")