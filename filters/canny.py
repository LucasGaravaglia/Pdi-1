import cv2

def cannyCv(image):
    imageBlur = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image=imageBlur, threshold1=100, threshold2=200)
