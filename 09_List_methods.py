My_list = [1,2,3]
My_list.append(4)
# append(): Adds a single element to the end of the list.
print(My_list)

My_list.extend([5,6,7])
# extend([]): Adds multiple elements to the end of the list.
print(My_list)

My_list.insert(1,"a")
# insert(): Adds the element on the specified position.
print(My_list)

My_list.remove("a")
# remove(): It removes the specified position or element.
print(My_list)

index = My_list.index(3)
# index(): it returns the index of the specified value
print(index)

count = My_list.count(2)
# count(): it returns the number of occurrences of the specified value
print(count)

My_list.sort()
# sort: it sorts the list in ascending manner
print(My_list)

My_list.clear()
# clear(): it clears the list
print(My_list)


