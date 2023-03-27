#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    try:
        while i < list_length:
            try:
                y = my_list_1[i] / my_list_2[i]
            except TypeError:
                print('wrong type')
                y = 0
            except ZeroDivisionError:
                print('division by 0')
                y = 0
            except IndexError:
                print('out of range')
                y = 0
            finally:
                result.append(y)
                i += 1
    finally:
        return result

