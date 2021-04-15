#!/usr/bin/env python3
import unittest
from os import path

from src.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config(path.abspath('test/config.json'),
                             'royaloctavo')

    def test___init__(self):
        wrong_path = path.abspath('wrong.txt')
        self.assertRaises(FileNotFoundError, Config,
                          wrong_path, cover_type='royaloctavo')

    def test_get_cover_geometry(self):
        self.assertEqual(self.config.get_cover_geometry(),
                         [748, 9, 1190, 672])

    def test_get_output_width(self):
        self.assertEqual(self.config.get_output_width(),
                         [1200])
