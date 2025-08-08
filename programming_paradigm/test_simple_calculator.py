## Writing Unit Tests for a Simple Calculator Class

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        result = SimpleCalculator.add(self, 10, 3)
        self.assertEqual(result, 13)

    def test_subtract(self):
        result = SimpleCalculator.subtract(self, 10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = SimpleCalculator.divide(self, 6, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        result = SimpleCalculator.divide(self, 6, 0)
        self.assertRaises(ZeroDivisionError)
