from tkinter import *
from random import randint

def ruch(*a):
    global xx, yy, b
    if xx > 230:
        xx = randint(0, 217)
    else:
        xx = randint(280, 435)
    if yy > 230:
        yy = randint(0, 237)
    else:
        yy = randint(238, 475)
    b.place(x=xx, y=yy)
    



o=Tk()
o.geometry("500x500")
o.resizable(width=FALSE, height=FALSE)
b=Button(o, text="Złap mnie!")
b.bind("<Enter>", ruch)
xx=0
yy=0
b.place(x=xx, y=yy)


o.mainloop()
