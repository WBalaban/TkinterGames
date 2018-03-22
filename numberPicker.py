from tkinter import *
import random

class NUMapp():        
    def __init__(self):
        self.root = Tk()
        self.buildControls()
        self.root.mainloop()

    def buildControls(self):
        self.root.wm_title("Random Number Picker") 
        x = 0; y = 0
        self.numbers = []; self.numbtn = []

        while len(self.numbers) < 25:
            r = random.randint(0,999)
            if r not in self.numbers:
                self.numbers.append(r)

        for i in range(1,26):
            self.numbtn.append(Button(self.root, text=str(self.numbers[i-1]), width=10, 
                               command=lambda i=i:self.btnclick(i-1)))
            self.numbtn[i-1].grid(row=x, column=y)    
            x+=1    
            if i % 5 == 0:
                x = 0
                y += 1

    def btnclick(self, mynum):
        currnum = int(self.numbtn[mynum].cget('text'))     # CAPTURE BUTTON TEXT
        if currnum == min(self.numbers):            
            self.numbtn[mynum].config(state="disabled")    # DISABLE BUTTON
            self.numbers.remove(currnum)                   # REMOVE FOR NEW MINIMUM

NUMapp()
