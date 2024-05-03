# 물건 가격
FRUIT_PRICE = 1000
SNACK_PRICE = 800
DRINK_PRICE = 1200


# 장바구니 추가
def add_cart(item, cart):
    if item == 1:
        cart["Fruit"] += 1
    elif item == 2:
        cart["Snack"] += 1
    elif item == 3:
        cart["Drink"] += 1
    else:
        print(f"Number {item} does not exist")


# 장바구니 제거
def del_cart(item, cart):
    if item == 1:
        if cart["Fruit"] < 1:
            print("You have no Fruit to delete")
        else:
            cart["Fruit"] -= 1
    elif item == 2:
        if cart["Snack"] < 1:
            print("You have no Snack to delete")
        else:
            cart["Snack"] -= 1
    elif item == 3:
        if cart["Drink"] < 1:
            print("You have no Drink to delete")
        else:
            cart["Drink"] -= 1
    else:
        print(f"Number {item} does not exist")


# 계산
def pay(total_price):
    balance = 0
    while True:
        inserted_money = int(input(f"Insert money at least {total_price - balance}KRW: "))
        balance += inserted_money
        if balance < total_price:
            print("Your balance is not enough!")
        else:
            print("Purchase success!")
            break


# main function
def shopping():
    cart = {
        "Fruit": 0,
        "Snack": 0,
        "Drink": 0
    }

    while True:
        total_price = cart["Fruit"] * FRUIT_PRICE + cart["Snack"] * SNACK_PRICE + cart["Drink"] * DRINK_PRICE
        print(f"\n{'Welcome':_^25}")
        print(f"Current items in your cart:"
              f"\nFruit: {cart['Fruit']}, Snack: {cart['Snack']}, Drink: {cart['Drink']}"
              f"\nTotal price is {total_price}KRW\n"
              f"\n1. Add to the cart"
              f"\n2. Delete from the cart"
              f"\n3. Finish")
        action = int(input("Choose your action: "))

        if action == 1:
            print(f"{'Add to the cart!':=^30}")
            print(f"1) Fruit: {FRUIT_PRICE}KRW, 2) Snack: {SNACK_PRICE}KRW, 3) Drink: {DRINK_PRICE}KRW")
            item = int(input("Choose the item: "))
            add_cart(item, cart)
        elif action == 2:
            print(f"{'Delete from the cart!':=^30}")
            print(f"1) Fruit: {cart['Fruit']}, 2) Snack: {cart['Snack']}, 3) Drink: {cart['Drink']}")
            item = int(input("Choose the item: "))
            del_cart(item, cart)
        elif action == 3:
            print(
                f"Your items in the cart are fruits({cart['Fruit']}), snacks({cart['Snack']}), drinks({cart['Drink']})")
            # 계산
            pay(total_price)
            break
        else:
            print("Wrong action")


shopping()