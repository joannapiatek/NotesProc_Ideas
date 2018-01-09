import cv2
import glob
import os


# def show_img(image, name):
#     cv2.namedWindow(name, cv2.WINDOW_NORMAL)
#     cv2.imshow(name, image)
#     cv2.waitKey(0)


def load_img_grayscale(filename, ext):
    # Check if image is loaded fine - TODO
    return cv2.imread(filename + '.' + ext, 0)


def get_files_base_names_from_dir(path, file_extension):
    initial_dir = os.getcwd()
    os.chdir(path)
    files_names = glob.glob("*." + file_extension)

    files_base_names = []
    for filename in files_names:
        files_base_names.append(os.path.splitext(filename)[0])

    os.chdir(initial_dir)

    return files_base_names


def move_files_with_letters_to_dir(path, letters):
    initial_dir = os.getcwd()
    os.chdir(path)
    files_to_move = glob.glob("*" + letters + "*")

    os.makedirs(letters)

    for file_to_move in files_to_move:
        os.rename(file_to_move, letters + "/" + file_to_move)

    os.chdir(initial_dir)