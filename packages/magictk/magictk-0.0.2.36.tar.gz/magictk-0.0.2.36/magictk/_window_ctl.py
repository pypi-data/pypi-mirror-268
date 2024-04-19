import tkinter
from tkinter import ttk
try:
    import color_tmpl
except:
    from magictk import color_tmpl
try:
    import photoload
except:
    from magictk import photoload


def exit_btn_set(self, root):
    img_exit = photoload.loadimg("close")
    img_act_exit = photoload.loadimg("close_active")
    self.style.configure(
        'BarExitButton.TFrame', background=self.color["background"])
    self.style.configure(
        'BarExitButton.TLabel', background=self.color["background"])
    exit_btn = ttk.Frame(root, style='BarExitButton.TFrame',
                         height=self.top_h, width=48)
    exit_btn.pack(anchor="n", side='right')
    exit_btn_flash = 0  # total 6f
    exit_btn_flash_mode = 0
    label = ttk.Label(
        exit_btn, style='BarExitButton.TLabel', image=img_exit, anchor=tkinter.CENTER)
    label.place(width=48, height=self.top_h, x=0, y=0)

    def animation():
        nonlocal exit_btn_flash, exit_btn_flash_mode
        if (exit_btn_flash_mode == 0 and exit_btn_flash > 0):
            exit_btn_flash -= 1
            self.style.configure(
                'BarExitButton.TFrame', background=color_tmpl.mix_color(self.color["background"], "#C42B1C", exit_btn_flash/6))
            self.style.configure(
                'BarExitButton.TLabel', background=color_tmpl.mix_color(self.color["background"], "#C42B1C", exit_btn_flash/6))
            if (exit_btn_flash >= 3):
                label.configure(image=img_act_exit)
            else:
                label.configure(image=img_exit)
        if (exit_btn_flash_mode == 1 and exit_btn_flash < 6):
            exit_btn_flash += 1
            self.style.configure(
                'BarExitButton.TFrame', background=color_tmpl.mix_color(self.color["background"], "#C42B1C", exit_btn_flash/6))
            self.style.configure(
                'BarExitButton.TLabel', background=color_tmpl.mix_color(self.color["background"], "#C42B1C", exit_btn_flash/6))
            if (exit_btn_flash >= 3):
                label.configure(image=img_act_exit)
            else:
                label.configure(image=img_exit)
        if (exit_btn_flash_mode == 2):
            exit_btn_flash = 6
            self.style.configure(
                'BarExitButton.TFrame', background="#94141E")
            self.style.configure(
                'BarExitButton.TLabel', background="#94141E")
            if (exit_btn_flash >= 3):
                label.configure(image=img_act_exit)
            else:
                label.configure(image=img_exit)
    self.anim.append(animation)

    def enters_exit(event):
        nonlocal exit_btn_flash_mode
        exit_btn_flash_mode = 1

    def leaves_exit(event):
        nonlocal exit_btn_flash_mode
        exit_btn_flash_mode = 0

    def presshold_exit(event):
        nonlocal exit_btn_flash_mode
        exit_btn_flash_mode = 2

    def press_exit(event):
        nonlocal exit_btn_flash_mode
        if (exit_btn_flash_mode == 2):
            exit_btn_flash_mode = 0
            self.quit()
        else:
            exit_btn_flash_mode = 0
    exit_btn.bind("<Enter>", enters_exit)
    exit_btn.bind("<Leave>", leaves_exit)
    exit_btn.bind("<Button-1>", presshold_exit)
    exit_btn.bind("<ButtonRelease-1>", press_exit)
    label.bind("<Enter>", enters_exit)
    label.bind("<Leave>", leaves_exit)
    label.bind("<Button-1>", presshold_exit)
    label.bind("<ButtonRelease-1>", press_exit)


