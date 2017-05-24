import cv2


def erode_and_dilate(src, structure, iterations):
    result = cv2.erode(src, structure, iterations=iterations)
    result = cv2.dilate(result, structure, iterations=iterations)
    return result


def get_horizontal_structure(horizontal_size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))


def get_vertical_structure(vertical_size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
