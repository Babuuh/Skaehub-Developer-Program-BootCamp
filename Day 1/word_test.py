import unittest
from unittest.case import TestCase
from word_length import *


class test_split(unittest.TestCase):
    def test_word(self):
        self.assertEqual(sentence, "should be {}" .format(sentence))

    def test_splitter(self):
        self.assertEqual(sentence.split(), sentence.split())

    def test_last_word(self):
        words = sentence.split()
        last_word = words[-1]
        self.assertEqual((last_word), words[-1])
        

if __name__=="__main__":
    unittest.main()