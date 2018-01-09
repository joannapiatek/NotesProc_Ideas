import numpy as np
from itertools import *
from collections import Counter
import Constants.Colors as Color
from operator import itemgetter


def encode_rle(x):
    return [(name, len(list(group))) for name, group in groupby(x)]


def calc_staff_heights(binarized_img):
    lines = get_colors_vertical_lengths(binarized_img)

    lines = sorted(lines)
    counted_pairs = Counter(elem for elem in lines)
    most_common = counted_pairs.most_common(counted_pairs.__len__())

    line_height = next((x for x in most_common if x[0][0] == Color.BLACK), None)[0][1]
    space_height = next((x for x in most_common if x[0][0] == Color.WHITE), None)[0][1]
    return line_height, space_height


def get_colors_vertical_lengths(binarized_img):
    img_size = np.shape(binarized_img)
    encoded_lines = []

    for line in binarized_img:
        encoded_item = encode_rle(line)
        if encoded_item != [(Color.WHITE, img_size[1])] and encoded_item.__len__() % 10 == 1:
            encoded_lines += encoded_item
    return encoded_lines


def create_stafflines_set_model(line_height, space_height):
    lines_set = []
    for repeat in range(1, 5):
        lines_set = add_space(lines_set, space_height)
        lines_set = add_line(lines_set, line_height)

    lines_set = add_space(lines_set, space_height)
    return lines_set


def add_line(lines_set, line_height):
    for row in range(1, line_height):
        lines_set.append(Color.WHITE)
    return lines_set


def add_space(lines_set, space_height):
    for row in range(1, space_height):
        lines_set.append(Color.BLACK)
    return lines_set


def get_stafflines_coordinates(binarized_img, stafflines_model):
    window_height = len(stafflines_model)

    i = -1
    for line in binarized_img:
        i += 1
        # funkcja index nie działa tu
        index = line.index(Color.WHITE)

    return 0

# def get_stafflines_coordinates(binarized_img):
#
#     counted = []
#     index = -1
#     for line in binarized_img:
#         index += 1
#         if Color.WHITE not in line:
#             continue
#         count_for_staffline = Counter(line)[Color.WHITE]
#         counted.append((count_for_staffline, index))
#
#
#     max_width_line = max(counted, key=itemgetter(0))
#     f = int(round(0.5*max_width_line[0]))
#     result = filter(lambda x: x[0] >= f, counted)
#
#     return 0