"""
Created on February 2023

@author: Claudio Munoz Crego (ESAC)

Unit Tests for tds_psicey

"""

import unittest
import datetime

import spiceypy as spi
import esac_juice_pyutils.commons.tds_spicey as tds_spicey

spi.furnsh('./naif0012.tls')


class MyTestCase(unittest.TestCase):

    def test_et2utc(self):
        """
        Test ephemeris time to UTC
        """

        dt_format_isot = '2019-07-13T12:48:32'
        et_ref = spi.utc2et(dt_format_isot)

        self.assertEqual(tds_spicey.et2utc(et_ref, format="%Y-%m-%dT%H:%M:%S"), dt_format_isot)

    def test_et2datetime(self):
        """
        Test ephemeris time to datetime
        """

        dt_format_isot = '2019-07-13T12:48:32'
        et_ref = spi.utc2et(dt_format_isot)

        self.assertEqual(tds_spicey.et2datetime(et_ref), datetime.datetime(2019, 7, 13, 12, 48, 32, 0))
