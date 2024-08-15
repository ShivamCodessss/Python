"""
The Anonymous Function
    We do not declare them as we declare usual function

    it use lambda keyword to define  the short single output, anonymous function

    Lambda expression can accept an unlimited number of arguments

    it returns only one value

    Can't have numerous expression or instruction

    since lambda needs, an anonymous expression, an anonymous function cannot be directly called to print
"""

lambda_ = lambda argument1, argument2: argument1 + argument2;

print("value of the function is : ", lambda_(20,30))
print("value of the function is : ", lambda_(50,40))
