from tkinter import *

o= Tk()
o.title('Bitownik')

def spr7():
    global check7, wynik, v7, x
    if v7.get()==1:
        wynik+=128
        x.set(str(wynik))
    else:
        wynik-=128
        x.set(str(wynik))
def spr6():
    global check6, wynik, v6, x
    if v6.get()==1:
        wynik+=64
        x.set(str(wynik))
    else:
        wynik-=64
        x.set(str(wynik))
def spr5():
    global check5, wynik, v5, x
    if v5.get()==1:
        wynik+=32
        x.set(str(wynik))
    else:
        wynik-=32
        x.set(str(wynik))
def spr4():
    global check4, wynik, v4, x
    if v4.get()==1:
        wynik+=16
        x.set(str(wynik))
    else:
        wynik-=16
        x.set(str(wynik))
def spr3():
    global check3, wynik, v3, x
    if v3.get()==1:
        wynik+=8
        x.set(str(wynik))
    else:
        wynik-=8
        x.set(str(wynik))
def spr2():
    global check2, wynik, v2, x
    if v2.get()==1:
        wynik+=4
        x.set(str(wynik))
    else:
        wynik-=4
        x.set(str(wynik))
def spr1():
    global check1, wynik, v1, x
    if v1.get()==1:
        wynik+=2
        x.set(str(wynik))
    else:
        wynik-=2
        x.set(str(wynik))
def spr0():
    global check0, wynik, v0, x
    if v0.get()==1:
        wynik+=1
        x.set(str(wynik))
    else:
        wynik-=1
        x.set(str(wynik))


wynik=0
v7=IntVar()
v6=IntVar()
v5=IntVar()
v6=IntVar()
v4=IntVar()
v3=IntVar()
v2=IntVar()
v1=IntVar()
v0=IntVar()

x=StringVar()
licze = Label(o, textvariable = x)
licze.config(font=("Arial", 25), foreground="blue")

licze.grid(row=1, column=3, columnspan=2)

wyjscie = Button(o, text='Koniec', command=o.destroy)
wyjscie.grid(row=2, column=3, columnspan=2)



x.set(str(wynik))

check7 = Checkbutton(o, text='7', variable=v7, command=spr7)
check7.grid(row=0, column=0)
check6 = Checkbutton(o, text='6', variable=v6, command=spr6)
check6.grid(row=0, column=1)
check5 = Checkbutton(o, text='5', variable=v5, command=spr5)
check5.grid(row=0, column=2)
check4 = Checkbutton(o, text='4', variable=v4, command=spr4)
check4.grid(row=0, column=3)
check3 = Checkbutton(o, text='3', variable=v3, command=spr3)
check3.grid(row=0, column=4,)
check2 = Checkbutton(o, text='2', variable=v2, command=spr2)
check2.grid(row=0, column=5,)
check1 = Checkbutton(o, text='1', variable=v1, command=spr1)
check1.grid(row=0, column=6,)
check0 = Checkbutton(o, text='0', variable=v0, command=spr0)
check0.grid(row=0, column=7,)
o.mainloop()
