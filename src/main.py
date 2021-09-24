#!/usr/bin/env python3
from os import path
import argparse

from pdf import Pdf
from img import Img
from config import Config


def main():
    pdf_path = path.abspath('cover.pdf')
    out_folder = path.abspath('out')
    config_path = path.abspath('config.json')

    parser = argparse.ArgumentParser()
    parser.add_argument('cover_type',
                        help='Define the type of cover')
    parser.add_argument('-w', '--output_width',
                        help='Define output image width')
    args = parser.parse_args()

    config = Config(config_path, cover_type=args.cover_type)

    pdf = Pdf(pdf_path)
    pdf.set_cropbox(config.get_cover_geometry())

    img = Img(pdf.cover.name, output_folder=out_folder)
    img.convert(args.output_width)


if __name__ == '__main__':
    main()
