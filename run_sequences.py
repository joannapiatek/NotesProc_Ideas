import LinesServices.Morphology as Morph
import numpy as np
import cv2


def run_morphology_operations(binarized_img, filename):
    img_size = np.shape(binarized_img)

    horizontal = Morph.get_horizontal_lines(binarized_img.copy(), img_size[1])
    cv2.imwrite(filename + '_horizontal.png', horizontal)

    vertical = Morph.get_vertical_lines(binarized_img.copy(), img_size[0])
    cv2.imwrite(filename + '_vertical.png', vertical)

    cv2.bitwise_not(vertical, vertical)
    cv2.imwrite(filename + '_vertical_bit.png', vertical)

    cv2.bitwise_not(horizontal, horizontal)
    cv2.imwrite(filename + '_horizontal_bit.png', horizontal)

    Morph.smooth_image_with_saving(vertical, filename)