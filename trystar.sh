#!/bin/sh
# Copyright (c) 2017 Po Huit
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

python3 genstar.py |
gnuplot -p -e "plot '-' with linespoints;"
