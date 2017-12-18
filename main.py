import sys
import os
import ImageServices.InOut as Img_io
import ImageServices.Transform as Img_bas
from run_sequences import *
import Segmentation.Scaling as scal


dir_path = 'patterns/100/quaver_2_down/'
ext = 'PNG'
files_base_names = Img_io.get_files_base_names_from_dir(dir_path, ext)

for file_basename in files_base_names:
    filename = dir_path + file_basename

    img = Img_io.load_img_grayscale(filename, ext)
    img = scal.resize_image(img, filename)
    # binarized_img = Img_bas.binarize_img(img, filename)
    # run_morphology_operations(binarized_img, filename)
    # cut_stafflines_paste_notes(filename)
    # run_segmentation(filename)
    #
    # Img_io.move_files_with_letters_to_dir(dir_path, file_basename)

sys.exit(0)

