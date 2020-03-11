import numpy as np
import string

class ScrapBooker():
	def crop(self, array, dimensions, position=(0,0)):
		px = position[0]
		ex = position[0] + dimensions[0]
		py = position[1]
		ey = position[1] + dimensions[1]
		if ex > len(array) or ey > len(array[0]):
			print("Error, array is too small.")
			return array
		return array[px:ex,py:ey]

	def thin(self, array, n, axis):
		if axis:
			for i in range(n-1, len(array), n-1):
				array = np.concatenate((array[:i,:], array[i+1:,:]), axis=0)
			return array
		else:
			for i in range(n-1, len(array[0]), n-1):
				array = np.concatenate((array[:,:i], array[:,i+1:]), axis=1)
			return array

	def juxtapose(self, array, n, axis):
		copy = array
		for i in range(n-1):
			array = np.concatenate((array, copy), axis=axis)
		return array


	def mosaic(self, array, dimensions):
		array = ScrapBooker.juxtapose(self, array, dimensions[0], 0)
		return ScrapBooker.juxtapose(self, array, dimensions[1], 1)



if __name__ == "__main__":
	scb = ScrapBooker()
	arr = np.eye(2)
	print(arr)
	print("\nMosaic (2x3) :\n")
	arr = scb.mosaic(arr, (2,3))
	print(arr)
	print("\nCrop to 3x4 from index [1,1] :\n")
	arr = scb.crop(arr, (3,4), (1,1))
	print(arr)
	print("\nThin every third line vertically (n=3, axis=0)\n")
	arr = scb.thin(arr, 3, 0)
	print(arr)
