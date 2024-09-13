#  CREATING A BUTTON

import tkinter as tk

top = tk.Tk()
top.title("Counting Seconds")
# .title() set the title of the main window


button = tk.Button(top,
                   text="stop",
                   width=25,
                   font="poppins",
                   command=top.destroy)
# tk.button() creates a button
# top, Specifies that the button will be placed on the top of the window
# width. it sets the width of the button
# font, will change the font of the text.
# command, what you want to command the button to execute.
# command=top.destroy, in this we're commanding the button to destroy the connection. it will close the window


button.pack()
# This line tells Tkinter to pack (display) the button in the main window.


top.mainloop()
