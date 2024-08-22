"""
Destructor in Python

Destructor is called when an object gets destroyed

Python has a garbage collector that handles memory management automatically
The __del__() method is known as destructor in python
it is called when all the references to the object have been deleted
i.e. is when an object is garbage collector

"""

class Employee:
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destructor called!")

def createObj():
    print("making Object....")
    obj = Employee()
    print("Function End")
    return obj

print("Calling create_obj() function... ")
obj = createObj()
print("program End")

