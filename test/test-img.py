#!/usr/bin/env python3
import unittest
from pdf2image import convert_from_path
from os import path
import tempfile
import shutil
import imghdr

from src.img import Img


class TestImg(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.img = Img(path.abspath('test/cover-cropped.pdf'),
                       output_folder=self.temp_dir)

    def tearDown(self):
        if path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_set_cropbox(self):
        width = 1200
        self.img.convert(width)

        out_img = path.join(self.temp_dir, f'cover-{width}px.jpg')
        self.assertTrue(path.isfile(out_img))

        self.assertEqual(imghdr.what(out_img), 'jpeg')
