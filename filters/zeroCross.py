import numpy as np
import cv2


def laplace_of_gaussian(image, sigma=1., kappa=0.75, pad=False):
    """
    Aplica o filtro de zero Cross na imagem.
    Parameters:
    image -> imagem que recebera o filtro.
    sigma -> parametro de peso para o filtro.
    kappa -> parametro de condição para o filtro.
    pad -> Aplica um pad ou não na imagem.
    """
    img = cv2.GaussianBlur(image, (0, 0), sigma) if 0. < sigma else image
    img = cv2.Laplacian(img, cv2.CV_64F)
    rows, cols = img.shape[:2]

    min_map = np.minimum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    max_map = np.maximum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))

    pos_img = 0 < img[1:rows-1, 1:cols-1]

    neg_min = min_map < 0
    neg_min[1 - pos_img] = 0

    pos_max = 0 < max_map
    pos_max[pos_img] = 0

    zero_cross = neg_min + pos_max

    value_scale = 255. / max(1., img.max() - img.min())
    values = value_scale * (max_map - min_map)
    values[1 - zero_cross] = 0.

    if 0. <= kappa:
        thresh = float(np.absolute(img).mean()) * kappa
        values[values < thresh] = 0.
    log_img = values.astype(np.uint8)
    if pad:
        log_img = np.pad(log_img, pad_width=1,
                         mode='constant', constant_values=0)
    return log_img
