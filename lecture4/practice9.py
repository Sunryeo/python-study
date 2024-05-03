import random

gameCount = 0
while gameCount < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    inputValue = int(input(f"{num1} + {num2} = "))
    if inputValue != answer:
        print("You lost the game!")
        break
    else:
        gameCount += 1
        print("Congratulations! You got a correct answer!")
else:
    print("You win the game!")

