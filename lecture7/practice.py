# practice1
# text = open('prac01.txt', 'r').readlines()
#
# info_list = []
# for person in text:
#     new_list = []
#     info = person.split(',')
#     new_list.append(info[0])
#     new_list.append(info[2])
#     new_list.append(info[3])
#     info_list.append(new_list)
#
# print(info_list)

# practice2
text = open('prac01.txt', 'r').readlines()

result_list = []
for person in text:
    info = person.split(',')
    del info[1]
    del info[3:]
    result_list.append(info)

# print(result_list)

# practice3
# text_2 = open('Prac02.txt', 'r').readlines()
#
# word_list = []
#
# for el in text_2:
#     eli = el.lower().split(' ')
#     for word in eli:
#         if 't' in word:
#             word_list.append(word)
#
# print(word_list, len(word_list))

# practice4
lyrics = open('Prac02.txt', 'r').readlines()

word_t = [word for lyric in lyrics for word in lyric.lower().split(" ") if 't' in word]

print(word_t, len(word_t))