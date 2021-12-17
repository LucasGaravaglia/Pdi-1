import cv2


def greyScaleCv(image):
    """
    Aplica a escala de cinza na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
