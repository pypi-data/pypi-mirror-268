"""
Created on March, 2019

@author: Claudio Munoz Crego (ESAC)

This Module allows to test functions to handle GTI (Good Time intervals, list of periods)
"""

import unittest

from numpy.testing import assert_array_equal, assert_allclose

from esac_juice_pyutils.gti import gti_handler


class MyTestCase(unittest.TestCase):

    def test_gti_inverse(self):
        """
        Test gti_inverse which returns the complementary of a given list os intervals [start0, end0],...]
        """

        gti_1 = [[2, 3.14], [6.0, 8.1]]

        self.assertEqual(gti_handler.gti_inverse(gti_1), [[3.14, 6.0]])
        self.assertEqual(gti_handler.gti_inverse(gti_1, start=0., end=10.), [[0, 2], [3.14, 6.0], [8.1, 10]])

    def test_gti_val_0(self):
        """
        The gti_val function allows to calculate periods of consecutive intervals in a series of numbers
        interpolating the limits (start end of each periods)
        """

        et_series = [10, 20, 30, 40, 50]
        val_series = [-1, 1, 2, 2, -2]

        self.assertEqual(gti_handler.gti_val_0(et_series, val_series), [[15.0, 45.0]])

    def test_gti_val_x0(self):
        """
        Test gti_val_x0 wich return the list of interpolated values of etime
        """

        et_series = [10, 20, 30, 40, 50]
        val_series = [-1, 1, 2, 2, -2]

        self.assertEqual(gti_handler.gti_val_x0(et_series, val_series), [15.0, 30., 45.0])

    def test_gti_val_to_x0(self):
        """
        Test gti_val_x0 wich return the list of interpolated values of etime
        """

        et_series = [10, 20, 30, 40, 50]
        val_series = [-1, 1, 2, 2, -2]

        self.assertEqual(gti_handler.gti_val_to_x0(et_series, val_series), [15.0, 45.0])

    def test_gti_val_1(self):
        """
        The gti_val function allows to calculate periods of consecutive intervals in a series of numbers
        interpolating the limits (start end of each periods)
        """

        et_series = [10, 20, 30, 40, 50]
        val_series = [-1, 1, 2, 2, -2]


        self.assertEqual(gti_handler.gti_val_1(et_series, val_series), [[15.0, 45.0]])

    def test_gti_val(self):
        """
        The gti_val function allows to calculate periods of consecutive intervals in a series of numbers
        without interpolating the limits (start end of each periods)
        """

        et_series = [10, 20, 30, 40, 50]
        val_series = [-1, 1, 2, 2, -2]

        self.assertEqual(gti_handler.gti_val(et_series, val_series), [[20.0, 40.0]])

    def test_gti_merge_0(self):
        """
        The gti_merge function allows to merge 2 Good Time Interval (GTI) - no overlapping and adjoining
        Notes: we normalize a Good Time Interval (GTI) - no overlapping and adjoining
        - 0 duration events/periods are removed
        - events/periods with duration <= min_gti are removed too (default is 0)
        - any gap within two consecutive events/periods <= max_gap is removed.
          This mean join the corresponding consecutive events.
        """

        self.assertEqual(gti_handler.gti_merge_0([[1, 3.14]], [[1, 3.14]]), [[1, 3.14]])
        self.assertEqual(gti_handler.gti_merge_0([[1, 3.14]], [[3.14, 6.2]]), [[1, 6.2]])
        self.assertEqual(gti_handler.gti_merge_0([[1, 3.14], [7, 8]], [[3.14, 6.2], [5, 6.0], [10, 12]]),
                         [[1, 6.2], [7, 8], [10, 12]])

        gti_1 = [[1, 3.14], [6.0, 8.1]]
        gti_2 = [[2.5, 5.9], [7.0, 8.2], [11, 11.1], [12, 12]]

        self.assertEqual(gti_handler.gti_merge_0(gti_1, gti_2), [[1, 5.9], [6.0, 8.2], [11, 11.1]])
        self.assertEqual(gti_handler.gti_merge_0(gti_1, gti_2, min_gti=0.1), [[1, 5.9], [6.0, 8.2]])
        self.assertEqual(gti_handler.gti_merge_0(gti_1, gti_2, max_gap=0.1), [[1, 8.2], [11, 11.1]])

    def test_gti_merge(self):
        """
        The gti_merge function allows to merge 2 Good Time Interval (GTI) - no overlapping and adjoining
        Notes:  we don't normalize the Good Time Interval (GTI)
                So all interval are valid, even 0 duration ones ( i.e. [12, 12])
        """

        self.assertEqual(gti_handler.gti_merge([[1, 3.14]], [[1, 3.14]]), [[1, 3.14]])
        self.assertEqual(gti_handler.gti_merge([[1, 3.14]], [[3.14, 6.2]]), [[1, 6.2]])
        self.assertEqual(gti_handler.gti_merge([[1, 3.14], [7, 8]], [[3.14, 6.2], [5, 6.0], [10, 12]]),
                         [[1, 6.2], [7, 8], [10, 12]])

        gti_1 = [[1, 3.14], [6.0, 8.1]]
        gti_2 = [[2.5, 5.9], [7.0, 8.2], [11, 11.1], [12, 12]]

        self.assertEqual(gti_handler.gti_merge(gti_1, gti_2), [[1, 5.9], [6.0, 8.2], [11, 11.1], [12, 12]])

    def test_gti_range_0(self):
        """
        The gti_range functions allows to calculate periods of consecutive intervals in a series of numbers
        interpolating the limits (start end of each periods) by using gti_val.
        And next select f_max >= f >= f_min periods
        """

        et_series = [10, 20, 30, 40, 50, 60, 70]
        val_series = [-1, 1, 2, 3, 2, 1, -1]
        (f_min, f_max) = (1, 1.5)
        self.assertEqual(gti_handler.gti_range_0(et_series, val_series, f_min, f_max), [[20.0, 25.0], [55.0, 60.0]])
        (f_min, f_max) = (0.5, 1.5)
        self.assertEqual(gti_handler.gti_range_0(et_series, val_series, f_min, f_max), [[17.5, 25.0], [55.0, 62.5]])

    def test_git_overlap_0(self):
        """
        The gti_overlap function allows ot merge good intervals providing min_gti: The smallest acceptable interval;
        :return:
        """

        gti_1 = [[1, 3.14], [6.2, 8.1], [8.5, 10.3]]
        gti_2 = [[2.5, 4.1], [6.0, 8.2], [8.6, 8.7], [9, 10]]

        self.assertEqual(gti_handler.gti_overlap_0(gti_1, gti_2), [[2.5, 3.14], [6.2, 8.1], [8.6, 8.7], [9, 10]])

        self.assertEqual(gti_handler.gti_overlap_0(gti_1, gti_2, min_gti=0.1), [[2.5, 3.14], [6.2, 8.1], [9, 10]])

    def test_git_overlap(self):
        """
        The gti_overlap function allows ot merge good intervals
        :return:
        """

        gti_1 = [[1, 3.14], [6.2, 8.1], [8.5, 10.3]]
        gti_2 = [[2.5, 4.1], [6.0, 8.2], [8.6, 8.6], [9, 10]]

        self.assertEqual(gti_handler.gti_overlap(gti_1, gti_2), [[2.5, 3.14], [6.2, 8.1], [8.6, 8.6], [9, 10]])

    def test_mask2gti(self):
        """
        The mask2gti function allows to generate a Good Time Interval (GTI) for a given array of times and mask
        Note we event periods are [[etimes[i[0]], etimes[i[1]] + dt]; where dt = float(etimes[1] - etimes[0])
        """

        et_series = [10, 20, 30, 40, 70, 90, 100]
        self.assertEqual(gti_handler.mask2gti(et_series, [1, 1, 0, 1, 0, 1, 1]), [[10., 30.], [90, 110]])
        self.assertEqual(gti_handler.mask2gti(et_series, [1, 1, 0, 1, 0, 0, 1]), [[10., 30.]])

    def test_gti_extend_events(self):
        """
        Test Extend all gti time interval
        """
        gti = [[3300, 3600], [10000, 10000]]

        assert_array_equal(gti_handler.gti_extend_events(gti), gti)  # no changes
        assert_array_equal(gti_handler.gti_extend_events(gti, before=300, after=1800), [[3000, 5400], [9700, 11800]])
        assert_array_equal(gti_handler.gti_extend_events(gti, before=150, after=150, center=1), [[3300, 3600],
                                                                                                 [9850, 10150]])

    def test_gti_trim(self):
        """
        Test gti_trim which allows to normalize a Good Time Interval (GTI) - no overlapping and adjoining
        """

        gti = [[882542299.71, 882542966.60], [882542966.60, 882544671.28], [882544771.28, 882544971.28]]

        self.assertEqual(gti_handler.gti_trim(gti), [[882542299.71, 882544671.28], [882544771.28, 882544971.28]])
        self.assertEqual(gti_handler.gti_trim(gti, max_gap=100), [[882542299.71, 882544671.28], [882544771.28, 882544971.28]])
        self.assertEqual(gti_handler.gti_trim(gti, max_gap=101), [[882542299.71, 882544971.28]])
        self.assertEqual(gti_handler.gti_trim(gti, max_gap=100, min_gti=200),
                         [[882542299.71, 882544671.28]])
        self.assertEqual(gti_handler.gti_trim(gti, max_gap=100, min_gti=201),
                         [[882542299.71, 882544671.28]])

    def test_gti_where_extended(self):
        """
        Test gti_where_extended which allows to Locate a list of intervals
         within a Good Time Interval (GTI) array containing e_times
        """

        et_serie = [10, 20, 30, 40, 70, 90, 100]
        gti = [[5., 15.], [20, 70], [95, 99], [100, 110]]

        self.assertEqual(gti_handler.gti_where_extended(et_serie, gti), (
            [0, 1, 3],
            [[5., 15.], [20, 70], [100, 110]],
            [0, 1, 6],
            [10, 20, 100]))

    def test_gti_where(self):
        """
        Test gti_where which allows to Locate a list of intervals
         within a Good Time Interval (GTI) array containing e_times
        """

        et_serie = [10, 20, 30, 40, 70, 90, 100]
        gti = [[5., 15.], [20, 70], [95, 99], [100, 110]]

        self.assertEqual(gti_handler.gti_where(et_serie, gti), (
            [0, 1, 3], [[5., 15.], [20, 70], [100, 110]],))

        self.assertEqual(gti_handler.gti_where(et_serie, gti, inverse=True), (
            [2], [[95, 99]]))

        self.assertEqual(gti_handler.gti_where([5, 70], gti), (
            [0, 1], [[5., 15.], [20, 70]]))

        self.assertEqual(gti_handler.gti_where([5, 70], gti, inverse=True), (
            [2, 3], [[95, 99], [100, 110]]))

        et = [5., 15., 20, 70]  # list(zip(*gti)[0])
        self.assertEqual(gti_handler.gti_where(et, gti), (
            [0, 1], [[5.0, 15.0], [20, 70]]))

        et = [5., 20]  # list(zip(*gti)[0])
        self.assertEqual(gti_handler.gti_where(et, gti), (
            [0, 1], [[5.0, 15.0], [20, 70]]))


if __name__ == '__main__':
    unittest.main()