import cv2

def medianCv(image, figure_size=3):
    return cv2.medianBlur(image, figure_size) 

