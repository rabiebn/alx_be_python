## Writing Unit Tests for a Simple Calculator Class

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 2), 12)
        self.assertEqual(self.calc.add(22, 2), 24)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(2, -5), -10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(50, 5), 10)
        self.assertIsNone(self.calc.divide(1, 0))
