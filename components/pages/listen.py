from components.pages.page import Page
import tkinter as tk
from components.home_button import HomeButton


class Listen(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        HomeButton(self, global_app)
        label = tk.Label(self, text="Listen")
        label.pack(side="top", fill="both", expand=True)

