import json
import tkinter
from tkinter import ttk
from tkinter import font as tkfont
try:
    import color_tmpl
except ImportError:
    from magictk import color_tmpl
try:
    import photoload
except ImportError:
    from magictk import photoload


class ProgressBar:
    color = color_tmpl.default_color
    __fill_obj = {}
    progress = 0.0
    __progress_pixel = 0
    __move_progress_pixel = 0
    __flash_t = 0
    max_flash = 4
    __anim_obj_id = -1

    def __draw_corner(self, r_x, r_y, x, y, colors="#000000", rid="", bgcolor=None, **kwargs):
        if bgcolor is None or self.progress == 1:
            bgcolor = self.color["border_light"]
        self.__fill_obj[rid] = []
        self.__fill_obj[rid+"_pos"] = []
        border_info = json.loads(photoload.loadres("progressborder"))
        y_n = 0
        for i in border_info:
            x_n = 0
            for j in i:
                if (r_x == 0):
                    px = x+x_n+1
                else:
                    px = x+3-x_n-1
                if (r_y == 0):
                    py = y+y_n+1
                else:
                    py = y+6-y_n-1
                if (j < 0):
                    lcolor = -j
                else:
                    lcolor = j
                # if(lcolor==255):
                #     continue
                g_color = color_tmpl.mix_color(
                    bgcolor, colors, int((1-lcolor/255)*1000)/1000)

                obj = self.canvas.create_rectangle(
                    px, py, px, py, width=0, fill=g_color)

                self.__fill_obj[rid].append(obj)
                self.__fill_obj[rid+"_pos"].append([x_n, y_n])

                x_n += 1
            y_n += 1

    def __init__(self, master=None, root_anim=None, w=200, h=8, colors="primary", color_list: dict = None):
        self.w = max(200, w)
        self.h = 8
        self.__master = master
        self.colors = colors
        if (color_list is not None):
            self.color = color_list
        if (root_anim == None):
            self.__root = master.root
        else:
            self.__root = root_anim

        self.canvas = tkinter.Canvas(
            master, bg=self.color["background"], width=self.w, height=self.h, borderwidth=0, bd=0, highlightcolor=self.color["background"], highlightthickness=0)

        self.__draw()
        # self.__bind_event()
        self.bind_anim()

    def pack(self, *args, **kwargs):
        self.canvas.pack(*args, **kwargs)

    def guid(self, *args, **kwargs):
        self.canvas.guid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.canvas.place(*args, **kwargs)

    def __draw(self):
        self.__fill_obj["bgbar"] = [
            self.canvas.create_rectangle(4, 1, self.w-5, self.h-1, width=0, fill=self.color["border_light"])]
        self.__draw_corner(1, 0, self.w-5, 0,
                           self.color["border_light"], "rightside", bgcolor=self.color["background"])
        self.__fill_obj["fgbar"] = [
            self.canvas.create_rectangle(4, 1, self.__progress_pixel+4, self.h-1, width=0, fill=self.color[self.colors])]
        self.__draw_corner(
            0, 0, 1, 0, self.color[self.colors], "leftside", bgcolor=self.color["background"])
        self.__draw_corner(1, 0, self.__progress_pixel+3, 0,
                           self.color[self.colors], "rightprog")

    def __update_pixel(self):
        self.__move_progress_pixel = max(4, int((self.w-6)*self.progress))

    def add_progress(self, n):
        self.progress = max(min(self.progress+n, 1.0), 0.0)
        self.__update_pixel()

    def set_progress(self, n):
        self.progress = max(min(n, 1.0), 0.0)
        self.__update_pixel()

    def __update_prog(self):
        for i in range(len(self.__fill_obj["rightprog"])):
            self.canvas.coords(
                self.__fill_obj["rightprog"][i], self.__progress_pixel+3-int(self.__fill_obj["rightprog_pos"][i][0]), self.__fill_obj["rightprog_pos"][i][1]+1, self.__progress_pixel+3-int(self.__fill_obj["rightprog_pos"][i][0])+1, self.__fill_obj["rightprog_pos"][i][1]+1)
        self.canvas.coords(
            self.__fill_obj["fgbar"][0], 4, 1, self.__progress_pixel+4, self.h-1)

    def bind_anim(self):
        def anim_magictk():
            if (int(self.__progress_pixel) < int(self.__move_progress_pixel)):
                if (self.__move_progress_pixel-self.__progress_pixel > 8):
                    self.__progress_pixel += 8
                else:
                    add_n = int(
                        (self.__progress_pixel-self.__move_progress_pixel)/2)
                    if (add_n <= 2):
                        self.__progress_pixel = self.__move_progress_pixel
                    else:
                        self.__progress_pixel += add_n
                self.__update_prog()
            elif (int(self.__progress_pixel) > int(self.__move_progress_pixel)):
                if (self.__progress_pixel-self.__move_progress_pixel > 8):
                    self.__progress_pixel -= 8
                else:
                    add_n = int(
                        (self.__progress_pixel-self.__move_progress_pixel)/2)
                    if (add_n <= 2):
                        self.__progress_pixel = self.__move_progress_pixel
                    else:
                        self.__progress_pixel -= add_n
                self.__update_prog()
            # else:
            #     self.__progress_pixel = self.__move_progress_pixel
            #     self.__update_prog()

        def anim_normal(*args):
            self.__root.after(anim_normal, 16)

        try:
            self.__root.anim == 0
        except:
            self.__root.after(anim_normal, 16)
        else:
            if (anim_magictk not in self.__root.anim):
                self.__root.anim.append(anim_magictk)
                self.__anim_obj_id = self.__root.anim[-1]
