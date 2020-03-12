import sys
import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
	def invert(self, array):
		return 1 - array

	def to_blue(self, array):
		new = np.zeros(array.shape)
		new[:,:,0] = np.zeros(array[:,:,0].shape)
		new[:,:,1] = np.zeros(array[:,:,1].shape)
		new[:,:,2] = array[:,:,2]
		return new

	def to_green(self, array):
		return array * [0, 1, 0]

	def to_red(self, array):
		return array - self.to_blue(array) - self.to_green(array)

	def celluloid(self, array, tresh=4):
		new = np.array(array)
		hold = np.linspace(0.0, 1.0, num=tresh, endpoint=False)[::-1]
		for i in hold:
			indexes = array >= i
			array[indexes] = -1
			new[indexes] = i
		return new

	def to_grayscale(self, array, filter):
		new = array * [0.299, 0.587, 0.114]
		for i in range(array.shape[0]):
			pixel = np.sum(array[i], axis=1)
			pixel = np.broadcast_to(pixel, (3, 1240))
			# Using forbidden .transpose because couldn't figure it out
			pixel = np.transpose(pixel)
			array[i] = pixel
		return array

if __name__ == "__main__":
	imp = ImageProcessor()
	cf = ColorFilter()
	arr = imp.load("../resources/elon_musk.png")
	arr = cf.invert(arr)
	imp.display(arr)
