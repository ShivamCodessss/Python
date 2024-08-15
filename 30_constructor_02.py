class cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hi I am a cat, my name is "
              f"{self.name}."
              f"I am {self.age} year old.")

    def sound(self):
        print("meow!")


obj = cat("andy", 1)
obj1 = cat("sam", 3)
obj.info(); obj.sound()
obj1.info(); obj1.sound()
