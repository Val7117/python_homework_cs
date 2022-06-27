#!/usr/bin/env python3

def n_arr(array):
    length = len(array)
    if length == 1:
        num_of_elem = array[0]
        blue_print = [""] * num_of_elem
        return blue_print
    elif length == 2:
        num_of_elem = array[0]
        num_of_selem = array[1]
        blue_print = [[""] * num_of_elem for i in range(num_of_selem)]
        return blue_print
    elif length > 2:
        num_of_elem = array[0]
        num_of_selem = array[2]
        blue_print = [[""] * num_of_elem for i in range(num_of_elem)]
        res = [blue_print for j in range(num_of_selem)]
        for i in array[3:]:
            key = [res for k in range(i)]
            res = key
        return res
