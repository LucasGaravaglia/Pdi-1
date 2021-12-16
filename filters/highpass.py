import cv2
def highpassCv(img, sigma=3):
    return img - cv2.GaussianBlur(img, (5, 5), sigma) + 127
