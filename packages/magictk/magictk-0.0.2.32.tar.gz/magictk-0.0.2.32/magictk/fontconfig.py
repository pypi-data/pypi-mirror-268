
from tkinter import font as tkfont

font = None


def set_font():
    font_family = ["Helvetica Neue", "Helvetica", "PingFang SC", "Hiragino Sans GB",
                   "Microsoft YaHei",
                   "微软雅黑",
                   "Arial", "sans-serif"]
    t_family = tkfont.families(root=None, displayof=None)
    for i in font_family:
        if i in t_family:
            use_font = i
            break
    else:
        print("Unknown font")
    return use_font


def getfont():
    global font
    if (font is None):
        font = set_font()
    return font
