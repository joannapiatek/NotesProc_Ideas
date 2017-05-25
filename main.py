import cv2
import sys
import ImageServices.InOut as Img_io
import ImageServices.Basic as Img_bas
import Constants.Colors as Color
from run_sequences import *
import numpy as np
import matplotlib.pyplot as plt

filename = 'img/frag'
img = Img_io.load_img_grayscale(filename + '.jpg')

hist, bin_edges = np.histogram(img)
# plt.hist(img.ravel(), bins=256)
xd = plt.hist(img.ravel(), bins=range(0, 255)) #, range=[-1, 256]) # , fc='k', ec='k')
# fig = plt.gcf()
plt.show()

# binarized_img = Img_bas.binarize_img(img, filename)
# run_morphology_operations(binarized_img, filename)

sys.exit(0)
