"""
Created on October, 2018

@author: Claudio Munoz Crego (ESAC)

This module is a container included function to handle series (list of numbers)
"""

import os
import sys
import logging
import numpy as np
import copy

from esac_juice_pyutils.periods import series_handler as series
import esac_juice_pyutils.periods.intervals_handler as intervals_handler


def gti_seg_numbers(e_times, max_gap, min_gti=0):
    """
    Return periods of consecutive number in a series of numbers

    :param e_times: list of ephemeris time in ascending order
    :param max_gap: The maximum acceptable gap between values;
    join interval if gaps between 2 consecutive intervals < max_gaps
    :param min_gti: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    return series.series_without_gaps(e_times, max_gap, min_gti)


def gti_seg(e_times, max_gap, min_gti=0, dt=None):
    """
    Return periods of consecutive intervals in a series of numbers
    adding an additional values at the end of each period
    Note: this function must be avoided (comes from original code)

    :param e_times: list of ephemeris time in ascending order
    :param max_gap: The maximum acceptable gap between values;
    join interval if gaps between 2 consecutive intervals < max_gaps
    :param min_gti: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :param dt: interval in seconds
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    if dt is None:
        dt = e_times[1] - e_times[0]

    my_periods = series.series_without_gaps(e_times, max_gap, min_gti)

    my_periods = [[p[0], p[1] + dt] for p in my_periods]

    return my_periods


def gti_trim(e_times, max_gap=0, min_gti=0):
    """
    Normalize a Good Time Interval (GTI) - no overlapping and adjoining

    :param e_times: list of ephemeris time in ascending order
    :param max_gap: The maximum acceptable gap between values;
    join interval if gaps between 2 consecutive intervals < max_gaps
    :param min_gti: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    p = intervals_handler.IntervalHandlers()

    e_times = p.merge_intervals(e_times)
    # logging.debug('etimes: {}'.format(len(e_times)))
    e_times = p.intervals_clean(e_times, max_gap, min_gti)
    # logging.debug('etimes: {}'.format(len(e_times)))

    return e_times


def gti_extend_events(gti, before=0, after=0, center=False):
    """
    Extend all gti time interval

    :param center: Flag: if true git is extended around the centre value
    :param gti: list of ephemeris time in ascending order
    :param before: number of seconds to add before each event
    :param after: number of seconds to add after each event
    :return:
    """

    e_times = copy.deepcopy(gti)

    if center:
        for event in e_times:
            tc = event[0] + (event[1] - event[0])/2.0
            event[0] = tc - before
            event[1] = tc + after
    else:

        for event in e_times:
            event[0] -= before
            event[1] += after

    if before == 0 and after == 0:
        return e_times

    return gti_trim(e_times)


def gti_where(e_times, gti, inverse=False):
    """
    Locate a list of intervals within a Good Time Interval (GTI) array containing e_times
    together with and the corresponding list of index.

    if inverse = True, the return the opposite: that are list of intervals within a GTI array not containing e_times,
    together with and the corresponding list of index.

    :param e_times: list of ephemeris time in ascending order for event 1
    :param gti: list of ephemeris intervals in ascending order for event 2
    :param inverse: optional parameter allowing to return the opposite
    :return: tuple (index_i, ogti[index_i], index_j, o_etimes[index_j])
        - list of index of gti list of intervals [[start0, end0]...] values including a etimes
        - and the corresponding list of gti
        - list of index of e_times falling in a gti list of intervals [[start0, end0]...]
        - and the corresponding list of e_times
    """

    (index, ogti) = gti_where_extended(e_times, gti)[0:2]

    if inverse:
        index = list(set(range(len(gti))) - set(index))
        ogti = [gti[i] for i in index]

    return index, ogti


def gti_where_extended(e_times, gti):
    """
    Locate a list of intervals within a Good Time Interval (GTI) array containing e_times
    together with and the corresponding list of index.

    :param e_times: list of ephemeris time in ascending order for event 1
    :param gti: list of ephemeris intervals in ascending order for event 2
    :return: tuple (index_i, ogti[index_i], index_j, o_etimes[index_j])
        - list of index of gti list of intervals [[start0, end0]...] values including a etimes
        - and the corresponding list of gti
        - list of index of e_times falling in a gti list of intervals [[start0, end0]...]
        - and the corresponding list of e_times
    """

    index_i = []
    index_j = []

    n = len(e_times)

    j_min = 0

    for i in range(len(gti)):

        (s, e) = (gti[i][0], gti[i][1])

        if e_times[j_min] > gti[-1][1]:
            break

        j_range = range(j_min, n)

        for j in j_range:

            t = e_times[j]

            if t < s:
                continue

            elif t > e:
                j_min = j
                break

            index_i.append(i)
            index_j.append(j)

    index_i_uniq = list(set(index_i))

    ogti = [gti[i] for i in index_i_uniq]
    o_etimes = [e_times[j] for j in index_j]
    # ogti = list(itemgetter(*index)(gti))

    return index_i_uniq, ogti, index_j, o_etimes, index_i


def gti_overlap(gti_1, gti_2):
    """
    Merge a Good Time Interval (GTI) - no overlapping and adjoining

    :param gti_1: list of ephemeris time in ascending order for event 1
    :param gti_2: list of ephemeris time in ascending order for event 2

    :return: list of intervals [[start0, end0]...] values
    """

    e_times = intervals_handler.overlaps(gti_1, gti_2)

    return e_times


def gti_overlap_0(gti_1, gti_2, min_gti=0):
    """
    Merge a Good Time Interval (GTI) - no overlapping and adjoining

    here the smallest valid interval is 0 by default, but can be provided.
    - 0 duration events/periods are removed
    - events/periods with duration < min_gti are removed too (default is 0)

    :param gti_1: list of ephemeris time in ascending order for event 1
    :param gti_2: list of ephemeris time in ascending order for event 2
    :param min_gti: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    e_times = intervals_handler.overlaps(gti_1, gti_2)
    p = intervals_handler.IntervalHandlers()
    e_times = p.intervals_clean(e_times, min_interval=min_gti)

    return e_times


