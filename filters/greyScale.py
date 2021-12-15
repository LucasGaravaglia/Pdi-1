import cv2

def greyScale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
