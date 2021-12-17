import cv2

def eqHist(image):
    """
    Equaliza o histograma em escala de cinza da imagem.

    Parameters:
    image -> imagem que recebera o filtro.
    """
    return cv2.equalizeHist(image)
