# practice 1
# value = input("What animal do you want to print?")
#
# def dog():
#     print(" /\\___/\\")
#     print("|  .  . |")
#     print("\\    .  /")
#     print("  _____ ")
#
# def cat():
#     cat = """
#     \\            /\\
#      )           ( ')
#       (         / )
#        \(_ _)    |
#     """
#     print(cat)
#
# def print_animal(value):
#     if value == 'dog':
#         dog()
#     elif value == 'cat':
#         cat()
#     else:
#         print(f"Cannot print {value}")
#
#
# print_animal(value)

# practice 2
population = {
    'KOREA': 51844675,
    'GERMANY': 83783942,
    'UK': 67886011,
    'USA': 331002651,
    'INDIA': 1380004385,
    'FRANCE': 65273511
    }

result = sorted(population.items(), key=lambda x: x[1], reverse=True)
print(dict(result))

# practice 3

