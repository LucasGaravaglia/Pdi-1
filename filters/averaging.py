import cv2


def averagingCv(image, figure_size=3):
    """
    Aplica o filtro de passa baixa de média na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    figure_size -> Tamanho da matriz.
    """
    return cv2.blur(image, (figure_size, figure_size))
