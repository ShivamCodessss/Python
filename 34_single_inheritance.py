# Single Inheritance occurs when child class inherit only a single parent class

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks.
