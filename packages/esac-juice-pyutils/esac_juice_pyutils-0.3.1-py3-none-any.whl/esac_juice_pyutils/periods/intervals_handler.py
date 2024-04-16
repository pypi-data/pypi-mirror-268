"""
Created on October, 2018

@author: Claudio Munoz Crego (ESAC)

Class to handle list of intervals
"""

import numpy as np


class IntervalHandlers(object):
    """
    This class allows to handle list of intervals where periods are list of [start, end] numbers
    """

    def __init__(self):
        pass

    def intervals_clean(self, intervals, max_gap=0, min_interval=0):
        """
        Clean a list of intervals removing intervals <= min_interval and if gaps < max_gap join intervals

        :param intervals: list of interval
        :param max_gap: The maximum acceptable gap between values;
        Consecutive values with Intervals smaller than max_gaps will be combined into a single interval.
        Default: 0   (any gap keeps intervals separate)
        :param min_interval: The smallest acceptable interval;
        Any interval smaller is discarded; Default: 0   (all intervals are accepted)
        :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
        """

        import copy
        list_of_intervals = copy.deepcopy(intervals)

        n = len(list_of_intervals) - 1
        for i in range(n, 0, -1):
            if list_of_intervals[i][0] - list_of_intervals[i - 1][1] < max_gap:
                list_of_intervals[i - 1] = [list_of_intervals[i - 1][0], list_of_intervals[i][1]]
                list_of_intervals.pop(i)

        list_of_intervals = [interval for interval in list_of_intervals if (interval[1] - interval[0]) > min_interval]

        return list_of_intervals

    def substract_intervals(self, a, b, start=None, end=None):
        """
        Substract intervals

        A - B = intersection(A, Not B)
        :param a: list of interval
        :param b: list of intervals to substract
        :return:
        """

        if len(b) == 0 or len(a) == 0:
            return a

        if b[0][0] > a[0][0]:
            start = a[0][0]
        if b[-1][1] > a[-1][1]:
            end = a[-1][1]

        result = overlaps(a, self.not_intervals(b, start=start, end=end))

        return result

    def not_intervals(self, intervals, start=None, end=None):
        """
        Get the complementary of a given list os intervals [start0, end0],...]
        If absolute start/end values of interval is provided, the corresponding interval is included

        :param intervals: list of intervals
        :param start: absolute start value of intervals; default None
        :param end: absolute end value of intervals; default None
        :return: not_events: list of intervals
        """
        not_events = []
        for i in range(len(intervals[:-1])):
            not_events.append([intervals[i][1], intervals[i+1][0]])

        if len(not_events) == 0 and len(intervals) != 1:
            if start is not None and end is not None:
                not_events = [[start, end]]
        else:
            if start is not None:
                if start <= intervals[0][0]:
                    not_events.insert(0, [start, intervals[0][0]])

            if end is not None:
                if end >= intervals[-1][1]:
                    not_events.append([intervals[-1][1], end])

        return not_events

    def merge_intervals(self, list_of_intervals):
        """
        Merge list of intervals [[start0, end0]...]

        :param list_of_intervals:
        :return:
        """

        from operator import itemgetter

        if not list_of_intervals:
            return []

        intervals = sorted(list_of_intervals, key=itemgetter(0))

        count = 0
        for p in intervals:
            (start, end) = tuple(p)
            if start > intervals[count][1]:
                count += 1
                intervals[count] = p
            elif end > intervals[count][1]:
                intervals[count] = [intervals[count][0], end]

        return intervals[:count + 1]


def get_overlap_2(interval_1, interval_2):
    """
    Get intervals overlaps between interval_1 and interval_2

    :param interval_1: interval
    :param interval_2: interval
    :return: interval overlap if exists else None
    """

    overlap_start = max(interval_1[0], interval_2[0])
    overlap_end = min(interval_1[1], interval_2[1])

    if overlap_end >= overlap_start:
        return [overlap_start, overlap_end]
    else:
        return None


def overlaps_2(events_1, events_2):
    """
    Generate list of overlap periods between event periods 1 and 2

    :param events_1: list of periods
    :param events_2: list of periods
    :return: events_overlap, list of all overlap; Can be an empty list
    """

    events_overlap = []
    for ev1 in events_1:
        for ev2 in events_2:
            if ev2[0] > ev1[1]:
                break
            ev_overlap = get_overlap_2(ev1, ev2)
            if ev_overlap is not None:
                events_overlap.append(ev_overlap)

    return events_overlap


def overlaps(events_1, events_2):
    """
    Generate list of overlap periods between event periods 1 and 2

    :param events_1: list of periods
    :param events_2: list of periods
    :return: events_overlap, list of all overlap; Can be an empty list
    """

    events_overlap = []
    for [s1, e1] in events_1:
        for [s2, e2] in events_2:
            if s2 > e1:
                break
            elif e2 < s1:
                continue

            # ev_overlap = get_overlap(s1, e1, s2, e2)
            # if ev_overlap is not None:
            #     events_overlap.append(ev_overlap)

            overlap_start = max(s1, s2)
            overlap_end = min(e1, e2)
            if overlap_end >= overlap_start:
                events_overlap.append([overlap_start, overlap_end])

    return events_overlap


def get_overlap(interval_1_start, interval_1_end, interval_2_start, interval_2_end):
    """
    Get intervals overlaps between interval_1 and interval_2

    :param interval_1_start: interval
    :param interval_2: interval
    :return: interval overlap if exists else None
    """

    overlap_start = max(interval_1_start, interval_2_start)
    overlap_end = min(interval_1_end, interval_2_end)

    if overlap_end >= overlap_start:
        return [overlap_start, overlap_end]
    else:
        return None
