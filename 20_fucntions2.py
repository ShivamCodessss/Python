# Python Function call by Reference or call by value
"""
in the event that you passing arguments like whole number, strings or tuples to a function
the passing is like call by value because you cannot change the value of the immutable
objects being passed to the function

whereas passing mutable objects can be considered as call by reference because when their values
are changed  inside the function then it will also be reflected outside the function
"""
# call by value

string = "greeks"


def test(string):
    string = "Greeks_of_greeks"
    print("inside function string ", string)


test(string)
print("outside function ", string)


# call by reference

def add_more(list):
    list.append(50)
    print("inside function ", list)


myList = [22, 33, 44]
add_more(myList)
print("outside function", myList)