def gti_inverse(gti, start=None, end=None):
    """
    Get the complementary of a given list os intervals [start0, end0],...]
    If absolute start/end values of interval is provided, the corresponding interval is included

    :param gti_1: list of ephemeris time in ascending order for event 1
    :param start: absolute start value of intervals; default None
    :param end: absolute end value of intervals; default None
    :return: not_events: list of intervals
    """
    p = intervals_handler.IntervalHandlers()
    e_times = p.not_intervals(gti, start, end)

    return e_times


def gti_merge_0(gti_1, gti_2, max_gap=0, min_gti=0):
    """
    Merge Two Good Time Interval (GTI) - no overlapping and adjoining

    Notes: we normalize a Good Time Interval (GTI) - no overlapping and adjoining
            - 0 duration events/periods are removed
            - events/periods with duration <= min_gti are removed too (default is 0)
            - any gap within two consecutive events/periods <= max_gap is removed.
              This mean join the corresponding consecutive events.


    :param gti_1: list of ephemeris time in ascending order for event 1
    :param gti_2: list of ephemeris time in ascending order for event 2
    :param max_gap: The maximum acceptable gap between values;
    join interval if gaps between 2 consecutive intervals < max_gaps
    :param min_gti: The smallest acceptable interval;
     Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    gti = gti_1 + gti_2

    p = intervals_handler.IntervalHandlers()

    e_times = p.merge_intervals(gti)
    # logging.debug('etimes: {}'.format(len(e_times)))
    e_times = p.intervals_clean(e_times, max_gap, min_gti)
    # logging.debug('etimes: {}'.format(len(e_times)))

    return e_times


def gti_merge(gti_1, gti_2):
    """
    Merge Two Good Time Interval (GTI) as is

    Notes:  we don't normalize the Good Time Interval (GTI)

    :param gti_1: list of ephemeris time in ascending order for event 1
    :param gti_2: list of ephemeris time in ascending order for event 2
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    gti = gti_1 + gti_2

    p = intervals_handler.IntervalHandlers()

    e_times = p.merge_intervals(gti)

    return e_times


def gti_val_X0(e_times, v):
    """
    Return the list of interpolated values of etimes

    :param e_times: ephemeris times
    :param v: values of the functions
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    x = np.array(e_times)
    y = np.array(v)

    nx = len(x)
    ny = len(y)

    ic = np.where((y[:-1][1]*y) <= 0)[0]

    dx = x[ic[1:]] - x[ic]
    dy = y[ic[1:]] - y[ic]

    x0 = x[ic] - y[ic] * dx / dy

    return x0


def gti_val_x0(e_times, v):
    """
    Return periods of consecutive intervals in a series of numbers interpolating the limits (start end of each periods)
    Only v >0 periods are returned

    v(e_times(i)) is the list of values of  the function v

    Note: this is equivalent to the original code from IDL code.

    1) Check both list have the same size
    2) Interpol the cut of v = 0
    3) Select ephemeris time where x > 0
    4) generate GTI periods


    :param e_times: ephemeris times
    :param v: values of the functions
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(v) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(v)))

    dt = float(e_times[1] - e_times[0])

    et = copy.copy(e_times)

    for i in range(nt-1):

        if v[i] * v[i+1] <= 0:

            if v[i] <= 0:

                et[i + 1] = e_times[i] - v[i] * dt / (v[i + 1] - v[i])

            else:

                et[i] = e_times[i] - v[i] * dt / (v[i + 1] - v[i])

    et = [et[i] for i, x in enumerate(v) if x > 0]

    return et


