#!/usr/bin/env python3
import fitz
import tempfile
from pdf2image import convert_from_path

class Trimmer:
    '''
    Class for trimming PDF cover artwork to output images (JPEG files) of the
    front cover.

    This class gets a PDF file as input and offers methods to set the cropbox
    to the size of the front cover. Lastly, this class offers method to trim
    the PDF to the cropbox size and export the result to jpeg format with
    specified width.
    '''

    def __init__(self, pdf_path, output_folder=''):
        self.doc = fitz.open(pdf_path)
        self.output_folder = output_folder

        self.cover = tempfile.NamedTemporaryFile()

    def set_cropbox(self, rect):
        x0, y0, x1, y1 = rect

        page = self.doc.loadPage(0)
        page.set_cropbox(fitz.Rect(x0, y0, x1, y1))

        self.doc.save(self.cover.name)

    def convert(self, width, prefix='cover-', postfix='-RGB'):
        file_name = f'{prefix}{width}px{postfix}'

        convert_from_path(self.cover.name,
                          single_file=True,
                          output_folder=self.output_folder,
                          use_cropbox=True,
                          size=(None, width),
                          fmt='jpg',
                          output_file=file_name)
