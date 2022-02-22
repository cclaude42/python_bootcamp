"""ImageProcessor file"""
from PIL import Image
import numpy as np

class ImageProcessor():
    """ImageProcessor class"""
    def load(self, path):
        """Load the image"""
        try:
            img = Image.open(path)
            arr = np.array(img)
            print(f"Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}")
            return np.divide(arr, 255)
        except Exception as e:
            print(f"Exception : {e.__class__.__name__} -- strerror: {e}")
        return None

    def display(self, array):
        """Display the image"""
        array = np.multiply(array, 255)
        array = array.astype(np.uint8)
        img = Image.fromarray(array, 'RGB')
        img.show()
