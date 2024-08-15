# abs() it is used to return the absolute value of a number

integer = -20

print("printing absolute value of -20 is :", abs(integer))

float_ = 20.86

print("printing absolute value of 20.86 is :", abs(float_))

# all() function accepts an iterable object(such as list, dict etc)
# it returns true if all the item in passed iteragble are true,otherwise it returns false

# all true values
k = [1,2,3,4,5]
print(all(k))

# all false value
k = [0, False]
print(all(k))

# one false value
k = [1,2,3,4,0]
print(all(k))

# one true value
k = [0, False, 5]
print(all(k))

# empty
k = []
print(all(k))


# bin() it is used to return the binary representation of a specific integer
#  a result always starts with the prefix 0b

x = 10
y = bin(x)
print(y)

# sorted() it is used to sort elements

str = "javapoint"

sorted1 = sorted(str)

print(sorted1)

# range() function returns an immutable sequence of numbers starting from
# 0 by default, increment by 1(by default) and ends at a specified number

# empty range
print(list(range(0)))

#  it will stop on 3 , becuase in the indexing starts with 0 , 1 , 2 , 3
print(list(range(4)))

# it always print -1 of the end value. because the loops end when it find the stop number
print(list(range(1,4)))

