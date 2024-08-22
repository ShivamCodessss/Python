"""
PUBLIC ATTRIBUTES
.   In Python, every member of the class is public by default
.   public members in a class can be accessed from anywhere outside the class
.   you can access the public members by creating the object of the class
.   Even derived class can access the public members
 """

class music:

    def __init__(self):
        self.genre = "pop"
        self.singer = "coldplay"
        # These are public attributes

    def foo(self0):
        song = "Song of the evening"
        return song

m = music()

#  Accessing the public member inside the class
print("Song: ",m.foo())
print("Genre: ",m.genre)
print("Singer: ",m.singer)
