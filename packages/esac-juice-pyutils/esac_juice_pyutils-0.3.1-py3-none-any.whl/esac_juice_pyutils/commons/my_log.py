#!/usr/bin/python
"""
Created on March 31, 2017

@author: Claudio Munoz Crego (ESAC)

This Module define the log format
"""

import os
import logging
import sys


def setup_logger(level='info'):
    """
    Setup logging level
    :param level: logger level define in ['info', 'debug']. Default value is 'info'.
    """

    # home = os.getenv("HOME")
    logging_level = logging.INFO
    logging_format = '%(asctime)s[%(levelname)s]: %(message)s'
    logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

    if level == 'debug':
        logging_level = logging.DEBUG
        logging_format = '%(asctime)s[%(module)s.%(funcName)s][%(levelname)s]: %(message)s'
        # logging_format = '%(asctime)s[%(module)s][%(levelname)s]: %(message)s'
        logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

        print('\nreset log level to "{}"'.format(level))

    logging.basicConfig(level=logging_level,
                        # filename='a.log',
                        stream=sys.stdout,
                        format=logging_format,
                        datefmt=logging_datefmt)


def setup_logger_standard_output_and_file(log_file, level='debug'):
    """
    Setup logging level and log file

    1) Set log level for standard output
    2) Set up logging to file
    3) Add the handler to the root logger


    :param level: logger level define in ['info', 'debug']. Default value is 'info'.
    :param log_file:
    :param level:
    :return:
    """

    logging_level = logging.INFO
    logging_format = '%(asctime)s[%(levelname)s]: %(message)s'
    logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

    if level == 'debug':
        logging_level = logging.DEBUG
        logging_format = '%(asctime)s[%(module)s.%(funcName)s][%(levelname)s]: %(message)s'
        logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

        print('\nreset log level to "{}"'.format(level))

    f_handler = logging.FileHandler(log_file)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter(logging_format)
    f_handler.setFormatter(f_format)
    logging.getLogger('').addHandler(f_handler)

    logging.warning('Start')

    console = logging.StreamHandler()
    console.setLevel(logging_level)
    formatter = logging.Formatter(logging_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.info('log_file: {}'.format(log_file))


def add_console_logger(level):
    """
    Add log file to logging

    1) Set log level for standard output
    2) Set up logging to file
    3) Add the handler to the root logger

    :param log_file:

    """

    logging_format = '%(asctime)s[%(levelname)s]: %(message)s'
    logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

    level = logging.INFO
    if level == 'debug':
        level = logging.DEBUG
        logging_format = '%(asctime)s[%(module)s.%(funcName)s][%(levelname)s]: %(message)s'
        logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

        print('\nreset log level to "{}"'.format(level))

    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter(logging_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def add_log_file_logger(log_file):
    """
    Add log file to logging

    1) Set log level for standard output
    2) Set up logging to file
    3) Add the handler to the root logger

    :param log_file:

    """

    if os.path.exists(log_file):
        os.remove(log_file)
        logging.warning('Previous version of log file deleted: {}'.format(log_file))

    logging_format = '%(asctime)s[%(module)s.%(funcName)s][%(levelname)s]: %(message)s'

    f_handler = logging.FileHandler(log_file)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter(logging_format)
    f_handler.setFormatter(f_format)
    logging.getLogger('').addHandler(f_handler)

    logging.info('log_file: {}'.format(log_file))
