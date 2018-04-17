#!/usr/bin/env python
import os
import ghostscript
from glob import glob

from PIL import Image
from resizeimage import resizeimage

try:
    from conf import get_sizes
except:
    # fallback to default values
    from _conf import get_sizes

# some constants
FULL_PATH = os.path.realpath(__file__)
CURRENT_DIRECTORY = os.path.dirname(FULL_PATH)
INPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'input')
OUTPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'output')


# some functions
def convert(pdf_input_path, img_output_path, extension='jpg'):
    # converts the pdf input into the img output
    img = OUTPUT_DIRECTORY + '/' + img_output_path + '.' + extension
    pdf = INPUT_DIRECTORY + '/' + pdf_input_path

    args = ["pdf2img",  # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r144",
            "-sOutputFile=" + img,
            pdf]
    ghostscript.Ghostscript(*args)


def read_files(directory=INPUT_DIRECTORY, extension='.pdf'):
    # reads files in a directory with a specific extension
    files = glob('%s/*%s' % (directory ,extension))
    return [
        f.replace('%s/' % directory, '')
        for f in files]

def resize_all(extension='.jpg'):
    # does the image resizing
    print "Resizing all imgs..."
    for img in read_files(OUTPUT_DIRECTORY, extension):
        # keeps the name if normal, adds -t before the extension if thumb
        # doesn't overwrite, adds _ before the img name
        ipt = "%s/%s" % (OUTPUT_DIRECTORY, img)
        opt = "%s/%s" % (OUTPUT_DIRECTORY, img)

        with open(ipt, 'r+b') as f:
            with Image.open(f) as image:
                for key, item in get_sizes():
                    w = item.get('w')
                    h = item.get('h')
                    a = item.get('afflix')

                    if w:
                        tmp = resizeimage.resize_width(image, w)
                    if h:
                        tmp = resizeimage.resize_height(image, h)
                    if a:
                        opt = opt.replace(extension, a+extension)
                    print "Saving %s with %s settings..." % (opt, key)
                    tmp.save(opt, image.format)
                    print "Done"


# main
if __name__ == "__main__":

    for pdf in read_files(INPUT_DIRECTORY, '.pdf'):
        # pdf is the relative filename
        img = pdf.replace('.pdf', '')
        print "Converting %s to %s.jpg" % (pdf, img)
        convert(pdf, img)

    # resize the output
    resize_all()
