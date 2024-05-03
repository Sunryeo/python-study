from string import ascii_lowercase

alpha_list = list(ascii_lowercase)

dictionary = {alpha: [] for alpha in alpha_list}
while True:
    is_exist = False
    action = int(input("1. Add, 2. Search, 3. Exit: "))

    if action == 3:
        print("Finish dictionary!")
        exit()

    word = input("Input a word: ")
    f_letter = word[0]

    for w in dictionary[f_letter]:
        if w == word:
            is_exist = True

    # is_exist = [True if w == word else False for w in dictionary[f_letter]]
    """
    위 for loop을 간단하게 comprehension으로 구현할 수 있을 것 같은데 21번 라인 코드처럼 배열로 밖에 구현을 못했어요. is_exist의 값을 boolean으로 할당할 수 있는 
    comprehension 구현법이 있을까요?
    """

    if action == 1:
        if not is_exist:
            dictionary[f_letter].append(word)
        print(f"{word} added!")

    elif action == 2:
        if not is_exist:
            print(f"{word} cannot find!")
        else:
            print(f"{word} found!")


