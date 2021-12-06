#!/usr/bin/env python3
from os import path
import argparse
from thothlibrary import ThothClient

# from pdf import Pdf
# from img import Img

MAP = {'royaloctavo' : {'width': 156.0,
                        'height': 234.0,
                        'geometry': [748, 9, 1190, 672]},
       'a4'          : {'width': 210.0,
                        'height': 297.0,
                        'geometry': [892, 9, 1487, 851]},
       '7x10'        : {'width': 178.0,
                        'height': 254.0,
                        'geometry': [264, 3, 441, 257]}
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

    
    for size, data in MAP.items():
        if data['width'] == query['width'] and \
           data['height'] == query['height']:
            geometry = data['geometry']
            break
    else:
        raise 'Size not found in MAP'

    print(geometry)

    # config = Config(config_path, cover_type=args.cover_type)

    # pdf = Pdf(pdf_path)
    # pdf.set_cropbox(config.get_cover_geometry())

    # img = Img(pdf.cover.name, output_folder=out_folder)
    # img.convert(args.output_width)


if __name__ == '__main__':
    main()
