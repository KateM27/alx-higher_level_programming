#!/usr/bin/python3
def max_integer(my_list=[]):
    lst = len(my_list)

    if lst > 0:
        my_list.sort()
        return my_list[-1]
    else:
        return None
