import cv2
import Constants.Colors as Color
import matplotlib.pyplot as plt
import numpy as np


def binarize_img(img, filename, threshold=0):
    # 11 - uzalezniac od r-ru pieciolini
    img = cv2.GaussianBlur(img, (5, 5), 0)

    if threshold == 0:
        threshold = count_binarization_threshold(img)

    ret, binarized_img = cv2.threshold(img, threshold, Color.WHITE, cv2.THRESH_BINARY_INV)
    cv2.imwrite(filename + '_binarized.png', binarized_img)
    return binarized_img


def count_binarization_threshold(img):
    colors_intensity, b, patches = plt.hist(img.ravel(), bins=range(0, 256), normed=True)
    plt.close()
    background_color = np.argmax(colors_intensity)
    factor = (background_color * 50) / 255
    return background_color - factor
