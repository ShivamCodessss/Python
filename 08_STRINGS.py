# anything which is sotored in quotations are strings
# for exmaple
print("This is a String")
#  we can use multi strings by three quotations

a = """
    this is multi string
"""

# string can be sliced also with indexing

b = "hellow"
print(b[1]) # it will print "e"

# indexing always starts from 0
print(b[0:])
print(b[1:4])

# we can also check the string
print("h" in b ) # it will return true
print("t" in b ) # it will return false

INTEGER = 10;
Float = 2.2;
String = "hellow"

print(""" Hi i am integer ....my value is%d\n Hi i'm float .... my value is %f\n
        Hi i am string ... my value is %s   """%(INTEGER, Float, String))