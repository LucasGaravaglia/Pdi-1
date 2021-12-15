import cv2
import random

def SaltPepper(image, salt=0.004):
    pepper = 1 - salt
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < salt:
                image[i][j] = 0
            elif rdn > pepper:
                image[i][j] = 255
            else:
                pass
    return image

