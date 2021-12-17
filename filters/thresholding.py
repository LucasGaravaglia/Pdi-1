import cv2


def thresholdingCv(image, trash=200, type=0):
    """
    Aplica Limiarização na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    trash -> valor de limiarização.
    type -> tipo de limiarização.
    """
    return cv2.threshold(image, trash, 255, type)[1]
