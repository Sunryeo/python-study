class Animal():
    def __init__(self):
        print("Animal is called")

class Cat(Animal):
    def __init__(self, name, food):
        Animal.__init__(self)
        self.food = food
        print(f"{name} is called")

    def eat(self):
        print(f"Eating {self.food}")

    def jump(self):
        print("Jumping")

class Dog(Animal):
    def __init__(self, name, food):
        Animal.__init__(self)
        self.food = food
        print(f"{name} is called")

    def eat(self):
        print(f"Eating {self.food}")

    def run(self):
        print("Running")

cat = Cat("cat", "fish")
cat.eat()
cat.jump()

dog = Dog("dog", "foods")
dog.eat()
dog.run()