def zoom_btn_set(self, root):
    img_default = photoload.loadimg("zoom")
    img_inzoom = photoload.loadimg("zoom2normal")

    self.style.configure(
        'BarZoomButton.TFrame', background=self.color["background"])
    self.style.configure(
        'BarZoomButton.TLabel', background=self.color["background"])
    zoom_btn = ttk.Frame(root, style='BarZoomButton.TFrame',
                         height=self.top_h, width=48)
    zoom_btn.pack(anchor="n", side='right')
    zoom_btn_flash = 0  # total 4f
    zoom_btn_flash_mode = 0
    label = ttk.Label(
        zoom_btn, style='BarZoomButton.TLabel', image=img_default, anchor=tkinter.CENTER)
    label.place(width=48, height=self.top_h, x=0, y=0)

    def animation():
        nonlocal zoom_btn_flash, zoom_btn_flash_mode
        if (zoom_btn_flash_mode == 0 and zoom_btn_flash > 0):
            zoom_btn_flash -= 1
            self.style.configure(
                'BarZoomButton.TFrame', background=color_tmpl.mix_color(self.color["background"], self.color["border_base"], zoom_btn_flash/4))
            self.style.configure(
                'BarZoomButton.TLabel', background=color_tmpl.mix_color(self.color["background"], self.color["border_base"], zoom_btn_flash/4))
        if (zoom_btn_flash_mode == 1 and zoom_btn_flash < 4):
            zoom_btn_flash += 1
            self.style.configure(
                'BarZoomButton.TFrame', background=color_tmpl.mix_color(self.color["background"], self.color["border_base"], zoom_btn_flash/4))
            self.style.configure(
                'BarZoomButton.TLabel', background=color_tmpl.mix_color(self.color["background"], self.color["border_base"], zoom_btn_flash/4))
        if (zoom_btn_flash_mode == 2):
            zoom_btn_flash = 4
            self.style.configure(
                'BarZoomButton.TFrame', background=color_tmpl.setlight(self.color["border_base"], 0.76))
            self.style.configure(
                'BarZoomButton.TLabel', background=color_tmpl.setlight(self.color["border_base"], 0.76))
    self.anim.append(animation)

    def enters_zoom(event):
        nonlocal zoom_btn_flash_mode
        zoom_btn_flash_mode = 1

    def leaves_zoom(event):
        nonlocal zoom_btn_flash_mode
        zoom_btn_flash_mode = 0

    def presshold_zoom(event):
        nonlocal zoom_btn_flash_mode
        zoom_btn_flash_mode = 2

    def press_zoom(event):
        nonlocal zoom_btn_flash_mode
        if (zoom_btn_flash_mode == 2):
            zoom_btn_flash_mode = 0
            self.zoom()
        else:
            zoom_btn_flash_mode = 0

    def update_icon(*args):
        if (self.fullscreen):
            label.configure(image=img_inzoom)
        else:
            label.configure(image=img_default)
    self.update_icon = update_icon
    zoom_btn.bind("<Enter>", enters_zoom)
    zoom_btn.bind("<Leave>", leaves_zoom)
    zoom_btn.bind("<Button-1>", presshold_zoom)
    zoom_btn.bind("<ButtonRelease-1>", press_zoom)
    label.bind("<Enter>", enters_zoom)
    label.bind("<Leave>", leaves_zoom)
    label.bind("<Button-1>", presshold_zoom)
    label.bind("<ButtonRelease-1>", press_zoom)


def iconic_btn_set(self, root):
    img_iconic = photoload.loadimg("iconic")

    self.style.configure(
        'BarIconicButton.TFrame', background=self.color["background"])
    self.style.configure(
        'BarIconicButton.TLabel', background=self.color["background"])

    iconic_btn = ttk.Frame(root, style='BarIconicButton.TFrame',
                           height=self.top_h, width=48)
    iconic_btn.pack(anchor="n", side='right')
    iconic_btn_flash = 0  # total 4f
    iconic_btn_flash_mode = 0
    label = ttk.Label(
        iconic_btn, style='BarIconicButton.TLabel', image=img_iconic, anchor=tkinter.CENTER)
    label.place(width=48, height=self.top_h, x=0, y=0)

    def animation():
        nonlocal iconic_btn_flash, iconic_btn_flash_mode
        if (iconic_btn_flash_mode == 0 and iconic_btn_flash > 0):
            iconic_btn_flash -= 1
            self.style.configure(
                'BarIconicButton.TFrame', background=color_tmpl.mix_color(self.color["background"], self.color["border_light"], iconic_btn_flash/4))
            self.style.configure(
                'BarIconicButton.TLabel', background=color_tmpl.mix_color(self.color["background"], self.color["border_light"], iconic_btn_flash/4))
        if (iconic_btn_flash_mode == 1 and iconic_btn_flash < 4):
            iconic_btn_flash += 1
            self.style.configure(
                'BarIconicButton.TFrame', background=color_tmpl.mix_color(self.color["background"], self.color["border_light"], iconic_btn_flash/4))
            self.style.configure(
                'BarIconicButton.TLabel', background=color_tmpl.mix_color(self.color["background"], self.color["border_light"], iconic_btn_flash/4))
        if (iconic_btn_flash_mode == 2):
            iconic_btn_flash = 4
            self.style.configure(
                'BarIconicButton.TFrame', background=color_tmpl.setlight(self.color["border_base"], 0.76))
            self.style.configure(
                'BarIconicButton.TLabel', background=color_tmpl.setlight(self.color["border_base"], 0.76))
    self.anim.append(animation)

    def enters_iconic(event):
        nonlocal iconic_btn_flash_mode
        iconic_btn_flash_mode = 1

    def leaves_iconic(event):
        nonlocal iconic_btn_flash_mode
        iconic_btn_flash_mode = 0

    def presshold_iconic(event):
        nonlocal iconic_btn_flash_mode
        iconic_btn_flash_mode = 2

    def press_iconic(event):
        nonlocal iconic_btn_flash_mode
        if (iconic_btn_flash_mode == 2):
            iconic_btn_flash_mode = 0
            self.iconify()
        else:
            iconic_btn_flash_mode = 0
    iconic_btn.bind("<Enter>", enters_iconic)
    iconic_btn.bind("<Leave>", leaves_iconic)
    iconic_btn.bind("<Button-1>", presshold_iconic)
    iconic_btn.bind("<ButtonRelease-1>", press_iconic)
    label.bind("<Enter>", enters_iconic)
    label.bind("<Leave>", leaves_iconic)
    label.bind("<Button-1>", presshold_iconic)
    label.bind("<ButtonRelease-1>", press_iconic)
