import cv2
import numpy as np


def eqHist(image):
    """
    Equaliza o histograma em escala de cinza da imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    """
    img_array = np.asarray(image)
    histogram_array = np.bincount(img_array.flatten(), minlength=256)
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array/num_pixels
    chistogram_array = np.cumsum(histogram_array)
    transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
    img_list = list(img_array.flatten())
    eq_img_list = [transform_map[p] for p in img_list]
    eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)
    return eq_img_array
