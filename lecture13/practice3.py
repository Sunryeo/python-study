class ShoppingCart:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def __str__(self):
        return f"Items in the cart: {self.cart}"

    def __len__(self):
        return len(self.cart)

    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            cart_new = ShoppingCart(f'{self.name}+{other.name}')
            cart_new.cart = self.cart + other.cart
            return cart_new


if __name__ == '__main__':
    cart1 = ShoppingCart("Cart1")
    cart1.add_item("Milk")
    cart1.add_item("Pork")
    cart1.add_item("Onion")

    cart2 = ShoppingCart("Cart2")
    cart2.add_item("Cola")
    cart2.add_item("Beef")
    cart2.add_item("Carrots")

    print(cart1)
    print(f"Total number of items in {cart1.name}: {len(cart1)}\n")
    print(cart2)
    print(f"Total number of items in {cart2.name}: {len(cart2)}\n")

    cart_new = cart1 + cart2
    print(cart_new)
    print(f"Total number of items in {cart_new.name}: {len(cart_new)}\n")
