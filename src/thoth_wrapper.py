#!/usr/bin/env python3
from os import path
import argparse
from thothlibrary import ThothClient

from cover_trimmer import Trimmer

MAP = {'royaloctavo' : {'width': 156.0,
                        'height': 234.0,
                        'geometry': [748, 9, 1190, 672]},
       'a4'          : {'width': 210.0,
                        'height': 297.0,
                        'geometry': [892, 9, 1487, 851]},
       '7x10'        : {'width': 178.0,
                        'height': 254.0,
                        'geometry': [747, 9, 1251, 728]}
       }

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

    if not query['width'] and \
       not query['height']:
        raise 'Cover size not defined in Thoth'


    for size, data in MAP.items():
        if data['width'] == query['width'] and \
           data['height'] == query['height']:
            geometry = data['geometry']
            break
    else:
        raise 'Size not found in MAP'


    trimmer = Trimmer(pdf_path, output_folder=out_folder)
    trimmer.set_cropbox(geometry)
    trimmer.convert(args.output_width)


if __name__ == '__main__':
    main()
