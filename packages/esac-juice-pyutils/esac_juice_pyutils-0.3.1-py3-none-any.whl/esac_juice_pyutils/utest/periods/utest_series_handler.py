"""
Created on October, 2018

@author: Claudio Munoz Crego (ESAC)

This Module allows to test functions to handle intervals (list of numbers)
"""

import unittest

from esac_juice_pyutils.periods.series_handler import *

my_integer_serie = [2, 3, 4, 7, 8, 9, 10, 15]


class MyTestCase(unittest.TestCase):

    def test_gaps(self):
        """
        Get the gaps within a series of numerical values
        """

        series_in = my_integer_serie
        series_out = [[4, 7], [10, 15]]

        self.assertEqual(gaps(series_in, 1), series_out)
        self.assertEqual(gaps(series_in, 3), [[10, 15]])  # [4,7] window = 3 so this is no longer a gap

    def test_series_without_gaps(self):
        """
        Get the periods without gaps within a series of numerical values
        with conditions:
        - max_gap: The maximum acceptable gap between values = 1; the default value
        """

        series_in = my_integer_serie
        series_out = [(2, 4), (7, 10)]

        self.assertEqual(series_without_gaps(series_in, 1), series_out)

    def test_series_without_gaps_2(self, max_gap=1, min_interval=2):
        """
        Get the periods without gaps within a series of numerical values
        with conditions:
        - max_gap: The maximum acceptable gap between values = 1
        - min_interval The smallest acceptable interval = 2
        """
        series_in = my_integer_serie
        series_out = [(7, 10)]

        self.assertEqual(series_without_gaps(series_in, max_gap, min_interval), series_out)


if __name__ == '__main__':

    unittest.main()
