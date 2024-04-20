import tkinter
from tkinter import ttk
from magictk import color_tmpl


class Frame(tkinter.Frame):
    color = color_tmpl.default_color

    def __init__(self, master, color=None, *args, **kwargs):
        self.root = master.root
        kwargs["bg"] = self.color["background"]
        super().__init__(master, *args, **kwargs)
        self.configure()