def gti_val_0(e_times, v, margin=0.5):
    """
    Return periods of consecutive intervals in a series of numbers interpolating the limits (start end of each periods)
    Only v >0 periods are returned

    v(etimes(i)) is the list of values of  the function v

    Note: this is equivalent to the original code from IDL code.

    1) Check both list have the same size
    1.1) In case len(etimes) = len(v) = nt == 1: return a single period [[etimes[0], etimes[0]]]
    2) Interpol the cut of v = 0
    3) Select ephemeris time where x > 0
    4) generate GTI periods


    :param e_times: ephemeris times
    :param v: values of the functions;
    :param margin: optional parameters only used if len(etimes) = len(v) = nt == 1; Default is 0.5 seconds
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(v) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(v)))

    if nt == 1:
        margin = 0.5  # seconds
        if v[0] >= 0:
            return [[e_times[0] - margin, e_times[0] + margin]]
        else:
            return []

    dt = float(e_times[1] - e_times[0])

    et = copy.copy(e_times)

    for i in range(nt-1):

        if v[i] * v[i+1] <= 0:

            if v[i] <= 0:

                et[i + 1] = e_times[i] - v[i] * dt / (v[i + 1] - v[i])

            else:

                et[i] = e_times[i] - v[i] * dt / (v[i + 1] - v[i])

    et = [et[i] for i, x in enumerate(v) if x > 0]

    list_of_intervals = series.series_without_gaps(et, max_gap=2 * dt, min_interval=2 * dt)

    return list_of_intervals


def gti_val_to_x0(e_times, v):
    """
    Return periods of consecutive intervals in a series of numbers interpolating the limits (start end of each periods)
    Only v >0 periods are returned

    v(e_times(i)) is the list of values of  the function v

    Note: this is equivalent to the original code from IDL code.

    1) Check both list have the same size
    2) Interpol the cut of v = 0
    3) Select ephemeris time where x > 0
    4) generate GTI periods


    :param e_times: ephemeris times
    :param v: values of the functions
    :param maxgap: The maximum acceptable gap between values;
    :return: list of times
    """

    import operator
    import sys
    if sys.version_info > (3, 6):
        from functools import reduce

    gti = gti_val_0(e_times, v)

    x0 = reduce(operator.concat, gti)

    return list(x0)


def gti_val_like_idl(e_times, v):
    """
    Return periods of consecutive intervals in a series of numbers without interpolating the limits (start end of each periods)
    Only v >=0 periods are returned

    Notes: This routine do not interpol the cut of v = 0. git_val_0 do it!
    This routines is used by gti_range_0 only.

    v(e_times(i)) is the list of values of  the function v

    1) Check both list have the same size
    2) Select ephemeris time where x > 0
    3) generate GTI periods

    :param e_times: ephemeris times
    :param v: values of the functions
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(v) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(v)))

    et = e_times[:]

    valid_index = [i for i, x in enumerate(v) if x >= 0]

    valid_index_periods = series.series_without_gaps(valid_index, max_gap=1.05, min_interval=0)
    # valid_periods = [[et[i[0]], et[i[1]]] for i in valid_index_periods]

    valid_periods = []
    for i_start, i_end in valid_index_periods:

        if i_start > 0:

            # (a, b, c, d) = ( et[i_start], v[i_start], (et[i_start+1] - et[i_start]), (v[i_start+1] - v[i_start]))

            et_start = et[i_start] - v[i_start] * (et[i_start] - et[i_start-1]) / (v[i_start] - v[i_start-1])

        else:

            et_start = et[i_start]

        if i_end < nt - 1:

            if v[i_end] == 0:

                et_end = et[i_end] + (et[i_end + 1] - et[i_end]) / 2.0

            else:

                et_end = et[i_end] - v[i_end] * (et[i_end + 1] - et[i_end]) / (v[i_end + 1] - v[i_end])

        else:

            et_end = et[i_end]

        valid_periods.append([et_start, et_end])

    return valid_periods


