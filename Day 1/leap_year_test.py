import unittest
from unittest.case import TestCase
from leap_year import *

class test_leap_year(unittest.TestCase):
    def test_is_divisible_by_4(self):
        self.assertEqual(year % 4, 0)

    def test_is_divisible_by_100(self):
        self.assertEqual(year % 100, 0)

    def test_is_divisible_by_400(self):
        self.assertEqual(year % 400, 0)

if __name__ == '__main__':
    unittest.main()
