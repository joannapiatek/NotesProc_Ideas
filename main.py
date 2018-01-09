import sys

import ImageServices.Transform as Img_bas

from run_sequences import *

# dir_path = 'patterns/100/note_dot/'
dir_path = 'binarization_test/'
ext = 'JPG'
files_base_names = Img_io.get_files_base_names_from_dir(dir_path, ext)

for file_basename in files_base_names:
    filename = dir_path + file_basename

    img = Img_io.load_img_grayscale(filename, ext)
    # img = scal.resize_image(img, filename)
    binarized_img = Img_bas.binarize_img(img, filename)
    # run_morphology_operations(binarized_img, filename)
    # cut_stafflines_paste_notes(filename)
    # run_segmentation(filename)
    #
    # Img_io.move_files_with_letters_to_dir(dir_path, file_basename)

sys.exit(0)

