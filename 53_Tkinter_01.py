# CREATING A WINDOW

import tkinter as tk
# This line imports the tkinter module and aliases it as tk.
# you can use the tk as a shorthand of tkinter throughout the code

top = tk.Tk()
# This line creates the main window of application
# The Tk() function initializes the main window of the Tkinter application.
# top is a variable . It can be anything

top.mainloop()
# This line starts the tkinter event loop
# mainloop is an infinite loop used to run the application, it waits for an event occur and process the event as long
# as the window is not closed
# Without this line, the window would appear and then immediately close
