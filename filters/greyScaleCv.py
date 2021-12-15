import cv2

def greyScaleCv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
