import json
import tkinter
from tkinter import ttk

from magictk import color_tmpl
from magictk import photoload
from magictk import fontconfig


class Button:
    color = color_tmpl.default_color
    hover_mode = 0.0
    _is_hover = 0
    _flash_t = 0
    max_flash = 4
    _anim_obj_id = -1
    text = "Button"

    def _draw_corner(self, r_x, r_y, x, y, **kwargs):
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
                    self.color["background"], self.color[self._color_bd], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    f_color = color_tmpl.mix_color(
                        self.color[self._color_fg2], self.color[self._color_fg1], int((1-lcolor/255)*1000)/1000)
                else:
                    f_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_fg1], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    h_color = color_tmpl.mix_color(
                        self.color[self._color_fg2], self.color[self._color_fg], int((1-lcolor/255)*1000)/1000)
                else:
                    h_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_fg], int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)

                def update_color(obj, g_color, f_color, h_color):
                    if (self._is_hover == 2):
                        self.canvas.itemconfig(
                            obj, fill=h_color)
                    else:
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))

                self._fill_func.append(update_color)
                self._fill_gc.append(g_color)
                self._fill_fc.append(f_color)
                self._fill_hc.append(h_color)
                self._fill_obj.append(obj)
                x_n += 1
            y_n += 1

    def _update_color(self):
        n = 0
        for i in self._fill_func:
            i(self._fill_obj[n], self._fill_gc[n],
              self._fill_fc[n], self._fill_hc[n])
            n += 1

    def __init__(self, master=None, root_anim=None, w=80, h=30, text="Button", func=lambda s: print("Press"), color_list: dict = None, _set_defaultcolor=None):
        global use_font
        use_font = fontconfig.getfont()
        self._fill_obj = []
        self._fill_func = []
        self._fill_gc = []
        self._fill_fc = []
        self._fill_hc = []
        self._func = func
        if (_set_defaultcolor is None):
            self._color_bd = "border_base"
            self._color_bg = "background"
            self._color_bg1 = "background"
            self._color_fg = "primary"
            self._color_fg1 = "primary_light"
            self._color_fg2 = "primary_light2"
            self._color_fg3 = "primary_light2"
            self._color_text = None
        self.w = max(30, w)
        self.h = h
        self.text = text
        self.__master = master
        if (color_list is not None):
            self.color = color_list
        if (root_anim == None):
            self.root = master.root
        else:
            self.root = root_anim

        self.canvas = tkinter.Canvas(
            master, bg=self.color["background"], width=self.w, height=self.h, borderwidth=0, bd=0, highlightcolor=self.color["background"], highlightthickness=0)

        self._draw()
        self._update_color()
        self._bind_event()
        self.bind_anim()

    def pack(self, *args, **kwargs):
        self.canvas.pack(*args, **kwargs)

    def guid(self, *args, **kwargs):
        self.canvas.guid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.canvas.place(*args, **kwargs)

    def _draw(self, _use_self_text=None):
        self._draw_corner(0, 0, 0, 0)
        self._draw_corner(1, 0, self.w-4, 0)
        self._draw_corner(0, 1, 0, self.h-5)
        self._draw_corner(1, 1, self.w-4, self.h-5)

        def update_color(obj, g_color, f_color, h_color):
            if (self._is_hover == 2):
                self.canvas.itemconfig(
                    obj, fill=h_color)
            else:
                self.canvas.itemconfig(
                    obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            1, 5, 1, self.h-5, width=1, fill=self.color[self._color_bd]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            5, 1, self.w-4, 1, width=1, fill=self.color[self._color_fg1]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            self.w-1, 5, self.w-1, self.h-5, width=1, fill=self.color[self._color_fg1]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            5, self.h-2, self.w-4, self.h-2, width=1, fill=self.color[self._color_fg1]))

        self._fill_fc.append(self.color[self._color_fg3])
        self._fill_gc.append(self.color[self._color_bg1])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_rectangle(
            2, 5, self.w-1, self.h-5, width=0, fill=self.color[self._color_fg2]))

        self._fill_fc.append(self.color[self._color_fg3])
        self._fill_gc.append(self.color[self._color_bg1])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_rectangle(
            5, 2, self.w-4, self.h-2, width=0, fill=self.color[self._color_fg2]))

        if (_use_self_text is None):
            if (self._color_text is None):
                self._fill_fc.append(self.color[self._color_fg])
                self._fill_gc.append(self.color["regular_text"])
                self._fill_hc.append(self.color[self._color_fg])
            else:
                self._fill_fc.append(self._color_text)
                self._fill_gc.append(self._color_text)
                self._fill_hc.append(self._color_text)
            self._fill_func.append(update_color)
            self._fill_obj.append(
                self.canvas.create_text(int(self.w/2), int(self.h/2), text=self.text, font=(use_font, 10)))

    def bind_anim(self):
        def anim_magictk():
            if (self._is_hover == 1 and self._flash_t < self.max_flash):
                self._flash_t += (1 if (len(self.root.anim) > 6) else 1)
                self._flash_t = min(self._flash_t, self.max_flash)
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            elif (self._is_hover == 0 and self._flash_t > 0):
                self._flash_t -= (1 if (len(self.root.anim) > 6) else 1)
                self._flash_t = max(self._flash_t, 0)
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            else:
                return -1

        def anim_normal(*args):
            if (self._is_hover == 1 and self._flash_t < self.max_flash):
                self._flash_t += 1
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            elif (self._is_hover == 0 and self._flash_t > 0):
                self._flash_t -= 1
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            self.root.after(anim_normal, 16)

        try:
            self.root.anim == 0
        except:
            self.root.after(anim_normal, 16)
        else:
            if (anim_magictk not in self.root.anim):
                self.root.anim.append(anim_magictk)
                self._anim_obj_id = self.root.anim[-1]

    def _bind_event(self):
        def enter_v(*args):
            self.bind_anim()
            if (self._is_hover == 0):
                self._is_hover = 1
        self.canvas.bind("<Enter>", enter_v)

        def leave_v(*args):
            self.bind_anim()
            if (self._is_hover == 1):
                self._is_hover = 0
        self.canvas.bind("<Leave>", leave_v)

        def press_v(*args):
            self._is_hover = 2
            self._update_color()
        self.canvas.bind("<Button-1>", press_v)

        def pressrelease_v(*args):
            self.bind_anim()
            self._is_hover = 1
            self._func(self)
            self._update_color()
        self.canvas.bind("<ButtonRelease-1>", pressrelease_v)


