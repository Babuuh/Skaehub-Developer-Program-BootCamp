import  unittest 
from unittest.case import TestCase
from password_generator import *

class test_password(unittest.TestCase):
    def test_password_length(self):
        if user_input.lower == 'weak':
            self.assertEqual(len(password), 4)

        elif user_input.lower == 'medium':
            self.assertEqual(len(password), 8)

        elif user_input.lower == 'strong':
            self.assertEqual(len(password), 16)

if __name__ == '__main__':
    unittest.main()