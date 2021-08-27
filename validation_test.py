# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:47:51 2021

@author: vjham
"""


from validation import validate_clerk_input
import unittest
from unittest import TestCase


class TestValidation(TestCase):
    
    #happy path section
    
    def test_validate_clerk_input_valid_product_id_string(self):
        clerk_input = "1"
        self.assertEqual(validate_clerk_input(clerk_input), True)
    
    def test_validate_clerk_input_done_allcaps(self):
        clerk_input = "DONE"
        self.assertEqual(validate_clerk_input(clerk_input), True)
    
    #unhappy path section
    
    def test_validate_clerk_input_valid_product_id_integer(self):
        clerk_input = 1
        self.assertEqual(validate_clerk_input(clerk_input), False)
    
    def test_validate_clerk_input_invalid_product_id_string(self):
        clerk_input = "30"
        self.assertEqual(validate_clerk_input(clerk_input), False)
    
    def test_validate_clerk_input_invalid_product_id_integer(self):
        clerk_input = 30
        self.assertEqual(validate_clerk_input(clerk_input), False)
    
    def test_validate_clerk_input_random_string(self):
        clerk_input = "invalid"
        self.assertEqual(validate_clerk_input(clerk_input), False)
    
    def test_validate_clerk_input_done_lowercase(self):
        clerk_input = "done"
        self.assertEqual(validate_clerk_input(clerk_input), False)
        
if __name__ == '__main__':
    unittest.main()