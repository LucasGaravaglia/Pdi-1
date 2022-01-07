import cv2


def cannyCv(image):
    """
    Aplica o filtro de canny na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    return cv2.Canny(image=image, threshold1=100, threshold2=200)
