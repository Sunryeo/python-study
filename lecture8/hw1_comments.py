'''
정말 잘 해주셨습니다 :) 
사실 모듈을 사용하면 편한 경우가 굉장히 많죠~ 잘 찾아서 사용해주셨네요!! ㅎㅎ

아래 주신 코멘트에대한 답변은 물론 가능하죠 :) w가 dictionary[f_letter]의 값 중 word와 같으면 is_exist를 True로 할당하고 싶으신거죠? 
해당 코드는 아래처럼 작성하시면 됩니다.
dictionary[f_letter]가 이미 리스트이기 떄문에, x in list 구문을 사용할 수 있는거죠 :)
is_exist = True if word in dictionary[f_letter] else False

코드 로직이 매우 견고하고 좋아요!! ㅎㅎ
'''


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


