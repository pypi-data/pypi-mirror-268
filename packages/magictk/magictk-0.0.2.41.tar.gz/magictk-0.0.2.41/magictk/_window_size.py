import tkinter
from tkinter import ttk


def place_move_up(self, root):
    global change_bar_move_up, up_move_start, up_move
    move_up = ttk.Frame(
        root, style="Size.TFrame", height=6, width=self.tk_w_without_bar.get(), cursor="top_side")

    def change_bar_move_up(*args, **kwargs):
        move_up.configure(width=self.tk_w_without_bar.get())
    self.tk_w_without_bar.trace_add('write', change_bar_move_up)
    move_up.place(x=0, y=0)
    upstart_h = self.h
    upstart_y = self.y

    def up_move_start(event: tkinter.Event):
        # self.disable_move = True
        # print(1)
        nonlocal upstart_h, upstart_y
        upstart_h = self.h-self.top_h
        upstart_y = event.y_root

    def up_move(event: tkinter.Event):
        nonlocal upstart_h, upstart_y
        if (self.fullscreen):
            return
        now_y = event.y_root
        delta_y = upstart_y-now_y
        now_h = upstart_h+delta_y
        if (now_h < self.min_h):
            return
        self.normal_x = -1
        self.y = upstart_y-delta_y
        self.h = now_h+self.top_h
        self.update_size()
        self.main_tk.update()
    move_up.bind("<Button-1>", up_move_start)
    move_up.bind("<B1-Motion>", up_move)


def place_move_up_bar(self, root):
    move_up_bar = ttk.Frame(
        root, style="Size.TFrame", height=1, width=48*3, cursor="top_side")

    def change_bar_move_up(*args, **kwargs):
        move_up_bar.place(x=self.tk_w_without_bar.get(), y=0)
    self.tk_w_without_bar.trace_add('write', change_bar_move_up)

    self.tk_w_without_bar.trace_add('write', change_bar_move_up)
    move_up_bar.place(y=0, x=self.tk_w_without_bar.get())
    move_up_bar.bind("<Button-1>", up_move_start)
    move_up_bar.bind("<B1-Motion>", up_move)


def place_move_down(self, root):
    global down_move_start, down_move
    move_down = ttk.Frame(
        root, style="Size.TFrame", height=4, width=self.tk_w_without_bar.get(), cursor="bottom_side")

    def change_bar_move_up(*args, **kwargs):
        move_down.place(x=0, y=self.top_h+self.h-4, relwidth=1)
    self.tk_w_without_bar.trace_add('write', change_bar_move_up)
    move_down.place(x=0, y=self.top_h+self.h-4, relwidth=1)
    downstart_h = self.h
    downstart_y = self.y

    def down_move_start(event: tkinter.Event):
        nonlocal downstart_h, downstart_y
        downstart_h = self.h-self.top_h
        downstart_y = event.y_root

    def down_move(event: tkinter.Event):
        nonlocal downstart_h, downstart_y
        if (self.fullscreen):
            return
        now_y = event.y_root
        delta_y = downstart_y-now_y
        now_h = downstart_h-delta_y
        if (now_h < self.min_h):
            return
        self.normal_x = -1
        self.h = now_h+self.top_h
        self.update_size()
        self.main_tk.update()
    move_down.bind("<Button-1>", down_move_start)
    move_down.bind("<B1-Motion>", down_move)


def place_move_left(self, root):
    global left_move_start, left_move
    move_left = ttk.Frame(
        root, style="Size.TFrame", width=6, height=self.top_h, cursor="left_side")

    move_left.place(x=0, y=0)
    leftstart_w = self.w
    leftstart_x = self.x

    def left_move_start(event: tkinter.Event):
        # self.disable_move = True
        # print(1)
        nonlocal leftstart_w, leftstart_x
        leftstart_w = self.w
        leftstart_x = event.x_root

    def left_move(event: tkinter.Event):
        nonlocal leftstart_w, leftstart_x
        if (self.fullscreen):
            return
        now_x = event.x_root
        delta_x = leftstart_x-now_x
        now_w = leftstart_w+delta_x
        if (now_w < self.min_w):
            return
        self.normal_x = -1
        self.x = leftstart_x-delta_x
        self.w = now_w
        self.update_size()
        self.main_tk.update()
    move_left.bind("<Button-1>", left_move_start)
    move_left.bind("<B1-Motion>", left_move)


