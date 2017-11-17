import numpy as np
import Constants.Colors as Colors
import Models.Geometry as Geom
import cv2
import ImageServices.InOut as Img_io
import os


def extract_plain_segments(filename):
    segments_borders = []
    img = Img_io.load_img_grayscale(filename, 'png')
    im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    selected_contours = contours
    for current_contours in selected_contours:
        segments_borders.append(get_segment_borders(current_contours))

    min_size = 10
    selected_borders = []
    for rect in segments_borders:
        if rect.left_bott.x_coor - rect.left_up.x_coor > min_size \
                and rect.right_bott.y_coor - rect.left_up.y_coor > min_size:
            selected_borders.append(rect)

    for rect in selected_borders:
        start = (rect.left_up.x_coor, rect.left_up.y_coor)
        end = (rect.right_bott.x_coor, rect.right_bott.y_coor)
        cv2.rectangle(img, start, end, Colors.RED, 3)

    cv2.imwrite(filename + '_segments.png', img)

    # cv2.drawContours(img, contours, -1, (128, 255, 0), 3)
    # Img_io.show_img(img, 'contours')
    return selected_borders


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


def save_image_segments(filename, segments):
    img = Img_io.load_img_grayscale(filename, 'PNG')
    counter = 1
    new_folder_path = filename + '_crop/'
    os.mkdir(new_folder_path)

    for rect in segments:
        x1 = rect.left_up.x_coor
        y1 = rect.left_up.y_coor
        x2 = rect.right_bott.x_coor
        y2 = rect.right_bott.y_coor

        crop_img = img[y1:y2, x1:x2]
        crop_filename = new_folder_path + str(counter) + '.png'
        cv2.imwrite(crop_filename, crop_img)
        counter += 1
