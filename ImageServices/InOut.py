import cv2


def show_img(image, name):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)


def load_img_grayscale(filename):
    # Check if image is loaded fine - TODO
    return cv2.imread(filename, 0)