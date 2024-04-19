import colorsys

default_color = {
    "primary": "#409EFF",
    "primary_light": "#C6E2FF",
    "primary_light2": "#ECF5FF",
    "primary_light3": "#79BBFF",
    "primary_dark": "#337ECC",
    "success": "#67C23A",
    "success_light": "#E1F3D8",
    "success_light2": "#F0F9EB",
    "success_light3": "#95D475",
    "success_dark": "#529B2E",
    "warning": "#E6A23C",
    "warning_light": "#FAECD8",
    "warning_light2": "#E6A23C",
    "warning_light3": "#EEBE77",
    "warning_dark": "#B88230",
    "danger": "#F56C6C",
    "danger_light": "#FDE2E2",
    "danger_light2": "#FEF0F0",
    "danger_light3": "#F89898",
    "danger_dark": "#C45656",
    "info": "#909399",
    "info_light": "#E9E9EB",
    "info_light2": "#F4F4F5",
    "info_light3": "#B1B3B8",
    "info_dark": "#73767A",
    "primary_text": "#303133",
    "regular_text": "#606266",
    "secondary_text": "#909399",
    "placeholder": "#C0C4CC",
    "placeholder_light": "#F5F7FA",
    "border_base": "#DCDFE6",
    "border_light": "#E4E7ED",
    "background": "#FFFFFF"
}


def hex2rgb(color: str):
    return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))


def rgb2hex(r, g, b):
    return f"#{str(hex(int(r)))[2:].upper():0>2}{str(hex(int(g)))[2:].upper():0>2}{str(hex(int(b)))[2:].upper():0>2}"


def hex2hls(color: str):
    r, g, b = hex2rgb(color)
    return colorsys.rgb_to_hls(r/255, g/255, b/255)


def hls2hex(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return rgb2hex(r*255, g*255, b*255)


def setlight(color: str, light: float):
    h, l, s = hex2hls(color)
    return hls2hex(h, light, s)


def mix_color(c1: str, c2: str, alpha: float):
    r2, g2, b2 = hex2rgb(c1)
    r1, g1, b1 = hex2rgb(c2)
    r3 = int(r1*alpha+r2*(1-alpha))
    g3 = int(g1*alpha+g2*(1-alpha))
    b3 = int(b1*alpha+b2*(1-alpha))
    return rgb2hex(r3, g3, b3)
