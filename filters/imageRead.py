import skimage.color
import skimage.io
import cv2

def imageRead(path, histogram=False):
    if histogram:
        return skimage.io.imread(path, as_gray=histogram)
    else:
        return cv2.imread(path)