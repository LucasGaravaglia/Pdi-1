import cv2


def medianCv(image, figure_size=3):
    """
    Aplica o filtro de passa baixa de mediana na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    figure_size -> Tamanho da matriz.
    """
    return cv2.medianBlur(image, figure_size)
