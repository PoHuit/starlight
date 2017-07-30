# Copyright (c) 2017 Po Huit
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

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
        self.star = genstar.gen_star()

        self.use_lines = BooleanVar(window, True)
        self.use_points = BooleanVar(window, False)

        fig = Figure(figsize=(18, 6))
        self.plot = fig.add_subplot(1, 1, 1)
        self.plot.set_title ("Star Luminance", fontsize=16)
        self.plot.set_ylabel("%", fontsize=14)
        self.plot.set_xlabel("day", fontsize=14)
        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()
        self.plot_current()

        buttons = Frame(window)
        lines = Checkbutton(buttons, text="Lines",
                            variable=self.use_lines,
                            command=self.plot_current)
        lines.pack(side=LEFT)
        points = Checkbutton(buttons, text="Points",
                             variable=self.use_points,
                             command=self.plot_current)
        points.pack(side=LEFT)
        generate = Button(buttons, text="Generate",
                          command=self.do_generate)
        generate.pack(side=LEFT)
        buttons.pack(fill=BOTH, expand=True)

    def do_generate(self):
        self.star = genstar.gen_star()
        self.plot_current()

    def plot_current(self):
        spd = genstar.samples_per_day
        n = spd * genstar.days_per_trace
        x = [float(i) / spd for i in range(n)]
        y = [100.0 + s for s in self.star]
        self.plot.cla()

        use_points = self.use_points.get()
        use_lines = self.use_lines.get()
        if use_lines or not use_points:
            style = '-'
            if not use_lines and not use_points:
                style = ':'
            self.plot.plot(x, y, style, color="blue", linewidth=0.5)
        if use_points:
            self.plot.scatter(x, y, c="red", s=1.5)

        self.canvas.draw()

window= Tk()
start= StarWidget(window)
window.mainloop()
