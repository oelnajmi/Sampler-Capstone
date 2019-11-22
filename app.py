import tkinter as tk
from components.pages.listen import Listen
from components.pages.produce import Produce
from components.pages.home import Home
from components.pages.setup_pad_step_one import SetupPadStepOne
from components.pages.setup_pad_step_two import SetupPadStepTwo
from services.volume_service import VolumeService
from hardware.interface import Interface


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.hardware_interface = Interface()

        tk.Frame.__init__(self, *args, **kwargs)
        self.listen = Listen(self)
        self.produce = Produce(self)
        self.home = Home(self)
        self.set_up_pad_step_one = SetupPadStepOne(self)
        self.set_up_pad_step_two = SetupPadStepTwo(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.listen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.produce.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.set_up_pad_step_one.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.set_up_pad_step_two.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.show_home()

    def show_listen(self):
        self.listen.show()

    def show_produce(self):
        self.produce.show()

    def show_home(self):
        self.home.show()

    def show_set_up_pad_step_one(self, pad_row, pad_column):
        self.set_up_pad_step_one.set_pad(pad_row, pad_column)
        self.set_up_pad_step_one.show()

    def show_set_up_pad_step_two(self, track, pad_row, pad_column):
        self.set_up_pad_step_two.setup(track, pad_row, pad_column)
        self.set_up_pad_step_two.show()

    def get_produce_page(self):
        return self.produce

    def get_listen_page(self):
        return self.listen

    def get_hardware_interface(self):
        return self.hardware_interface


if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    VolumeService.set_global_app(main)
    root.wm_geometry("400x400+120+120")
    root.mainloop()
