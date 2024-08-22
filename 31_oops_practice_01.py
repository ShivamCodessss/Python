# create a  class programmer for storing information of few programmer working at microsoft

class programmer:
    company  = "Microsoft"

    def __init__(self, name, salary, post):
        self.name = name
        self.salary = salary
        self.post = post

obj = programmer("shivam", 100000, "It-guy")
print(obj.name, obj.salary, obj.post, obj.company)

# create a class calculator capable of finding square, cube and square root of a number

class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is : {self.num*self.num}")

    def cube(self):
        print(f"Cube = {self.num*self.num*self.num}")

    def squareRoot(self):
        print(f"Cube = {self.num**1/2}")

calc = Calculator(4)
calc.square()
calc.cube()
calc.squareRoot()



