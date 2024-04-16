#!/usr/bin/python
"""
Created on September 20, 2016

@author: cmunoz

This file includes common data and time functions using spiceypy python package for data and time handling

"""

import datetime
import logging
import spiceypy as spi


def et2utc(e_time_isoc_format_string, format="%d-%b-%Y_%H:%M:%S"):
    """
    Translate etime in "ISOC" string format "1987-04-12T16:31:12.814", with 3 dec seconds,
    :param e_time_isoc_format_string: ephemeris time in ISOC format
    :param format: UTC sting format
    :return utc_string utc string format "01-JAN-2016_10:20:00"
    :rtype string
    """

    s_time = spi.et2utc(e_time_isoc_format_string, "ISOC", 3, 25)
    c_time = datetime.datetime.strptime(s_time, '%Y-%m-%dT%H:%M:%S.%f')
    utc_string = datetime.datetime.strftime(c_time, format).upper()

    return utc_string


def et2datetime(e_time, format='%Y-%m-%dT%H:%M:%S.%f'):
    """
    Translate ephemeris time to datetime
    :param e_time: ephemeris time
    :param format: UTC sting format
    :return: c_time datetime
    """

    s_time = spi.et2utc(e_time, "ISOC", 3, 25)
    c_time = datetime.datetime.strptime(s_time, format)

    return c_time
