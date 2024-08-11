# a function is a block of organized, reusable code that is used to perform a single,
# related action.

# A function is a group of statement    performing a specific task
# A function can be reused by the programmer in a given program

# Whenever we want to call a function we put the name of the function followed by parentheses

# by including function, we can prevent repeating the same code block repeatedly in a program
# python function once defined can be called many times and from anywhere in program
# python fucntion can also help in troubleShooting

def square(num):
    return num ** 2
object = square(9)
print("the sqaure of the number is ", object)

def a_function(string):
    return len(string)
print("length of the string Function is ", a_function("functions"))
print("length of the string Python is ", a_function("Python"))
