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
from compare_files import FileCompareByLine


if __name__ == '__main__':

    from cjmc_pyutils.commons.my_log import setup_logger

    #setup_logger('debug')
    setup_logger()
    print('local directory = ', os.getcwd())

    print('\n-----------------------------------------------\n')
    logging.debug('start test')

    filename_1 = 'final_states.out'
    filename_2 = 'final_states_2.out'

    # p1 = StringListHandler()
    # list1 = p1.read_file(filename_1, mask=[r'^#', '^\r?\n'], select=False)
    # p2 = StringListHandler()
    # list2 = p2.read_file(filename_2, mask=[r'^#', '^\r?\n'], select=False)
    #
    # d = difflib.Differ()
    # print('list1 = {}', p1.my_lines)
    # print('list2 = {}', p2.my_lines)
    #
    # # get only 6 first decimal of float number
    # list1 = p1.round_float_filter(nb_digit=6)
    # list2 = p2.round_float_filter(nb_digit=6)
    # res = d.compare(list1, list2)
    #
    # # Get only differences; that is line with differences (the ones starting by "-", "+", or "?")
    # smask = r'^[-+?]'
    # res = [lines for lines in list(res) if re.search(smask, lines)]
    #
    # if len(res) == 1:
    #     print '\n# Difference(s) in one line'
    #     print ''.join(res)
    # elif len(res) > 1:
    #     print '\n#There are {} differences'.format(len(res))
    #     print ''.join(res)
    # else:
    #     print '\n#There are no differences'
    #
    # print('\n-----------------------------------------------\n')

    # fcp = FileCompareByLine(filename_1, filename_2)
    # fcp.load_files()
    # fcp.apply_round_float_filter(2)
    # fcp.report()

    # fcp = FileCompareByLine(filename_2, filename_2)
    # fcp.load_files()
    # fcp.apply_round_float_filter(2)
    # fcp.report()
    #
    # fcp = FileCompareByLine(filename_1, filename_2)
    # fcp.load_files()
    # fcp.apply_round_float_filter(2)
    # fcp.report()
    #
    # fcp = FileCompareByLine(filename_2, filename_2)
    # fcp.load_files()
    # fcp.apply_round_float_filter(2)
    # print 'status: ', fcp.compare()

    base_dir = os.path.expandvars('$HOME/JUICE_SO/MAPPS/REGRESSION_TEST')
    dir_1 = 'REF_DATA/Europa_flyby_CDR_crema_3_1_2018/eps_output'
    dir_2 = 'output/Europa_flyby_CDR_crema_3_1_2018/eps_output'
    # dir_2 = 'TEST_DATA_SET/Jupiter_perijove_2018/eps_output'

    print ('# Comparing {} against {}'.format(dir_1, dir_2))

    dir_2 = os.path.join(base_dir, dir_2)
    dir_1 = os.path.join(base_dir, dir_1)
    # dir_1 = os.path.join(base_dir, 'REF_DATA/Europa_flyby_CDR_crema_3_1_2018/eps_output')

    dir1_list_of_files = os.listdir(dir_1)
    dir2_list_of_files = os.listdir(dir_2)

    logging.info(dir1_list_of_files)
    logging.info(dir2_list_of_files)

    filename_1 = os.path.join(dir_1, 'modes.out')
    filename_2 = os.path.join(dir_2, 'modes.out')
    fcp = FileCompareByLine(filename_1, filename_2)
    fcp.load_files()
    fcp.apply_round_float_filter(2)
    fcp.report()

    for f in dir2_list_of_files:

        filename_2 = os.path.join(dir_2, f)
        print(filename_2)

        if f in dir2_list_of_files:
            filename_1 = os.path.join(dir_1, f)

            fcp = FileCompareByLine(filename_1, filename_2)
            fcp.load_files()
            status = fcp.compare()

            if status:
                logging.info('File {}: No diffs!'.format(f))
            else:
                logging.info('File {}: Nb diffs = {}!'.format(f, len(fcp.res)))
                fcp.report(nb_lines=10)