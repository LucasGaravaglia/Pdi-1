from matplotlib import pyplot as plt


def histCv(image):
    """
    Gera o histograma da escala de cinzas.
    Parameters:
    image -> imagem que irá gerar o histograma.
    """
    plt.hist(image.ravel(), 256, [0, 256])
    plt.savefig('histogram.jpg')
    plt.close()
