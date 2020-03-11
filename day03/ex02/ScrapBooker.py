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
				array = np.concatenate((array[:i,:], array[i+1:,:]))
			return array
		else:
			for i in range(n-1, len(array[0]), n-1):
				array = np.concatenate((array[:,:i], array[:,i+1:]), axis=1)
			return array

	def juxtapose(self, array, n, axis):
		pass

	def mosaic(self, array, dimensions):
		pass



if __name__ == "__main__":
	scb = ScrapBooker()
	arr = np.random.choice([' ', 'X'], size=(5, 5))
	print(arr)
	print()
	arr = scb.thin(arr, 2, 0)
	print(arr)
