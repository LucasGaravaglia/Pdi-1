from matplotlib import pyplot as plt


def histCv(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.savefig('histogram.jpg')
    plt.close()
