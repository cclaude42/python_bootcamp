#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imp = ImageProcessor()
elon = imp.load("elon.png")
flower = imp.load("flower.jpg")

cf = ColorFilter()

imp.display(cf.invert(flower))
imp.display(cf.invert(elon))

imp.display(cf.to_blue(flower))
imp.display(cf.to_blue(elon))

imp.display(cf.to_green(flower))
imp.display(cf.to_green(elon))

imp.display(cf.to_red(flower))
imp.display(cf.to_red(elon))

imp.display(cf.to_celluloid(flower))
imp.display(cf.to_celluloid(elon))

imp.display(cf.to_grayscale(flower, 'm'))
imp.display(cf.to_grayscale(elon, 'm'))

imp.display(cf.to_grayscale(flower, 'weighted', weight=[0.2, 0.3, 0.5]))
imp.display(cf.to_grayscale(elon, 'weighted', weight=[0.2, 0.3, 0.5]))
