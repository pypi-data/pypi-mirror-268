import magictk
import random
from multiprocessing import Process
if __name__ == "__main__":
    win = magictk.Window()

    frame = magictk.Frame(win)
    magictk.Button(frame, text="Default",
                   func=lambda s: print("Btn 1")).pack(side='left')
    magictk.ButtonFill(frame, text="Primary",
                       func=lambda s: print("Btn 2")).pack(side='left')
    magictk.ButtonFill(frame, color_type="success", text="Success",
                       func=lambda s: print("Btn 3")).pack(side='left')
    magictk.ButtonFill(frame, color_type="info", text="Info",
                       func=lambda s: print("Btn 4")).pack(side='left')
    magictk.ButtonFill(frame, color_type="warning", text="Warning",
                       func=lambda s: print("Btn 5")).pack(side='left')
    magictk.ButtonFill(frame, color_type="danger", text="Danger",
                       func=lambda s: print("Btn 6")).pack(side='left')
    frame.pack()

    frame2 = magictk.Frame(win)
    magictk.Select(frame2, text="Select", items=[
                   f"Option {i}" for i in range(1, 6)]).pack(side='left')
    magictk.Select(frame2, text="Select(1000 items)", items=[
                   f"Option {i}" for i in range(1, 1001)]).pack(side='left')
    obj1 = magictk.MenuObjs()
    for i in range(1, 10):
        obj1.addmenu(f"Option {i}", lambda s, t: print(i))
    magictk.Button(frame2, text="Menu",
                   func=lambda s: magictk.Menu(win, menuobj=obj1), w=60).pack()
    frame2.pack()

    frame3 = magictk.Frame(win)
    groups = magictk.RadioGroup()
    magictk.Checkbox(frame3, text="Radio 1", w=100,
                     group=groups).pack(side='left')
    magictk.Checkbox(frame3, text="Radio 2", w=100,
                     group=groups).pack(side='left')
    magictk.Checkbox(frame3, text="Radio 3", w=100,
                     group=groups).pack(side='left')
    magictk.Checkbox(frame3, text="Radio 4", w=100,
                     group=groups).pack(side='left')
    frame3.pack()

    frame4 = magictk.Frame(win)
    magictk.Checkbox(frame4, text="Option 1", w=100).pack(side='left')
    magictk.Checkbox(frame4, text="Option 2", w=100).pack(side='left')
    frame4.pack()

    frame5 = magictk.Frame(win)
    pb = magictk.ProgressBar(frame5)
    pb.pack(side='left')
    magictk.Button(frame5, text="+",
                   func=lambda s: pb.add_progress(0.1), w=30).pack(side='left')
    magictk.Button(frame5, text="-",
                   func=lambda s: pb.add_progress(-0.1), w=30).pack(side='left')
    magictk.Button(frame5, text="++",
                   func=lambda s: pb.add_progress(0.3), w=40).pack(side='left')
    magictk.Button(frame5, text="--",
                   func=lambda s: pb.add_progress(-0.3), w=40).pack(side='left')
    frame5.pack()

    frame6 = magictk.Frame(win)

    def kaoji():
        def test(*args):
            p = []
            size = 10000000
            for i in range(1, size):
                if (i % 100000 == 0):
                    print(f"make data... {i*100//size}%")
                p.append(random.randint(1, size))
            print("sort...")
            p.sort()
            print("finish!")
            del p
        ts = Process(target=test)
        ts.start()
    magictk.Button(frame6, text="Performance Test",
                   func=lambda s: kaoji(), w=130).pack(side='left')
    frame6.pack()

    frame7 = magictk.Frame(win)
    magictk.Entry(frame7, w=100).pack(side='left')
    frame7.pack()

    win.mainloop()
