import random

random_li1 = [random.randint(1, 10) for _ in range(6)]
random_li2 = [random.randint(1, 10) for _ in range(6)]

result_li = [li1 + li2 if i % 2 == 0 else li1 - li2 for i, (li1, li2) in enumerate(zip(random_li1, random_li2))]

print(f"Random list1: {random_li1}"
      f"\nRandom list2: {random_li2}"
      f"\n{'Result:':<13} {str(result_li)}")



