# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""

from shopping_cart import products


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

items = []

print("Enter 'DONE' at anytime to generate the final receipt.")

while True:

    item_id_input = input("Please enter item identifier: ")
    validated_item_id_input = validate_clerk_input(item_id_input)
    if validated_item_id_input == 'DONE':
        break
    items.append(validated_item_id_input)

print (items)


