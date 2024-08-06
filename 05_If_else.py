# IF else statement
#  it is used to check the condition wheher  it is true or not
#  if it is true print this otherwise this
# for example

a = -2

if (a >= 10 ):
    print("correct")
else:
    print("false")

    # we can use multiple if in one use. it is called IF ELIF LADDER

i = int(input("enter a number between 1 t0 100 : "))

if (i <=50 ):
    print(" i is less then 50")
elif(i <= 70 and i >= 50):
    print("i is less then 70 but greater then 50")
else:
    print("out of range, try again")
