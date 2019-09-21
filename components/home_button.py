import tkinter as tk


class HomeButton:
    def __init__(self, page, global_app):
        button_frame = tk.Frame(page)
        button_frame.pack(side="top", fill="x", expand=False)

        b1 = tk.Button(button_frame, text="Home", command=global_app.show_home)

        b1.pack(side="left")
