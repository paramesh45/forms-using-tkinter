from tkinter import *
from tkinter.ttk import *

gui=Tk()
gui.title("form")
gui.geometry('500x200')
a=Label(gui,text="first_name").grid(row=0,column=0)
a=Label(gui,text="second_name").grid(row=1,column=0)
a1=Entry(gui).grid(row=0,column=1)
b1=Entry(gui).grid(row=1,column=1)
button=Button(gui,text="submit").grid(row=2,column=0)
gui.mainloop()

