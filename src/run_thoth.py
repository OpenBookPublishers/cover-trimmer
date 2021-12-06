#!/usr/bin/env python3
from os import path
import argparse
from thothlibrary import ThothClient

# from pdf import Pdf
# from img import Img


def main():
    pdf_path = path.abspath('cover.pdf')
    out_folder = path.abspath('out')

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doi',
                        help='DOI of the work (registered in Thoth)')
    parser.add_argument('-w', '--output_width',
                        help='Define output image width')
    args = parser.parse_args()

    thoth = ThothClient(version="0.6.0")
    query = thoth.query('workByDoi',
                        {'doi':f'"https://doi.org/10.11647/{args.doi}"'})

    width = query['width']
    height = query['height']

    # config = Config(config_path, cover_type=args.cover_type)

    # pdf = Pdf(pdf_path)
    # pdf.set_cropbox(config.get_cover_geometry())

    # img = Img(pdf.cover.name, output_folder=out_folder)
    # img.convert(args.output_width)


if __name__ == '__main__':
    main()
