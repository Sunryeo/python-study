'''
zip 이용해서 딕셔너리 선언 참 잘해주셨네요 :)
zip 함수가 잘 다루기만 하면 정말 유용한 함수니까 잊지 말고 잘 사용하시면 좋을 것 같아요!
'''
animals = ["Monkey", "Horse", "Cat"]
foods = ["Banana", "Carrot", "Fish"]
dictionary = dict(zip(animals, foods))
new_dictionary = dict(zip(foods, animals))

print(f"Dictionary: {dictionary}"
      f"\nkeys to list: {animals}"
      f"\nvalues to list: {foods}"
      f"\nnew dictionary: {new_dictionary}")