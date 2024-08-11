# # Multiplication Table
# n = int(input("Enter a Number : "))
#
# for i in range(1, 11):
#     print(f"{n} X {i} = {n * i}")

# l =["John","Stark","Shubham","Tony","Steve"];
#
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}!")
#
# # Factorial
#
# n = int(input("Enter a Number:  "))
# product = 1;
# for i in range(1, n+1):
#     product = product * i
#
# print(f"The factorial of {n} is : {product}")

# Write a program to print the star pyramid
#
# n = int(input("Enter a Number:  "))
#
# for i in range(1,n+1):
#     print("*" * (i))

n = int(input("Enter a Number:  "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
        print("")
