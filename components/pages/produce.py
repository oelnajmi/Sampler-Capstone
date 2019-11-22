from components.pages.page import Page
from tkinter import *
from services.audio_services import AudioServices
from services.volume_service import VolumeService
import tkinter as tk

ALL = N+S+W+E


class Produce(Page):
    def __init__(self, global_app):
        Page.__init__(self)

        self.global_app = global_app
        self.pads = [[], [], [], []]
        self.pads_texts = [[], [], [], []]
        self.knobs = []
        self.knobs_texts = []
        self.knobs_status = []
        self.grid(sticky=ALL)

        for c in range(10):
            self.columnconfigure(c, weight=1)

        for r in range(6):
            self.rowconfigure(r, weight=1)

        Button(self, text="Home", command=global_app.show_home).grid(row=0, column=0, sticky=ALL)

        for row in range(4):
            for column in range(4):
                self.pads_texts[row].append(tk.StringVar())
                self.pads_texts[row][column].set("Click To Setup Pad")
                button = Button(self, textvariable=self.pads_texts[row][column], command=lambda row=row, column=column: global_app.show_set_up_pad_step_one(row, column))
                button.grid(row=row+1, column=column, sticky=ALL)
                self.pads[row].append(button)

        self.knobs_texts.append(tk.StringVar())
        self.knobs_status.append(False)
        self.knobs_texts[0].set("Low Pass Filter\nActivate")
        button = Button(self, textvariable=self.knobs_texts[0], command=self.toggle_low_pass_knob)
        button.grid(row=2, column=6, sticky=ALL)
        self.knobs.append(button)

        self.knobs_texts.append(tk.StringVar())
        self.knobs_status.append(False)
        self.knobs_texts[1].set("High Pass Filter\nActivate")
        button = Button(self, textvariable=self.knobs_texts[1], command=self.toggle_high_pass_knob)
        button.grid(row=2, column=7, sticky=ALL)
        self.knobs.append(button)

        self.knobs_texts.append(tk.StringVar())
        self.knobs_status.append(False)
        self.knobs_texts[2].set("Panning Filter\nActivate")
        button = Button(self, textvariable=self.knobs_texts[2], command=self.toggle_panning_knob)
        button.grid(row=2, column=8, sticky=ALL)
        self.knobs.append(button)

        self.knobs_texts.append(tk.StringVar())
        self.knobs_status.append(False)
        self.knobs_texts[3].set("Speedup\nActivate")
        button = Button(self, textvariable=self.knobs_texts[3], command=self.toggle_speedup_knob)
        button.grid(row=2, column=9, sticky=ALL)
        self.knobs.append(button)

        volume_frame = Frame(self, width=20, height=20)
        volume_frame.grid(row=0, column=6, sticky=ALL)
        self.volume = Scale(volume_frame, from_=0, to=100, orient=HORIZONTAL, command=self.__on_volume_change)
        self.volume.pack()
        self.volume.set(100)
        Label(volume_frame, text='Volume').pack()

        Button(self, text="Reset", command=self.__reset).grid(row=0, column=9, sticky=ALL)

    def activate_pad(self, row, column):
        self.pads[row][column].configure(bg='green')
        self.pads_texts[row][column].set("Ready")

    def toggle_low_pass_knob(self):
        if self.knobs_status[0]:
            self.knobs_status[0] = False
            self.knobs[0].configure(bg='SystemButtonFace')
            self.knobs_texts[0].set("Low Pass Filter\nActivate")
            AudioServices.deactivate_effect(0)
        else:
            self.knobs_status[0] = True
            self.knobs[0].configure(bg="green")
            self.knobs_texts[0].set("Low Pass Filter\nDeactivate")
            AudioServices.activate_effect(0)

    def toggle_high_pass_knob(self):
        if self.knobs_status[1]:
            self.knobs_status[1] = False
            self.knobs[1].configure(bg='SystemButtonFace')
            self.knobs_texts[1].set("High Pass Filter\nActivate")
            AudioServices.deactivate_effect(1)
        else:
            self.knobs_status[1] = True
            self.knobs[1].configure(bg="green")
            self.knobs_texts[1].set("High Pass Filter\nDeactivate")
            AudioServices.activate_effect(1)

    def toggle_panning_knob(self):
        if self.knobs_status[2]:
            self.knobs_status[2] = False
            self.knobs[2].configure(bg='SystemButtonFace')
            self.knobs_texts[2].set("Panning Filter\nActivate")
            AudioServices.deactivate_effect(2)
        else:
            self.knobs_status[2] = True
            self.knobs[2].configure(bg="green")
            self.knobs_texts[2].set("Panning Filter\nDeactivate")
            AudioServices.activate_effect(2)

    def toggle_speedup_knob(self):
        if self.knobs_status[3]:
            self.knobs_status[3] = False
            self.knobs[3].configure(bg='SystemButtonFace')
            self.knobs_texts[3].set("Speedup\nActivate")
            AudioServices.deactivate_effect(3)
        else:
            self.knobs_status[3] = True
            self.knobs[3].configure(bg="green")
            self.knobs_texts[3].set("    Speedup    \nDeactivate")
            AudioServices.activate_effect(3)

    def __reset(self):
        hardware_interface = self.global_app.get_hardware_interface()
        hardware_interface.reset()
        for row in range(4):
            for column in range(4):
                self.pads[row][column].configure(bg='SystemButtonFace')
                self.pads_texts[row][column].set("Click To Setup Pad")
        for i in range(4):
            self.knobs_status[i] = False
            self.knobs[i].configure(bg='SystemButtonFace')
        self.knobs_texts[0].set("Low Pass Filter\nActivate")
        self.knobs_texts[1].set("High Pass Filter\nActivate")
        self.knobs_texts[2].set("Panning Filter\nActivate")
        self.knobs_texts[3].set("    Speedup    \nActivate")
        AudioServices.reset_effect()

    def __on_volume_change(self, value):
        VolumeService.set_volume(value, 'PRODUCE')

    def set_volume(self, value):
        self.volume.set(value)
