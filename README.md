# pdf-to-img
Simple utility to convert PDF to IMG using Ghostscript and Python


## requirements
python 2.7

ghostscript

python-resize-image

pillow


## installation
Fetch the `ghostscript` python dependency by running:

    $ brew install ghostscript

For the `pip` dependencies, run:

    $ pip install -r requirements.txt

*Create a virtualenv for the previous step if you like*


## usage
1. Dump your PDF files inside the `input` folder
2. Run:

    $ ./pdf2img

3. Collect your output PNG files from the `output` folder

[optional] If you need a particular setting or set of, copy `_conf.py` in `conf.py` and modify it as you need. Instructions inside.
