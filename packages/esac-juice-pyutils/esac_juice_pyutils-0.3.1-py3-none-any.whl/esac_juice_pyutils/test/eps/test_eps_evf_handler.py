"""
Created on May, 2022

@author: Claudio Munoz Crego (ESAC)

This Module allows to test functions to handle evf files
"""

import os
import sys
import logging
import numpy as np
import datetime

import spiceypy as spi

import efinder.spot.eps_evf_handler as eps_evf_handler


def create_tmp_evf_file(file_path):
    """
    Create temporal file for test

    :param file_path:
    :return:
    """

    f = open(file_path, 'w')

    lines = ['# EVF Filename; \CEB_Ka_opt_visibility.evf',
             '# Generation Time: 15-Jun-2020 10:46:37',
             'Start_time: 01-March-2026_00:00:00',
             'End_time: 16-April-2027_00:00:00'
             '',
             '# (N events in list)]',
             '',
             '01-Mar-2026_09:31:20 GS_CEB_OPT_Ka_AOC (COUNT = 1)',
             '01-Mar-2026_16:48:47 GS_CEB_OPT_Ka_LOC (COUNT = 1)',
             '02-Mar-2026_10:03:43 GS_CEB_OPT_Ka_AOC (COUNT = 2)',
             '02-Mar-2026_16:03:36 GS_CEB_OPT_Ka_LOC (COUNT = 2)']

    for l in lines:

        f.writelines('{}\n'.format(l))

    f.close()


if __name__ == '__main__':

    from efinder.commons.my_log import setup_logger

    setup_logger('debug')

    logging.info('Start Test')

    tmp_file_path = './CEB_Ka_opt_visibility.evf'
    create_tmp_evf_file(tmp_file_path)

    eps_evf_handler.get_list_of_periods(tmp_file_path)

    # dico = eps_evf_handler.read_eps_events(tmp_file_path)
    #
    # [val_start, val_stop] = list(dico.values())
    # if len(val_start) != len(val_stop):
    #
    #     logging.error('There is no pair of start/end values in SOE evf; Please Check file {}'.format(file_path))
    #     sys.exit()
    #
    # else:
    #
    #     opp_periods = []
    #     for i in range(len(val_start)):
    #         s = datetime.datetime.strftime(val_start[i], '%Y-%m-%dT%H:%M:%S')
    #         e = datetime.datetime.strftime(val_stop[i], '%Y-%m-%dT%H:%M:%S')
    #         opp_periods.append([s, e])

    os.remove(tmp_file_path)

    logging.info('End Test')
