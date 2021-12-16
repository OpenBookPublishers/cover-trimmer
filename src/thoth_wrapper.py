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
        raise ValueError('Cover size is not defined in Thoth (blank fields).')


    for size, data in MAP.items():
        if data['width'] == query['width'] and \
           data['height'] == query['height']:
            geometry = data['geometry']
            break
    else:
        message = 'Width: {}\n'.format(query['width']) + \
                  'Height: {}\n'.format(query['height']) + \
                  'Dimensions retrieved from Thoth do not match ' + \
                  'local presets mapped in MAP. Dimensions defined in ' + \
                  'Thoth are either incorrect or not yet supported by ' + \
                  'this software.'

        if query['width'] > query['height']:
            message += '\n\nNOTE: width value greater than height.'

        raise ValueError(message)

    trimmer = Trimmer(pdf_path, output_folder=out_folder)
    trimmer.set_cropbox(geometry)
    trimmer.convert(args.output_width)


if __name__ == '__main__':
    main()
