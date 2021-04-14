#!/usr/bin/env python3
from os import path
from pdf import Pdf
from img import Img


def main():
    # DEV
    pdf_path = path.abspath('test.pdf')
    rect = [748, 9, 1190, 672]
    out_folder = path.abspath('out')
    widths = [1200]

    pdf = Pdf(pdf_path)
    pdf.set_cropbox(rect)

    img = Img(pdf.cover.name, output_folder=out_folder)
    for width in widths:
        img.convert(width)


if __name__ == '__main__':
    main()
