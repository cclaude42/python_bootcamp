import numpy as np
import string

class ScrapBooker():
    """Scrapbooker class"""

    def shape(self, tpl):
        """Utility to check if object is a valid 'shape' of format (x, y)"""
        if not isinstance(tpl, tuple):
            return False
        if not len(tpl) == 2:
            return False
        if not isinstance(tpl[0], int) or not isinstance(tpl[1], int):
            return False
        if tpl[0] < 0 or tpl[1] < 0:
            return False
        return True

    def crop(self, array, dimensions, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not self.shape(dimensions) or not self.shape(position):
            return None
        px = position[0]
        ex = position[0] + dimensions[0]
        py = position[1]
        ey = position[1] + dimensions[1]
        if ex > len(array) or ey > len(array[0]):
            return None
        return array[px:ex,py:ey]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Returns:
            new_arr: thined numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in (0, 1):
            return None
        if axis:
            real_axis = 0
        else:
            real_axis = 1
        if n > array.shape[real_axis]:
            return None
        return np.delete(array, n-1, real_axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in (0, 1):
            return None
        if axis:
            return np.tile(array, (1, n))
        else:
            return np.tile(array, (n, 1))

    def mosaic(self, array, dimensions):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dimensions, tuple):
            return None
        if not isinstance(dimensions[0], int) or not isinstance(dimensions[1], int) or dimensions[0] <= 0 or dimensions[1] <= 0:
            return None
        return np.tile(array, dimensions)
