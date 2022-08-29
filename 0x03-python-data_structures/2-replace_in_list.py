#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    lst = len(my_list)
    if idx < 0:
        return my_list
    elif idx > lst - 1:
        return my_list
    my_list[idx] = element
    return my_list
