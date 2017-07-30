# Copyright (c) 2017 Bart Massey

# Code by Dania and Eric Levieil used under license from
# http://stackoverflow.com/a/31453958

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

import genstar

class StarWidget:
    def __init__(self,  window):
        self.window = window
        self.button = Button (window, text="Generate",
                              command=self.do_generate)
        self.button.pack()
        self.star = genstar.gen_star()
        self.plot()

    def do_generate(self):
        self.star = genstar.gen_star()
        self.plot()

    def plot(self):
        x = [float(i) / genstar.samples_per_day for i in range(len(self.star))]
        y = [100.0 + s for s in self.star]

        fig = Figure(figsize=(18,6))
        a = fig.add_subplot(111)
        a.scatter(x,y,color='blue')
        #a.plot(p, range(2 +max(x)),color='blue')
        #a.invert_yaxis()

        a.set_title ("Star Luminance", fontsize=16)
        a.set_ylabel("%", fontsize=14)
        a.set_xlabel("day", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= StarWidget(window)
window.mainloop()
