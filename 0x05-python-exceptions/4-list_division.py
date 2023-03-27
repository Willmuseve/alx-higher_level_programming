#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    while i < list_length:
        y = 0  # Define quotient before the inner try block
        try:
            y = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            result.append(y)
            i += 1
    return result
