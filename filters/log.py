import numpy as np


def logCv(image):
    """
    Aplica o filtro de log na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    c = 255 / np.log(1 + np.max(image))
    logImage = c * (np.log(image + 1))
    return np.array(logImage, dtype=np.uint8)
