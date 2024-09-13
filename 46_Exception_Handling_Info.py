"""
Error in python can be two typed
1. Syntax Error
2. Exception

Syntax Error caused by the wrong syntax in the code. it leads to termination of the program

Exception is raised when the program is syntactically correct, but the code resulted error.
This error does not stop the execution of the  program, however it changes the normal flow of program

For example:
Syntax Error

amount = 1000
if (amount > 2999)      # NO colon used
print("You are eligible")

Example of Exception
This program is syntactically correct.

marks = 100
a = marks / 0
print(a)
"""

"""
Handling Exception using "Try.....................Catch"

Try and except statement is used to catch and handle the exception in python
Statement that can raise exception are kept inside the try clause.

The statement that handle the exception are written inside the catch clause.  
"""