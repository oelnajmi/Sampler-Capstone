import tkinter as tk


class PadButton:
    def __init__(self, page, global_app, index):
        button_frame = tk.Frame(page)
        button_frame.pack(side="top", fill="x", expand=False)
        self.index = index
        b1 = tk.Button(button_frame, text="Pad", command=print("Pad " + str(self.index) + " has been created"))
        b1.pack(side="left")