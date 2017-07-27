#!/bin/sh
# Copyright © 2017 Bart Massey
python3 genstar.py |
gnuplot -p -e "plot '-' with linespoints;"
