import numpy as np
from ImageProcessor import ImageProcessor

class AdvancedFilter():
	def mean_blur(self, array):
		new = np.array(array)
		return new

	def gaussian_blur(self, array):
		new = np.array(array)
		return new

if __name__ == "__main__":
	imp = ImageProcessor()
	af = AdvancedFilter()
	arr = imp.load("../resources/elon_musk.png")
	arr = af.mean_blur(arr)
	imp.display(arr)
