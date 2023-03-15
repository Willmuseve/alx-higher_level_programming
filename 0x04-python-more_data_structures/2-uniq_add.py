#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a new set to store unique integers
    unique_integers = set()
    
    # Loop over each element of the input list
    for element in my_list:
        # If the element is an integer and not already in the set, add it to the set
        if isinstance(element, int) and element not in unique_integers:
            unique_integers.add(element)
    
    # Compute the sum of the unique integers
    result = sum(unique_integers)
    
    # Return the result
    return result
