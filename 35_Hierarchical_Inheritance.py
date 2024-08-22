class Animal:
   def __init__(self,name):
       self.name = name

class Dog(Animal):
    def speak(self):
        print(f"{self.name} Barks....")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meoww......")

dog = Dog("Buddy")
cat = Cat("SnowBell")

dog.speak()
cat.speak()