import tkinter as tk
from services.files_services import FilesServices
from services.audio_services import AudioServices
from components.pages.page import Page
from tkinter import *

ALL = N+S+W+E


class SetupPadStepOne(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        tracks = FilesServices.get_tracks()

        self.global_app = global_app
        self.pad_row = None
        self.pad_column = None

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=1)

        self.play_buttons = []
        self.play_button_texts = []
        self.play_button_status = []

        for i in range(len(tracks) + 1 if len(tracks) > 20 else 21):
            self.rowconfigure(i+1, weight=1)

        tk.Label(self, text="Select Track To Slice").grid(row=0, column=0, sticky=W)
        Button(self, text="Cancel", command=global_app.show_produce).grid(row=0, column=2, sticky=ALL)

        for i in range(len(tracks)):
            tk.Label(self, text=tracks[i]).grid(row=i+2, column=0, sticky=ALL)
            self.play_button_status.append(False)
            self.play_button_texts.append(tk.StringVar())
            self.play_buttons.append(Button(self, textvariable=self.play_button_texts[i], command=lambda i=i: self.__on_play_button_clicked(tracks[i], i)).grid(row=i+2, column=1, sticky=ALL))
            self.play_button_texts[i].set("Play")
            Button(self, text="Select", command=lambda i=i: self.__on_select_clicked(tracks[i])).grid(row=i+2, column=2, sticky=ALL)

    def set_pad(self, pad_row, pad_column):
        self.pad_row = pad_row
        self.pad_column = pad_column

    def __on_select_clicked(self, track):
        self.global_app.show_set_up_pad_step_two(track, self.pad_row, self.pad_column)

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
