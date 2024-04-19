import pickle
import os
import tkinter
import base64
image_all = None
load_cache = {}


def fresh_image():
    global image_all
    if (image_all == None):
        with open(os.path.dirname(__file__).replace("\\", "/")+"/res.pickle", "rb") as file:
            image_all = pickle.load(file)


fresh_image()


def loadimg(imgid: str):
    global image_all
    if imgid not in load_cache:
        load_cache[imgid] = tkinter.PhotoImage(
            data=base64.b64decode(image_all[imgid]))
    return load_cache[imgid]


def loadres(imgid: str):
    global image_all
    if imgid not in load_cache:
        load_cache[imgid] = base64.b64decode(image_all[imgid])
    return load_cache[imgid]
