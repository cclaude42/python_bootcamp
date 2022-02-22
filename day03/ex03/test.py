#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imp = ImageProcessor()
arr = imp.load("elon.png")

cf = ColorFilter()
imp.display(cf.invert(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_blue(arr))
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr, 'm'))
imp.display(cf.to_grayscale(arr, 'weighted', [0.2, 0.3, 0.5]))