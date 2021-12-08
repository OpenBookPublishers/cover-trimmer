#!/usr/bin/env python3
import unittest

# imports for test_set_cropbox()
import fitz
from os import path

# imports for test_convert()
import tempfile
import shutil
import imghdr

from cover_trimmer import Trimmer


class TestTrimmer(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        if path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_set_cropbox(self):
        doc = Trimmer(path.abspath('test/cover.pdf'),
                           output_folder=self.temp_dir)

        doc.set_cropbox([748, 9, 1190, 672])

        new_doc = fitz.open(doc.cover.name)
        new_page = new_doc.loadPage(0)
        self.assertEqual(new_page.rect, fitz.Rect(0.0, 0.0, 442.0, 663.0))
        new_doc.close()

    def test_convert(self):
        front_cover = Trimmer(path.abspath('test/cover-cropped.pdf'),
                              output_folder=self.temp_dir)
        front_cover.doc.save(front_cover.cover.name)

        front_cover.convert(1200, prefix='cover-', postfix='-RGB')

        out_img = path.join(self.temp_dir, 'cover-1200px-RGB.jpg')
        self.assertTrue(path.isfile(out_img))

        self.assertEqual(imghdr.what(out_img), 'jpeg')


if __name__ == '__main__':
    unittest.main()
