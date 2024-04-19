import json
import tkinter
import sys
from tkinter import ttk
from tkinter import font as tkfont

from magictk import color_tmpl
from magictk import photoload
from magictk import submenu
from magictk import fontconfig
from magictk import button


class Select(button.Button):
    color = color_tmpl.default_color
    _fill_obj = []
    _fill_func = []
    _fill_gc = []
    _fill_fc = []
    _fill_hc = []
    hover_mode = 0.0
    _is_hover = 0
    _flash_t = 0
    max_flash = 6
    _anim_obj_id = -1

    def _draw_arrow(self, x, y, **kwargs):
        border_info = self.__arrow_json[0]
        self.__arrow_list = []
        y_n = 0
        for i in border_info:
            x_n = 0
            self.__arrow_list.append([])
            for j in i:
                px = x+x_n+1
                py = y+y_n+1
                lcolor = j
                g_color = color_tmpl.mix_color(
                    self.color["background"], self.color[self._color_bd], int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)
                self.__arrow_list[-1].append(obj)

                x_n += 1
            y_n += 1

    def __init__(self, master=None, root_anim=None, w=200, h=30, text="Select",  color_list: dict = None, items=[]):
        global use_font
        use_font = fontconfig.getfont()
        self.__arrow_json = json.loads(photoload.loadres("selectarrow"))
        self.items = items
        self._color_bd = "border_base"
        self._color_bg = "background"
        self._color_bg1 = "background"
        self._color_fg = "primary"
        self._color_fg1 = "primary"
        self._color_fg2 = "background"
        self._color_fg3 = "background"
        self._color_text = None
        super().__init__(master=master, root_anim=root_anim, w=w,
                         h=h, text=text,  color_list=color_list, _set_defaultcolor=True)
        self.__menuobj = submenu.MenuObjs()
        self.__last = 0
        for i in self.items:
            self.__menuobj.addmenu(i, self._callback_menu)

    def _draw(self):
        super()._draw(True)

        def update_color(obj, g_color, f_color, h_color):
            if (self._is_hover == 2):
                self.canvas.itemconfig(
                    obj, fill=h_color)
            else:
                self.canvas.itemconfig(
                    obj, fill=color_tmpl.mix_color(g_color, f_color, self.hover_mode))
        self.__text_obj = self.canvas.create_text(
            20, int(self.h/2), text=self.text, font=(use_font, 10), justify="left")
        self._fill_fc.append(self.color["placeholder"])
        self._fill_gc.append(self.color["regular_text"])
        self._fill_hc.append(self.color["placeholder"])
        self._fill_func.append(update_color)
        self._fill_obj.append(self.__text_obj)
        self.canvas.moveto(self.__text_obj, 16, self.h//2-10)
        self._draw_arrow(self.w-30, (self.h-12)//2)

    def bind_anim(self):
        def update_arrow():
            datas = self.__arrow_json[self._flash_t]
            y_n = 0
            for i in datas:
                x_n = 0
                for j in i:
                    self.canvas.itemconfigure(self.__arrow_list[y_n][x_n], fill=(color_tmpl.mix_color(
                        self.color["background"], self.color[self._color_bd], int((1-j/255)*1000)/1000)))
                    x_n += 1
                y_n += 1

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
            elif (self._is_hover == 0 and self._flash_t == 0):
                return -1
            update_arrow()

        def anim_normal(*args):
            if (self._is_hover == 1 and self._flash_t < self.max_flash):
                self._flash_t += 1
                self.hover_mode = self._flash_t/self.max_flash
                self.__update_color()
            elif (self._is_hover == 0 and self._flash_t > 0):
                self._flash_t -= 1
                self.hover_mode = self._flash_t/self.max_flash
                self.__update_color()
            self.root.after(anim_normal, 16)
            update_arrow()

        try:
            self.root.anim == 0
        except:
            self.root.after(anim_normal, 16)
        else:
            if (anim_magictk not in self.root.anim):
                self.root.anim.append(anim_magictk)
                self.__anim_obj_id = self.root.anim[-1]

    def _callback_menu(self, obj, ids):
        self.__menuobj.menu_effect[self.__last] = {}
        self.__menuobj.menu_effect[ids] = {
            "fill": self.color["primary"], "font": (obj.font[0], obj.font[1], "bold")}
        self.__last = ids
        self.canvas.itemconfigure(self.__text_obj, text=self.items[ids])
        self.canvas.moveto(self.__text_obj, 16, self.h//2-10)

    def _bind_event(self):
        def closecallback(obj):
            self._is_hover = 0

        def pressrelease_v(event):
            self.bind_anim()
            if (self._is_hover == 1):
                self.menus.close()
            else:
                self._is_hover = 1
                self.menus = submenu.Menu(
                    x=event.x_root-event.x,
                    y=event.y_root-event.y+self.h+4,
                    w=self.w,
                    h=min(8*34, len(self.items)*34+12+4),
                    root=self.root, menuobj=self.__menuobj, closecallback=closecallback
                )
            self._update_color()
        self.canvas.bind("<ButtonRelease-1>", pressrelease_v)
