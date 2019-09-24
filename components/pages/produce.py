from components.pages.page import Page
from components.home_button import HomeButton
from components.pad_button import PadButton
from components.effect_button import EffectButton
import tkinter as tk


class Produce(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        self.grid(column=0, row=0, columnspan=4, rowspan=4)
        HomeButton(self, global_app)
        pad_one = PadButton(self, global_app, 1)
        pad_one.grid(column=2, row=2)
        PadButton(self, global_app, 2)
        PadButton(self, global_app, 3)
        PadButton(self, global_app, 4)
        PadButton(self, global_app, 5)
        PadButton(self, global_app, 6)
        PadButton(self, global_app, 7)
        PadButton(self, global_app, 8)
        PadButton(self, global_app, 9)
        PadButton(self, global_app, 10)
        PadButton(self, global_app, 11)
        PadButton(self, global_app, 12)
        PadButton(self, global_app, 13)
        PadButton(self, global_app, 14)
        PadButton(self, global_app, 15)
        PadButton(self, global_app, 16)
        EffectButton(self, global_app, 1)
        EffectButton(self, global_app, 2)
        EffectButton(self, global_app, 3)
        EffectButton(self, global_app, 4)
        EffectButton(self, global_app, 5)
        EffectButton(self, global_app, 6)
        EffectButton(self, global_app, 7)
        EffectButton(self, global_app, 8)
        EffectButton(self, global_app, 9)
        label = tk.Label(self, text="Produce")
        label.pack(side="top", fill="both", expand=True)
