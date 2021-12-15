import numpy as np
import cv2

def sobel(image):
    gradX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    gradY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    grad = np.sqrt(gradX**2 + gradY**2)
    return (grad * 255 / grad.max()).astype(np.uint8), gradX, gradY
