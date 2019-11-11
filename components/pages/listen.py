from components.pages.page import Page
import tkinter as tk
from services.audio_services import AudioServices
from services.files_services import FilesServices
from tkinter import *

ALL = N + S + W + E


class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.master.rowconfigure(0, weight=100)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        self.play_buttons = []
        self.play_button_texts = []
        self.play_button_status = []

        for c in range(4):
            if c == 1:
                self.columnconfigure(c, weight=3)
            else:
                self.columnconfigure(c, weight=1)

        Button(self, text="Home", command=global_app.show_home).grid(row=0, column=0, sticky=ALL)

        frame1 = Frame(self, width=25, height=25)
        frame1.grid(row=0, column=2, sticky=ALL)
        Scale(frame1, from_=0, to=100, orient=HORIZONTAL).pack()
        Label(frame1, text='Volume').pack()

        self.master.rowconfigure(1, weight=100)
        Label(self, text="").grid(row=1, column=1, sticky=W)
        self.master.rowconfigure(2, weight=1)
        Label(self, text="Name").grid(row=2, column=1, sticky=W)
        Label(self, text="").grid(row=3, column=1, sticky=W)

        tracks = FilesServices.get_tracks()
        for index, song in enumerate(tracks):
            self.master.rowconfigure(index + 4, weight=100)
            Label(self, text=song).grid(row=index + 4, column=1, sticky=W)
            self.play_button_status.append(False)
            self.play_button_texts.append(tk.StringVar())
            self.play_buttons.append(Button(self, textvariable=self.play_button_texts[index], command=lambda i=index: self.__on_play_button_clicked(tracks[i], i)).grid(row=index + 4, column=2, sticky=ALL))
            self.play_button_texts[index].set("Play")

    def __on_play_button_clicked(self, track, index):
        if self.play_button_status[index] is False:
            AudioServices.play_track(track)
            self.__reset_all_play_buttons()
            self.play_button_status[index] = True
            self.play_button_texts[index].set("Stop")
        else:
            AudioServices.end_track()
            self.play_button_status[index] = False
            self.play_button_texts[index].set("Play")

    def __reset_all_play_buttons(self):
        for index in range(len(self.play_button_texts)):
            self.play_button_texts[index].set("Play")
            self.play_button_status[index] = False
