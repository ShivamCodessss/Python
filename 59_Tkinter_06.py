# POSITIONING A BUTTON

import tkinter

window = tkinter.Tk()

btn = tkinter.Button(window,
                     text="This is button widget",
                     fg="blue")
# we are initializing the button

btn.place(x=80, y=90)
# Positioning the button

window.title("Hello Python")
window.geometry("300x200+500+200")
window.mainloop()