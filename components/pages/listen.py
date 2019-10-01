from components.pages.page import Page
import tkinter as tk
from components.home_button import HomeButton
from services.files_services import FilesServices
from pydub.playback import play


class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        HomeButton(self, global_app)
        label = tk.Label(self, FilesServices.get_tracks())
        sound = FilesServices.get_tracks()
        play(sound)
        label.pack(side="top", fill="both", expand=True)

