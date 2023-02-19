# File: Translator.py by Old Man Rikdo

from Tkinter import *
import tkFont

def readfile(fn):
    retstring = ''
    f = open(fn)
    for line in f:
        for ch in line.strip():
            retstring += ch
    return retstring
            
class App:

    def __init__(self, master):

        frame = Frame(master, bg="Light Grey")
        frame.pack()
        frame2 = Frame(frame,)
        frame2.pack(side=RIGHT)

        self.trans = Button(frame, text="Translate", command=self.translate, bg="Light Grey")
        self.trans.pack(side=TOP)
        

        self.list = Listbox(frame, )
        for item in ["Zapfino", "Times", "Elvish Ring NFI", "Tengwar Elfica"]:
            self.list.insert(END, item)
        self.list.activate(0)
        self.list.pack(side=BOTTOM)

        
        self.text = Text(frame2, height=7, width=20, font=Default, relief=GROOVE)
        self.text.pack()

        self.reply = Text(frame2, height=7, width=20, font=Default, relief=GROOVE)
        self.reply.pack(side=BOTTOM)

    def translate(self):
        content = self.text.get(1.0, END)
        language = tkFont.Font(family=self.list.get(ACTIVE), size=20)
        self.reply.config(state=NORMAL, font=language)
        self.reply.delete(1.0, END)
        self.reply.insert(END, content)
        self.reply.config(state=DISABLED)

root = Tk()

Default = tkFont.Font(family="Times", size=20)

app = App(root)




root.mainloop()
