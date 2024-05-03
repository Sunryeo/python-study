'''
이 문제도 진짜 잘 해주셨네요!!

리스트 컴프리핸션도 이제는 많이 자유로이 사용하시는 것 같아요!
지금같은 성장세라면 금방 중급 / 고급까지도 갈 수 있을 것 같아요!
'''
import random

random_li1 = [random.randint(1, 10) for _ in range(6)]
random_li2 = [random.randint(1, 10) for _ in range(6)]

result_li = [li1 + li2 if i % 2 == 0 else li1 - li2 for i, (li1, li2) in enumerate(zip(random_li1, random_li2))]

print(f"Random list1: {random_li1}"
      f"\nRandom list2: {random_li2}"
      f"\n{'Result:':<13} {str(result_li)}")



