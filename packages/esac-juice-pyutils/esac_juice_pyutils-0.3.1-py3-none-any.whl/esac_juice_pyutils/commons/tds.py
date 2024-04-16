#!/usr/bin/python
"""
Created on September 20, 2016

@author: cmunoz

This file includes common data and time functions
"""

import sys
import datetime
import logging

from dateutil.parser import parse


def datetime2utc(date_time, dateformat='%Y-%m-%dT%H:%M:%S.%f'):
    """
    Translates a date time from datetime to utc string
    :param date_time:
    :param dateformat:
    :return:
    """
    return datetime.datetime.strftime(date_time, dateformat)


def get_current_datetime_label(dateformat='%Y%m%dT%H%M%S'):
    """
    Provide a string corresponding to current time
    Mainly for directory,and file naming conventions
    :param dateformat:
    :return:
    """

    return datetime2utc(datetime.datetime.now(), dateformat)


def get_datetime_range(start, end, N=4000):
    """
    Returns a list of N epoch value within a given period of time
    :param start: start date time
    :param end: end date time
    :param N: Number of epoch values
    :return: list of epoch values
    :rtype list of datetime
    """
    # timeRange = np.linspace(start,end,N)

    dateWindow = end - start
    dts = dateWindow / (N - 1)
    logging.debug('dts = {0} = "{1}"/{2}'.format(dts, dateWindow, N - 1))
    timeRange = [start + i * dts for i in range(N)]
    return timeRange


def get_datetime_string_range(start, end, N=4000, dateformat='%Y-%m-%dT%H:%M:%S.%f'):
    """
    Returns a list of N epoch value within a given period of time
    :param start: start date time
    :param end: end date time
    :param N: Number of epoch values
    :return: list of epoch values
    :rtype list of string
    """
    # timeRange = np.linspace(start,end,N)

    timerange = get_datetime_range(start, end, N)
    timerange = [datetime2utc(i, dateformat) for i in timerange]
    return timerange


def get_utc_seconds_j2000(date_time):
    """
    TODO
    """

def utc_jd_2_datetime(jd_date):
    """
    Tranlates JD to datetime.
    Note that Julian dates (UTC (JD)) count from 12:00:00 noon, 1 January 2000
    For instance ground station link budget periods of time can be provided as JD
    # GS Start time    End time
    #      UTC (JD)    UTC (JD)
    #
    FILE_TYPE = GS_VIS_PERIODS
    TIME_SCALE = JD
    #
    MAD	8186.74383316	8187.05772205
    CEB	8186.74383316	8187.05772205
    MLG	8186.81605538	8187.26536094
    GDS	8186.97022205	8187.37369427
    :param jd_date, Julian dates (UTC (JD)) count from 12:00:00 noon, 1 January 2000
    :return: a datetime
    """
    ref_jd = datetime.datetime(2000, 1, 1, 12, 0, 0)
    return ref_jd + datetime.timedelta(days=float(jd_date))


def utc_mjd_2_datetime(jd_date):
    """
    Tranlates JD to datetime.
    Note that the Modified Julian Date [MJD] used here counts from 00:00:00 on 1 January 2000. It is also known as MJD2000
    For instance ground station link budget periods of time can be provided as JD
    # GS Start time    End time
    #      UTC (JD)    UTC (JD)
    #
    FILE_TYPE = GS_VIS_PERIODS
    TIME_SCALE = JD
    #
    MAD	8186.74383316	8187.05772205
    CEB	8186.74383316	8187.05772205
    MLG	8186.81605538	8187.26536094
    GDS	8186.97022205	8187.37369427
    :param jd_date, MJD2000, Modified Julian dates (UTC (MJD)) count from 00:00:00 noon, 1 January 2000
    :return: a datetime
    """
    ref_mjd = datetime.datetime(2000, 1, 1, 0, 0, 0)
    return ref_mjd + datetime.timedelta(days=float(jd_date))


def deltatime_itl_like_2_timedelta(time_string, delta_time_fmt="([+-]?)([0-9]{3}_)?([0-9]{2}):([0-9]{2}):([0-9]{2})"):
    """
    Translate itl_deltatime string to datetime.timedelta object

    by default expected delta_time_fmt format is:

    "([+-]?)([0-9]{3}_)?([0-9]{2}):([0-9]{2}):([0-9]{2})" for

    [+-][000_]00:00:00
    for instance -00:11:32, +001_00:10:00

    Another formt could be
    "([+-]?)([0-9]{3}T)?([0-9]{2}):([0-9]{2}):([0-9]{2})" for

        [+-][000T]00:00:00
        for instance -00:11:32, +001T00:10:00


    :param delta_time_fmt:
    :param time_string:
    :return:
    """

    import re

    # itl_deltatime = "([+-]?)([0-9]{3}_)?([0-9]{2}):([0-9]{2}):([0-9]{2})"
    itl_deltatime_parser = re.compile(delta_time_fmt)
    m_delta_time = itl_deltatime_parser.match(time_string)

    if m_delta_time is None:

        logging.error('Cannot parse time_delta {}'.format(time_string))
        sys.exit()

    sign, days, hh, mm, ss = m_delta_time.groups()

    if days is None:
        days = 0
    else:
        days = int(days[:3])

    time_delta = datetime.timedelta(days=int(days), hours=int(hh), minutes=int(mm), seconds=int(ss))
    if sign == '-':
        time_delta *= -1

    return time_delta


