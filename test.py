import cv2
import filters

listImages = []

def saveLastImage():
    cv2.imwrite("lastImage.jpg",listImages[listImages.count-1])
