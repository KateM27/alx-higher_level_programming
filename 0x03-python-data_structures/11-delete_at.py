#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lst = len(my_list)

    if idx < 0 and idx > lst:
        return my_list
    del my_list[idx]
    return my_list
