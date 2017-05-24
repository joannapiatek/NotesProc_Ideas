import numpy as np
import Constants.Colors as Color
import Models.Elements as Elements

def clear_image_from_no_stafflines(img):
    img_height = np.shape(img)[0]
    img_width = np.shape(img)[1]
    cleared_image = img.copy()

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

    return line_lenght > 0.5 * img_width


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
