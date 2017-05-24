import numpy as np
import Constants.Colors as Color
import Models.Elements as Elements
import ImageServices.InOut as Img_io


def paste_horizontal_notes_elements(vertical_notes, horizontal_lines):
    if not are_equal_sizes(vertical_notes, horizontal_lines):
        raise ValueError('Arrays sizes are not the same')

    img_height = np.shape(horizontal_lines)[0]
    img_width = np.shape(horizontal_lines)[1]
    result = vertical_notes.copy()

    for i in range(0, img_height - 1):
        if Color.BLACK not in horizontal_lines[i, :]:
            continue

        for j in range(0, img_width - 1):
            pixel = Elements.Pixel(i, j, horizontal_lines[i, j])
            if (pixel.value == Color.BLACK) and not (is_line_staffline(horizontal_lines, pixel)):
                    result[i, j] = Color.BLACK

    return result


def clear_stafflines_from_notes_elements(horizontal_lines):
    img_height = np.shape(horizontal_lines)[0]
    img_width = np.shape(horizontal_lines)[1]
    cleared_image = horizontal_lines.copy()

    for i in range(0, img_height - 1):
        for j in range(0, img_width - 1):
            pixel = Elements.Pixel(i, j, cleared_image[i, j])
            if (pixel.value == Color.BLACK) and not (is_line_staffline(cleared_image, pixel)):
                cleared_image[i, j] = Color.WHITE

    return cleared_image


def is_line_staffline(img, pixel):
    row = img[pixel.x_coor, :]

    line_lenght = check_line_lenght(row, pixel)
    img_width = np.shape(img)[1]

    return line_lenght > 0.2 * img_width


def check_line_lenght(row, pixel):
    row_leng = np.shape(row)[0]
    i = pixel.y_coor
    line_end = 0
    line_start = 0

    while i < row_leng:
        if row[i] == Color.WHITE:
            line_end = i-1
            break
        i += 1

    i = pixel.y_coor
    while i >= 0:
        if row[i] == Color.WHITE:
            line_start = i+1
            break
        i -= 1

    return line_end - line_start + 1


def are_equal_sizes(array1, array2):
    size1 = np.shape(array1)
    size2 = np.shape(array2)

    for i in range(0, np.shape(size1)[0]):
        if not size1[i] == size2[i]:
            return False

    return True
