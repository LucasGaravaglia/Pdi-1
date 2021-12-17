import cv2
import numpy as np


def robertsCv(image):
    """
    Aplica o filtro de robers na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    kernelX = np.array([[-1, 0], [0, 1]], dtype=int)
    kernelY = np.array([[0, -1], [1, 0]], dtype=int)

    x = cv2.filter2D(image, cv2.CV_16S, kernelX)
    y = cv2.filter2D(image, cv2.CV_16S, kernelY)

    return cv2.addWeighted(x, 0.5, y, 0.5, 0)