class ButtonFill(Button):

    def _draw_corner(self, r_x, r_y, x, y, **kwargs):
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
                if (j < 0):
                    g_color = color_tmpl.mix_color(
                        self.color[self._color_bg], self.color[self._color_bd], int((1-lcolor/255)*1000)/1000)
                else:
                    g_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_bd], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    f_color = color_tmpl.mix_color(
                        self.color[self._color_fg1], self.color[self._color_fg1], int((1-lcolor/255)*1000)/1000)
                else:
                    f_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_fg1], int((1-lcolor/255)*1000)/1000)
                if (j < 0):
                    h_color = color_tmpl.mix_color(
                        self.color[self._color_fg2], self.color[self._color_fg2], int((1-lcolor/255)*1000)/1000)
                else:
                    h_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_fg2], int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)

                def update_color(obj, g_color, f_color, h_color):
                    if (self._is_hover == 2):
                        self.canvas.itemconfig(
                            obj, fill=h_color)
                    else:
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))

                self._fill_func.append(update_color)
                self._fill_gc.append(g_color)
                self._fill_fc.append(f_color)
                self._fill_hc.append(h_color)
                self._fill_obj.append(obj)
                x_n += 1
            y_n += 1

    def __init__(self, master=None, root_anim=None, color_type="primary", w=80, h=30, text="Button", func=lambda s: print("Press"), color_list: dict = None, _dis_color=None):
        if (_dis_color is None):
            self._color_bd = color_type
            self._color_bg = color_type
            self._color_bg1 = color_type
            self._color_fg1 = color_type+"_light3"
            self._color_fg = color_type+"_dark"
            self._color_fg3 = color_type+"_light3"
            self._color_fg2 = color_type+"_dark"
            self._color_text = "#FFFFFF"
        super().__init__(master=master, root_anim=root_anim, w=w, h=h,
                         text=text, color_list=color_list, func=func, _set_defaultcolor=True)
