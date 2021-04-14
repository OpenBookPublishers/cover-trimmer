#!/usr/bin/env python3
from os import path
from pdf import Pdf


def main():
    # DEV
    pdf_path = path.abspath('test.pdf')
    rect = [748, 9, 1190, 672]

    pdf = Pdf(pdf_path)
    pdf.set_cropbox(rect)


if __name__ == '__main__':
    main()
