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
        self.b_mul=Button(w,text="mutliplication")
        self.b_mul.bind("<Button-1>",self.mul)
        self.b_div = Button(w, text="division")
        self.b_div.bind("<Button-1>", self.div)
        self.b_mod = Button(w, text="modlues")
        self.b_mod.bind("<Button-1>", self.mod)
        self.b_floor = Button(w, text="floor division")
        self.b_floor.bind("<Button-1>", self.floor)
        self.b_add.place(x=50,y=220)
        self.b_sub.place(x=150,y=220)
        self.b_mul.place(x=250,y=220)
        self.b_div.place(x=350,y=220)
        self.b_mod.place(x=450,y=220)
        self.b_floor.place(x=270,y=275)

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

    def mul(self,event):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 * num2
        self.ent_res.insert(END, str(result))

    def div(self,event):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 / num2
        self.ent_res.insert(END, str(result))

    def mod(self,event):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 % num2
        self.ent_res.insert(END, str(result))
    def floor(self,event):
        self.ent_res.delete(0, 'end')
        num1 = int(self.ent_n.get())
        num2 = int(self.ent_s.get())
        result = num1 // num2
        self.ent_res.insert(END, str(result))




AddSub(window)
window.geometry("600x600")
window.title("add sub")
window.mainloop()