"""
Types of Function we can use to call a function

1. Default
2. keyword Argument
3. Required
4. Variable Length

"""
#  A Default argument is a kind of parameter that takes as input a default value
# if no value is supplied for the argument when the function is called
def funciton(num1, num2 = 40):
    print("Num1 is ", num1)
    print("Num2 is ", num2)

print("Passing one argument ")
funciton(10)


print("Passing two argument ")
funciton(10,20)

# Keyword Argument
# Since the Python interpreter will connect  the keywords given to link the values with
# its parameters, we can omit some arguments or arrange them out of order

def Func(a , b):
    print("printing a", a)
    print("printing b", b)

print("without using keyword")
Func(10,20)

print("with using keyword")
Func(b = 10, a = 20)

