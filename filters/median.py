import cv2

def median(image, figure_size=3):
    return cv2.medianBlur(image, figure_size)

