#!/usr/bin/env python3
from os import path
from pdf import Pdf


def main():
    # DEV
    pdf_path = path.abspath('test.pdf')
    out_pdf_path = path.abspath('out.pdf')
    rect = [748, 9, 1190, 672]

    pdf = Pdf(pdf_path)
    pdf.set_cropbox(out_pdf_path, rect)


if __name__ == '__main__':
    main()
