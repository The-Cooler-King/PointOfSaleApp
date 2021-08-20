# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:26:19 2021

@author: vjham
"""

from product_list import products


def validate_clerk_input(clerk_input):
    
    list_of_valid_product_ids = [str(product['id']) for product in products]
    
    if clerk_input in list_of_valid_product_ids:
        return clerk_input
    elif clerk_input.upper() == 'DONE':
        return_value = clerk_input.upper()
        return return_value
    else:
        amended_clerk_input = input("You entered an invalid input. Try again or enter 'DONE' to generate the final receipt: ")
        return validate_clerk_input(amended_clerk_input)