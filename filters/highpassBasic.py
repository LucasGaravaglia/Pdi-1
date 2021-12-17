import cv2
import numpy as np

from filters.averaging import averagingCv


def highpassBasicCv(image, figure_size=3):
    """
    Aplica o filtro de passa alta de alto contraste na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    figure_size -> Tamanho da matriz.
    """
    data = np.array(image, dtype=float)
    return data - averagingCv(image, figure_size)
