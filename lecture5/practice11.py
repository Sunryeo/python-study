fruit = 1000
snack = 800
drink = 1200

fruitCount = 0
snackCount = 0
drinkCount = 0

totalPrice = 0

while True:
    print(f"\n{'Welcome':_^25}")
    print(f"Current items in your cart:"
          f"\nFruit: {fruitCount}, Snack: {snackCount}, Drink: {drinkCount}"
          f"\nTotal price is {totalPrice}KRW\n"
          f"\n1. Add to the cart"
          f"\n2. Delete from the cart"
          f"\n3. Finish")
    action = input("Choose your action: ")

    # add to the cart
    if action == "1":
        print(f"{'Add to the cart!':=^30}")
        print(f"1) Fruit: {fruit}KRW, 2) Snack: {snack}KRW, 3) Drink: {drink}KRW")
        selectedItem = input("Choose the item: ")
        if selectedItem == "1":
            fruitCount += 1
            totalPrice += fruit
        elif selectedItem == "2":
            snackCount += 1
            totalPrice += snack
        elif selectedItem == "3":
            drinkCount += 1
            totalPrice += drink
        else:
            print("No items exist")
    # delete from the cart
    elif action == "2":
        print(f"{'Delete from the cart!':=^30}")
        print(f"1) Fruit: {fruitCount}, 2) Snack: {snackCount}, 3) Drink: {drinkCount}")
        selectedItem = input("Choose the item: ")
        if selectedItem == "1":
            if fruitCount > 0:
                fruitCount -= 1
                totalPrice -= fruit
            else:
                print("It is already empty!")
        elif selectedItem == "2":
            if snackCount > 0:
                snackCount -= 1
                totalPrice -= snack
            else:
                print("It is already empty!")
        elif selectedItem == "3":
            if drinkCount > 0:
                drinkCount -= 1
                totalPrice -= drink
            else:
                print("It is already empty!")
        else:
            print("No items exist")
    # pay and finish
    elif action == "3":
        print(f"Your items in the cart are fruits({fruitCount}), snacks({snackCount}), drinks({drinkCount})."
              f"\nThe total price is {totalPrice}KRW")
        insertedMoney = 0
        while True:
            balance = int(input(f"Insert money at least {totalPrice - insertedMoney}KRW: "))
            insertedMoney += balance
            if insertedMoney < totalPrice:
                print("Your balance is not enough!")
            else:
                print("Purchase success!"
                      f"\nYour change: {insertedMoney - totalPrice}KRW")
                break
        break
    else:
        print("Wrong action")
