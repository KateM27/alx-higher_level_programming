#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_dict = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
        }
    rom_sum = 0
    conv_dict = roman_string[::-1]
    max_str = 'I'

    for i in conv_dict:
        if rom_dict[i] >= rom_dict[max_str]:
            max_str = i
            rom_sum += rom_dict[i]
        else:
            rom_sum -= rom_dict[i]
    return rom_sum

