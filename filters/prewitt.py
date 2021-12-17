from scipy import ndimage


def prewittCv(image):
    """
    Aplica o filtro de prewitt na imagem.

    Parameters:
    image -> imagem que recebera o filtro.
    """
    return ndimage.prewitt(image)

