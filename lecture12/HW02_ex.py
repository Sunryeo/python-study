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
            }

            if sum(self.stat.values()) == 15:
                break
        # pass

    def Attack(self):
        self.attackCnt += 1
        print("You attacked a monster!")
        print(f"Attack count: {self.attackCnt}")
        self.GetExp()
        return self.stat['strength']

    def GetExp(self):
        self.exp += 1

        if self.exp == LVEXP:
            print("Congratulation! Your level is up!")
            self.DistStat()
            self.exp = 0
            self.lv += 1
        # pass

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
        return "Strength: {0}\tHealth: {1}\tDefense: {2}".format(*self.stat.values())

class Monster:
    def __init__(self):
        self.stat = None

        self.initStat()
        print("Monster generated!")

    # 소멸자라고 해요.
    # 클래스를 삭제하고 싶을 때, del "class" 를 하면 돼요.
    # 클래스가 삭제될 때 실행되는 코드에요.  __init__은 객체가 생성될 때 실행되는 코드였죠?
    def __del__(self):
        print("Monster died")


    def initStat(self):
        self.stat = {
            "strength": random.randint(1, 5),
            "health": random.randint(5, 10),
            "defense": random.randint(0, 2)
        }
        # pass

    def damaged(self, att):
        damage = att - self.stat['defense'] # 글자가 회색이 되었다는 말은 선언은 되었지만 아직 사용되지 않은 변수에요. 사용해야 겠죠? (tip 이에요 :))

        self.stat['health'] = self.stat['health'] - damage
        # pass

        if self.stat['health'] <= 0: # monster의 체력이 0 이하가 되면 몬스터는 죽어야 하기 때문에 True를 반환해줄거에요.
            return True

        return False

    def printInfo(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"Monster status: {self.printStat()}")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@\n")

    def printStat(self):
        return "Strength: {0}\tHealth: {1}\tDefense: {2}".format(*self.stat.values())


# Since the program runs when __name__ == "__main__", python indicates the code runs from this line.
# Therefore, a green button is generated.
if __name__ == "__main__":
    user = User()
    monster = Monster()

    while IS_RUN:
        user.printInfo()

        # 예외처리문이에요.
        # 만약에 monster.printInfo()를 실행했을 때 에러가 난다면,
        # 이 경우 NameError에 대한 처리를 해주었네요,
        # 에러가 나면 except 절로 들어가서 monster를 생성하고, printInfo()를 했어요.
        # 즉, monster가 생성 돼있다면 printInfo()를 바로 실행하고, 아니라면 monster를 생성 후 실행하라는 코드에요.
        try:
            monster.printInfo()
        except NameError:
            monster = Monster()
            monster.printInfo()

        action = int(input("1. attack, 2. defense\nPress any key to exit: "))

        if action == 1:
            att = user.Attack() # user가 공격했을 때 user의 공격력을 반환받을 거에요.
            isDie = monster.damaged(att) # 반환받은 공격을 monster의 damaged method로 보내 monster의 체력을 계산한 후 monseter가 죽었는지를 반환할거에요.
            if isDie:
                user.GetExp() # monster가 죽었다면, user는 exp를 얻게 될 것이고,
                del monster # monster 객체는 삭제해줄거에요. 그래야 위에 예외처리문에서 새로운 몬스터가 생성되겠죠?

        elif action == 2:
            print("You defense yourself from the monster!")
        else:
            print("Terminate the game!")
            IS_RUN = False
        print()
