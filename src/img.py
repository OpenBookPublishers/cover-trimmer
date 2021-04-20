#!/usr/bin/env python3
from pdf2image import convert_from_path


class Img:
    '''
    Class to convert pdf covers to jpeg.

    This class offers method to convert pdf covers to jpeg format
    with specified width.
    '''

    def __init__(self, pdf_cover, output_folder):
        self.pdf_cover = pdf_cover
        self.output_folder = output_folder

    def convert(self, width):
        convert_from_path(self.pdf_cover,
                          single_file=True,
                          output_folder=self.output_folder,
                          use_cropbox=True,
                          size=(None, width),
                          fmt='jpg',
                          output_file=f'cover-{width}px')
