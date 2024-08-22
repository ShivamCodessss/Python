# add static method in problem 2

class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is : {self.num * self.num}")

    def cube(self):
        print(f"Cube = {self.num * self.num * self.num}")

    def squareRoot(self):
        print(f"Cube = {self.num ** 1 / 2}")

    @staticmethod  #static method is used when the function doesnt need any argument
    def hello():
        print("Hello there!")


calc = Calculator(4)
calc.square()
calc.cube()
calc.squareRoot()
calc.hello()

# write a class Train which has method to book tickets, get status (no of seats)
# and get fare information of train running under indian railways
fare = 500


class Train:

    def __init__(self, trainNo, ticket):
        self.ticket = ticket
        self.trainNo = trainNo

    def BookTicket(self):
        self.ticket = int(input("How many ticket you want to book: "))

    def Status(self):
        print(f"Train {self.trainNo} is running on time")

    def Fare(self, fro, to):
        print(f"Ticket fare of {self.trainNo} from {fro} to {to} is {fare * self.ticket}")


tt = Train(21231234,122334)
tt.BookTicket()
tt.Status()
tt.Fare("delhi", "mumbai")
