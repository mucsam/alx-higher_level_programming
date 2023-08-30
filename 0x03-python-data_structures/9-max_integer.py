#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maxim = my_list[0]
        for item in my_list:
            if item > maxim:
                maxim = item
        return maxim
