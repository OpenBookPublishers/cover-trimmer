#!/usr/bin/env python3
import fitz


class Pdf:
    '''
    PDF class to handle input PDFs

    This class gets a PDF file as input and offers methods to crop the
    front cover.
    '''

    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)

    def set_cropbox(self, out_pdf_path, rect):
        x0, y0, x1, y1 = rect

        page = self.doc.loadPage(0)
        page.set_cropbox(fitz.Rect(x0, y0, x1, y1))

        self.doc.save(out_pdf_path)
