# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
from validation import validate_clerk_input

items = []

while True:

    item_id_input = input("Please enter item identifier: ")
    validated_item_id_input = validate_clerk_input(item_id_input)
    if validated_item_id_input == 'DONE':
        break
    items.append(validated_item_id_input)

print (items)


