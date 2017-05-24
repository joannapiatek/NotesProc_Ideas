import cv2
import sys
import ImageServices.InOut as ios
import numpy as np

filename = 'img/frag'
# Load the image in grayscale
img = cv2.imread(filename + '.jpg', 0)
cv2.imwrite(filename + '_grayscale.png', img)

ret, binarized_image = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
#ios.show_img(binarized_image, "Plain binarization")

ret, binarized_image = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY_INV)
#ios.show_img(binarized_image, "Only black")

ret, binarized_image = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
#ios.show_img(binarized_image, "Only gray")


imgSize = np.shape(img)
# img = cv2.GaussianBlur(img, (11, 11), 0)

ios.show_img(img, "img")
#img = cv2.bilateralFilter(img, 9, 200, 200)

for i in range(0, 10):
    img = cv2.bilateralFilter(img, 3, 20, 200)

ios.show_img(img, "Bilateral")


for i in range(0, imgSize[0]):
    for j in range(0, imgSize[1]):
        if (img[i, j] > 115) and (img[i, j] < 160):
            img[i, j] = 255
        else:
            img[i, j] = 0

ios.show_img(img, "After loop")

# dst = np.array(img)
# cv2.inRange(img, 150, 255, dst)
# ios.show_img(dst, "Test")

sys.exit(0)
