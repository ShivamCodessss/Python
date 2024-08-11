# What is set
# It is collection of unOrdered Items.
# each element in the set is unique. mutable and set removes the duplicate items
# it is mutable that means you can modify it later as well

my_set = {1,2,3}
print(my_set)

another_set = {3, 4, 5 , 5 ,6}
print(another_set)

# that's how we create an empty set
empty_set = set()
print(type(empty_set))

my_set.add(6)
# adding element: adds a single element to the set
print(my_set)

my_set.remove(1)
# remove L removes a specified element. raise a keyerror if the element is not found
print(my_set)

my_set.discard(1)
# remove: removes the specified element if found. otherwise it do nothing
print(my_set)

# my_set.clear()
# clear: clears the whole set
# print(my_set)

union_set = my_set.union(another_set)
# Returns a new set with elements from both sets.
print(union_set)

intersection_set = my_set.intersection(another_set)
# returns a new set with common values in both set
print(intersection_set)

difference_set = my_set.difference(another_set)
# difference(): Returns a new set with elements in the first set but not in the second
print(difference_set)



