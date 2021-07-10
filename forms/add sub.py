from tkinter import *
from tkinter.ttk import *

window=Tk()

class AddSub:
    def __init__(self,w):
        self.n=Label(w,text="firstnumber")
        self.second=Label(w,text="second number")
        self.res=Label(w,text="result")
        self.ent_n=Entry(w)
        self.ent_s=Entry(w)
        self.ent_res=Entry(w)
        self.n.place(x=100,y=100)
        self.ent_n.place(x=250,y=100)
        self.second.place(x=100,y=150)
        self.ent_s.place(x=250,y=150)
        self.res.place(x=100,y=300)
        self.ent_res.place(x=250,y=300)
        self.b_add=Button(w,text="add",command=self.add)
        self.b_sub=Button(w,text="subract")
        self.b_sub.bind('<Button-1>',self.sub)
        self.b_add.place(x=150,y=220)
        self.b_sub.place(x=300,y=220)

    def add(self):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 + num2
        self.ent_res.insert(END, str(result))

    def sub(self, event):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 - num2
        self.ent_res.insert(END, str(result))





AddSub(window)
window.geometry("600x600")
window.title("add sub")
window.mainloop()