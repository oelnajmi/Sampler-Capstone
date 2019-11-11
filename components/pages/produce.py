from components.pages.page import Page
from tkinter import *

ALL = N+S+W+E

class Produce(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)


        for c in range(9):
            self.columnconfigure(c, weight=1)

        for r in range(5):
            self.rowconfigure(r, weight=1)
            if r == 0:
                Button(self, text="Home", command=global_app.show_home).grid(row=r, column=0, sticky=ALL)
            else:
                Button(self, text="Pad {0}".format(r)).grid(row=r, column=0, sticky=ALL)
            for s in range(1, 5):
                for c in range(1, 4):
                    Button(self, text="Pad {0}".format(s)).grid(row=s, column=c, sticky=ALL)
                    self.columnconfigure(c, weight=1)

        self.rowconfigure(5, weight=1)

        for r in range (1,3):
            for c in range (5,8):
                Button(self, text="Effect Knob").grid(row=r, column=c, sticky=ALL)

        frame1 = Frame(self, width=20, height=20)
        frame1.grid(row=0, column=6, sticky=ALL)
        Scale(frame1, from_=0, to=100, orient=HORIZONTAL).pack()
        label1 = Label(frame1, text='Volume').pack()

        # Need to configure command
        Button(self, text="Reset").grid(row=0, column=8, sticky=ALL)
