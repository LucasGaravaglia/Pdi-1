import cv2


def imageReadCv(path):
    """
    Lê um arquivo e retorna a instancia da imagem dele.
    Parameters:
    path -> caminho da imagem.
    """
    return cv2.imread(path)
