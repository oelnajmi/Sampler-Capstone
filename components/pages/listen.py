from components.pages.page import Page
import tkinter as tk
from components.home_button import HomeButton
from services.files_services import FilesServices
from tkinter import *
from components.volume_slider import VolumeSlider

ALL = N + S + W + E


class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.master.rowconfigure(0, weight=100)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for c in range(4):
            if c == 1:
                self.columnconfigure(c, weight=3)
            else:
                self.columnconfigure(c, weight=1)

        Button(self, text="Home", command=global_app.show_home).grid(row=0, column=0, sticky=ALL)

        frame1 = Frame(self, width=25, height=25)
        frame1.grid(row=0, column=2, sticky=ALL)
        Scale(frame1, from_=0, to=100, orient=HORIZONTAL).pack()
        label1 = Label(frame1, text='Volume').pack()

        self.master.rowconfigure(1, weight=100)
        Label(self, text="").grid(row=1, column=1, sticky=W)
        self.master.rowconfigure(2, weight=1)
        Label(self, text="Name").grid(row=2, column=1, sticky=W)
        Label(self, text="").grid(row=3, column=1, sticky=W)

        counter = 4
        for song in FilesServices.get_tracks():
            self.master.rowconfigure(counter, weight=100)
            Label(self, text=song).grid(row=counter, column=1, sticky=W)
            # need to configure command
            Button(self, text="Play").grid(row=counter, column=2, sticky=ALL)
            counter = counter + 1
