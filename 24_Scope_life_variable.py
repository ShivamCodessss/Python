"""
    Scope and lifetime of Variable

    the scope of a variable refers to the  domain of a program wherever it declared

    A function argument and variable are not accessible outside the defined function
    As a result they have a local domain

    the period of a variable existence in ram is referred to as its lifetime

    variable within a function have the same lifespan as it function itself

"""

def number():
    num = 10
    print("Value of num inside the number", num)

num = 20
number()
print("value outside the function ", num)

def function():
    string = "hello"

    def function2():
        print(string)

    function2()
function()