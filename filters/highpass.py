import cv2
import numpy as np

from filters.highpassBasic import highpassBasicCv


def highpassCv(image, figure_size=3, sigma=1):
    """
    Aplica o filtro de passa alta de alto contraste na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    figure_size -> Tamanho da matriz.
    sigma -> Parametro de peso do filtro.
    """
    data = np.array(image, dtype=float)
    return (sigma*data)+highpassBasicCv(image, figure_size)
