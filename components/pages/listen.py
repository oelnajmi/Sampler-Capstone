from components.pages.page import Page
import tkinter as tk
from components.home_button import HomeButton
from services.files_services import FilesServices
from services.audio_services import AudioServices



class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        HomeButton(self, global_app)
        label = tk.Label(self, FilesServices.get_tracks())
        label = tk.Label(self, AudioServices.play_track())
        label.pack(side="top", fill="both", expand=True)

