import cv2
def highpass(img, sigma=3):
    return img - cv2.GaussianBlur(img, (5, 5), sigma) + 127
