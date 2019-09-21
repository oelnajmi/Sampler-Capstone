import tkinter as tk
from components.pages.page import Page


class Home(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        b1 = tk.Button(button_frame, text="Listen", command=global_app.show_listen)
        b2 = tk.Button(button_frame, text="Produce", command=global_app.show_produce)

        b1.pack(side="left")
        b2.pack(side="left")
