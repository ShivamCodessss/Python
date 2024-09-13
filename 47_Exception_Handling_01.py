# Basic Exception handling


a = [1, 2, 3]

try:
    print("Second Element = %d" % (a[1]))

    print("Fourth Element = %d" % (a[3]))

except:
    print("Error occur")

# Catching Specific Exception
# A try Statement can have more than one except clause, to specify handlers for different exception
# however , at the most one will be executed

try:
    result = "String" + 5
except TypeError as e:
    print(f"Error Occurred: {e}")

# TypeError is a specific Exception
# "as e" assigns the caught exception to the variable e.
# e is a temporary variable, now it contains the system defined message

# There are so many specific exception::

"""
ZeroDivisionError: Raised when dividing by zero.
ValueError: Raised when a function gets the right type but inappropriate value.
TypeError: Raised when an operation is applied to an inappropriate type.
IndexError: Raised when accessing an out-of-range index in a list.
KeyError: Raised when a dictionary key is not found.
AttributeError: Raised when an attribute reference or assignment fails.
ImportError / ModuleNotFoundError: Raised when importing fails.
FileNotFoundError: Raised when a file is not found.
IOError: Raised when an I/O operation fails.
NameError: Raised when a variable is not defined.
RuntimeError: A generic error indicating a runtime issue.
StopIteration: Raised when an iterator has no more items.
MemoryError: Raised when a memory allocation fails.
OverflowError: Raised when an arithmetic operation exceeds limits.
AssertionError: Raised when an assert statement fails.

These examples cover a wide range of possible exceptions you may encounter in Python,
 along with how to handle them using try-except blocks.







"""
