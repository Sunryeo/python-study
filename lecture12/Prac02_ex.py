class coffee():
    def __init__(self, brand="Starbucks", menu="Americano"):
        self.brand = brand
        self.menu = menu
        pass

    def info(self):
        print(f"Coffee brand: {self.brand}")
        print(f"Coffee menu: {self.menu}")
        pass


mycoffee = coffee()
mycoffee.info()

yourcoffee = coffee("Ediya", "Cappuccino")
yourcoffee.info()


