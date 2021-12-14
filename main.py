import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
import cv2
import numpy as np
import random


def greyScale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def roberts(image):
    kernelX = np.array([[-1, 0], [0, 1]], dtype=int)
    kernelY = np.array([[0, -1], [1, 0]], dtype=int)

    x = cv2.filter2D(image, cv2.CV_16S, kernelX)
    y = cv2.filter2D(image, cv2.CV_16S, kernelY)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def prewitt(image):
    kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)

    x = cv2.filter2D(image, cv2.CV_16S, kernelX)
    y = cv2.filter2D(image, cv2.CV_16S, kernelY)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def sobel(image):
    gradX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    gradY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    grad = np.sqrt(gradX**2 + gradY**2)
    return (grad * 255 / grad.max()).astype(np.uint8), gradX, gradY


def log(image):
    c = 255 / np.log(1 + np.max(image))
    logImage = c * (np.log(image + 1))
    return np.array(logImage, dtype=np.uint8)


def canny(image):
    imageBlur = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image=imageBlur, threshold1=100, threshold2=200)


def histogram(image):
    return cv2.calcHist([image], [0], None, [256], [0, 256])


def averaging(image, figure_size=3):
    return cv2.blur(image, (figure_size, figure_size))


def median(image, figure_size=3):
    return cv2.medianBlur(image, figure_size)


def highpassBasic(img, sigma=3):
    return img - cv2.GaussianBlur(img, (3, 3), sigma) + 127


def highpass(img, sigma=3):
    return img - cv2.GaussianBlur(img, (5, 5), sigma) + 127


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


def thresholding(image, thresh=0):
    return cv2.threshold(image, 120, 255, thresh)[1]


def zeroCross(image):
    log = cv2.Laplacian(image, cv2.CV_16S)
    minLoG = cv2.morphologyEx(log, cv2.MORPH_ERODE, np.ones((3, 3)))
    maxLoG = cv2.morphologyEx(log, cv2.MORPH_DILATE, np.ones((3, 3)))
    return (minLoG < 0 and log > 0) or (maxLoG > 0 and log < 0)


def watershedPrivate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(
        dist_transform, 0.7*dist_transform.max(), 255, 0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)

    markers = markers+1

    markers[unknown == 255] = 0

    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    return image


image1 = cv2.imread('input8.jpg')

# teste = watershedPrivate(image1)

averagingImage = averaging(image1)
medianImage = median(image1)
highpassBasicImage = highpassBasic(image1)
highpassImage = highpass(image1)
while True:
    if cv2.waitKey(1) == 27:
        break

image1.realease()
cv2.destroyAllWindows()
