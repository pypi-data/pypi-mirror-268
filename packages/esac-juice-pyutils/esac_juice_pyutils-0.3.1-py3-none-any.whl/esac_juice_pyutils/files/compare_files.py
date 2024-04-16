"""
Created on September 21, 2018

@author: Claudio Munoz Crego

This file includes common compare files functions using

"""

import os
import sys
import re
import logging
import difflib
from string_handler import *
from string_list_handler import StringListHandler


class FileCompareByLine(object):
    """
        Allow to compare two ascii file line by line using filters to customize the comparison
    """

    def __init__(self, file_name_1, file_name_2):
        """
        ""
        :param file_name_1: path of file 1
        :param file_name_2: path of file 2 (usually de reference file for comparison)
        """

        self.file_name_1 = file_name_1
        self.file_name_2 = file_name_2

        self.str_list_1 = StringListHandler()
        self.str_list_2 = StringListHandler()

        self.status = None
        self.res = None

    def load_files(self, mask=[r'^#', '^\r?\n'], select=False):
        """
        Load files applying a filter (mask).

        Default values are:
        - not select comments (line staring by #);  mask=[r'^#'] and select=False
        - not select blank line; mask=['^\r?\n'] and select=False

        :param mask: re mask format
        :param select: Flag to indicate if the lines matching with mask must be selected or not.
        """

        logging.debug('Comparing Files line by line: "{}" and "{}"'.format(self.file_name_1, self.file_name_2))

        self.str_list_1.read_file(self.file_name_1, mask, select)
        self.str_list_2.read_file(self.file_name_2, mask, select)

    def apply_round_float_filter(self, nb_digit):
        """
        Comparison filtering: Apply round float to a given number of digits

        :param nb_digit: number of digit to round float values
        """

        self.str_list_1.round_float_filter(nb_digit)
        self.str_list_2.round_float_filter(nb_digit)

    def apply_trunc_float_filter(self, nb_digit):
        """
        Comparison filtering: Trunc float to a given number of digits

        :param nb_digit: number of digit to round float values
        """

        self.str_list_1.trunc_float_filter(nb_digit)
        self.str_list_2.trunc_float_filter(nb_digit)

    def get_filtered_file_1(self):
        return self.str_list_1.my_lines

    def get_filtered_file_1(self):
        return self.str_list_2.my_lines

    def compare(self):
        """
        Compare file
        :return: comparison status
        """

        nb_lines = -1
        if len(self.str_list_1.my_lines) > 1000 or len(self.str_list_2.my_lines) > 1000:

            count = 0
            for i in range(1000):
                if self.str_list_1.my_lines[i] != self.str_list_2.my_lines[i]:
                    count += 1

            if count > 500:  # then limit detailed comparison to 1000
                nb_lines = 1000

        return self.__compare(nb_lines)

    def __compare(self, nb_lines=-1):
        """
        Compare file
        :return: comparison status
        """

        d = difflib.Differ()

        stl1 = ''.join(self.str_list_1.my_lines[:nb_lines])
        stl2 = ''.join(self.str_list_2.my_lines[:nb_lines])
        self.res = list(d.compare(stl1, stl2))
        # Get only differences; that is line with differences (the ones starting by "-", "+", or "?")
        smask = r'^[-+?]'
        res = [lines for lines in self.res if re.search(smask, lines)]

        if len(res) == 0:
            self.status = True
        else:
            self.status = False

        logging.debug('Comparison status: {}'.format(self.status))

        return self.status

    def report(self, only_diff=True, nb_lines=-1):
        """
        Print difference to stdout
        :param only_diff: Flag to get only differences
        :param nb_lines:  number of lines to be print; -1 that means all by default
        :return:
        """

        if self.status is None:
            self.compare()

        res = self.res

        if only_diff:

            # Get only differences; that is line with differences (the ones starting by "-", "+", or "?")
            smask = r'^[-+?]'
            res = [lines for lines in res if re.search(smask, lines)]

            if len(res) == 1:
                print('\n#Difference(s) in one line')
            elif len(res) > 1:
                print('\n#There are {} differences'.format(len(res)))
            else:
                print('{} vs {}: No diff!'.format(self.file_name_1, self.file_name_2))
        else:

            if len(res) >= 1:
                print('\n#There are {} differences'.format(len(res)))

        print(''.join(list(res)[0:nb_lines]))
        for l in list(res)[0:100]:
            print(l)