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
        self.canvas = None
        self.plot = None
        self.plot_current()

    def do_generate(self):
        self.star = genstar.gen_star()
        self.plot_current()

    def plot_current(self):

        if not self.canvas:
            fig = Figure(figsize=(18,6))
            self.plot = fig.add_subplot(1,1,1)
            self.plot.set_title ("Star Luminance", fontsize=16)
            self.plot.set_ylabel("%", fontsize=14)
            self.plot.set_xlabel("day", fontsize=14)
            self.canvas = FigureCanvasTkAgg(fig, master=self.window)
            self.canvas.get_tk_widget().pack()

        spd = genstar.samples_per_day
        n = spd * genstar.days_per_trace
        x = [float(i) / spd for i in range(n)]
        y = [100.0 + s for s in self.star]
        self.plot.cla()
        self.plot.scatter(x,y,color='blue')
        self.canvas.draw()

window= Tk()
start= StarWidget(window)
window.mainloop()
