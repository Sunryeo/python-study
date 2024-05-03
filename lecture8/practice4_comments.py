'''
아이고,, 이 문제 제가 템플릿을 올리는걸 깜빨했네요!
템플릿 올려드렸으니 한번 문제 보시구 문제 풀어보세요!
아마 정말 잘 하실것 같긴 해요 ㅎㅎ
'''

lyrics = open('prac01.txt', 'r').readlines()
lyrics_words = [word for lyric in lyrics for word in lyric.split(" ")]

lyrics_set = set(lyrics_words)

for i, word in enumerate(lyrics_set):
    print(f"{word}의 개수: {lyrics_words.count(word)}")
