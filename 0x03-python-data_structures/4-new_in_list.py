#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    # Check if index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list
    
    # Create a new list with the updated element
    new_list = my_list.copy()
    new_list[idx] = element
    
    return new_list
