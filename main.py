import cv2
import sys
import ImageServices.InOut as Img_io
import ImageServices.Colors as Img_bas
import Constants.Colors as Color
from run_sequences import *


filename = 'img/frag1/frag1'
img = Img_io.load_img_grayscale(filename + '.png')

binarized_img = Img_bas.binarize_img(img, filename)
run_morphology_operations(binarized_img, filename)

sys.exit(0)
