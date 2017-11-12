import cv2
import Constants.Colors as Color
import numpy as np


def erode_and_dilate(src, structure, iterations):
    result = cv2.erode(src, structure, iterations=iterations)
    result = cv2.dilate(result, structure, iterations=iterations)
    return result


def get_horizontal_structure(horizontal_size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))


def get_vertical_structure(vertical_size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))


def get_horizontal_lines(img, img_width):
    horizontal_size = img_width / 30
    horizontal_structure = get_horizontal_structure(horizontal_size)
    horizontal = erode_and_dilate(img, horizontal_structure, 1)
    return finishing_dilate(horizontal)


def get_vertical_lines(img, img_height):
    vertical_size = img_height / 30
    vertical_structure = get_vertical_structure(vertical_size)
    vertical = erode_and_dilate(img, vertical_structure, 1)
    return finishing_dilate(vertical)


def smooth_image_with_saving(img, filename):
    # Extract edges and smooth image
    # Step 1 - extract edges
    edges = cv2.adaptiveThreshold(img, Color.WHITE, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)
    cv2.imwrite(filename + '_edges.png', edges)

    # Step 2 - dilate(edges)
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=2)
    cv2.imwrite(filename + '_dilate.png', edges)

    # Step 3 - src.copyTo(smooth)
    smooth = img.copy()

    # Step 4 - blur smooth img
    smooth = cv2.blur(smooth, (4, 4))
    cv2.imwrite(filename + '_smooth_blur.png', smooth)

    smooth_edges = smooth * (edges.astype(smooth.dtype))
    cv2.bitwise_not(smooth_edges, smooth_edges)
    cv2.imwrite(filename + '_smooth.png', smooth_edges)


# uzaleznic (5,5) od rozmiaru pieciolini. pomyslec nad normowaniem
def finishing_dilate(img):
    #kernel = np.ones((5, 5), np.uint8)
    #return cv2.dilate(img, kernel, iterations=1)
    return img
