"""
Created on September 21, 2018

@author: Claudio Munoz Crego

This file includes common method to parse strings

"""

import os
import sys
import re
import logging


def round_float(my_string, nb_digit=2):
    """
    Round float to a given number of digits in the string

    "3.14159265 and 99.999; .000001" --> 3.14 and 100.00; 0.00'
    :param nb_digit: number of digit to round float values
    :param my_string: a given string
    :return: string with rounded float (if any)
    """

    simpledec = re.compile(r"\d*\.\d+")

    my_format = '{:.' + str(nb_digit) + 'f}'
    # print my_format

    def mround(match):
        return my_format.format(float(match.group()))

    return re.sub(simpledec, mround, my_string)


def trunc_float(my_string, nb_digit=2):
    """
    Trunc float to a given number of digits in the string

    "3.14159265 and 99.999; .000001" --> 3.14 and 99.99; 0.00
    :param nb_digit: number of digit to trunc float values
    :param my_string: a given string
    :return: string with rounded float (if any)
    """

    my_decimal = re.compile(r"\d*\.\d+")
    print(my_decimal)

    my_format = '{:.' + str(nb_digit) + 'f}'
    my_digit_pow = float(10 ** nb_digit)

    def mtrunc(match):
        return my_format.format(int(float(match.group()) * my_digit_pow) / my_digit_pow)

    return re.sub(my_decimal, mtrunc, my_string)
