#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = 0
        div_2 = 0

        for tup in my_list:
            num += tup[0] * tup[1]
            div_2 += tup[1]
        return num / div_2
    else:
        return 0
