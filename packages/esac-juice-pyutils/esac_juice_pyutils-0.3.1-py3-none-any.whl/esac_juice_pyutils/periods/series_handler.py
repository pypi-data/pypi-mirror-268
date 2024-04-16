"""
Created on October, 2018

@author: Claudio Munoz Crego (ESAC)

This module is a container included function to handle series (list of numbers)
"""

import sys
import logging


def ranges_of_consecutive_integers_in_list(series):
    """
    Return periods of consecutive integer in a serie of integer

    series: list of numbers
    :return: list of intervals containing consecutive integers
    """
    return series_without_gaps(series, 1)


def gaps(series, max_gap):
    """
    Return gaps in a serie of number

    :param series: list of number;
    :param maxgap: The maximum acceptable gap between values;
    Consecutive values with gap (e - s) > max_gaps are grouped into gaps; Default: series[1] - series[0]
    :return: list of gaps

    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if (e - s > max_gap)]

    Note max_gap must be positive, and actually > dt, thta is the step between consecutive values.
    """
    if max_gap <= 0:
        logging.error('max_gap must be positive!')
        sys.exit()

    series = sorted(series)

    gaps = []
    for s, e in zip(series, series[1:]):
        if e - s > max_gap:
            gaps.append([s, e])

    return gaps


def series_without_gaps(series, max_gap, min_interval=0):
    """
    Return periods of consecutive number in a serie of numbers

    :param series: list of numbers
    :param max_gap: The maximum acceptable gap between values;
    Consecutive values with max_gaps greater are grouped into gaps; Default: series[1] - series[0]
    :param min_interval: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """
    if len(series) == 0:
        return []

    my_gaps = gaps(series, max_gap)
    if len(my_gaps) == 0:
        return [[series[0], series[-1]]]

    intervals = iter(series[:1] + sum(my_gaps, []) + series[-1:])
    list_of_intervals = list(zip(intervals, intervals))
    # if min_interval != 0:
    list_of_intervals = [list(interval) for interval in list_of_intervals if (interval[1] - interval[0]) >= min_interval]
    return list_of_intervals