# def gti_val_like_idl_without_intermediate(etimes, v):
#     """
#     Return periods of consecutive intervals in a series of numbers without interpolating the limits (start end of each periods)
#     Only v >=0 periods are returned
#
#     Notes: This routine do not interpol the cut of v = 0. git_val_0 do it!
#     This routines is used by gti_range_0 only.
#
#     v(etimes(i)) is the list of values of  the function v
#
#     1) Check both list have the same size
#     2) Select ephemeris time where x > 0
#     3) generate GTI periods
#
#     :param etimes: ephemeris times
#     :param y: values of the functions
#     :return: list of intervals [[start0, end0]...] values without gaps > max_gap
#     """
#
#     nt = len(etimes)
#
#     if len(v) != nt:
#         logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(v)))
#
#     et = etimes[:]
#
#     valid_index = [i for i, x in enumerate(v) if x >= 0]
#
#     valid_index_periods = series.series_without_gaps(valid_index, max_gap=1.05, min_interval=0)
#     if len(valid_index_periods) > 1:
#         valid_index_periods = [valid_index_periods[0]] \
#                           + [p for p in valid_index_periods[1:-1] if (p[1] - p[1]) > 0] + [valid_index_periods[-1]]
#
#     # valid_periods = [[et[i[0]], et[i[1]]] for i in valid_index_periods]
#
#     valid_periods = []
#     for i_start, i_end in valid_index_periods:
#
#         if i_start > 0:
#
#             if v[i_start] == 0:
#
#                 et_start = et[i_start] - v[i_start] * (et[i_start] - et[i_start - 1]) / 2.0
#
#             else:
#
#                 et_start = et[i_start] - v[i_start] * (et[i_start] - et[i_start - 1]) / (v[i_start] - v[i_start - 1])
#
#         else:
#
#             et_start = et[i_start]
#
#         if i_end < nt - 1:
#
#             if v[i_end] == 0:
#
#                 et_end = et[i_end] + (et[i_end + 1] - et[i_end]) / 2.0
#
#             else:
#
#                 et_end = et[i_end] - v[i_end] * (et[i_end + 1] - et[i_end]) / (v[i_end + 1] - v[i_end])
#
#         else:
#
#             et_end = et[i_end]
#
#         valid_periods.append([et_start, et_end])
#
#     return valid_periods
#

def gti_val(e_times, v):
    """
    Return periods of consecutive intervals in a series of numbers without interpolating the limits (start end of each periods)
    Only v >=0 periods are returned

    v(e_times(i)) is the list of values of  the function v

    1) Check both list have the same size
    2) Select ephemeris time where x > 0
    3) generate GTI periods

    Notes: This routine do not interpol the cut of v = 0. git_val_0 do it!

    :param e_times: ephemeris times
    :param v: values of the functions
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(v) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(v)))

    et = e_times[:]

    valid_index = [i for i, x in enumerate(v) if x > 0]

    valid_index_periods = series.series_without_gaps(valid_index, max_gap=1.05, min_interval=1)
    valid_periods = [[et[i[0]], et[i[1]]] for i in valid_index_periods]

    return valid_periods


def gti_range_0(e_times, f, f_min, f_max):
    """
    Return periods of consecutive intervals in a series of numbers interpolating the limits (start end of each periods)
    Only f_max >= f >= f_min periods are returned

    This is the inverse( overlap([fmin, f], [max, f])

    :param e_times: ephemeris times
    :param f: values of the functions
    :param f_min: minimum valid value of the function f
    :param f_max: maximum valis values of the functions f
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(f) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(f)))

    if f_min > f_max:
        logging.error('f_min={} > f_max={}!'.format(f_min, f_max))

    # gti_max = gti_inverse(gti_val_without_interpolation(etimes, np.array(f) - f_max), start=etimes[0], end=etimes[-1])
    gti_max = gti_val_like_idl(e_times, f_max - np.array(f))
    gti_min = gti_val_like_idl(e_times, np.array(f) - f_min)

    gti = gti_overlap_0(gti_max, gti_min, min_gti=0.1)

    return gti


