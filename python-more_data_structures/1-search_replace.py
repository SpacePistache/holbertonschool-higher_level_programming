#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listicus_maximus = []
    for i in my_list:
        if i == search:
            listicus_maximus.append(replace)
        else:
            listicus_maximus.append(i)
    return listicus_maximus
