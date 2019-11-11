from components.pages.page import Page
from tkinter import *


ALL = N+S+W+E


class Home(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for c in range(5):
            self.columnconfigure(c, weight=1)

        for c in range(5):
            self.rowconfigure(c, weight=1)

        Button(self, text="Listen", command=global_app.show_listen).grid(row=2, column=1, sticky=ALL)
        Button(self, text="Produce", command=global_app.show_produce).grid(row=2, column=3, sticky=ALL)
