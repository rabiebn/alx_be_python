#!/usr/bin/python3

## test

import unittest

def div(a, b):
    return a/b

class TestDiv(unittest.TestCase):

    def test_div_pos(self):
        result = div(3, 9)
        self.assertEqual(result, 1/3)

    def test_div_neg(self):
        result = div(3, -3)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()