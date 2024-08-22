# Multilevel inheritance is a type of inheritance where a class is derived from another class, which is itself
# derived from another class. This creates a chain of inheritance, where each class inherits properties and methods
# from its parent class.


class Vehicle:  #GrandParent Class
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def startEngine(self):
        print(f"Company: {self.company}. Model: {self.model}")


class Car(Vehicle):  # Parent Clas Inheriting from vehicle class
    def __init__(self, company, model, doors):
        super().__init__(company, model) # Call the constructor of Vehicle class
        self.doors = doors

    def openDoors(self):
        print(f"Opening {self.doors} doors")


class ElectricCar(Car): #CHild class inherit from Car
    def __init__(self, company, model, doors, battery):
        super().__init__(company, model, doors) # Call the constructor of Car class
        self.battery = battery

    def charge_batter(self):
        print(f"charing the battery with {self.battery}")

# creating an instance of Electric car
tesla = ElectricCar("Tesla", "S-Model", 4, 300)


# Accessing methods from all levels of the inheritance class
tesla.startEngine()
tesla.openDoors()
tesla.charge_batter()
