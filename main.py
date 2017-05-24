import cv2
import sys
import numpy as np
import ImageServices.InOut as Img_io
import LinesServices.Morphology as Morph

filename = 'img/frag'
img = Img_io.load_img_grayscale(filename + '.jpg')

# Binarize
img = cv2.GaussianBlur(img, (11, 11), 0)
low_val = 150
ret, binarized_img = cv2.threshold(img, low_val, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite(filename + '_binarized.png', binarized_img)

# Create the images that will use to extract the horizontal and vertical lines
horizontal = binarized_img.copy()
vertical = binarized_img.copy()

imgSize = np.shape(binarized_img)

horizontalSize = imgSize[1] / 30
horizontalStructure = Morph.get_horizontal_structure(horizontalSize)
horizontal = Morph.erode_and_dilate(horizontal, horizontalStructure, 1)

# Show extracted horizontal lines
# show_img(horizontal, 'horizontal')
cv2.imwrite(filename + '_horizontal.png', horizontal)

verticalSize = imgSize[0] / 30
verticalStructure = Morph.get_vertical_structure(verticalSize)
vertical = Morph.erode_and_dilate(vertical, verticalStructure, 1)

# Show extracted vertical lines
# show_img(vertical, 'vertical')
cv2.imwrite(filename + '_vertical.png', vertical)

##################################
# Inverse vertical image
cv2.bitwise_not(vertical, vertical)
# show_img(vertical, 'vertical_bit')
cv2.imwrite(filename + '_vertical_bit.png', vertical)

# Extract edges and smooth image
# Step 1 - extract edges
edges = cv2.adaptiveThreshold(vertical, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)
# show_img(edges, "edges")
cv2.imwrite(filename + '_edges.png', edges)

# Step 2 - dilate(edges)
kernel = np.ones((2, 2), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=2)
# show_img(edges, "dilate")
cv2.imwrite(filename + '_dilate.png', edges)

# Step 3 - src.copyTo(smooth)
smooth = vertical.copy()

# Step 4 - blur smooth img
smooth = cv2.blur(smooth, (4, 4))
cv2.imwrite(filename + '_smooth_blur.png', smooth)

vertical = smooth * (edges.astype(smooth.dtype))
# Step 5 - smooth.copyTo(src, edges)

# Show final result
cv2.bitwise_not(vertical, vertical)
# show_img(vertical, "smooth")
cv2.imwrite(filename + '_smooth.png', vertical)

sys.exit(0)
