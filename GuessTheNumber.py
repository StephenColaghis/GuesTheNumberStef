from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random


win = ThemedTk(theme="equilux")
win.config(themebg="equilux")
win.title("GuessTheNumber")
win.geometry("525x450")

trs = 0


def exit():
    win.destroy()

def guess(*args):
    global trs
    global rnd
    global g
    g = ges.get()
    if int(g) > rnd:
        imG.config(image=downarrow)
        trs = trs + 1
        Tries.config(text=("Tries:" + str(trs)))
    elif int(g) < rnd:
        imG.config(image=uparrow)
        trs = trs + 1
        Tries.config(text=("Tries:" + str(trs)))

    else:
        imG.config(image=check)
        ges.config(state= "disabled")
        Rndm["state"] = "enabled"

def randm():
    ges.config(state="enabled")
    pt=opt.get()
    global rnd

    if pt == "50":
        rnd = random.randint(0, 50)
    elif pt == "100":
        rnd = random.randint(0, 100)
    else:
        rnd=random.randint(0, 200)
    Rndm["state"] = "disabled"


uparrow= PhotoImage(file="uparrow.png")
downarrow= PhotoImage(file="downarrow.png")
dice= PhotoImage(file="pngegg (1).png")
check= PhotoImage(file="chk.png")


Title= ttk.Label(win, text="[Guess The Number]", font=('Times', 20, 'bold'))
Title.place(x=125, y=10)
Directions= ttk.Label(win, text="!First select your difficulty, then press random and guess!", font=('Times', 15, 'bold'))
Directions.place(x=10, y=130)
imG = ttk.Label(win, image=dice)
imG.place(x=0, y=250)
Rndm = ttk.Button(win, text="random", command=randm)
Rndm.place(x=250, y=350)
ges= ttk.Entry(win)
ges.place(x=250, y=325)
ext = ttk.Button(win, text="exit", command=exit)
ext.place(x=330, y=350)
Tries = ttk.Label(win, font=('Times',20, 'bold'), text="Tries:0")
Tries.place(x=250, y=400)

opt= StringVar()
#opt.trace("w", Change)

rad1 = ttk.Radiobutton (win, text="Easy(0-50)", value="50", variable=opt)
rad1.place(x=20, y=70)
rad2 = ttk.Radiobutton (win, text="Medium(0-100)", value="100", variable=opt)
rad2.place(x=170, y=70)
rad3 = ttk.Radiobutton (win, text="Hard(0-200)", value="200", variable=opt)
rad3.place(x=360, y=70)


win.bind('<Return>', guess)
win.resizable(False, False)
win.mainloop()