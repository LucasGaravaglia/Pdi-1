import cv2 
import numpy as np


def greyScale(image):
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

def roberts(image) :
  kernelX = np.array([[-1, 0], [0, 1]], dtype=int)
  kernelY = np.array([[0, -1], [1, 0]], dtype=int) 

  x = cv2.filter2D(image,cv2.CV_16S,kernelX)
  y = cv2.filter2D(image,cv2.CV_16S,kernelY)

  absX = cv2.convertScaleAbs(x)
  absY = cv2.convertScaleAbs(y)
  return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

def prewitt(image):
  kernelX = np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype=int)
  kernelY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)

  x = cv2.filter2D(image, cv2.CV_16S, kernelX)
  y = cv2.filter2D(image, cv2.CV_16S, kernelY)

  absX = cv2.convertScaleAbs(x)
  absY = cv2.convertScaleAbs(y)
  return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


image1 = cv2.imread('input1.jpg') 

while True:
  greyImage = greyScale(image1)
  robertsImage = roberts(greyImage)
  prewittImage = prewitt(greyImage)
  cv2.imshow('robertsImage', robertsImage) 
  cv2.imshow('prewittImage', prewittImage) 
  if cv2.waitKey(1) == 27:  
    break

image1.realease()
cv2.destroyAllWindows()