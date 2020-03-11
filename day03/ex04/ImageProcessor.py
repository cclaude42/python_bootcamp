from PIL import Image
import numpy as np

class ImageProcessor():
	def load(self, path):
		img = Image.open(path)
		arr = np.array(img)
		print("Loading image of dimensions {} x {}".format(len(arr), len(arr[0])))
		return np.divide(arr, 255)

	def display(self, array):
		array = np.multiply(array, 255)
		array = array.astype(np.uint8)
		img = Image.fromarray(array, 'RGB')
		img.show()
