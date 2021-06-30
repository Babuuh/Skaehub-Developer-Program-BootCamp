import unittest
from duplicate_remover import *

class test_duplicates(unittest.TestCase):
    def test_data(self):
        self.assertEqual(type(my_list), list,"should be list")

    def test_data2(self):
        self.assertEqual(type(list2), list,"should be dict")

    def test_duplicate(self):
        self.assertNotEqual(my_list,list2,"should not be equal")


if __name__=="__main__":
    unittest.main()