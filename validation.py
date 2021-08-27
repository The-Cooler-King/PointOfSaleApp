# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:26:19 2021

@author: vjham
"""

from product_list import product_IDs


def is_clerk_input_valid(clerk_input):
    
    return clerk_input in product_IDs() or clerk_input == 'DONE'