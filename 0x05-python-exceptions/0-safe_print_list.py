#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while True:
            if i == x:
                break
            print(my_list[i], end=' ')
            i += 1
    except IndexError:
        pass
    finally:
        print("Finally")
    return i
