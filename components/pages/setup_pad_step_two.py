#########################################################################################################
# To remove the useless buttons (Config and Save) in the toolkit edit the
# `class NavigationToolbar2(object):` line in a file that will be located somewhere like
# C:\Users\Samuel\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\matplotlib\backend_bases.py
#########################################################################################################

import tkinter as tk
from services.audio_services import AudioServices
from components.pages.page import Page
from tkinter import *
from constants import Constants
import numpy as np
import wave
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

ALL = N+S+W+E


class SnapToCursor(object):
    def __init__(self, ax, x, y, parent_class, default_beginning=True):
        self.active = False
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.x = x
        self.y = y
        self.txt = ax.text(0.7, 0.9, '')
        self.parent_class = parent_class
        if default_beginning:
            self.marker, = ax.plot([0], [0], marker="o", color="crimson", zorder=3)
        else:
            self.ly.set_xdata(x[-1])
            self.marker, = ax.plot(x[-1], y[-1], marker="o", color="crimson", zorder=3)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def mouse_click(self, event):
        if not event.inaxes:
            return
        if not self.active:
            return
        x, y = event.xdata, event.ydata
        index = np.searchsorted(self.x, [x])[0]
        x = self.x[index]
        y = self.y[index]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.txt.set_position((x,y))
        self.ax.figure.canvas.draw_idle()
        self.parent_class.set_cursor_value(x)


class SetupPadStepTwo(Page):
    def __init__(self, global_app):
        Page.__init__(self)
        self.global_app = global_app
        self.pad_row = None
        self.pad_column = None
        self.track = None
        self.song = None
        self.cursor_one_active = False
        self.cursor_two_active = False
        self.cursor_one_value = None
        self.cursor_two_value = None
        self.play_button_status = False
        self.track_range = None
        self.trackName = StringVar()
        self.cursor_one_button_text = StringVar()
        self.cursor_two_button_text = StringVar()
        self.play_button_text = StringVar()

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for column_index in range(5):
            self.columnconfigure(column_index, weight=1)

        for row_index in range(20):
            self.rowconfigure(row_index, weight=1)

        self.cursor_one_button_text.set("Move Cursor One")
        self.cursor_two_button_text.set("Move Cursor Two")
        self.play_button_text.set("Play")

        Button(self, text="Back", command=self.__on_back).grid(row=0, column=0, sticky=W)
        tk.Label(self, textvariable=self.trackName).grid(row=0, column=1, columnspan=3, sticky=ALL)
        Button(self, text="Cancel", command=global_app.show_produce).grid(row=0, column=4, sticky=E)
        tk.Label(self, text="Slice Track Using Cursors").grid(row=1, column=0, columnspan=5, sticky=W)
        Button(self, textvariable=self.cursor_one_button_text, command=self.__toggle_cursor_one).grid(row=18, column=0, sticky=W)
        Button(self, textvariable=self.play_button_text, command=self.__on_play_button_clicked).grid(row=18, column=2, sticky=ALL)
        Button(self, textvariable=self.cursor_two_button_text, command=self.__toggle_cursor_two).grid(row=18, column=4, sticky=E)
        Button(self, text="Done", command=self.__on_done).grid(row=19, column=4, sticky=E)

    def setup(self, track, pad_row, pad_column):
        self.pad_row = pad_row
        self.pad_column = pad_column
        self.track = track
        self.song = AudioServices.slice_track(track, None, None)
        self.trackName.set(track)
        self.__draw_wave(track)

    def __on_back(self):
        self.global_app.show_set_up_pad_step_one(self.pad_row, self.pad_column)

    def __on_done(self):
        produce = self.global_app.get_produce_page()
        produce.activate_pad(self.pad_row, self.pad_column)
        self.global_app.show_produce()
        hardware_interface = self.global_app.get_hardware_interface()
        hardware_interface.assign_sample_to_pad(self.pad_row, self.pad_column, self.track, self.__get_start_value(), self.__get_end_value())

    def set_cursor_value(self, value):
        if self.cursor_one and self.cursor_one_active:
            self.cursor_one_value = value
        elif self.cursor_two and self.cursor_two_active:
            self.cursor_two_value = value

    def __toggle_cursor_one(self):
        if self.cursor_two and self.cursor_two_active:
            self.__toggle_cursor_two()

        if self.cursor_one and not self.cursor_one_active:
            self.cursor_one.activate()
            self.cursor_one_button_text.set("Freeze Cursor One")
            self.cursor_one_active = True
        elif self.cursor_one and self.cursor_one_active:
            self.cursor_one.deactivate()
            self.cursor_one_button_text.set("Move Cursor One")
            self.cursor_one_active = False

    def __toggle_cursor_two(self):
        if self.cursor_one and self.cursor_one_active:
            self.__toggle_cursor_one()

        if self.cursor_two and not self.cursor_two_active:
            self.cursor_two.activate()
            self.cursor_two_button_text.set("Freeze Cursor Two")
            self.cursor_two_active = True
        elif self.cursor_two and self.cursor_two_active:
            self.cursor_two.deactivate()
            self.cursor_two_button_text.set("Move Cursor Two")
            self.cursor_two_active = False

    def reset_play_button(self):
        self.play_button_status = False
        self.play_button_text.set("Play")

    def __get_start_value(self):
        if self.cursor_one_value < self.cursor_two_value:
            return self.cursor_one_value // (self.song.frame_rate / 1000)
        else:
            return self.cursor_two_value // (self.song.frame_rate / 1000)

    def __get_end_value(self):
        if self.cursor_one_value < self.cursor_two_value:
            return self.cursor_two_value // (self.song.frame_rate / 1000)
        else:
            return self.cursor_one_value // (self.song.frame_rate / 1000)

    def __on_play_button_clicked(self):
        if self.play_button_status is False:
            start = self.__get_start_value()
            end = self.__get_end_value()
            AudioServices.play_track(self.track, start, end, self.reset_play_button)
            self.play_button_status = True
            self.play_button_text.set("Stop")
        else:
            AudioServices.end_track()
            self.play_button_status = False
            self.play_button_text.set("Play")

    def __draw_wave(self, track):
        spf = wave.open(Constants.SAMPLES_FILE_PATH + '/' + track, 'r')
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        signals = []
        if spf.getnchannels() == 2:
            if len(signal) > 5000000:
                signals.append(signal[0:5000000:2])
                signals.append(signal[1:5000000:2])
            else:
                signals.append(signal[0::2])
                signals.append(signal[1::2])
        else:
            if len(signal) > 2500000:
                signals.append(signal[0:2500000])
            else:
                signals.append(signal)

        fig = Figure(figsize=(14, 5))
        for signal in signals:
            fig.add_subplot().plot(signal)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, columnspan=5, rowspan=14)

        toolbar_frame = Frame(master=self)
        toolbar_frame.grid(row=17, column=0, columnspan=5, sticky=W)
        NavigationToolbar2Tk(canvas, toolbar_frame)

        self.cursor_one = SnapToCursor(fig.axes[0], range(len(signal)), signal, self)
        fig.canvas.mpl_connect('button_press_event', self.cursor_one.mouse_click)

        self.cursor_two = SnapToCursor(fig.axes[0], range(len(signal)), signal, self, False)
        fig.canvas.mpl_connect('button_press_event', self.cursor_two.mouse_click)

        self.cursor_one_value = 0
        self.cursor_two_value = len(signal)

        del signal
        del signals
