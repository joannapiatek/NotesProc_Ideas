import sys
import ImageServices.InOut as Img_io
import ImageServices.Transform as Img_bas
from run_sequences import *


filename = 'img/frag'

# img = Img_io.load_img_grayscale(filename + '.jpg')
# binarized_img = Img_bas.binarize_img(img, filename)
# run_morphology_operations(binarized_img, filename)

run_segmentation(filename + '_test')

sys.exit(0)

