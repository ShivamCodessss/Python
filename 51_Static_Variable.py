"""
Static Variable in Python

Features of Static Variable

Static variable are allocated memory once when the object for the class is created for the first time
Static variable is created outside the method but inside the class
Static Variable can be accessed through a class but not directly with an instance
Static variable behaviour doesn't change for every object
"""

# Example 1

class CSStudent: #Class for computer science

    # Class Variable
    stream = "cse"
    def __init__(self, name, roll):
        # instance Variable
        self.name = name
        self.roll = roll

# objects of class
a = CSStudent("John", 1)
b = CSStudent("Doe",2)


print(a.stream) # print cse
print(b.stream) # print cse
print(a.name)   # print john
print(b.name)   # print doe
print(a.roll)   # print 1
print(b.roll)   # print 2

# Class variable can be access through the class name also
print(CSStudent.stream)

# now if we change the stream for the "a", it will not change for the "b"
a.stream = "ece"
print(a.stream)
print(b.stream)

# To change the stream for all instance of the class, we can change directly through the class
CSStudent.stream = "mTech"
print(a.stream) # print ece
print(b.stream) # print mtech


"""
Static Method in Python

Static method are methods that are bound to a class rather than its object
they do not require a class instance creation, so they are not dependent on the state of the object

"""
# Example 2

class Person:
    def __init__(self,age):
        self.age = age

    def IsAdult(age):
        return age > 18

person1 = Person(19)

print(person1.age)

print(Person.IsAdult(22))

