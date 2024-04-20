import json
import tkinter
import sys
from tkinter import ttk
from magictk import color_tmpl
from magictk import photoload
from magictk import fontconfig
from magictk import button


class Entry:
    color = color_tmpl.default_color
    __fill_obj = []
    __fill_func = []
    __fill_gc = []
    __fill_fc = []
    __fill_hc = []
    hover_mode = 0.0
    __is_hover = 0
    __flash_t = 0
    max_flash = 6
    __anim_obj_id = -1
    __color_bd = "border_base"
    __color_bg = "background"
    __color_fg = "primary"
    __color_fg1 = "primary"
    __color_fg2 = "background"
    text = "Input"
    input_text = ""

    def __draw_corner(self, r_x, r_y, x, y, **kwargs):
        border_info = json.loads(photoload.loadres("buttonborder"))
        y_n = 0
        for i in border_info:
            x_n = 0
            for j in i:
                if (r_x == 0):
                    px = x+x_n+1
                else:
                    px = x+4-x_n-1
                if (r_y == 0):
                    py = y+y_n+1
                else:
                    py = y+4-y_n-1
                if (j < 0):
                    lcolor = -j
                else:
                    lcolor = j
                g_color = color_tmpl.mix_color(
                    self.color["background"], self.color[self.__color_bd], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    f_color = color_tmpl.mix_color(
                        self.color[self.__color_fg2], self.color[self.__color_fg1], int((1-lcolor/255)*1000)/1000)
                else:
                    f_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self.__color_fg1], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    h_color = color_tmpl.mix_color(
                        self.color[self.__color_fg2], self.color[self.__color_fg], int((1-lcolor/255)*1000)/1000)
                else:
                    h_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self.__color_fg], int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)

                def update_color(obj, g_color, f_color, h_color):
                    if (self.__is_hover == 2):
                        self.canvas.itemconfig(
                            obj, fill=h_color)
                    else:
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))

                self.__fill_func.append(update_color)
                self.__fill_gc.append(g_color)
                self.__fill_fc.append(f_color)
                self.__fill_hc.append(h_color)
                self.__fill_obj.append(obj)
                x_n += 1
            y_n += 1

    def __update_color(self):
        n = 0
        for i in self.__fill_func:
            i(self.__fill_obj[n], self.__fill_gc[n],
              self.__fill_fc[n], self.__fill_hc[n])
            n += 1

    def __init__(self, master=None, root_anim=None, w=200, h=30, text="Input",  color_list: dict = None, items=[]):
        global use_font
        use_font = fontconfig.getfont()
        self.input_text = ""
        self.items = items
        self.w = max(120, w)
        self.h = max(30, h)
        self.text = text
        self.choose = -1
        self.__master = master
        if (color_list is not None):
            self.color = color_list
        if (root_anim == None):
            self.root = master.root
        else:
            self.root = root_anim

        self.frames = tkinter.Frame(
            master, width=self.w, height=self.h, bg=self.color["background"])
        self.canvas = tkinter.Canvas(
            self.frames,
            bg=self.color["background"],
            width=self.w,
            height=self.h,
            borderwidth=0,
            bd=0,
            highlightcolor=self.color["background"],
            highlightthickness=0
        )
        self.canvas.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.__input_textvar = tkinter.StringVar()
        self.inputobj = tkinter.Entry(
            self.frames,
            bg=self.color["background"],
            fg=self.color["regular_text"],
            highlightthickness=0,
            bd=0,
            font=(use_font, 10),
            textvariable=self.__input_textvar
        )
        self.inputobj.place(x=10, y=6, width=self.w-20, height=self.h-12)
        self.show_label = tkinter.Label(self.frames,
                                        text=self.text,
                                        bg=self.color["background"],
                                        fg=self.color["secondary_text"],
                                        anchor="w",
                                        font=(use_font, 10)
                                        )
        self.show_label.place(x=10, y=6, width=self.w-20, height=self.h-12)
        self.packed = True

        self.__draw()
        self.__update_color()
        self.__bind_event()
        self.bind_anim()

    def pack(self, *args, **kwargs):
        self.frames.pack(*args, **kwargs)

    def guid(self, *args, **kwargs):
        self.frames.guid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.frames.place(*args, **kwargs)

    def __draw(self):
        self.__draw_corner(0, 0, 0, 0)
        self.__draw_corner(1, 0, self.w-4, 0)
        self.__draw_corner(0, 1, 0, self.h-5)
        self.__draw_corner(1, 1, self.w-4, self.h-5)

        def update_color(obj, g_color, f_color, h_color):
            if (self.__is_hover == 2):
                self.canvas.itemconfig(
                    obj, fill=h_color)
            else:
                self.canvas.itemconfig(
                    obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))
        self.__fill_fc.append(self.color[self.__color_fg1])
        self.__fill_gc.append(self.color[self.__color_bd])
        self.__fill_hc.append(self.color[self.__color_fg])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_line(
            1, 5, 1, self.h-5, width=1, fill=self.color[self.__color_bd]))
        self.__fill_fc.append(self.color[self.__color_fg1])
        self.__fill_gc.append(self.color[self.__color_bd])
        self.__fill_hc.append(self.color[self.__color_fg])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_line(
            5, 1, self.w-4, 1, width=1, fill=self.color[self.__color_fg1]))
        self.__fill_fc.append(self.color[self.__color_fg1])
        self.__fill_gc.append(self.color[self.__color_bd])
        self.__fill_hc.append(self.color[self.__color_fg])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_line(
            self.w-1, 5, self.w-1, self.h-5, width=1, fill=self.color[self.__color_fg1]))
        self.__fill_fc.append(self.color[self.__color_fg1])
        self.__fill_gc.append(self.color[self.__color_bd])
        self.__fill_hc.append(self.color[self.__color_fg])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_line(
            5, self.h-2, self.w-4, self.h-2, width=1, fill=self.color[self.__color_fg1]))

        self.__fill_fc.append(self.color[self.__color_fg2])
        self.__fill_gc.append(self.color["background"])
        self.__fill_hc.append(self.color[self.__color_fg2])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_rectangle(
            2, 5, self.w-1, self.h-5, width=0, fill=self.color[self.__color_fg2]))

        self.__fill_fc.append(self.color[self.__color_fg2])
        self.__fill_gc.append(self.color["background"])
        self.__fill_hc.append(self.color[self.__color_fg2])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.canvas.create_rectangle(
            5, 2, self.w-4, self.h-2, width=0, fill=self.color[self.__color_fg2]))

        self.__text_obj = self.canvas.create_text(
            20, int(self.h/2), text=self.text, font=(use_font, 10), justify="left")
        self.__fill_fc.append(self.color["placeholder"])
        self.__fill_gc.append(self.color["placeholder"])
        self.__fill_hc.append(self.color["placeholder"])
        self.__fill_func.append(update_color)
        self.__fill_obj.append(self.__text_obj)
        self.canvas.moveto(self.__text_obj, 16, self.h//2-10)

    def bind_anim(self):
        def anim_magictk():
            if (self.__is_hover == 1 and self.__flash_t < self.max_flash):
                self.__flash_t += (1 if (len(self.root.anim) > 6) else 1)
                self.__flash_t = min(self.__flash_t, self.max_flash)
                self.hover_mode = self.__flash_t/self.max_flash
                self.__update_color()
            elif (self.__is_hover == 0 and self.__flash_t > 0):
                self.__flash_t -= (1 if (len(self.root.anim) > 6) else 1)
                self.__flash_t = max(self.__flash_t, 0)
                self.hover_mode = self.__flash_t/self.max_flash
                self.__update_color()

        def anim_normal(*args):
            if (self.__is_hover == 1 and self.__flash_t < self.max_flash):
                self.__flash_t += 1
                self.hover_mode = self.__flash_t/self.max_flash
                self.__update_color()
            elif (self.__is_hover == 0 and self.__flash_t > 0):
                self.__flash_t -= 1
                self.hover_mode = self.__flash_t/self.max_flash
                self.__update_color()
            self.root.after(anim_normal, 16)
        try:
            self.root.anim == 0
        except:
            self.root.after(anim_normal, 16)
        else:
            if (anim_magictk not in self.root.anim):
                self.root.anim.append(anim_magictk)
                self.__anim_obj_id = self.root.anim[-1]

    def __bind_event(self):
        def closecallback(obj):
            if (self.__is_hover == 1):
                if sys.platform.startswith("linux"):
                    self.top.destroy()
                self.__is_hover = 0
                self.canvas.focus_force()

        def pressrelease_v(event: tkinter.Event):
            if (self.__is_hover == 1):
                closecallback(event)
            else:
                self.__is_hover = 1
                if sys.platform.startswith("linux"):  # what's fuck?
                    self.top = tkinter.Toplevel()
                    self.top.geometry(
                        f"{1}x{1}+{10000}+{10000}")
                    self.__top_entry = ttk.Entry(self.top, width=self.w)
                    self.__top_entry.place(
                        x=0, y=0, width=self.w, height=self.h)
                self.root.update()
                self.inputobj.focus_force()
            self.__update_color()

        def update_text(*args):
            self.input_text = self.__input_textvar.get()
            if (self.input_text == ""):
                if (self.packed == False):
                    self.show_label.place(
                        x=10, y=6, width=self.w-20, height=self.h-12)
                    self.packed = True
            else:
                if (self.packed):
                    self.show_label.place_forget()
                    self.packed = False
        self.frames.bind("<ButtonRelease-1>", pressrelease_v)
        self.canvas.bind("<ButtonRelease-1>", pressrelease_v)
        self.inputobj.bind("<ButtonRelease-1>", pressrelease_v)
        self.show_label.bind("<ButtonRelease-1>", pressrelease_v)
        self.__input_textvar.trace_add("write", update_text)
        # self.frames.bind_all("<FocusOut>", closecallback)
        if (sys.platform.startswith("linux")):
            self.frames.bind("<Leave>", closecallback)
