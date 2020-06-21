class Food:  # Base class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Food constructore in Base class")

    def eat(self):
        print("Eat method from Base class")


class Lunch(Food):  # Derived class
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        super().__init__(name, price)  #Override: inherit the functionality for name and price from the Base class
        print(f"Lunch constructor {self.name} the price: {self.price} quantity:{self.amount}")
    def eat(self):  #Override the BaseClass method
        print("Eat method from subClass")

#food1 = Food("mini Pizza", 50)
food2 = Lunch("Pizza", 100, 2)
print(food2.__init__("Hamburgare", 75, 3))
food2.eat()

