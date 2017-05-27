import LinesExtraction.Morphology as Morph
import LinesExtraction.CutAndPaste as CuP
import numpy as np
import cv2
import Segmentation.Basic as Segm
import ImageServices.InOut as Img_io


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

    test = CuP.paste_horizontal_notes_elements(vertical, horizontal)
    # Img_io.show_img(test, 'test')
    cv2.imwrite(filename + '_test.png', test)

    #Morph.smooth_image_with_saving(vertical, filename)


def run_segmentation(filename):
    img = Img_io.load_img_grayscale(filename + '.png')

    img_segments = Segm.extract_plain_segments(img)
    cv2.imwrite(filename + '_segments.png', img_segments)
