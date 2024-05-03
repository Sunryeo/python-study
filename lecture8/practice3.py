animals = ["Monkey", "Horse", "Cat"]
foods = ["Banana", "Carrot", "Fish"]
dictionary = dict(zip(animals, foods))
new_dictionary = dict(zip(foods, animals))

print(f"Dictionary: {dictionary}"
      f"\nkeys to list: {animals}"
      f"\nvalues to list: {foods}"
      f"\nnew dictionary: {new_dictionary}")