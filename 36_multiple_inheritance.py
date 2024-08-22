# Multiple inheritance is when a class (child class) inherits attributes and methods from more than one parent class.
# This allows the child class to access functionalities of multiple parent classes, creating a more complex and
# versatile object.

class Flyer:
    def fly(self):
        print("fly")

class Swimmer:
    def swim(self):
        print("swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("quack quack")


duck = Duck()

duck.fly()
duck.swim()
duck.quack()
