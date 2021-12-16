import numpy as np
import skimage.io
import cv2
from matplotlib import pyplot as plt
import matplotlib


def histCv(image):
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([0.0, 1.0])
    plt.plot(bin_edges[0:-1], histogram)
    plt.savefig('histogram.jpg')
