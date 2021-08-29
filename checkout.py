# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
from validation import is_clerk_input_valid

items = []
GROCERY_STORE_NAME = "Shop N Bag"

while True:

    item_id_input = input("Please enter item identifier: ")
    if is_clerk_input_valid(item_id_input):
        if item_id_input == 'DONE':
            break
        else:
            items.append(item_id_input)
    else:
        print ("That is an invalid product identifier. You are fired!")

print (items)

def create_custom_receipt():
    dashes = "--------------------------------"
    return dashes + "\n" + GROCERY_STORE_NAME + "\n" + dashes


receipt = create_custom_receipt()
print(receipt)