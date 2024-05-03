# practice1
# dict_ex = dict()
# dict_ex["nationality"] = "korea"
# dict_ex["hometown"] = "seoul"
#
# print(dict_ex)
# dict_ex["nationality"] = "germany"
# print(dict_ex)

# practice2
# name = input("Input your name: ")
# birthday = input("Input your birthday: ")
# gender = input("Input your gender: ")
#
# info_dict = dict()
# info_dict["name"] = name
# info_dict["birthday"] = birthday
# info_dict["gender"] = gender
#
# print(f"Hello my name is {info_dict['name']}"
#       f"\nMy birthday is {info_dict['birthday']}"
#       f"\nI am a {info_dict['gender']}")

# practice3
# is_run = True
# keys = ['fruit', 'beverage', 'fresh']
# cart = {key: [] for key in keys}
#
# while is_run:
#     choice = int(input("1. fruit 2. beverage 3. fresh 0. exit: "))
#
#     if choice == 0:
#         for key, value in cart.items():
#             print(f"{key}: {value}")
#         exit()
#
#     your_item = input("Add your item: ")
#     cart_key = "fruit" if choice == 1 else 'beverage' if choice == 2 else 'fresh'
#
#     cart[cart_key].append(your_item)

# practice4
# students = []
# total_avg = 0
# for _ in range(2):
#     student = dict()
#     student['name'] = input("Input a student name: ")
#     student['kor'] = int(input(f"Input {student['name']}'s kor score: "))
#     student['eng'] = int(input(f"Input {student['name']}'s eng score: "))
#     student['math'] = int(input(f"Input {student['name']}'s math score: "))
#     student['avg'] = (student['kor'] + student['eng'] + student['math']) // 3
#     total_avg += student['avg']
#
#     students.append(student)
#
# total_avg //= 2
#
# print('='*(5+5*2+1))
# for key in students[0].keys():
#     text = ''.join(f"{students[i][key]:>5}" for i in range(2))
#     print(f"{key:<5}: {text}")
#
# print(f"Total average: {total_avg}")
