# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:26:19 2021

@author: vjham
"""

from product_list import ProductService


def is_clerk_input_valid(clerk_input):
    
    list_of_valid_product_ids = [str(product['id']) for product in ProductService.products]
    
    return clerk_input in list_of_valid_product_ids or clerk_input == 'DONE'