import cv2
import random


def SaltPepperCv(image, salt=0.004):
    """
    Aplica ruido de salt & pepper na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    salt -> parametro de peso do ruido.
    """
    nImage = image.copy()
    pepper = 1 - salt
    for i in range(nImage.shape[0]):
        for j in range(nImage.shape[1]):
            rdn = random.random()
            if rdn < salt:
                nImage[i][j] = 0
            elif rdn > pepper:
                nImage[i][j] = 255
            else:
                pass
    return nImage
