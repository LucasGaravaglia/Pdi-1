import cv2


def thresholdingCv(image, trash=200,type=0):
    return cv2.threshold(image, trash, 255, type)[1]
