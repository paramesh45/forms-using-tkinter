from tkinter import *
from tkinter.ttk import *


window=Tk()
window.title("list and combo")
# var = StringVar()
# var.set("python")      #optional
window.geometry("500x600")
data=["python","django","data analysis","github"]
cb=Combobox(window,values=data)
cb.place(x=100,y=50)

li=Listbox(window,height=5,selectmode='multiple')
for x in data:
    li.insert(END,x)
li.place(x=300,y=50)








window.mainloop()