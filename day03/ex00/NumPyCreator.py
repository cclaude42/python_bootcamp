import numpy as np

class NumPyCreator():
	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, tpl):
		return np.array(tpl)

	def from_iterable(self, itr):
		return np.array(itr)

	def from_shape(self, tpl, val=0):
		return np.full(tpl, val)

	def random(self, tpl):
		return np.random.random(tpl)

	def identity(self, n):
		return np.identity(n)
