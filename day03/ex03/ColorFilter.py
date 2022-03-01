import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
    """Apply filter to images"""

    def invert(self, array):
        """
            Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        return 1 - array

    def to_blue(self, array):
        """
            Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        new = np.zeros(array.shape)
        new[:,:,2] = array[:,:,2]
        return new

    def to_green(self, array):
        """
            Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        new = array.copy()
        new[:,:,0] *= 0
        new[:,:,2] *= 0
        return new

    def to_red(self, array):
        """
            Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        new = array - self.to_blue(array) - self.to_green(array)
        return new

    def to_celluloid(self, array):
        """
            Applies a celluloid filter to the image received as a numpy array.
            Celluloid filter must display at least four thresholds of shades.
            Be careful! You are not asked to apply black contour on the object,
            you only have to work on the shades of your images.
            Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        new = np.array(array)
        treshholds = np.linspace(0.0, 1.0, num=4, endpoint=False)
        for shade in treshholds:
            new[array >= shade] = shade
        return new

    def to_grayscale(self, array, filter, **kwargs):
        """
            Applies a grayscale filter to the image received as a numpy array.
            For filter = 'mean'/'m': performs the mean of RBG channels.
            For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if filter in ['m', 'mean']:
            new = np.array(array)
            for row in new:
                for pixel in row:
                    gray = pixel.sum() / 3
                    pixel[0] = gray
                    pixel[1] = gray
                    pixel[2] = gray
            return new
        elif filter in ['w', 'weighted']:
            new = np.array(array)
            weight = np.array(kwargs['weight'])
            for row in new:
                for pixel in row:
                    gray = (pixel * weight).sum()
                    pixel[0] = gray
                    pixel[1] = gray
                    pixel[2] = gray
            return new
        else:
            return None

