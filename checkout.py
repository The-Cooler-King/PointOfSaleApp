# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
from validation import validate_clerk_input

items = []

while True:

    item_id_input = input("Please enter item identifier: ")
    if validate_clerk_input(item_id_input):
        if item_id_input == 'DONE':
            break
        else:
            items.append(item_id_input)
    else:
        print ("That is an invalid product identifier. You are fired!")

print (items)


