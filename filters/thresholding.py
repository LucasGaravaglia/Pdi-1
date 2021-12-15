import cv2

def thresholding(image, thresh=0):
    return cv2.threshold(image, 120, 255, thresh)[1]