def place_move_left_bar(self, root):
    move_left = ttk.Frame(
        root, style="Size.TFrame", width=4, height=self.h, cursor="left_side")

    def change_bar_move_up(*args, **kwargs):
        move_left.configure(height=self.h)
    self.tk_w_without_bar.trace_add('write', change_bar_move_up)
    move_left.place(x=0, y=self.top_h)

    move_left.bind("<Button-1>", left_move_start)
    move_left.bind("<B1-Motion>", left_move)


def place_move_right(self, root):
    global right_move, right_move_start
    move_right = ttk.Frame(
        root, style="Size.TFrame", width=1, height=self.top_h, cursor="right_side")

    def change_bar_move(*args, **kwargs):
        move_right.place(x=self.w-1, y=0)
    self.tk_w_without_bar.trace_add('write', change_bar_move)
    move_right.place(x=self.w-1, y=0)
    rightstart_w = self.w
    rightstart_x = self.x

    def right_move_start(event: tkinter.Event):
        # self.disable_move = True
        # print(1)
        nonlocal rightstart_w, rightstart_x
        rightstart_w = self.w
        rightstart_x = event.x_root

    def right_move(event: tkinter.Event):
        nonlocal rightstart_w, rightstart_x
        if (self.fullscreen):
            return
        now_x = event.x_root
        delta_x = rightstart_x-now_x
        now_w = rightstart_w-delta_x
        if (now_w < self.min_w):
            return
        self.normal_x = -1
        self.w = now_w
        self.update_size()
        self.main_tk.update()
    move_right.bind("<Button-1>", right_move_start)
    move_right.bind("<B1-Motion>", right_move)


def place_move_right_bar(self, root):
    move_right = ttk.Frame(
        root, style="Size.TFrame", width=4, height=self.h, cursor="right_side")

    def change_bar_move_right(*args, **kwargs):
        move_right.place(x=self.w-4, y=self.top_h)
        move_right.configure(height=self.h)
    self.tk_w_without_bar.trace_add('write', change_bar_move_right)
    move_right.place(x=self.w-4, y=self.top_h)
    move_right.bind("<Button-1>", right_move_start)
    move_right.bind("<B1-Motion>", right_move)


def place_move_LT_bar(self, root):
    move_LT = ttk.Frame(
        root, style="Size.TFrame", width=8, height=8, cursor="top_left_corner")

    move_LT.place(x=0, y=0)

    leftstart_w = self.w
    leftstart_x = self.x
    upstart_h = self.h
    upstart_y = self.y

    def LT_move_start(event=None):
        nonlocal leftstart_w, leftstart_x
        leftstart_w = self.w
        leftstart_x = event.x_root
        nonlocal upstart_h, upstart_y
        upstart_h = self.h-self.top_h
        upstart_y = event.y_root

    def LT_move(event=None):
        while 1:
            nonlocal leftstart_w, leftstart_x
            if (self.fullscreen):
                break
            now_x = event.x_root
            delta_x = leftstart_x-now_x
            now_w = leftstart_w+delta_x
            if (now_w < self.min_w):
                break
            self.normal_x = -1
            self.x = leftstart_x-delta_x
            self.w = now_w
            break
        while 1:
            nonlocal upstart_h, upstart_y
            if (self.fullscreen):
                break
            now_y = event.y_root
            delta_y = upstart_y-now_y
            now_h = upstart_h+delta_y
            if (now_h < self.min_h):
                break
            self.normal_x = -1
            self.y = upstart_y-delta_y
            self.h = now_h+self.top_h
            break
        self.update_size()
        self.main_tk.update()

    move_LT.bind("<Button-1>", LT_move_start)
    move_LT.bind("<B1-Motion>", LT_move)


def place_move_RT_bar(self, root):
    move_RT = ttk.Frame(
        root, style="Size.TFrame", width=2, height=2, cursor="top_right_corner")

    def change_bar_move(*args, **kwargs):
        move_RT.place(x=self.w-2, y=0)
    self.tk_w_without_bar.trace_add('write', change_bar_move)
    move_RT.place(x=self.w-2, y=0)

    upstart_h = self.h
    upstart_y = self.y
    rightstart_w = self.w
    rightstart_x = self.x

    def RT_move_start(event=None):
        nonlocal upstart_h, upstart_y
        upstart_h = self.h-self.top_h
        upstart_y = event.y_root
        nonlocal rightstart_w, rightstart_x
        rightstart_w = self.w
        rightstart_x = event.x_root

    def RT_move(event=None):
        while 1:
            nonlocal upstart_h, upstart_y
            if (self.fullscreen):
                break
            now_y = event.y_root
            delta_y = upstart_y-now_y
            now_h = upstart_h+delta_y
            if (now_h < self.min_h):
                break
            self.normal_x = -1
            self.y = upstart_y-delta_y
            self.h = now_h+self.top_h
            break
        while 1:
            nonlocal rightstart_w, rightstart_x
            if (self.fullscreen):
                break
            now_x = event.x_root
            delta_x = rightstart_x-now_x
            now_w = rightstart_w-delta_x
            if (now_w < self.min_w):
                break
            self.normal_x = -1
            self.w = now_w
            break
        self.update_size()
        self.main_tk.update()

    move_RT.bind("<Button-1>", RT_move_start)
    move_RT.bind("<B1-Motion>", RT_move)


