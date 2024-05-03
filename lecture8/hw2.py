import random

lotto_num = int(input("로또 횟수입력: "))

for i in range(1, lotto_num+1):
    lotto_set = set()
    while len(lotto_set) < 6:
        lotto_set.add(random.randint(1, 45))

    print(f"{i} 회 당첨번호: {lotto_set}")
