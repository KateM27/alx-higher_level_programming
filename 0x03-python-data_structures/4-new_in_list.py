#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = len(my_list)
    new_list = my_list.copy()

    if 0 <= idx < lst:
        new_list[idx] = element
    return new_list
