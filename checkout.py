# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
"""
After the clerk indicates there are no more items, the program should print a custom 
receipt on the screen. At this point, the receipt should only include a grocery store 
name of your choice.

"""
items = []
while True:

    item_id_input = input("Please enter item identifier: ")
    if item_id_input == 'DONE':
        break
    items.append(item_id_input)


print (items)
grocery_store_name = "Shop 'N Bag"
print (grocery_store_name)

