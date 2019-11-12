from components.pages.page import Page
from tkinter import *
import tkinter as tk

ALL = N+S+W+E

class Produce(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.global_app = global_app
        self.pads = [[], [], [], []]
        self.pads_texts = [[], [], [], []]
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for c in range(9):
            self.columnconfigure(c, weight=1)

        for r in range(6):
            self.rowconfigure(r, weight=1)

        Button(self, text="Home", command=global_app.show_home).grid(row=0, column=0, sticky=ALL)

        for row in range(4):
            for column in range(4):
                self.pads_texts[row].append(tk.StringVar())
                self.pads_texts[row][column].set("Click To Setup Pad")
                self.pads[row].append(Button(self, textvariable=self.pads_texts[row][column], command=lambda row=row, column=column: global_app.show_set_up_pad_step_one(row, column)).grid(row=row+1, column=column, sticky=ALL))

        for row in range(2):
            for column in range(3):
                Button(self, text="Effect Knob").grid(row=row+1, column=column+5, sticky=ALL)

        volume_frame = Frame(self, width=20, height=20)
        volume_frame.grid(row=0, column=6, sticky=ALL)
        Scale(volume_frame, from_=0, to=100, orient=HORIZONTAL).pack()
        Label(volume_frame, text='Volume').pack()

        Button(self, text="Reset", command=self.__reset).grid(row=0, column=8, sticky=ALL)

    def activate_pad(self, row, column):
        self.pads_texts[row][column].set("Ready")

    def __reset(self):
        hardware_interface = self.global_app.get_hardware_interface()
        hardware_interface.reset()
        for row in range(4):
            for column in range(4):
                self.pads_texts[row][column].set("Click To Setup Pad")
