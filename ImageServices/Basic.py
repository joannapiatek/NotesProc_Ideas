import cv2
import Constants.Colors as Color


def binarize_img(img, filename):
    img = cv2.GaussianBlur(img, (11, 11), 0)
    ret, binarized_img = cv2.threshold(img, 150, Color.WHITE, cv2.THRESH_BINARY_INV)
    cv2.imwrite(filename + '_binarized.png', binarized_img)
    return binarized_img

