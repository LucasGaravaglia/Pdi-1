import cv2

def highpassBasicCv(img, sigma=3):
    return img - cv2.GaussianBlur(img, (3, 3), sigma) + 127
