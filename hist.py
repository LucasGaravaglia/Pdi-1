import numpy as np
import skimage.color
import skimage.io
from matplotlib import pyplot as plt


def hist(image):
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([0.0, 1.0])
    plt.plot(bin_edges[0:-1], histogram)
    plt.savefig('book.jpeg')
