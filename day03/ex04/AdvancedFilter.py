import numpy as np
from ImageProcessor import ImageProcessor

class AdvancedFilter():
	def mean_blur(self, array):
		new = np.array(array)
		imax = array.shape[0] - 1
		jmax = array.shape[1] - 1
		for i in range(imax + 1):
			for j in range(jmax + 1):
				if i > 0 and i < imax and j > 0 and j < jmax:
					sub = array[i-1:i+2,j-1:j+2]
					new[i][j][0] = np.sum(sub[:,:,0]) / 9
					new[i][j][1] = np.sum(sub[:,:,1]) / 9
					new[i][j][2] = np.sum(sub[:,:,2]) / 9
		return new

	def gaussian_blur(self, array):
		new = np.array(array)
		imax = array.shape[0] - 1
		jmax = array.shape[1] - 1
		for i in range(imax + 1):
			for j in range(jmax + 1):
				if i > 0 and i < imax and j > 0 and j < jmax:
					new[i][j] = (4 * array[i][j] + 2 * array[i][j+1] + 2 * array[i][j-1] + 2 * array[i+1][j] + array[i+1][j+1] + array[i+1][j-1] + 2 * array[i-1][j] + array[i-1][j+1] + array[i-1][j-1]) / 16
		return new

	def psy(self, array):
		new = np.array(array)
		imax = array.shape[0] - 1
		jmax = array.shape[1] - 1
		for i in range(imax + 1):
			for j in range(jmax + 1):
				if i > 0 and i < imax and j > 0 and j < jmax:
					new[i][j] = array[i][j] + array[i][j+1] + array[i][j-1] + array[i+1][j] + array[i+1][j+1] + array[i+1][j-1] + array[i-1][j] + array[i-1][j+1] + array[i-1][j-1]
		return new

	def trance(self, array):
		new = np.array(array)
		imax = array.shape[0] - 1
		jmax = array.shape[1] - 1
		for i in range(imax + 1):
			for j in range(jmax + 1):
				if i > 0 and i < imax and j > 0 and j < jmax:
					new[i][j] = 4 * array[i][j] + 2 * array[i][j+1] + 2 * array[i][j-1] + 2 * array[i+1][j] + array[i+1][j+1] + array[i+1][j-1] + 2 * array[i-1][j] + array[i-1][j+1] + array[i-1][j-1]
		return new

	def psytrance(self, array):
		new = self.psy(array)
		return self.trance(new)

if __name__ == "__main__":
	imp = ImageProcessor()
	af = AdvancedFilter()
	arr = imp.load("../resources/42AI.png")
	imp.display(arr)

	# arr = af.mean_blur(arr)
	arr = af.gaussian_blur(arr)
	# arr = af.psy(arr)
	# arr = af.psytrance(arr)

	imp.display(arr)
