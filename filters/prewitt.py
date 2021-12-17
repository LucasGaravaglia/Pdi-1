import cv2
import numpy as np


def prewittCv(image):
    """
    Aplica o filtro de prewitt na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv2.filter2D(image, -1, kernelx)
    img_prewitty = cv2.filter2D(image, -1, kernely)
    return img_prewittx+img_prewitty
