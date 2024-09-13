# TEXT BOX

from tkinter import *

# This line import every module from tkinter library

top = Tk()
# This line creates the main window

L1 = Label(top, text="User Name")
L1.pack(side="left")
# In this, we are creating label name and we are packing it on the left side


E1 = Entry(top, bd=2)
E1.pack(side="right")  # we are packing it on the right side
# Entry. IT allows the user to input single line text
# b2 is the border width

top.mainloop()
# main loop waits the