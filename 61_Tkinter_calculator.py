from tkinter import *

class Mywindow():
    def __init__(self, win):
        #Declaring and defining controls
        self.lbl1 = Label(win, text="First Number")
        self.lbl2 = Label(win, text="Second Number")
        self.lbl3 = Label(win, text="Result")
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.b1 = Button(win, text="Add", command=self.add)
        self.b2 = Button(win, text="Subtract")

        #Placing control on form
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1.place(x=100 , y=150)
        self.b2.place(x=200 , y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

window = Tk()
mywin = Mywindow(window)
window.title("Hello python")
window.geometry("400x300+10+10")
window.mainloop()
