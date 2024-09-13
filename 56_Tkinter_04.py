# CREATING A BUTTON SHOWING A MESSAGE

import tkinter
import tkinter.messagebox as _mymsgbox
# import tkinter.messagebox as _mymsgbox: This imports the messagebox module from tkinter under the alias _mymsgbox.
# This module provides functions to display different types of message boxes, like information, warning,
# and error dialogs.

top = tkinter.Tk()
# This Initializes the main window

def ShowHelloMsg():
    _mymsgbox.showinfo("Hello Python","Hello World")
#     This is the function that will execute when the button is clicked
# we are initializing the title and the message



B = tkinter.Button(top,
                   text="Hello",
                   activebackground="orange",
                   bg="grey",
                   command=ShowHelloMsg)
# In This we are creating a button . Top() is used to put it on the top.
#  And at the end we are commanding the button to execute the function.

B.pack()
# pack. We are placing the button

top.mainloop()
