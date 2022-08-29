#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    lst = len(my_list)

    if 0 <= idx < lst:
        my_list[idx] = element
        return my_list
    else:
        return my_list
