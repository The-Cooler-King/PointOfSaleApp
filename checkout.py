# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""

items = []
grocery_store_name = "Shop N Bag"
while True:

    item_id_input = input("Please enter item identifier: ")
    if item_id_input == 'DONE':
        break
    items.append(item_id_input)

print(grocery_store_name)



