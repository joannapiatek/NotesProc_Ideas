import cv2
import sys
import numpy as np


def show_img(image, name):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)


filename = 'img/frag'
# Load the image in grayscale
img = cv2.imread(filename + '.jpg', 0)

# Check if image is loaded fine
#

# Binarize
img = cv2.GaussianBlur(img, (11, 11), 0)
low_val = 150
ret, binarized_img = cv2.threshold(img, low_val, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite(filename + '_binarized.png', binarized_img)

# Create the images that will use to extract the horizontal and vertical lines
horizontal = binarized_img.copy()
vertical = binarized_img.copy()

imgSize = np.shape(binarized_img)
# Specify size on horizontal axis
horizontalSize = imgSize[1] / 30

# Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalSize, 1))

# Apply morphology operations
horizontal = cv2.erode(horizontal, horizontalStructure, iterations=1)
horizontal = cv2.dilate(horizontal, horizontalStructure, iterations=1)

# Show extracted horizontal lines
# show_img(horizontal, 'horizontal')
cv2.imwrite(filename + '_horizontal.png', horizontal)

# Specify size on vertical axis
verticalSize = imgSize[0] / 30

# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalSize))

# Apply morphology operations
vertical = cv2.erode(vertical, verticalStructure, iterations=1)
vertical = cv2.dilate(vertical, verticalStructure, iterations=1)

# Show extracted vertical lines
# show_img(vertical, 'vertical')
cv2.imwrite(filename + '_vertical.png', vertical)

##################################
# Inverse vertical image
cv2.bitwise_not(vertical, vertical)
# show_img(vertical, 'vertical_bit')
cv2.imwrite(filename + '_vertical_bit.png', vertical)

# Extract edges and smooth image according to the logic
# 1. extract edges
# 2. dilate(edges)
# 3. src.copyTo(smooth)
# 4. blur smooth img
# 5. smooth.copyTo(src, edges)

# Step 1
edges = cv2.adaptiveThreshold(vertical, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)
# show_img(edges, "edges")
cv2.imwrite(filename + '_edges.png', edges)

# Step 2
# , cv2.CV_8UC1)
kernel = np.ones((2, 2), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=2)
# show_img(edges, "dilate")
cv2.imwrite(filename + '_dilate.png', edges)

# Step 3
smooth = vertical.copy()

# Step 4
smooth = cv2.blur(smooth, (4, 4))
cv2.imwrite(filename + '_smooth_blur.png', smooth)

vertical = smooth * (edges.astype(smooth.dtype))
# Step 5

# Show final result
cv2.bitwise_not(vertical, vertical)
# show_img(vertical, "smooth")
cv2.imwrite(filename + '_smooth.png', vertical)

sys.exit(0)
