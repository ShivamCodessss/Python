"""
Raise Exception

The Raise Statement allows the programmer to force a specific exception occurs
raise statement is used to manually trigger an exception.
The raise statement can be followed by an exception class or an instance of an exception class.


"""

try:
    amount = 1999
    if amount < 2999:

        raise ValueError("Please add money in your account")
    else:
        print("You are eligible to purchase this")
except ValueError as e:
    print(f"Error: {e}")
