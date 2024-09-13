# ORGANIZING WIDGETS WITH FRAME

from tkinter import *
# This import every module from tkinter

root = Tk()
# We are creating the main window

frame = Frame(root)
frame.pack()
# A Frame is a container widget that can hold other widgets.
# The frame variable creates a frame inside the root window.

bottomframe = Frame(root)
bottomframe.pack(side= BOTTOM)
# Another frame is created inside the root

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="Black", fg="Black")
blackbutton.pack(side = BOTTOM)

# These all are buttons. with the label red and the fg=color also red
# and we are placing them left right bottom


root.mainloop()
