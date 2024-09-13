"""
USER DEFINE EXCEPTION

you can create your own custom exceptions by defining a new class that inherits from Python's
 built-in Exception class (or any other built-in exception class).
"""
class MyCustomError(Exception):
    """Custom exception class for specific error cases."""
    pass

def check_value(value):
    if value < 0:
        raise MyCustomError("Value cannot be negative!")

try:
    check_value(-5)
except MyCustomError as e:
    print(f"Caught a custom exception: {e}")
