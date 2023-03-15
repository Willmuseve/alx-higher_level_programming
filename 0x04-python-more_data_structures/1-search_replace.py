#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the result
    result = []

    # Loop over each element of the input list
    for element in my_list:
        # If the element matches the search value, replace it with the new value
        if element == search:
            result.append(replace)
        else:
            result.append(element)

    # Return the new list
    return result
