# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
from datetime import datetime
from validation import is_clerk_input_valid

items = []
GROCERY_STORE_NAME = "Shop N Bag"
DATE_AND_TIME = datetime.now()
DATE_TIME_FORMAT = DATE_AND_TIME.strftime("%B %d %Y %H:%M:%S")

while True:

    item_id_input = input("Please enter item identifier: ")
    if is_clerk_input_valid(item_id_input):
        if item_id_input == 'DONE':
            break
        else:
            items.append(item_id_input)
    else:
        print("That is an invalid product identifier. You are fired!")

print(items)

def create_custom_receipt():
    dashes = "--------------------------------"
    return dashes + "\n" + " "*9 + GROCERY_STORE_NAME + "\n\n" + DATE_TIME_FORMAT + "\n" + dashes


receipt = create_custom_receipt()
print(receipt)