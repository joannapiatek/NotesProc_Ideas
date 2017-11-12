import sys
import ImageServices.InOut as Img_io
import ImageServices.Transform as Img_bas
from run_sequences import *


filename = 'NotesPhotos/prepared/3/3'

img = Img_io.load_img_grayscale(filename + '.jpg')
binarized_img = Img_bas.binarize_img(img, filename)
run_morphology_operations(binarized_img, filename)
cut_stafflines_paste_notes(filename)
run_segmentation(filename + '_result')

sys.exit(0)

