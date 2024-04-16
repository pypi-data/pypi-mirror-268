"""
Created on September 21, 2018

@author: Claudio Munoz Crego

This file includes common compare files functions using

"""


import os
import re
import sys
import logging
import difflib

from esac_juice_pyutils.files.string_handler import *


class StringListHandler(object):
    """
    Contains method to compare two files line by line applying filters
    """

    def __init__(self):

        self.my_lines = []

    def read_file(self, file_path_name, mask=[r'^#', '^\r?\n'], select=False):
        """
        Read file and return it as a list of string (one per line)
        A "mask" can be provided.

        Default values are:
        - not select comments (line staring by #);  mask=[r'^#'] and select=False
        - not select blank line; mask=['^\r?\n'] and select=False

        :param file_path_name: path of the input file
        :param mask: re mask format
        :param select: Flag to indicate if the lines matching with mask must be selected or not.
        :return: list of lines
        """

        if not os.path.exists(file_path_name):
            logging.error('path "{}" does not exist!'.format(file_path_name))
            sys.exit()

        f = open(file_path_name, 'r')

        self.my_lines = f.readlines()

        self.my_lines = self.mask_filter(mask, select)

        return self.my_lines

    def mask_filter(self, mask=[], select=False):
        """
        Parse a list of string according to a given "mask"

        Typical values are:
        - not select comments (line staring by #);  mask=[r'^#'] and select=False
        - not select blank line; mask=['^\r?\n'] and select=False

        :param mask: re mask format
        :param select: Flag to indicate if the lines matching with mask must be selected or not.
        :return: list of lines
        """

        if select:
            for my_filter in mask:
                self.my_lines = [line for line in self.my_lines if re.search(my_filter, line)]
        else:
            for my_filter in mask:
                self.my_lines = [line for line in self.my_lines if re.search(my_filter, line) is None]

        return self.my_lines

    def round_float_filter(self, nb_digit):
        """
        Round float to a given number of digits in the string of the list

        For instance with nb_digit=2 all float are rounded to 2 decimals
        "3.14159265 and 99.999; .000001" --> 3.14 and 100.00; 0.00'

        :param nb_digit: number of digit to round float values
        :param my_string: a given string
        :return: string with rounded float (if any)
        """

        self.my_lines = [round_float(line, 6) for line in self.my_lines]

        return self.my_lines

    def trunc_float_filter(self, nb_digit):
        """
        Trunc float to a given number of digits in the string of the list

        For instance with nb_digit=2 all float are rounded to 2 decimals
        "3.14159265 and 99.999; .000001" --> 3.14 and 99.99; 0.00

        :param nb_digit: number of digit to trunc float values
        :param my_string: a given string
        :return: string with rounded float (if any)
        """

        self.my_lines = [trunc_float(line, nb_digit) for line in self.my_lines]

        return self.my_lines
