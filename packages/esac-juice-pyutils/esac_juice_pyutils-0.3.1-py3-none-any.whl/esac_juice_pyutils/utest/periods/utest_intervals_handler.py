"""
Created on October, 2018

@author: Claudio Munoz Crego (ESAC)

This Module allows to test functions to handle intervals (list of numbers)
"""

import unittest


from esac_juice_pyutils.periods.intervals_handler import IntervalHandlers


class MyTestCase(unittest.TestCase):

    def test_intervals_clean(self):
        """
        Clean a list of intervals removing intervals <= min_interval and if gaps < max_gap join intervals
        """

        p = IntervalHandlers()

        intervals_in = [[1, 6.2], [7, 8], [10, 12], [14, 15]]

        self.assertEqual(p.intervals_clean(intervals_in, max_gap=0.7, min_interval=1), [[1, 6.2], [10, 12]])
        self.assertEqual(p.intervals_clean(intervals_in, max_gap=0.8, min_interval=1), [[1, 8], [10, 12]])
        self.assertEqual(p.intervals_clean(intervals_in, max_gap=0.7999, min_interval=0),
                         [[1, 6.2], [7, 8], [10, 12], [14, 15]])
        # The result of this last case should be [[1, 6.2], [7, 8], [10, 12], [14, 15]] too, but round effect.
        self.assertEqual(p.intervals_clean(intervals_in, max_gap=0.8, min_interval=0), [[1, 8], [10, 12], [14, 15]])

        intervals_in = [[1, 6.2], [7, 8], [8, 12], [14, 15]]
        self.assertEqual(p.intervals_clean(intervals_in, min_interval=0), [[1, 6.2], [7, 8], [8, 12], [14, 15]])
        self.assertEqual(p.intervals_clean(intervals_in, max_gap=0.01, min_interval=0),
                         [[1, 6.2], [7, 12], [14, 15]])

    def test_merge_intervals(self):
        """
        Merge list of intervals [[start0, end0]...]
        """
        p = IntervalHandlers()

        self.assertEqual(p.merge_intervals([]), [])
        self.assertEqual(p.merge_intervals([[1, 3.14]]), [[1, 3.14]])
        self.assertEqual(p.merge_intervals([[1, 3.14], [3.14, 6.2]]), [[1, 6.2]])
        self.assertEqual(p.merge_intervals([[1, 3.14], [3.14, 6.2], [5, 6.0], [7, 8], [10, 12]]),
                         [[1, 6.2], [7, 8], [10, 12]])

    def test_overlap_2(self):
        """
        Get overlaps between 2 intervals and 2 list of intervals
        """
        import efinder.commons.intervals_handler as e

        self.assertEqual(e.get_overlap_2([3.14, 6.2], [5, 6.0]), [5, 6.0])
        self.assertEqual(e.get_overlap_2([1, 3.14], [3.14, 6.2]), [3.14, 3.14])
        self.assertEqual(e.get_overlap_2([1, 3.14], [4.0, 6.2]), None)
        self.assertEqual(e.get_overlap_2([1, 3.14], [3.0, 6.2]), [3.0, 3.14])

        intervals_in_1 = [[1, 6.2], [7, 8], [10, 12]]

        self.assertEqual(e.overlaps_2(intervals_in_1, [[6.21, 6.8]]), [])
        self.assertEqual(e.overlaps_2(intervals_in_1, [[6.0, 6.8]]), [[6.0, 6.2]])
        self.assertEqual(e.overlaps_2(intervals_in_1, [[6.2, 7]]), [[6.2, 6.2], [7, 7]])
        self.assertEqual(e.overlaps_2(intervals_in_1, [[6.0, 7.5]]), [[6.0, 6.2], [7, 7.5]])

    def test_overlap(self):
        """
        Get overlaps between 2 intervals and 2 list of intervals
        """
        import efinder.commons.intervals_handler as e

        self.assertEqual(e.get_overlap(3.14, 6.2, 5, 6.0), [5, 6.0])
        self.assertEqual(e.get_overlap(1, 3.14, 3.14, 6.2), [3.14, 3.14])
        self.assertEqual(e.get_overlap(1, 3.14, 4.0, 6.2), None)
        self.assertEqual(e.get_overlap(1, 3.14, 3.0, 6.2), [3.0, 3.14])

        intervals_in_1 = [[1, 6.2], [7, 8], [10, 12]]

        self.assertEqual(e.overlaps(intervals_in_1, [[6.21, 6.8]]), [])
        self.assertEqual(e.overlaps(intervals_in_1, [[6.0, 6.8]]), [[6.0, 6.2]])
        self.assertEqual(e.overlaps(intervals_in_1, [[6.2, 7]]), [[6.2, 6.2], [7, 7]])
        self.assertEqual(e.overlaps(intervals_in_1, [[6.0, 7.5]]), [[6.0, 6.2], [7, 7.5]])

    def test_not_intervals(self):
        """
        Get the complementary of a given list os intervals [start0, end0],...]
        :return:
        """

        p = IntervalHandlers()

        intervals_in = [[1, 6.2], [7, 8], [10, 12]]

        self.assertEqual(p.not_intervals(intervals_in), [[6.2, 7], [8, 10]])
        self.assertEqual(p.not_intervals(intervals_in, start=0, end=10), [[0, 1], [6.2, 7], [8, 10]])
        self.assertEqual(p.not_intervals(intervals_in, start=1, end=12), [[1, 1], [6.2, 7], [8, 10], [12, 12]])
        self.assertEqual(p.not_intervals([], start=0, end=10), [[0, 10]])

        intervals_in = [[1, 6.2]]
        self.assertEqual(p.not_intervals(intervals_in, start=1, end=12), [[1, 1], [6.2, 12]])


if __name__ == '__main__':
    unittest.main()
