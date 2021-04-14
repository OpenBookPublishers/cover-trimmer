#!/usr/bin/env python3
import json


class Config:
    '''
    Class to import config file.

    This class includes the methods to load the json config file and return
    data in appropriate format.
    '''

    def __init__(self, config_path, cover_type):
        self.cover_type = cover_type

        with open(config_path) as json_file:
            self.config = json.load(json_file)

    def get_cover_geometry(self):
        '''
        Get cover geomtry

        This method returns a python list with value to build a
        fitz.rect() object
        '''

        return self.config.get('cover_geometry', {}).get(self.cover_type)

    def get_output_width(self):
        '''
        Get width of image(s) to output

        This method returns a python list of the width of the images to output
        '''

        return self.config.get('output_width')
