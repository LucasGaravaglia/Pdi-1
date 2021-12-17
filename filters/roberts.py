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

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
