import cv2
import sys
import numpy as np
import ImageServices.InOut as Img_io
import LinesServices.Morphology as Morph
import Constants.Colors as Color
import LinesServices.Separation as sep

filename = 'img/frag'
img = Img_io.load_img_grayscale(filename + '.jpg')

img = cv2.GaussianBlur(img, (11, 11), 0)
ret, binarized_img = cv2.threshold(img, 150, Color.WHITE, cv2.THRESH_BINARY_INV)
cv2.imwrite(filename + '_binarized.png', binarized_img)

imgSize = np.shape(binarized_img)

horizontal = Morph.get_horizontal_lines(binarized_img.copy(), imgSize[1])
cv2.imwrite(filename + '_horizontal.png', horizontal)

vertical = Morph.get_vertical_lines(binarized_img.copy(), imgSize[0])
cv2.imwrite(filename + '_vertical.png', vertical)

cv2.bitwise_not(vertical, vertical)
cv2.imwrite(filename + '_vertical_bit.png', vertical)

cv2.bitwise_not(horizontal, horizontal)
cv2.imwrite(filename + '_horizontal_bit.png', horizontal)

# Morph.smooth_image_with_saving(vertical, filename)

cleared = sep.clear_image_from_no_stafflines(horizontal)
cv2.imwrite(filename + '_horizontal_cleared.png', cleared)

sys.exit(0)
