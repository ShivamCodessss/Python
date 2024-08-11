# a dictionary is a collection of key-value pairs.
# Each key is unique, and it maps to a value.

# Dictionaries are mutable, meaning they can be changed after creation
# key must be unique and values can be any type
empty_dict = {}
print(type(empty_dict))

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

another_dict = dict(name="John", age=30, city="New York")

name = my_dict["name"]
# accessing the value with key
print(name)

age = my_dict["age"] = 31
# modifying the value
print(age)

my_dict["email"] = "xyz@gmail.com"
# adding new key value pair
print(my_dict)

my_dict.pop("age")
# removes the item with the specified key
print(my_dict)

my_dict.popitem()
# it removes the last inserted key value pair
print(my_dict)

del my_dict["city"]
# it deletes the specified value
print(my_dict)

my_dict.get("name")
# it returns the value for the specified key
print(my_dict)

my_dict["profession"] = "Executive Manager"
my_dict["salary"] ="10,000"

# checking names
if "name" in my_dict:
    print("Name is present")

for key in my_dict.keys():
# returns all the keys present in the dictionary
    print(key)

for value in my_dict.values():
    # returns all the values
    print(value)

for key, value in my_dict.items():
    # it returns the ket value pair
    print(key,value)