def gti_range(e_times, f, f_min, f_max):
    """
    Return periods of consecutive intervals in a series of numbers interpolating the limits (start end of each periods)
    Only f_max >= f >= f_min periods are returned

    This is the inverse( overlap([fmin, f], [max, f])

    :param e_times: ephemeris times
    :param f: values of the functions
    :param f_min: minimum valid value of the function f
    :param f_max: ,aximum valis values of the functions f
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap
    """

    nt = len(e_times)

    if len(f) != nt:
        logging.error('both directory must have the same size!: len(et) = {}, len(f(et)) = {}'.format(nt, len(f)))

    gti_max = gti_inverse(gti_val(e_times, np.array(f) - f_max), start=e_times[0], end=e_times[-1])
    gti_min = gti_val(e_times, np.array(f) - f_min)

    gti = gti_overlap(gti_max, gti_min)
    return gti


def mask2gti(etimes, f_mask, add_Final_dt=True):
    """
    The function MASK2GTI accepts an array of times and mask, and
    converts valid data into corresponding good time intervals (GTIs).

    Note: By default dt add to end time to have a complete last step

    :param etimes: list of ephemeris times
    :param f_mask: binary mask
    :param add_Final_dt: if set to true, dt is added to the final date
    :return:
    """
    dt = 0
    if add_Final_dt:
        dt = float(etimes[1] - etimes[0])

    valid_index = [i for i, x in enumerate(f_mask) if x]
    valid_index_periods = series.series_without_gaps(valid_index, max_gap=1.05)
    valid_periods = [[etimes[i[0]], etimes[i[1]] + dt] for i in valid_index_periods]

    return valid_periods


def is_good_git(gti):
    """
    Check if GTIs are good.

    - Consecutive time windows ordered in ascending ephemeris times
    - No start > end
    - no overlaps

    :param gti: list of ephemeris time in ascending order for event
    return: flag True/False if Good/bad GTI
    """

    gti_start = gti[:, 0]
    gti_end = gti[:, 1]

    logging.debug('-- GTI: ' + repr(gti))
    # Check that GTIs are well-behaved
    assert np.all(gti_end >= gti_start), 'This GTI is incorrect'
    # Check that there are no overlaps in GTIs
    assert np.all(gti_start[1:] >= gti_end[:-1]), 'This GTI has overlaps'
    logging.debug('-- Correct')

    return


def gti_set_init(e, start_e_time, end_e_time, git_et_files_root_dir):
    """
    Set initial GTI

    :param e: structure including event parameters
    :param start_e_time: ephemeris start time
    :param end_e_time: ephemeris end time
    :param git_et_files_root_dir: root path of event file in ephemeris data and time
    :return: gti: list of intervals [[start0, end0]...]
    """

    import efinder.geometry.proc.utils.event_handler as event_handler

    if hasattr(e, 'gti'):

        gti = [[start_e_time, end_e_time]]
        print(e.gti)

        p = event_handler.EventHandler()

        for ev in e.gti:

            logging.debug('ev: {}'.format(ev))

            event_name = ev
            if ev[0] == '!':
                event_name = ev[1:]

            ev_gti_file_path = os.path.join(git_et_files_root_dir, event_name + '.txt')
            ev_gti = p.read_efinder_events_values(ev_gti_file_path)

            if ev[0] == '!':
                ev_gti = gti_inverse(ev_gti, start=start_e_time, end=end_e_time)

            if hasattr(e, 'mingti'):
                gti = gti_overlap_0(gti, ev_gti, e.mingti)
            else:
                gti = gti_overlap(gti, ev_gti)

    else:

        if hasattr(e, 'interval'):
            gti = reset_git_npmax(start_e_time, end_e_time, e.interval)
        else:
            gti = [[start_e_time, end_e_time]]

    logging.debug('gti = {}'.format(gti))

    return gti


def gti_specific_set_init(e, e_gti, start_e_time, end_e_time, git_et_files_root_dir):
    """
    Set initial specific GTI as per gti_exclusion for GS_KX

    :param e: structure including event parameters
    :param e_gti: specific gti list within e
    :param start_e_time: ephemeris start time
    :param end_e_time: ephemeris end time
    :param git_et_files_root_dir: root dir path where to pre-processed events file in ephemeris time format
    :return: gti: list of intervals [[start0, end0]...]
    """

    import efinder.geometry.proc.utils.event_handler as event_handler

    gti = [[start_e_time, end_e_time]]

    p = event_handler.EventHandler()

    for ev in e_gti:

        logging.debug('ev: {}'.format(ev))

        event_name = ev
        if ev[0] == '!':
            event_name = ev[1:]

        ev_gti_file_path = os.path.join(git_et_files_root_dir, event_name + '.txt')
        ev_gti = p.read_efinder_events_values(ev_gti_file_path)

        if ev[0] == '!':
            ev_gti = gti_inverse(ev_gti, start=start_e_time, end=end_e_time)

        if hasattr(e, 'mingti'):
            gti = gti_overlap_0(gti, ev_gti, e.mingti)
        else:
            gti = gti_overlap(gti, ev_gti)

    logging.debug('gti = {}'.format(gti))

    return gti


