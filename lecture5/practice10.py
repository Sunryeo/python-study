budget = int(input("Insert money: "))
cola = 1000
sprite = 1200
bongBong = 800
vita500 = 500

buttonList = (f"1. Coca Cola: {cola} KRW\n2. Sprite: {sprite} KRW"
              f"\n3. Bongbong: {bongBong} KRW\n4. Vita500: {vita500} KRW\n5. Return changes")

selectedItem = 0
colaCount = 0
spriteCount = 0
bongBongCount = 0
vita500Count = 0
while budget > 500:
    print(f"Current balance: {budget}")
    print("==========================")
    print(buttonList)
    print("==========================")

    item = input("Choose an item: ")
    if item == "1":
        selectedItem = cola
        print("Cola was selected!")
    elif item == "2":
        selectedItem = sprite
        print("Sprite was selected!")
    elif item == "3":
        selectedItem = bongBong
        print("Bongbong was selected!")
    elif item == "4":
        selectedItem = vita500
        print("Vita500 was selected!")
    elif item == "5":
        print(f"Your balance is {budget}")
        print(f"Your purchase items are cola({colaCount}), sprite({spriteCount}), bongbong({bongBongCount}), vita500({vita500Count}")
        break
    else:
        print("No items exist")

    print()

    if budget < selectedItem:
        print("Not enough money")
        continue
    else:
        # update shopping list
        if selectedItem == cola:
            colaCount += 1
        if selectedItem == sprite:
            spriteCount += 1
        if selectedItem == bongBong:
            bongBongCount += 1
        if selectedItem == vita500:
            vita500Count += 1
        budget = budget - selectedItem
else:
    print(f"Your balance is {budget}")
    print(f"Your purchase items are cola({colaCount}), sprite({spriteCount}), bongbong({bongBongCount}), vita500({vita500Count})")
