from components.pages.page import Page
from components.home_button import HomeButton
import tkinter as tk


class Produce(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        HomeButton(self, global_app)
        label = tk.Label(self, text="Produce")
        label.pack(side="top", fill="both", expand=True)
