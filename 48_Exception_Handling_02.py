"""
Finally Keyword in Python

Python provide a keyword finally, which is always executed after the try and catch block

try:
    # Code that might raise an exception
except SomeException as e:
    # Code to handle the exception
finally:
    # Code that will run no matter what

"""

try:
    print("Trying to divide by zero...")
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:
    print("This will run no matter what.")
