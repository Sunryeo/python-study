# practice 1
# age = int(input("Input your age: "))
# print(f'age: {age}')
# if age < 65:
#     print('fee: 2000 KRW')
# else:
#     print('fee: 0 KRW')

# practice 2
# num = int(input("Input a number: "))
# result = 'not a multiple of 3 and 5'
#
# if num % 3 == 0:
#     result = 'a multiple of 3'
# if num % 5 == 0:
#     result = 'a multiple of 5'
# if num % 15 == 0:
#     result = 'a multiple of 3 and 5'
#
# print(f'{num} is {result}')

# practice 3
# num = int(input('Input a number: '))
#
# if num % 2 == 0:
#     print('Even!')
# else:
#     print('Odd!')

# practice 4
# ID = input('input your ID: ')
# PW = input('input your PW: ')
# result = ''
#
# if ID == 'Admin' and PW == 'Password':
#     result = 'Login success!'
# else:
#     result = 'Login fail!'
#
# print(result)

# practice 5
# num = int(input("Input a number: "))
# result = 'not a multiple of 3 and 5'
#
# if num % 3 == 0 and num % 5 == 0:
#     result = 'a multiple of 3 and 5'
# elif num % 3 == 0:
#     result = 'a multiple of 3'
# elif num % 5 == 0:
#     result = 'a multiple of 5'
#
# print(f'{num} is {result}')

# practice 6
APPLE_PRICE = 2000
ORANGE_PRICE = 3000
amount_of_apple = int(input("Input the number of apple to buy: "))
amount_of_orange = int(input("Input the number of orange to buy: "))
budget = int(input("Input your budget: "))
total_price = amount_of_apple * APPLE_PRICE + amount_of_orange * ORANGE_PRICE

if total_price > budget:
    rest = total_price - budget
    print(f'Cannot buy\n{rest} KWR needed!')
else:
    change = budget - total_price
    print(f'Change: {change}')



