import LinesExtraction.Morphology as Morph
import LinesExtraction.CutAndPaste as CuP
import numpy as np
import cv2
import Segmentation.Borders as Segm
import ImageServices.InOut as Img_io


def run_morphology_operations(binarized_img, filename):
    img_size = np.shape(binarized_img)

    horizontal = Morph.get_horizontal_lines(binarized_img.copy(), img_size[1])
    cv2.imwrite(filename + '_horizontal.png', horizontal)

    vertical = Morph.get_vertical_lines(binarized_img.copy(), img_size[0])
    cv2.imwrite(filename + '_vertical.png', vertical)

    # test = CuP.paste_horizontal_notes_elements(vertical, horizontal)
    # Img_io.show_img(test, 'test')
    # cv2.imwrite(filename + '_horizontal_paste.png', test)

    #Morph.smooth_image_with_saving(vertical, filename)


def cut_stafflines_paste_notes(filename):
    staff_lines = cv2.imread(filename + '_horizontal.png')
    notes = cv2.imread(filename + '_vertical' + '.png')
    binarized_img = cv2.imwrite(filename + '_binarized.png')

    result = CuP.cut_white_elements(binarized_img, staff_lines)
    # cv2.imwrite(filename + '_result_without_lines.png', result)
    result = CuP.paste_white_elements(result, notes)
    # cv2.imwrite(filename + '_result_with_notes.png', result)

    kernel = np.ones((5, 5), np.uint8)
    result = cv2.morphologyEx(result, cv2.MORPH_OPEN, kernel)

    cv2.imwrite(filename + '_result.png', result)

def run_segmentation(filename):
    img = Img_io.load_img_grayscale(filename + '.png')

    img_segments = Segm.extract_plain_segments(img)
    cv2.imwrite(filename + '_segments.png', img_segments)
