#!/usr/bin/python3

import pathlib
import unittest

import main

class TestMainScript(unittest.TestCase):

    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_build(self):
        main.main()
        self.assertIsFile('build/index.html')


if __name__ == '__main__':
    unittest.main()