import os
import ghostscript
import glob


# some constants
FULL_PATH = os.path.realpath(__file__)
CURRENT_DIRECTORY = os.path.dirname(FULL_PATH)
INPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'input')
OUTPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'output')


# some functions
def convert(pdf_input_path, img_output_path, extension='jpeg'):
    args = ["pdf2img",  # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=" + extension,
            "-r144",
            "-sOutputFile=" + img_output_path,
            pdf_input_path]
    ghostscript.Ghostscript(*args)

def read_files():
    pass

# main
