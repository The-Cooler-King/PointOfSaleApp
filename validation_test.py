# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:47:51 2021

@author: vjham
"""


from validation import is_clerk_input_valid
import unittest
from unittest import TestCase


class TestValidation(TestCase):
    
    #happy path section
    
    def test_is_clerk_input_valid_valid_product_id_string(self):
        clerk_input = "1"
        self.assertEqual(is_clerk_input_valid(clerk_input), True)
    
    def test_is_clerk_input_valid_done_allcaps(self):
        clerk_input = "DONE"
        self.assertEqual(is_clerk_input_valid(clerk_input), True)
    
    #unhappy path section
    
    def test_is_clerk_input_valid_valid_product_id_integer(self):
        clerk_input = 1
        self.assertEqual(is_clerk_input_valid(clerk_input), False)
    
    def test_is_clerk_input_valid_invalid_product_id_string(self):
        clerk_input = "30"
        self.assertEqual(is_clerk_input_valid(clerk_input), False)
    
    def test_is_clerk_input_valid_invalid_product_id_integer(self):
        clerk_input = 30
        self.assertEqual(is_clerk_input_valid(clerk_input), False)
    
    def test_is_clerk_input_valid_random_string(self):
        clerk_input = "invalid"
        self.assertEqual(is_clerk_input_valid(clerk_input), False)
    
    def test_is_clerk_input_valid_done_lowercase(self):
        clerk_input = "done"
        self.assertEqual(is_clerk_input_valid(clerk_input), False)
        
if __name__ == '__main__':
    unittest.main()