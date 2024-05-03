word = input("Input a word: ")
character = "i"
is_exist = False

for i in word:
    if i == character:
        is_exist = True
        break
    else:
        continue
else:
    print("\"i\" is not included")

if is_exist:
    print("\"i\" is included")