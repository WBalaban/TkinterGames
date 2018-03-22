from tkinter import *

def clik(z=None):
    global T, litery, liczby, l, c, a
    litery = 0
    liczby = 0
    s = T.get("1.0",'end-1c')
    for i in s:
        if i.isalpha():
            litery += 1
        elif i.isdigit():
            liczby += 1
    l.set('Liter: '+str(litery))
    c.set('Cyfr: '+str(liczby))
    a.set('Znaków: ' +str(len(s)))
          
o= Tk()
litery = 0
liczby = 0
s='5'
T=Text(o, height=20, width=46)
T.pack()
T.bind("<KeyRelease>", clik)
a=StringVar()
l=StringVar()
c=StringVar()
znaczki=Entry(o, textvariable=a)
znaczki.pack(side=LEFT)
znaczki.configure(state="disabled")
literki=Entry(o, textvariable=l)
literki.pack(side=LEFT)
literki.configure(state="disabled")
cyferki=Entry(o, textvariable=c)
cyferki.pack(side=LEFT)
cyferki.configure(state="disabled")
l.set('Liter: ')
c.set('Cyfr: ')
a.set('Znaków: ')


o.mainloop()
