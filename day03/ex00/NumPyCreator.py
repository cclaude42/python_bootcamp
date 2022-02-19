import numpy as np
import collections

class NumPyCreator():
    """NumPyCreator class"""
    def _from_type(self, obj, otype):
        """Creates np array from simple type or nested type"""
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        # Check type
        if not isinstance(obj, otype):
            return None
        arr = np.array(obj)
        # Check valid shape
        if arr.dtype is np.dtype('object'):
            return None
        # Check nested type
        if len(arr.shape) == 2:
            for elem in obj:
                if not isinstance(elem, otype):
                    return None
        return arr

    def from_list(self, lst):
        """Creates np array from simple list or nested list"""
        return self._from_type(lst, list)

    def from_tuple(self, tpl):
        """Creates np array from simple tuple or nested tuple"""
        return self._from_type(tpl, tuple)

    def from_iterable(self, itr):
        """Creates np array from simple iter or nested iter"""
        return self._from_type(itr, collections.Iterable)

    def from_shape(self, shape, val=0):
        """Creates np array of the specified shape, filled with val (default 0)"""
        if isinstance(shape, tuple):
            return np.full(shape, val)
        return None

    def random(self, shape):
        """Creates np array of the specified shape, filled with random values"""
        if isinstance(shape, tuple):
            return np.random.random(shape)
        return None

    def identity(self, n):
        """Creates identity np array of shape (n, n)"""
        if isinstance(n, int) and n >= 0:
            return np.identity(n)
        return None
