#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    listx = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > listx:
            listx = my_list[i]

    return (listx)
