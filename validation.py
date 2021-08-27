# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:26:19 2021

@author: vjham
"""

from product_list import ProductService


def validate_clerk_input(clerk_input):
    
    list_of_valid_product_ids = [str(product['id']) for product in ProductService.products]
    
    if clerk_input in list_of_valid_product_ids or clerk_input == 'DONE':
        return True
    else:
        return False