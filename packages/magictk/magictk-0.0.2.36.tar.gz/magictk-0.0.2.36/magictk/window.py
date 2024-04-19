import time
import tkinter
import os
from tkinter import ttk
try:
    import color_tmpl
except ImportError:
    from magictk import color_tmpl
try:
    import _window_ctl
except ImportError:
    from magictk import _window_ctl
try:
    import _window_size
except ImportError:
    from magictk import _window_size
try:
    import workspace
except ImportError:
    from magictk import workspace
try:
    import photoload
except ImportError:
    from magictk import photoload
import sys

WIN_INF = -10000


class Window(ttk.Frame):
    x = 200
    y = 200
    w = 500
    h = 350
    normal_x = -1
    normal_y = 1
    top_h = 28
    __break_win = True
    fullscreen = False
    minmode = False
    color = color_tmpl.default_color
    anim = []
    disable_move = False
    min_w = 200
    min_h = 100

    def update_size(self) -> None:
        self.tk_w_without_bar.set(self.w-48*3)
        self.place(x=8, y=self.top_h+1+8, width=self.w-16, height=self.h-1-16)
        self.main_tk.geometry(
            f"{self.w}x{self.h+self.top_h}+{self.x}+{self.y}")
        self.__fake_tk.geometry(
            f"{self.w}x{self.h}+{WIN_INF}+{WIN_INF}")

    def __load_color(self) -> None:
        self.main_tk.configure(bg=self.color["background"])
        self.style.configure(
            'Test1.TFrame', background="#FF0000")
        self.style.configure(
            'Test2.TFrame', background="#00FF00")
        self.style.configure(
            'Test3.TFrame', background="#0000FF")
        self.style.configure(
            'Main.TFrame', background=self.color["background"])
        self.style.configure(
            'Root.TFrame', background=self.color["background"])
        self.style.configure(
            'Splitline.TFrame', background=self.color["border_light"])
        self.style.configure(
            'BarExitButton.TFrame', background=self.color["background"])
        self.style.configure(
            'LabBarZoomButton.TLabel', background=self.color["background"])
        self.style.configure(
            'LabBarIcon.TLabel', background=self.color["background"])
        self.style.configure(
            'LabTitle.TLabel', background=self.color["background"], fg=self.color["primary_text"])
        self.style.configure(
            'BarIconicButton.TFrame', background=self.color["background"])
        self.style.configure(
            'Size.TFrame', background=self.color["background"])
        self.style.configure(
            'LabelTitle.TFrame', background=self.color["background"])

    def __init_weights(self, root: tkinter.Frame) -> None:
        top_bar = ttk.Frame(root, style='Root.TFrame', height=self.top_h)
        startmove_x = 0
        startmove_y = 0
        title_frame = ttk.Frame(
            top_bar, style="LabelTitle.TFrame", height=self.top_h)

        def start_move(event: tkinter.Event):
            if (self.disable_move):
                return
            nonlocal startmove_x, startmove_y
            startmove_x = event.x_root-self.main_tk.winfo_x()
            startmove_y = event.y_root-self.main_tk.winfo_y()
            if (self.fullscreen):
                self.zoom()
                self.x = event.x_root-(event.x_root-self.main_tk.winfo_x())
                self.y = event.y_root-(event.y_root-self.main_tk.winfo_y())
                startmove_x = int(self.w/2)
                startmove_y = int(self.top_h/2)
                self.update_size()
            title_frame.configure(cursor="arrow")

        def move_win(event: tkinter.Event):
            if (self.disable_move):
                return
            nonlocal startmove_x, startmove_y
            if (self.fullscreen):
                return
            self.x = event.x_root-startmove_x
            self.y = event.y_root-startmove_y
            if (event.y_root < 5):
                title_frame.configure(cursor="dotbox")
            else:
                title_frame.configure(cursor="fleur")
            self.update_size()

        def special_move(event: tkinter.Event):
            if (event.y_root < 5):
                self.y = 50
                self.zoom()
            title_frame.configure(cursor="arrow")
        top_bar.place(x=0, y=0, relwidth=1)
        ttk.Frame(root, style='Splitline.TFrame',
                  height=1).place(x=0, y=self.top_h, relwidth=1)

        icons = ttk.Label(top_bar, image=photoload.loadimg(
            "icon"), width=2, compound="center", justify="center", style="LabBarIcon.TLabel")
        icons.bind("<ButtonRelease-2>", lambda event=None: self.quit())
        icons.pack(anchor="center", side='left', padx=8, pady=4)

        title_frame.pack(anchor="center", side='left',
                         fill=tkinter.X, expand=True)
        control_frame = ttk.Frame(
            top_bar, style="Root.TFrame", height=self.top_h, width=48*3)
        control_frame.pack(anchor="e", side='right')
        title_frame.bind("<Button-1>", start_move)
        title_frame.bind("<B1-Motion>", move_win)
        title_frame.bind("<ButtonRelease-1>", special_move)

        _window_ctl.exit_btn_set(self, root)
        _window_ctl.zoom_btn_set(self, root)
        _window_ctl.iconic_btn_set(self, root)
        _window_size.placeall(self, root)

        titles = ttk.Label(title_frame, text=self.title,
                           style="LabTitle.TLabel")
        titles.pack()
        titles.bind("<Button-1>", start_move)
        titles.bind("<B1-Motion>", move_win)
        titles.bind("<ButtonRelease-1>", special_move)

    def __init__(self, w=500, h=350, title="MagicTk", color_list: dict = None) -> None:
        self.root = self
        self.title = title
        self.w = w
        self.h = h
        if (color_list is not None):
            self.color = color_list
        self.main_tk = tkinter.Tk()
        self.main_tk.overrideredirect(True)
        self.__fake_tk = tkinter.Tk()
        self.style = ttk.Style()
        self.__load_color()
        self.tk_w_without_bar = tkinter.IntVar()
        self.tk_w_without_bar.set(self.w-48*3)

        ttk.Widget.__init__(self, self.main_tk, "ttk::frame", {
                            "style": "Main.TFrame"})
        self.place(x=8, y=self.top_h+1+8, width=self.w-16, height=self.h-1-16)

        self.update_size()
        self.__fake_tk.title(self.title)
        self.main_tk.title(self.title)
        self.__fake_tk.protocol("WM_DELETE_WINDOW", self.quit)
        self.__fake_tk.bind('<FocusIn>', self.__top_window)
        self.__fake_tk.resizable(0, 0)
        self.__init_weights(self.main_tk)
        try:
            self.main_tk.iconbitmap(
                os.path.dirname(__file__)+os.sep+"icon.ico")
            self.__fake_tk.iconbitmap(
                os.path.dirname(__file__)+os.sep+"icon.ico")
        except:
            # What's fuck in Linux
            self.zoom()
            self.main_tk.update()
            self.__fake_tk.update()
            self.zoom()
            self.main_tk.update()
            self.__fake_tk.update()

    def mainloop(self) -> None:
        t_start = time.time()
        while (self.__break_win):
            delta_t = time.time()-t_start
            if (delta_t > 0.02):  # flash animation
                t_start = time.time()
                n = 0
                for i in self.anim:
                    if (i is not None):
                        retn = i()
                        if (retn == -1):
                            self.anim[n] = None
                    n += 1
                self.anim = [i for i in self.anim if i is not None]
            else:
                pass
            if (self.__fake_tk.state() == "iconic"):
                if (self.normal_x == -1):
                    self.normal_x = self.x
                    self.normal_y = self.y
                    self.x = WIN_INF
                    self.y = WIN_INF
                    self.minmode = True
                    self.fullscreen = False
                    self.update_size()
            else:
                if (self.normal_x != -1):
                    self.x = self.normal_x
                    self.y = self.normal_y
                    self.normal_x = -1
                    self.minmode = False
                    self.update_size()
            self.main_tk.update()
            self.__fake_tk.update()
        self.main_tk.destroy()
        self.__fake_tk.destroy()
        self.main_tk.mainloop()
        self.__break_win = None

    def quit(self) -> None:
        self.__break_win = False

    def iconify(self) -> None:
        if (self.fullscreen == True):
            self.zoom()
        self.__fake_tk.iconify()

    def __top_window(self, event=None) -> None:
        self.main_tk.state("normal")
        self.main_tk.focus_set()
        self.main_tk.attributes('-topmost', 'true')
        self.main_tk.update()
        self.main_tk.attributes('-topmost', 'false')

    def zoom(self) -> None:
        if (self.fullscreen == False):
            self.normal_w = self.w
            self.normal_h = self.h
            self.old_x = self.x
            self.old_y = self.y
            nx = 0
            ny = 0
            nw, nh = self.__fake_tk.maxsize()
            try:
                wsp = workspace.get_workspace_size()
                nx = wsp[0]
                ny = wsp[1]
                nw = wsp[2]
                nh = wsp[3]-self.top_h
            except:
                pass
            self.normal_x = -1
            self.x = nx
            self.y = ny
            self.main_tk.geometry(
                f"+{self.x}+{self.y}")
            self.main_tk.update()
            self.w = nw
            self.h = nh
            self.update_size()
            self.fullscreen = True
            self.minmode = False
            self.__top_window()
        else:
            self.normal_x = -1
            self.x = self.old_x
            self.y = self.old_y
            self.main_tk.geometry(
                f"+{self.x}+{self.y}")
            self.main_tk.update()
            self.w = self.normal_w
            self.h = self.normal_h
            self.fullscreen = False
            self.minmode = False
            self.update_size()
            self.__top_window()
        self.update_icon()
