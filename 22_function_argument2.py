'''
Required Argument
* The arguments given to a function while calling in a pre-defined positional
sequence are required arguments.

* The count of required arguments in the method call must be equal to the count
of arguments provided while defining the function.

'''

def function(num1 , num2):
    print("printing num1", num1)
    print("printing num2", num2)

print("passing out of order arguments")
function(30,20)

print("Passing only one argument ")

try:
    function(30)
except:
    print("Function need two arguments")

