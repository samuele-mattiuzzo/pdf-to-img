# pdf-to-img
Simple utility to convert PDF to IMG using ImageMagick and Python


## requirements
python 2.7

imagemagick

python-resize-image

pillow

bash

## installation
Fetch the `imagemagick` bash dependency by running:

    $ brew update
    $ brew install imagemagick

For the `pip` dependencies, run:

    $ pip install -r requirements.txt

*Create a virtualenv for the previous step if you like*


## usage
1. Dump your PDF files inside the `input` folder
2. Run:

    $ ./pdf2img

3. Collect your output JPG files from the `output` folder

[optional] If you need a particular setting or set of, copy `_conf.py` in `conf.py` and modify it as you need. Instructions inside.
