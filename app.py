import tkinter as tk
from components.pages.listen import Listen
from components.pages.produce import Produce
from components.pages.home import Home


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.listen = Listen(self)
        self.produce = Produce(self)
        self.home = Home(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.listen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.produce.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.show_home()

    def show_listen(self):
        self.listen.show()

    def show_produce(self):
        self.produce.show()

    def show_home(self):
        self.home.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
