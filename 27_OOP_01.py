class function():
    a = 10
    b = 20
    c = a + b

obj = function()
print(obj.a)
print(obj.b)
print(obj.c)

"""
 Adding method
A method or function is going to be a block of code under the
class (so even further indented)

it's going to have at least one parameter: self.
"""

class myClass():
    a = 5

    def print_a(self):
        print(f"hi here is {self.a}")

myobj = myClass()
myobj.print_a()

"""
The Self
CLass method must have an extra parameter in the method definition.
we do not give a value for this parameter when we call the method, python provides it

if we have a method that takes no argument, we still have one argument
"""

