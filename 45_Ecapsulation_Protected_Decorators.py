"""
*       Understanding Protected Attributes

Protected Attributes are intended to be used only within the class and its
subclasses. They are marked by a single underscore (_) before the variable name. While Python doesn’t enforce strict
access control, the underscore convention indicates that these attributes should not be accessed directly outside the
class or subclass.

*        Using property and Getter/Setter Decorators

In Python, the @property decorator allows you to define a method as a
property. This means you can access it like an attribute but have the control of a method behind the scenes. When
combined with getters and setters, this allows you to manage access to protected attributes effectively.

"""

class Book:
    def __init__(self):
        self._name = "Race With Me"

    # property decorator ensures name() is considered as a property and not a method
    @property
    def name(self):
        return self._name

    # Setter allows to overload the name() mehtod
    @name.setter
    def name(self, new_name):
        self._name = new_name

obj = Book()

print("Current Book Name - ", obj.name)
obj.name =  "Tomorrow Never Comes"
print("New Name - ", obj.name)
