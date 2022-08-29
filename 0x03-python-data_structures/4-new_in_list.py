#!/usr/bin/python
def new_in_list(my_list, idx, element):
    lst = len(my_list)
    new_list = my_list.copy()

    if idx < 0 or idx > lst - 1:
        return my_list

    new_list[idx] = element
    return new_list
