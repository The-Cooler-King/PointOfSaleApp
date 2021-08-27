# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""

items = []
GROCERY_STORE_NAME = "Shop N Bag"
while True:

    item_id_input = input("Please enter item identifier: ")
    if item_id_input == 'DONE':
        break
    items.append(item_id_input)


def create_custom_receipt():
    dashes = "--------------------------------"
    return dashes + "\n" + GROCERY_STORE_NAME + "\n" + dashes


receipt = create_custom_receipt()
print(receipt)