import numpy as np
import Constants.Colors as Color
import Models.Geometry as Geom


def cut_white_elements(image, white_elements):
    return change_color_if_white(image, white_elements, Color.BLACK)


def paste_white_elements(image, white_elements):
    return change_color_if_white(image, white_elements, Color.WHITE)


def change_color_if_white(image, white_elements, color):
    if not are_equal_sizes(image, white_elements):
        raise ValueError('Arrays sizes are not the same')

    img_height = np.shape(image)[0]
    img_width = np.shape(image)[1]
    result = image.copy()

    for i in range(0, img_height - 1):
        if Color.WHITE not in white_elements[i, :]:
            continue
        for j in range(0, img_width - 1):
            pixel = Geom.Pixel(i, j, white_elements[i, j])
            if any(value == Color.WHITE for value in pixel.value):
                    result[i, j] = color

    return result


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
            pixel = Geom.Pixel(i, j, horizontal_lines[i, j])
            if (pixel.value == Color.BLACK) \
                    and not (is_pixel_in_staffline(horizontal_lines, pixel))\
                    and not (is_pixel_by_staffline(horizontal_lines, pixel, img_height)):
                    result[i, j] = Color.BLACK

    return result


def clear_stafflines_from_notes_elements(horizontal_lines):
    img_height = np.shape(horizontal_lines)[0]
    img_width = np.shape(horizontal_lines)[1]
    cleared_image = horizontal_lines.copy()

    for i in range(0, img_height - 1):
        for j in range(0, img_width - 1):
            pixel = Geom.Pixel(i, j, cleared_image[i, j])
            if (pixel.value == Color.BLACK) \
                    and not (is_pixel_in_staffline(cleared_image, pixel)):
                cleared_image[i, j] = Color.WHITE

    return cleared_image


def is_pixel_in_staffline(img, pixel):
    row = img[pixel.x_coor, :]

    line_lenght = check_line_lenght(row, pixel)
    img_width = np.shape(img)[1]

    return line_lenght > 0.2 * img_width


def is_pixel_by_staffline(img, pixel, img_height):

    if pixel.x_coor + 2 < img_height:
        pixel_below = Geom.Pixel(pixel.x_coor + 2, pixel.y_coor, Color.WHITE)
        pixel_below.value = img[pixel_below.x_coor, pixel_below.y_coor]
        if is_pixel_in_staffline(img, pixel_below):
            return True

    if pixel.x_coor - 2 >= 0:
        pixel_above = Geom.Pixel(pixel.x_coor - 2, pixel.y_coor, Color.WHITE)
        pixel_above.value = img[pixel_above.x_coor, pixel_above.y_coor]
        return is_pixel_in_staffline(img, pixel_above)


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
