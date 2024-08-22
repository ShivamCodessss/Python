# Name Mangling to access the private members

class Student:

    def __init__(self):
        # These are private attributes
        self.__rollNo = 25
        self.__Name = "Doe"

        # this is a public attribute
        self.marks = 60;


std = Student()

# Accessing the private members outside the class with the help of Name Mangling

print("Roll No : ", std._Student__rollNo)
print("Name : ", std._Student__Name)

# Accessing the public member normally
print("Marks: " , std.marks)

"""
What Is Name Mangling
Name Mangling is a process in Python, where, if a method has, in any event, two underscores before the
name, and at the most one underscore following the name, it gets replaced with _ClassName before it

 For instance, __method() becomes _ClassName__method().

 Since the name is changed internally by the interpreter, we cannot access the variable utilizing its original name
and that is how you can hide data in Python.
"""