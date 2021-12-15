import numpy as np

def logCv(image):
    c = 255 / np.log(1 + np.max(image))
    logImage = c * (np.log(image + 1))
    return np.array(logImage, dtype=np.uint8)