def reset_git_npmax(t_min, t_max, interval, np_max=500000):
    """
    Split GTI when number of values (or times) > np_max

    :param t_min: start time in seconds
    :param t_max: end time in seconds
    :param interval: step, number of seconds
    :param np_max: maximum number; The idea is to process all_value by slots of 500000 values maximum
    :return: gti: list of intervals [[start0, end0]...]
    """

    gti = []

    np = (t_max - t_min) / interval
    n_gti = int((np / np_max)) + 1
    logging.info('np, npmax, interval, ngti = ({}, {}, {}, {})'.format(np, np_max, interval, n_gti))
    logging.info('Number of tt = {} > np_max = {}; So split in {} GTI of {} tt'.format(np, np_max, n_gti, np / n_gti))

    start = t_min

    for i in range(n_gti - 1):
        end = start + np / n_gti * interval
        gti.append([start, end])
        start = end

    gti.append([start, t_max])

    for p in gti:
        print('({} - {})/{} = {}'.format(p[1], p[0], interval, (p[1] - p[0])/interval))

    return gti


def get_cross_events(gti_1, gti_2):
    """
    Get list of event_1 of gti_1  instance followed by even_2 of gti_2 instance

    Note: avoid event_1 = event_2

    :param gti_1: list of intervals [[start0, end0]...]
    :param gti_2: list of intervals [[start0, end0]...]
    :return: ogti, list of interval [[start0, end0]...] where event of gti_1 followed by gti_2
    """

    o_gti = intervals_handler.get_cross_events(gti_1, gti_2)

    o_gti = gti_remove_duplicated_overlaps(o_gti, priority_occurence="first")

    return o_gti


def gti_substract(gti_1, gti_2):
    """
    Remove gti_2 in gti_1

    This means ogti = gti_1 - gti_2

    :param gti_1: list of intervals [[start0, end0]...]
    :param gti_2: list of intervals [[start0, end0]...]
    :return: ogti; list of intervals
    """

    ogti = intervals_handler.get_event_sub(gti_1, gti_2)

    return ogti


def gti_remove_duplicated_overlaps(gti_1, priority_occurence="first"):
    """
    Normalize a Good Time Interval (GTI) - no overlapping
    removing duplicated overlaps

    - first means the first occurence of an event prevails,
    and then the overlap if remove for all the other event if needed

    - last means the last occurence of an event prevails,
    and then the overlap if remove for all the other event if needed

    :param gti_1: list of intervals [[start0, end0]...]
    :param gti_2:
    :param priority_occurence: first or last; First means the
    :param gti_1: list of intervals [[start0, end0]...]
    :param gti_2: list of intervals [[start0, end0]...]
    :return: ogti, list of interval [[start0, end0]...] whithout overlaps
    """

    import spiceypy as spi

    if len(gti_1) < 2:

        return gti_1

    ogti =[]
    tmp_ogti = copy.copy(gti_1)

    if priority_occurence == 'first':

        while len(tmp_ogti) >= 2:

            current_ev = tmp_ogti[0]

            ev_overlap = gti_overlap([current_ev], [tmp_ogti[1]])

            if ev_overlap:

                tmp_ogti = gti_substract(tmp_ogti[1:], ev_overlap)

            else:

                tmp_ogti = tmp_ogti[1:]

            ogti.append(current_ev)

        ogti.extend(tmp_ogti)  # append last event if any

    # elif priority_occurence == 'last':
    #
    #     while len(tmp_ogti) >= 2:
    #
    #         current_ev = tmp_ogti[-1]
    #
    #         ev_overlap = gti_overlap([current_ev], [tmp_ogti[-2]])
    #
    #         if ev_overlap:
    #
    #             tmp_ogti = gti_substract(tmp_ogti[:-1], ev_overlap)
    #
    #         else:
    #
    #             tmp_ogti = tmp_ogti[:-2]
    #
    #         ogti.insert(0, current_ev)
    #
    #     ogti.extend(tmp_ogti)  # append previous event if any

    else:

        logging.error('priority_occurence must be "first or "last": {} is no a valid value')
        sys.exit()

    return ogti


