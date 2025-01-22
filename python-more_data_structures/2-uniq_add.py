#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_int = set(my_list)
    list_total = 0
    for i in add_int:
        list_total += i
    return list_total
