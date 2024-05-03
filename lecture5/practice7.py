currentHour = int(input("Input current hour: "))
if currentHour > 24:
    print("Wrong input!")
    exit()

currentMin = int(input("Input current minute: "))
if currentMin > 59:
    print("Wrong input!")
    exit()

nMins = int(input("Input N mins: "))

addedHour = 0
newMin = 0
if currentMin + nMins >= 60:
    addedHour = (currentMin + nMins) // 60
    newMin = (currentMin + nMins) % 60
    currentHour += addedHour
    currentMin = newMin
else:
    currentMin += nMins

print(f"{nMins} mins later: {currentHour}H {currentMin}M")
