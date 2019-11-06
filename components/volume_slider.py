import tkinter as tk
from tkinter import *
ALL = N+S+W+E


class VolumeSlider:
    def __init__(self):

        button_frame = tk.Frame()
        w = Scale(button_frame, from_=0, to=100, orient=HORIZONTAL)
        w.pack()
