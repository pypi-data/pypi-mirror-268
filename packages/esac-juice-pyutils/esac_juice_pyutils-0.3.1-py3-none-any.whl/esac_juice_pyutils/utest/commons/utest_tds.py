"""
Created on October 2019

@author: Claudio Munoz Crego (ESAC)

Unit Tests for tds

"""

import os
import unittest
import datetime

import esac_juice_pyutils.commons.tds as tds


class MyTestCase(unittest.TestCase):

    def test_tl_deltatime_2_timedelta(self):
        """
        Test read and parse
        """

        func = tds.deltatime_itl_like_2_timedelta

        self.assertEqual(func('01:12:47'), datetime.timedelta(hours=1, minutes=12, seconds=47))
        self.assertEqual(func('-01:12:47'), -datetime.timedelta(hours=1, minutes=12, seconds=47))
        self.assertEqual(func('001_01:02:17'), datetime.timedelta(days=1, hours=1, minutes=2, seconds=17))
        self.assertEqual(func('+001_01:02:17'), datetime.timedelta(days=1, hours=1, minutes=2, seconds=17))
        self.assertEqual(func('-001_01:02:17'), -datetime.timedelta(days=1, hours=1, minutes=2, seconds=17))

    def test_eps_str_datetime_2_datetime(self):
        """
        Test Parse EPS date time format to datetime object
        """

        func = tds.eps_str_datetime_2_datetime

        dt_format_isot = '2019-07-13T12:48:32'
        dt2_format_isot = '2019-07-13T00:00:00'
        result = tds.str2datetime(dt_format_isot, d_format="%Y-%m-%dT%H:%M:%S")
        result2 = tds.str2datetime(dt2_format_isot, d_format="%Y-%m-%dT%H:%M:%S")

        self.assertEqual(func('13-Jul-2019_12:48:32'), result)
        self.assertEqual(func('13-July-2019_12:48:32'), result)
        self.assertEqual(func('13-July-2019'), result2)
        self.assertEqual(func('13-Jul-2019'), result2)

    def test_time_delta_2_string(self):
        """
        Test timedelta conversion to string using round_seconds parameters
        Note: default timedelta_format='%03dT%02d:%02d:%02d'
        :return:
        """

        func = tds.time_delta_2_string

        dt0 = datetime.datetime(2019, 7, 13, 15, 10, 45)
        dti = datetime.datetime(2019, 7, 13, 16, 14, 57, 679000)

        dt = dti - dt0

        self.assertEqual(func(dt), '000T01:04:12')
        self.assertEqual(func(-dt), '-000T01:04:12')
        self.assertEqual(func(dt, round_seconds=1), '000T01:04:13')

        self.assertEqual(func(dt, round_seconds=60), '000T01:04:00')
        self.assertEqual(func(dt, round_seconds=3600), '000T01:00:00')

        dt = dt - datetime.timedelta(minutes=5)
        self.assertEqual(func(dt), '000T00:59:12')
        self.assertEqual(func(dt, round_seconds=3600), '000T01:00:00')

        tdt_format = '%03dT%02d:%02d:%06.3f'  # including milliseconds

        self.assertEqual(func(dt, timedelta_format=tdt_format), '000T00:59:12.679')
        self.assertEqual(func(-dt, timedelta_format=tdt_format), '-000T00:59:12.679')
        self.assertEqual(func(dt, timedelta_format=tdt_format, round_seconds=1), '000T00:59:13.000')
        self.assertEqual(func(dt, timedelta_format=tdt_format, round_seconds=3600), '000T01:00:00.000')

    def test_round_datetime2seconds(self):
        """
        Test rounding a date to the nearest values aaccording to rounding factor
        if round_factor=60, the means round to the nearest minute.

        :return:
        """

        func = tds.round_datetime2seconds

        dt = datetime.datetime(2019, 7, 13, 16, 14, 37, 679000)

        self.assertEqual(func(dt, round_factor=60), datetime.datetime(2019, 7, 13, 16, 15, 0, 0))
        self.assertEqual(func(dt, round_factor=10), datetime.datetime(2019, 7, 13, 16, 14, 40, 0))




