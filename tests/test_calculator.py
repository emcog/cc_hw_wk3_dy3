import unittest
from src.calculator import *


class TestCalulator(unittest.TestCase):

    def test_convert_string_to_int(self):
        self.assertEqual((2, 2), str_to_int('2', '2'))

    def test_convert_int_to_str(self):
        self.assertEqual('2', int_to_str(2))


    # def test_add(self):
    #     self.assertEqual(4 , add(2, 2))
    
    # def test_subtract(self):
    #     self.assertEqual(0, subtract(2, 2))

    # def test_divide(self):
    #     self.assertEqual(1, divide(2, 2))

    # def test_multiply(self):
    #     self.assertEqual(8, multiply(2,4))