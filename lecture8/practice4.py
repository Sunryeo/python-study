lyrics = open('prac01.txt', 'r').readlines()
lyrics_words = [word for lyric in lyrics for word in lyric.split(" ")]

lyrics_set = set(lyrics_words)

for i, word in enumerate(lyrics_set):
    print(f"{word}의 개수: {lyrics_words.count(word)}")
