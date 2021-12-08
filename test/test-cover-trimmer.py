#!/usr/bin/env python3
import unittest
import fitz
from os import path

from cover_trimmer import Trimmer


class TestTrimmer(unittest.TestCase):
    def setUp(self):
        self.doc = Trimmer(path.abspath('test/cover.pdf'))

    def test_set_cropbox(self):
        self.doc.set_cropbox([748, 9, 1190, 672])

        new_doc = fitz.open(self.doc.cover.name)
        new_page = new_doc.loadPage(0)
        self.assertEqual(new_page.rect, fitz.Rect(0.0, 0.0, 442.0, 663.0))
        new_doc.close()


if __name__ == '__main__':
    unittest.main()
