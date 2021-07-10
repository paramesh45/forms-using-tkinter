from tkinter import *
from tkinter.ttk import *


window=Tk()
window.title("radio and check buttons")
window.geometry("500x500")
v0=IntVar()
v0.set(1)
male=Radiobutton(window,text="male",variable=v0,value=1)
female=Radiobutton(window,text="female",variable=v0,value=2)
male.place(x=100,y=50)
female.place(x=180, y=50)    #### x=width y= height

c1=IntVar()
c2=IntVar()
check1=Checkbutton(window,text="python",variable=c1)
check2=Checkbutton(window,text="django",variable="c2")

check1.place(x=100,y=100)
check2.place(x=180,y=100)

window.mainloop()
