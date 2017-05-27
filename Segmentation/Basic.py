import numpy as np
import Constants.Colors as Colors
import Models.Geometry as Geom
import cv2
import ImageServices.InOut as Img_io


def extract_plain_segments(img):
    segments_borders = []
    im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for current_contours in contours:
        segments_borders.append(get_segment_borders(current_contours))

    for rect in segments_borders:
        start = (rect.left_up.x_coor, rect.left_up.y_coor)
        end = (rect.right_bott.x_coor, rect.right_bott.y_coor)
        cv2.rectangle(img, start, end, (128, 255, 0), 3)

    # cv2.drawContours(img, contours, -1, (128, 255, 0), 3)
    Img_io.show_img(img, 'contours')
    return img


def get_segment_borders(contours):
    x_coors = []
    y_coors = []

    for point in contours:
        y_coors.append(point[0][1])
        x_coors.append(point[0][0])

    max_x = max(x_coors)
    min_x = min(x_coors)
    max_y = max(y_coors)
    min_y = min(y_coors)

    left_bott = Geom.Point(max_x, min_y)
    right_bott = Geom.Point(max_x, max_y)
    right_up = Geom.Point(min_x, max_y)
    left_up = Geom.Point(min_x, min_y)

    return Geom.Rectangle(left_bott, right_bott, right_up, left_up)
