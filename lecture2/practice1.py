word = 'I am happy!'

# print(word[0])
# print(len(word))


# def operation(num1, num2, operator):
#     if operator == '+':
#         print(int(num1 + num2))
#
#     if operator == '-':
#         print(int(num1 - num2))
#
#     if operator == '*':
#         print(int(num1 * num2))
#
#     if operator == '/':
#         print(int(num1 / num2))

# num = int(input("Input the number: "))
# print("divisor: ", num // 3)
# print("remains: ", num % 3)

# num1 = int(input('first number: '))
# num2 = int(input('second number: '))
# string = input('string: ')
# remains = int(num1 % num2)
# print('result: ', string*remains)

math = int(input('math score: '))
english = int(input('english score: '))
german = int(input('german score: '))
score_str = 'Scores'
average = (math + english + german) // 3
print(f"{score_str:_^21}")
print("{0:<10}{1}{2:>10}".format('Math', '|', math))
print("{0:<10}{1}{2:>10}".format('English', '|', english))
print("{0:<10}{1}{2:>10}".format('German', '|', german))
print("{0:<10}{1}{2:>10}".format('Average', '|', average))


