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

	def celluloid(self, array):
		pass

	def to_grayscale(self, array, filter):
		pass

if __name__ == "__main__":
	imp = ImageProcessor()
	cf = ColorFilter()
	arr = imp.load("../resources/elon_musk.png")
	arr = cf.invert(arr)
	imp.display(arr)
