import cv2

def averagingCv(image, figure_size=3):
    return cv2.blur(image, (figure_size, figure_size))
