"""
PRIVATE ATTRIBUTES

Python does not have a way to effectively restrict access to instance variables or methods
 To declare a member as private in Python, you have to use double underscore __ as a prefix to the
variables.

 Private members are restricted within the same class,
 i.e. we can access the private members only within the same class.

"""

class Student:
    def __init__(self, name , RollNo):
        self.name = name
        self.RollNo = RollNo

    def show(self):
        print(self.name)

std = Student("John", 36)

# This will create an error
# print(std.name)

# Accessing private member through same class method is possible
std.show()
