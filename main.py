import sys
import Common.InOut as IO
import Common.Transform as Transform
import SymbolsExtraction.Stafflines as Stafflines

# from run_sequences import *


# dir_path = 'patterns/100/note_dot/'
dir_path = 'test/'
ext = 'PNG'
files_base_names = IO.get_files_base_names_from_dir(dir_path, ext)

for file_basename in files_base_names:
    filename = dir_path + file_basename

    img = IO.load_img_grayscale(filename, ext)

    # line_height, space_height = Stafflines.calc_staff_heights(img)
    # stafflines_model = Stafflines.create_stafflines_set_model(line_height, space_height)

    # img = scal.resize_image(img, filename)
    binarized_img = Transform.binarize_img(img, filename)

    # horizontal, vertical = run_morphology_operations(img, filename)
    # Stafflines.get_stafflines_coordinates(img, stafflines_model)

    # cut_stafflines_paste_notes(filename)
    # run_segmentation(filename)
    #
    # Img_io.move_files_with_letters_to_dir(dir_path, file_basename)

sys.exit(0)

