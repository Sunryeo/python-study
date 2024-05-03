inputValue = int(input("Try guess: "))
answer = 3
gameCount = 0
while True:
    if inputValue == answer:
        gameCount += 1
        break
    else:
        inputValue = int(input("Try guess: "))
        gameCount += 1
print(f"Total game count: {gameCount}")