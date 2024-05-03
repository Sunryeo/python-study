'''
pass 부분을 체워 넣어 코드를 완성하세요.
'''

import random

# Initializing variables
MONSTERHEALTH = 2
LVEXP = 3
LVSTAT = 5
IS_RUN = True


class User:
    def __init__(self):
        self.lv = 1
        self.exp = 0
        self.attackCnt = 0
        self.stat = None

        # Initialize status
        self.initStat()
        print("User created!")

    def initStat(self):
        while True:
            self.stat = {
                "strength": random.randint(1,14),
                "health": random.randint(1, 14),
                "defense": random.randint(1, 14)
            } # strength, health, defense를 dictionary 로 묶었어요.

            if sum(self.stat.values()) == 15:
                break
            # pass

    def Attack(self):
        self.attackCnt += 1
        print("You attacked a monster!")
        print(f"Attack count: {self.attackCnt}")
        self.GetExp()
        # pass

    def GetExp(self):
        self.exp += 1

        if self.exp == LVEXP:
            print("Congratulation! Your level is up!")
            self.DistStat()
            self.exp = 0
            self.lv += 1

    def DistStat(self):
        print("Distribute your status")
        for _ in range(5):
            item = int(input("1. strength, 2. health, 3. defense: "))
            if item == 1:
                self.stat["strength"] += 1
            elif item == 2:
                self.stat["health"] += 1
            elif item == 3:
                self.stat["defense"] += 1
            else:
                print("Wrong action")
        # pass

    # Printing methods
    def printInfo(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"Your level: {self.lv}")
        print(f"Your exp: {self.exp}")
        print(self.printStat())
        # pass

    def printStat(self):
        # 항상 f-string이 편한것은 아니랍니다.
        # 가끔은 이렇게 string-format이 편할 때도 있어요.
        # 그렇기 때문에 여러 방법을 숙지하고 계시는게 중요합니다 :)
        # self.stat.values()는 list를 반환하는데, 앞에 *를 써줌으로써 리스트를 각각의 원소로 풀어주는거에요.
        # 만약 *를 써주지 않는다면, 가장 앞에 있는 빈 칸{}에 원소 3개 짜리 리스트가 들어가고, 나머지 뒤에 두 빈 칸{}에는 아무것도 들어가는게 없기때문에 에러가 나겠죠?
        return "Strength: {0}\tHealth: {1}\tDefense: {2}".format(*self.stat.values())


# Since the program runs when __name__ == "__main__", python indicates the code runs from this line.
# Therefore, a green button is generated.
if __name__ == "__main__":
    user = User() #class User를 콜해서 user라는 객체를 만들었어요.
    while IS_RUN:
        user.printInfo()
        action = int(input("1. attack, 2. defense\nPress any key to exit: "))

        # class로 객체화 하고, 기능들을 한 곳으로 몰아 넣으니 코드가 한결 정돈됐어요.
        if action == 1:
            user.Attack()
        elif action == 2:
            print("You defense yourself from the monster!")
        else:
            print("Terminate the game!")
            IS_RUN = False
        print()