def check_valid_date_time(date_text):
    """
    Check start and end date time within juice mission
    TODO
    :return:
    """
    try:
        good_dtformat = False

        if date_text != datetime.strptime(date_text, "%Y-%m-%dTHH:MM:SS").strftime("%Y-%m-%dTHH:MM:SS"):
            logging.error('expected date time format is YYYY-mm-ddTHH:MM:SS')
        return True
    except ValueError:
        return False


def check_datetime_format(start_date, d_format="%Y-%m-%dT%H:%M:%S"):
    """
    Check imput date time string format
    :return:
    """

    try:
        start_date = datetime.datetime.strptime(start_date, d_format)
        return True
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return False
    except ValueError:
        print('Bad date time format "{}"; Expected format is "{}"'.format(
            start_date, datetime.datetime.strftime(datetime.datetime.now(), d_format)))
        return False


def str2datetime(str_date, d_format="%Y-%m-%dT%H:%M:%S"):
    """
    Check input date time string format
    :return:
    """

    try:
        start_date = datetime.datetime.strptime(str_date, d_format)
        return start_date
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
    except ValueError:
        print('Bad date time format "{}"; Expected format is "{}"'.format(
            str_date, datetime.datetime.strftime(datetime.datetime.now(), d_format)))
        return None


def round2seconds(my_datetimes, round_factor=60):
    """
    Round a date to the nearest values aaccording to rounding factor
    if round_factor=60, this means round to the nearest minute.

    :param my_datetime:
    :param round_factor:
    :return:
    """

    ref_date = datetime.datetime(1970, 1, 1)

    t = (my_datetimes - ref_date).total_seconds()

    return ref_date + round(t / round_factor) * round_factor


def round_datetime2seconds(my_datetimes, round_factor=60):
    """
    Round a date to the nearest values aaccording to rounding factor
    if round_factor=60, this means round to the nearest minute.

    :param my_datetime:
    :param round_factor:
    :return: datetime
    """

    ref_date = datetime.datetime(1970, 1, 1)

    t = (my_datetimes - ref_date).total_seconds()

    return ref_date + datetime.timedelta(seconds=round(t / round_factor) * round_factor)


def ceil2seconds(my_datetimes, round_factor=60):
    """
    Get the ceil of a date to the nearest values according to rounding factor
    if round_factor=60, the means to get the date corresponding to the number of entire minutes

    :param my_datetime:
    :param round_factor:
    :return:
    """

    ref_date = datetime.datetime(1970, 1, 1)

    t = (my_datetimes - ref_date).total_seconds()

    return ref_date + int(t / round_factor) * round_factor


def eps_str_datetime_2_datetime(str_date):
    """
    Parse EPS date time format to datetime object

    1) Try EPS specific format first
    2) use datetutils wich support most common formats
    :return:
    """

    eps_datetime_formats = ['%d-%b-%Y_%H:%M:%S', '%d-%B-%Y_%H:%M:%S', '%Y-%m-%dT%H:%M:%SZ']

    dt = None

    for dt_format in eps_datetime_formats:

        try:

            dt = datetime.datetime.strptime(str_date, dt_format)

            if dt:
                break

        except IOError as e:
            logging.debug(("I/O error({0}): {1}".format(e.errno, e.strerror)))

        except ValueError:
            logging.debug('Bad date time format "{}"; Expected format is "{}"'.format(
                str_date, datetime.datetime.strftime(datetime.datetime.now(), dt_format)))

    try:

        if dt is None:
            dt = parse(str_date)

    except IOError as e:
        logging.debug(("I/O error({0}): {1}".format(e.errno, e.strerror)))

    except ValueError:
        logging.debug('Bad date time format "{}"; Expected format is "{}"'.format(
            str_date, datetime.datetime.strftime(datetime.datetime.now(), dt_format)))

    if dt is None:
        logging.debug('Cannot par "{}" to datetime format!'.format(str_date))

    return dt


def time_delta_2_string(my_timedelta, timedelta_format='%03dT%02d:%02d:%02d',
                        round_seconds=1E-6):
    """
    Customize timedelta conversion to string,
    applying round seconds factor.
    by default rounded to microseconds

    :param round_seconds: number of seconds (can be decimal); by default rounded to microseconds
    :param timedelta_format: datetime format
    :param my_timedelta: input datetime.timedelta
    :return: dhm timedelta string
    """

    sign = ''
    if my_timedelta < datetime.timedelta(seconds=0):
        sign = '-'

    seconds = my_timedelta.total_seconds()

    seconds = abs(round(seconds / round_seconds) * round_seconds)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    timedelta_str = sign + timedelta_format %(days, hours, minutes, seconds)

    return timedelta_str


class SimpleUtc(datetime.tzinfo):
    """
    class to define ISO 8601 format UTC, Zoulou time (+00:00), no time (or +00:00 time) zone
    """

    def tzname(self,**kwargs):
        return "UTC"

    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def dst(self, dt):
        return datetime.timedelta(0)