def place_move_RB_bar(self, root):
    move_RB = ttk.Frame(
        root, style="Size.TFrame", width=6, height=6, cursor="bottom_right_corner")

    def change_bar_move(*args, **kwargs):
        move_RB.place(x=self.w-6, y=self.h-6+self.top_h)
    self.tk_w_without_bar.trace_add('write', change_bar_move)
    move_RB.place(x=self.w-6, y=self.h-6+self.top_h)

    rightstart_x = self.x
    rightstart_w = self.w
    downstart_h = self.h
    downstart_y = self.y

    def RB_move_start(event=None):
        nonlocal rightstart_w, rightstart_x
        rightstart_w = self.w
        rightstart_x = event.x_root
        nonlocal downstart_h, downstart_y
        downstart_h = self.h-self.top_h
        downstart_y = event.y_root

    def RB_move(event=None):
        while 1:
            nonlocal rightstart_w, rightstart_x
            if (self.fullscreen):
                break
            now_x = event.x_root
            delta_x = rightstart_x-now_x
            now_w = rightstart_w-delta_x
            if (now_w < self.min_w):
                break
            self.normal_x = -1
            self.w = now_w
            break
        while 1:
            nonlocal downstart_h, downstart_y
            if (self.fullscreen):
                break
            now_y = event.y_root
            delta_y = downstart_y-now_y
            now_h = downstart_h-delta_y
            if (now_h < self.min_h):
                break
            self.normal_x = -1
            self.h = now_h+self.top_h
            break
        self.update_size()
        self.main_tk.update()

    move_RB.bind("<Button-1>", RB_move_start)
    move_RB.bind("<B1-Motion>", RB_move)


def place_move_LB_bar(self, root):
    move_LB = ttk.Frame(
        root, style="Size.TFrame", width=4, height=4, cursor="bottom_left_corner")

    def change_bar_move(*args, **kwargs):
        move_LB.place(x=0, y=self.h-4+self.top_h)
    self.tk_w_without_bar.trace_add('write', change_bar_move)
    move_LB.place(x=0, y=self.h-4+self.top_h)

    leftstart_w = self.w
    leftstart_x = self.x
    downstart_h = self.h
    downstart_y = self.y

    def LB_move_start(event=None):
        nonlocal leftstart_w, leftstart_x
        leftstart_w = self.w
        leftstart_x = event.x_root
        nonlocal downstart_h, downstart_y
        downstart_h = self.h-self.top_h
        downstart_y = event.y_root

    def LB_move(event=None):
        while 1:
            nonlocal leftstart_w, leftstart_x
            if (self.fullscreen):
                break
            now_x = event.x_root
            delta_x = leftstart_x-now_x
            now_w = leftstart_w+delta_x
            if (now_w < self.min_w):
                break
            self.normal_x = -1
            self.x = leftstart_x-delta_x
            self.w = now_w
            break
        while 1:
            nonlocal downstart_h, downstart_y
            if (self.fullscreen):
                break
            now_y = event.y_root
            delta_y = downstart_y-now_y
            now_h = downstart_h-delta_y
            if (now_h < self.min_h):
                break
            self.normal_x = -1
            self.h = now_h+self.top_h
            break
        self.update_size()
        self.main_tk.update()

    move_LB.bind("<Button-1>", LB_move_start)
    move_LB.bind("<B1-Motion>", LB_move)


def placeall(self, root):
    place_move_up(self, root)
    place_move_up_bar(self, root)
    place_move_down(self, root)
    place_move_left(self, root)
    place_move_left_bar(self, root)
    place_move_right(self, root)
    place_move_right_bar(self, root)
    place_move_LT_bar(self, root)
    place_move_RT_bar(self, root)
    place_move_LB_bar(self, root)
    place_move_RB_bar(self, root)
