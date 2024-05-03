'''
와우!! 진짜 깜짤 놀랐네요! 진짜 잘 했어요!!
제 솔루션 코드 보는 줄 알았네요 ㅎㅎ
'''
import random

lotto_num = int(input("로또 횟수입력: "))

for i in range(1, lotto_num+1):
    lotto_set = set()
    while len(lotto_set) < 6:
        lotto_set.add(random.randint(1, 45))

    print(f"{i} 회 당첨번호: {lotto_set}")
