# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:35:57 2021

@author: vjham
"""
from datetime import datetime
from validation import is_clerk_input_valid

GROCERY_STORE_NAME = "Shop N Bag"
DATE_TIME_FORMAT = "%B %d %Y %H:%M:%S"  # Example: August 29 2021 13:14:55

items = []
date_time = datetime.now()

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
    formatted_date_and_time = date_time.strftime(DATE_TIME_FORMAT)

    return dashes + "\n" \
           + " " * 9 + GROCERY_STORE_NAME + "\n\n" \
           + formatted_date_and_time + "\n" \
           + dashes


receipt = create_custom_receipt()
print(receipt)
