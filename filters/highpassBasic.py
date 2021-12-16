import cv2
import numpy as np

from filters.averaging import averagingCv

def highpassBasicCv(image, figure_size=3):
    data = np.array(image, dtype=float)
    return data - averagingCv(image,figure_size)