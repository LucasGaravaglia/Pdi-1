import cv2
import numpy as np


# def zeroCross(image):
#     kernel = np.array([[0, 1, 0],
#                       [1, -4, 1],
#                       [0, 1, 0]])
#     return cv2.filter2D(image, cv2.CV_16S, kernel)


import cv2
import numpy as np

DoG_kernel = [
            [0,   0, -1, -1, -1, 0, 0],
            [0,  -2, -3, -3, -3,-2, 0],
            [-1, -3,  5,  5,  5,-3,-1],
            [-1, -3,  5, 16,  5,-3,-1],
            [-1, -3,  5,  5,  5,-3,-1],
            [0,  -2, -3, -3, -3,-2, 0],
            [0,   0, -1, -1, -1, 0, 0]
        ]


def zeroCross(image):
    z_c_image = np.zeros(image.shape)

    for i in range(0,image.shape[0]-1):
        for j in range(0,image.shape[1]-1):
            if image[i][j]>0:
                if image[i+1][j] < 0 or image[i+1][j+1] < 0 or image[i][j+1] < 0:
                    z_c_image[i,j] = 1
            elif image[i][j] < 0:
                if image[i+1][j] > 0 or image[i+1][j+1] > 0 or image[i][j+1] > 0:
                    z_c_image[i,j] = 1
    return z_c_image