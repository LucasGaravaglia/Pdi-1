import cv2


def cannyCv(image):
    """
    Aplica o filtro de canny na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    imageBlur = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image=imageBlur, threshold1=100, threshold2=200)
