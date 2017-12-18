import cv2


def resize_image(img, filename):
    dim = (20, 50)

    res = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(filename + '.png', res)
    return res
