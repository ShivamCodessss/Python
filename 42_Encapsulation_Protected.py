"""
You can access protected attributes of a class from within the class,
and they can also be accessed by the sub-classes.

To make a variable protected, you have to add a single underscore (e.g. _x) as a prefix to it.
 To make it truly protected, you also have to use a property decorator.
"""

class Employee:
    def __init__(self, name, salary):
        self._name = name  # Protected attribute
        self._salary = salary  # Protected attribute

    def _display_info(self):  # Protected method
        return f"Name: {self._name}, Salary: {self._salary}"

class Manager(Employee):
    def display(self):
        return self._display_info()  # Accessing protected method in subclass

emp = Manager("Yuvraj", 70000)
print(emp.display())  # Accessing protected method through subclass

# Accessing protected attribute directly (not recommended)
print(emp._name)


