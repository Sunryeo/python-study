import random

# 능력치 랜덤 생성
def create_random_stat():
    stat = {
        "strength": 5,
        "health": 5,
        "defense": 5
    }

    rand_num1 = random.randint(0, 4)
    rand_num2 = random.randint(0, 4)
    stat['strength'] -= rand_num1
    stat['health'] += rand_num1
    stat['health'] -= rand_num2
    stat['defense'] += rand_num2

    return stat


# 공격
def attack(attack_count, exp, hunting_count):
    attack_count += 1
    print("You attacked a monster!")
    print(f"Attack count: {attack_count}")
    if attack_count > 1:
        print("You killed the monster!")
        print("You get 1 exp!")
        exp += 1
        hunting_count += 1
        attack_count = 0

    return attack_count, exp, hunting_count


# 레벨업
def get_exp(level):
    print("Congratulation! Your level is up!")
    level += 1

    return level


# 능력치 분배
def dist_stat(stat):
    print("Distribute your status")
    for _ in range(5):
        item = int(input("1. strength, 2. health, 3. defense: "))
        if item == 1:
            stat["strength"] += 1
        elif item == 2:
            stat["health"] += 1
        elif item == 3:
            stat["defense"] += 1
        else:
            print("Wrong action")


# play
def play():
    level = 1
    exp = 0
    stat = create_random_stat()
    attack_count = 0
    hunting_count = 0

    while True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"Your level: {level}")
        print(f"Your exp: {exp}")
        print(f"Your status\nStrength: {stat['strength']}   Health: {stat['health']}   Defense: {stat['defense']}")
        action = int(input("1. attack, 2. defense\nPress any key to exit: "))

        if action == 1:
            attack_count, exp, hunting_count = attack(attack_count, exp, hunting_count)
        elif action == 2:
            print("You defensed a monster!")
        else:
            print("Terminate the game!")
            break

        # 레벨업 체크
        if hunting_count > 2:
            level = get_exp(level)
            hunting_count = 0
            dist_stat(stat)
        else:
            pass


play()