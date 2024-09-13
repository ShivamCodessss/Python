# Various Button in a window

from tkinter import *
from tkinter.ttk import Combobox
# Imports all the classes and function from Tkinter
# Import the combo-box widget

window = Tk()
# It creates the main window

var = StringVar()
var.set("one")
data = ("one","two","three","four")

cb = Combobox(window, values=data)
cb.place(x=60, y=150)
# creating the combo box
#  Creates a StringVar object, which is used to manage the value of a widget like Entry or Combobox.
# var.set("one"): Sets the initial value of the StringVar to "one".
# A tuple of string, that will be the value of the combobox
# cb = ComboBox(): Creates a Combobox widget in the window with the options specified in the data tuple.

lb = Listbox(window, height=5, selectmode='multiple')

_indx = 1
for num in data:
    lb.insert(_indx, num)
    _indx = _indx+1

lb.place(x=250, y=150)
# lb = ListBox() creates a list box, with the 5 line height
# _indx = 1 : initialize an  index counter  to insert items into the listbox
# lb.insert() : insert each item from the data tuple into the listbox


v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=1)
# v0 = IntVar(): Creates an IntVar object to store the value associated with the selected radiobutton.



r1.place(x=100, y=50)
r2.place(x=180, y=50)

v1 = IntVar()
v2 = IntVar()

C1 = Checkbutton(window, text="Cricket", variable=v1)
C2 = Checkbutton(window, text="Tennis", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

window.title("hello python")
window.geometry("400x300+10+10")
window.mainloop()