#!/usr/bin/python3
def roman_to_int(roman_string):

    num, num_x, tmp = 0, 0, 0
    roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if type(roman_string) == str and roman_string is not None:
        for n in roman_string:
            if n in roman_dict:
                num_x = roman_dict[n]
                num += num_x - (tmp * 2) if tmp < num_x else num_x
                tmp = num_x
    return num
