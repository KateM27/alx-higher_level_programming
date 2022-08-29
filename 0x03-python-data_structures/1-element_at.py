#!/usr/bin/python3
def element_at(my_list, idx):
    element = len(my_list)
    if idx < 0:
        return None
    elif idx > element - 1:
        return None
    else:
        return (my_list[idx])
