from components.pages.page import Page
import tkinter as tk
from components.home_button import HomeButton
from services.files_services import FilesServices



class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        HomeButton(self, global_app)

        for song in FilesServices.get_tracks():
            label = tk.Label(self, text=song)
            label.pack(side="top", fill="both", expand=True)
            button_frame = tk.Frame(self)
            button_frame.pack(side="top", fill="x", expand=False)
            play_button = tk.Button(button_frame, text="play")
            play_button.pack(side="right", fill="x", expand=False)
            # Need to add a play button here
