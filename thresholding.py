import cv2
import sys
import ImageServices.InOutService as ios
import numpy as np

filename = 'img/frag'
# Load the image in grayscale
img = cv2.imread(filename + '.jpg', 0)

ret, binarized_image = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
ios.show_img(binarized_image, "Plain binarization")

ret, binarized_image = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
ios.show_img(binarized_image, "Only black")

ret, binarized_image = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY_INV)
ios.show_img(binarized_image, "Only gray")

dst = np.array(img)
cv2.inRange(img, 150, 255, dst)
ios.show_img(dst, "Test")

sys.exit(0)
