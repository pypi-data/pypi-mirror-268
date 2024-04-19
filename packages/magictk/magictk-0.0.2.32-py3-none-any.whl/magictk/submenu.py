import json
import tkinter
import sys
from tkinter import ttk

from magictk import color_tmpl
from magictk import photoload
from magictk import fontconfig

transcolor = "#41342F"
usetrans = sys.platform.startswith('win')


class MenuObjs:
    def __init__(self):
        self.menu_lst = []
        self.menu_func = []
        self.menu_effect = []

    def first_action(self, menuobj):
        pass

    def addmenu(self, name, func, effect={}):
        self.menu_lst.append(name)
        self.menu_func.append(func)
        self.menu_effect.append(effect)


class Menu:
    __relh = 0
    __color_bd = "border_base"
    __color_bg = "background"
    __color_fg = "primary"
    __color_fg1 = "primary_light"
    __color_fg2 = "primary_light2"
    color = color_tmpl.default_color
    __close_mode = 0

    __last_highlight = 0
    __y_move = 0
    ___last_move = 1
    ___last_highlight = 0
    __load_y_size = 10
    ht = 12
    lt = 22
    ft = 34

    def __anim(self, *args):
        if (self.__close_mode == 0):
            if (self.__relh != self.h):
                if (self.h-self.__relh <= 1):
                    self.__relh = self.h
                elif (self.h-self.__relh > 32):
                    self.__relh += 32
                else:
                    self.__relh += (self.h-self.__relh) >> 1
                self.toplevel.geometry(
                    f"{self.w}x{self.__relh}+{self.x}+{self.y}")
        elif self.__close_mode == 1:
            if (self.__relh != 0):
                if (self.__relh-0 <= 1):
                    self.toplevel.destroy()
                    self.__close_mode = 2
                    return
                elif (self.__relh-0 > 32):
                    self.__relh -= 32
                else:
                    self.__relh -= (self.__relh-0) >> 1
                self.toplevel.geometry(
                    f"{self.w}x{self.__relh}+{self.x}+{self.y}")
        else:
            return -1
        if (self.___last_move != self.__y_move):
            n = 0
            for i in self.__itemsf:
                self.canvas.moveto(i, 24, n*self.ft+self.ht +
                                   self.__y_move+(self.ft-self.font[1]*2.5)//2)
                n += 1
            n = 0
            for i in self.__items:
                self.canvas.moveto(i, 2, n*self.ft+self.ht-4 +
                                   self.__y_move)
                n += 1
            self.___last_move = self.__y_move
        n = 0
        for i_tmp in range((-self.__real_y_move+self.__y_move)//self.ft, min((-self.__real_y_move+self.__y_move)//self.ft+len(self.__items), len(self.menuobj.menu_effect))):
            i = self.menuobj.menu_effect[i_tmp]
            if (len(i) != 0):
                self.canvas.itemconfigure(
                    self.__itemsf[n], justify=tkinter.LEFT, **i)
                self.canvas.moveto(self.__itemsf[n], 24, n*self.ft+self.ht +
                                   self.__y_move+(self.ft-self.font[1]*2.5)//2)
            else:
                self.canvas.itemconfigure(
                    self.__itemsf[n], justify=tkinter.LEFT, fill=self.color["regular_text"], font=self.font)
                self.canvas.moveto(self.__itemsf[n], 24, n*self.ft+self.ht +
                                   self.__y_move+(self.ft-self.font[1]*2.5)//2)
            n += 1

    def __mouse_move(self, event: tkinter.Event):
        y = event.y
        self.__last_highlight = max(
            -1, min(len(self.__items), int((y-self.ht-self.__y_move)//self.ft)))
        for i in self.__items:
            self.canvas.itemconfig(
                i, fill=self.color["background"])
        if -1 < self.__last_highlight < len(self.__items):
            self.canvas.itemconfig(
                self.__items[self.__last_highlight], fill=self.color["placeholder_light"])

    def close(self, *args):
        self.__close_mode = 1
        if sys.platform.startswith('win'):
            self.toplevel.unbind_all("<MouseWheel>")
        elif sys.platform.startswith('darwin'):
            self.toplevel.unbind_all("<MouseWheel>")
        else:
            self.toplevel.unbind_all(
                "<Button-4>")
            self.toplevel.unbind_all(
                "<Button-5>")
        if (self.__closecallback is not None):
            self.__closecallback(self)

    def __init__(self, root, menuobj: MenuObjs, w=200, h=300, x=100, y=300, color_list: dict = None, closeonleave=True, fontsize=10, closecallback=None):
        global use_font
        use_font = fontconfig.getfont()
        self.__closecallback = closecallback
        self.font = (use_font, fontsize)
        self.__items = []
        self.__itemsf = []
        self.__itemsid = []
        self.__real_y_move = 0
        self.menuobj = menuobj
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        if (color_list is not None):
            self.color = color_list
        self.toplevel = tkinter.Toplevel(bg=transcolor)
        self.toplevel.wm_attributes('-topmost', True)
        self.toplevel.overrideredirect(True)
        self.toplevel.geometry(f"{self.w}x{self.__relh}+{self.x}+{self.y}")
        if (usetrans):
            self.toplevel.wm_attributes('-transparentcolor', transcolor)
        self.root = root
        self.canvas = tkinter.Canvas(
            self.toplevel, bg=self.color["background"],  highlightthickness=0, width=self.w+1, height=self.h+1)
        self.canvas.place(x=-1, y=-1)
        self.root.anim.append(self.__anim)
        self.toplevel.focus()
        self.__draw_menu()
        self.__draws()

        if (closeonleave):
            self.toplevel.bind("<FocusOut>", self.close)
            if (not usetrans):
                self.toplevel.bind("<Leave>", self.close)

        self.canvas.bind("<Motion>", self.__mouse_move)
        self.__bind_scroll()
        self.canvas.bind("<ButtonRelease-1>", self.__click)
        self.toplevel.bind_all("<Escape>", self.close)
        self.toplevel.bind_all("<Return>", self.__click)

    def __draw_menu(self):
        n = 0
        for i_tmp in range(0, min(self.__load_y_size, len(self.menuobj.menu_lst))):
            i = self.menuobj.menu_lst[i_tmp]
            self.__items.append(self.canvas.create_rectangle(
                2, n*self.ft+self.ht, self.w, (n+1)*self.ft+self.ht, fill=self.color["background"], width=0))
            self.__itemsf.append(self.canvas.create_text(
                10, n*self.ft+self.ht, text=i, font=self.font, justify=tkinter.LEFT, fill=self.color["regular_text"]))
            self.__itemsid.append(n)
            n += 1

    def __draw_corner(self, r_x, r_y, x, y, **kwargs):
        border_info = json.loads(photoload.loadres("menuborder"))
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
                if (lcolor == 255):
                    x_n += 1
                    continue
                if (j < 0):
                    if (usetrans):
                        g_color = transcolor
                    else:
                        g_color = self.color["background"]
                else:
                    g_color = color_tmpl.mix_color(
                        self.color["background"], self.color[self.__color_bd], int((1-lcolor/255)*1000)/1000)
                self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)
                x_n += 1
            y_n += 1

    def __draws(self):
        self.__draw_corner(0, 0, 0, 0)
        self.__draw_corner(1, 0, self.w-4+1, 0)
        self.__draw_corner(0, 1, 0, self.h-4+1)
        self.__draw_corner(1, 1, self.w-4+1, self.h-4+1)
        self.canvas.create_line(
            1, 5, 1, self.h-3, width=1, fill=self.color[self.__color_bd])
        self.canvas.create_line(
            5, 1, self.w-3, 1, width=1, fill=self.color[self.__color_bd])
        self.canvas.create_line(
            self.w, 5, self.w, self.h-3, width=1, fill=self.color[self.__color_bd])
        self.canvas.create_line(
            5, self.h, self.w-3, self.h, width=1, fill=self.color[self.__color_bd])

    def __bind_scroll(self):
        def scrollwheel(event: tkinter.Event, setdelta=None):
            if (len(self.menuobj.menu_lst) <= 8):
                return
            if (setdelta is None):
                delta = event.delta
            else:
                delta = setdelta
            if sys.platform.startswith('win'):
                delta //= 20
            if delta > 0:
                if (self.__real_y_move != 0):
                    self.__y_move += delta
                self.__real_y_move = min(0, self.__real_y_move+delta)
            else:
                if (self.__real_y_move != -(len(self.menuobj.menu_lst)*self.ft-self.h+8)):
                    self.__y_move += delta
                self.__real_y_move = max(self.__real_y_move+delta,
                                         -(len(self.menuobj.menu_lst)*self.ft-self.h+8))

            if (self.__y_move > 0):
                self.__y_move -= self.ft
                self.__items.insert(0, self.__items.pop())
                self.__itemsf.insert(0, self.__itemsf.pop())
                self.__itemsid.insert(0, self.__itemsid.pop()-10)
                self.__mouse_move(event)
                if (self.__itemsid[0] >= 0):
                    self.canvas.itemconfigure(
                        self.__itemsf[0], text=self.menuobj.menu_lst[self.__itemsid[0]])
            elif (self.__y_move < -self.ft+1):
                self.__y_move += self.ft
                self.__items.append(self.__items.pop(0))
                self.__itemsf.append(self.__itemsf.pop(0))
                self.__itemsid.append(self.__itemsid.pop(0)+10)
                self.__mouse_move(event)
                if (self.__itemsid[-1] < len(self.menuobj.menu_lst)):
                    self.canvas.itemconfigure(
                        self.__itemsf[-1], text=self.menuobj.menu_lst[self.__itemsid[-1]])

        if sys.platform.startswith('win'):
            self.toplevel.bind_all("<MouseWheel>", scrollwheel)
        elif sys.platform.startswith('darwin'):
            self.toplevel.bind_all("<MouseWheel>", scrollwheel)
        else:
            self.toplevel.bind_all(
                "<Button-4>", lambda event: scrollwheel(event, 8))
            self.toplevel.bind_all(
                "<Button-5>", lambda event: scrollwheel(event, -8))

    def __click(self, event):
        click_item = max(
            -1, min(len(self.menuobj.menu_func), int((event.y-self.ht-self.__real_y_move)//self.ft)))
        if (click_item == -1 or self.__last_highlight >= len(self.menuobj.menu_func)):
            return
        self.close()
        self.menuobj.menu_func[click_item](self, click_item)
