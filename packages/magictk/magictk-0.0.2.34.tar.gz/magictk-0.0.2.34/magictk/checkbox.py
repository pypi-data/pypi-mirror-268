import json
import tkinter
from tkinter import ttk
from magictk import color_tmpl
from magictk import photoload
from magictk import fontconfig
from magictk import button


class Checkbox(button.ButtonFill):
    hover_mode = 0.0
    ishover = 0
    _flash_t = 0
    max_flash = 4
    _anim_obj_id = -1
    checked = False
    text = "ButtonFill"
    _group_id = 0
    disable_unhover = 0
    def callback(*args): return None

    def _draw_corner(self, r_x, r_y, x, y, **kwargs):
        border_info = json.loads(photoload.loadres("checkboxborder"))
        y_n = 0
        for i in border_info:
            x_n = 0
            for j in i:
                if (r_x == 0):
                    px = x+x_n+1
                else:
                    px = x+2-x_n-1
                if (r_y == 0):
                    py = y+y_n+1
                else:
                    py = y+2-y_n-1
                if (j < 0):
                    lcolor = 255+j
                else:
                    lcolor = 255-j
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
                    if (self.ishover == 2):
                        self.canvas.itemconfig(
                            obj, fill=h_color)
                    elif (self._flash_t <= self.max_flash):
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))

                self._fill_func.append(update_color)
                self._fill_gc.append(g_color)
                self._fill_fc.append(f_color)
                self._fill_hc.append(h_color)
                self._fill_obj.append(obj)
                x_n += 1
            y_n += 1

    def _draw_img(self, x, y, **kwargs):
        border_info = json.loads(photoload.loadres("checkbox"))
        y_n = 0
        for i in border_info:
            x_n = 0
            for j in i:
                px = x+x_n+1
                py = y+y_n+1
                if (j < 0):
                    lcolor = 255+j
                else:
                    lcolor = 255-j
                g_color = self.color[self._color_fg]
                f_color = color_tmpl.mix_color(
                    self.color["background"], self.color[self._color_fg], int((1-lcolor/255)*1000)/1000)
                h_color = color_tmpl.mix_color(
                    self.color["background"], self.color[self._color_fg2], int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)

                def update_color(obj, g_color, f_color, h_color):
                    if (self._flash_t > self.max_flash):
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(g_color, f_color, (self._flash_t-self.max_flash)/self.max_flash))
                    else:
                        self.canvas.itemconfig(
                            obj, fill=color_tmpl.mix_color(self.color["background"], self.color[self._color_fg1], self.hover_mode))

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

    def __init__(self, master=None, root_anim=None, color_type="primary", w=80, h=16, text="Button", color_list: dict = None, group: None = None):
        global use_font
        use_font = fontconfig.getfont()
        self._color_bd = "border_base"
        self._color_bg = "background"
        self._color_fg = "primary"
        self._color_fg1 = "primary"
        self._color_fg2 = "primary_dark"
        super().__init__(master=master, root_anim=root_anim, w=w, h=h,
                         text=text, color_list=color_list, color_type=color_type, _dis_color=True)
        if (group is not None):
            group._add_checkbox(self)

    def pack(self, *args, **kwargs):
        self.canvas.pack(*args, **kwargs)

    def guid(self, *args, **kwargs):
        self.canvas.guid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.canvas.place(*args, **kwargs)

    def _draw(self):
        self._draw_corner(0, 0, 0, 0)
        self._draw_corner(1, 0, 12, 0)
        self._draw_corner(0, 1, 0, 12)
        self._draw_corner(1, 1, 12, 12)

        def update_color(obj, g_color, f_color, h_color):
            if (self.ishover == 2):
                self.canvas.itemconfig(
                    obj, fill=h_color)
            elif (self._flash_t <= self.max_flash):
                self.canvas.itemconfig(
                    obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            1, 3, 1, 12, width=1, fill=self.color[self._color_bd]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            3, 1, 12, 1, width=1, fill=self.color[self._color_fg1]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            13, 3, 13, 12, width=1, fill=self.color[self._color_fg1]))
        self._fill_fc.append(self.color[self._color_fg1])
        self._fill_gc.append(self.color[self._color_bd])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_line(
            3, 13, 12, 13, width=1, fill=self.color[self._color_fg1]))

        self._fill_fc.append(self.color[self._color_fg])
        self._fill_gc.append(self.color["background"])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_rectangle(
            2, 3, 13, 12, width=0, fill=self.color[self._color_fg2]))

        self._fill_fc.append(self.color[self._color_fg])
        self._fill_gc.append(self.color["background"])
        self._fill_hc.append(self.color[self._color_fg2])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.canvas.create_rectangle(
            3, 2, 12, 13, width=0, fill=self.color[self._color_fg2]))

        self._draw_img(2, 2)

        self._fill_fc.append(self.color[self._color_fg])
        self._fill_gc.append(self.color["regular_text"])
        self._fill_hc.append("#FFFFFF")
        self._fill_func.append(update_color)
        self._fill_obj.append(
            self.canvas.create_text(14+int((self.w-14)/2), 6, text=self.text, font=(use_font, 10)))

    def bind_anim(self):
        def anim_magictk():
            if (self.ishover == 1 and self._flash_t < self.max_flash*2):
                self._flash_t += (1 if (len(self.root.anim) > 6) else 1)
                self._flash_t = min(self._flash_t, self.max_flash*2)
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            elif (self.ishover == 0 and self._flash_t > 0):
                self._flash_t -= (1 if (len(self.root.anim) > 6) else 1)
                self._flash_t = max(self._flash_t, 0)
                self.hover_mode = self._flash_t/self.max_flash
                self._update_color()
            elif (self._is_hover == 0 and self._flash_t <= 0):
                return -1

        def anim_normal(*args):
            if (self.ishover == 1 and self._flash_t < self.max_flash*2):
                self._flash_t += 1
                self.hover_mode = self._flash_t/self.max_flash
                self.__update_color()
            elif (self.ishover == 0 and self._flash_t > 0):
                self._flash_t -= 1
                self.hover_mode = self._flash_t/self.max_flash
                self.__update_color()
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

        def press_v(*args):
            self.bind_anim()
            if (self.ishover == 1):
                if (self.disable_unhover == 0):
                    self.ishover = 0
            else:
                self.ishover = 1
                self.callback(self)
            self._update_color()
        self.canvas.bind("<Button-1>", press_v)

        def pressrelease_v(*args):
            self._update_color()
        self.canvas.bind("<ButtonRelease-1>", pressrelease_v)


class RadioGroup:
    value = 1
    __g_list = []

    def __change(self, btn):
        for i in self.__g_list:
            self.value = btn._group_id
            if (i != btn):
                i.ishover = 0
            else:
                i.ishover = 1

    def _add_checkbox(self, cb: Checkbox):
        self.__g_list.append(cb)
        cb.callback = self.__change
        cb._group_id = len(self.__g_list)
        cb.max_flash = 3
        cb.disable_unhover = 1
        if (len(self.__g_list) == 1):
            cb.ishover = 1
