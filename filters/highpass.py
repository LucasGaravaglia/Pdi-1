import cv2
import numpy as np

from filters.highpassBasic import highpassBasicCv

def highpassCv(image, figure_size=3, sigma=1):
    data = np.array(image, dtype=float)
    return (sigma*data)+highpassBasicCv(image,figure_size)
