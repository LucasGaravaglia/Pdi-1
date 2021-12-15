import cv2

def highpassBasic(img, sigma=3):
    return img - cv2.GaussianBlur(img, (3, 3), sigma) + 127
