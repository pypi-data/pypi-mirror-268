"""
Created on May, 2022

@author: Claudio Munoz Crego (ESAC)

This Module calculates the ground stations pass
"""

import logging
import spiceypy as spi
import numpy as np

from spiceypy import support_types as spi_support_types


class GfDistance:

    def get_distance_range_periods(self, gti, target, obsrvr, dist_min, dist_max, abcorr, adjust, interval):
        """
        Returns valid periods according to observer to target distance ranges (min, max) [km]

        For all gti (the etime start/end periods) in gti list

        - Calculate distance ranges using spice global finder
            where (max > distance > min  in km (i.e. [900000:0])

        - Generate new gti lists (using consecutive tt for each gti)

        Finally clean the resulting o_gti list
            (Normalizing a the Good Time Interval (GTI) - no overlapping and adjoining)

        :param gti: list of period including a start and end ephemeris time
                    (internal time used by spice library)
        :param target: Name/Id of the target body.
        :param obsrvr: Name/Id of the observing body.
        :param interval: dt step (i.e 100 seconds)
        :param dist_min: minimal distance in km
        :param dist_max: maximal distancedistance in km
        :param abcorr: Aberration correction flag; None by default
        :return: o_gti: list of ephemeris periods (as gti)
        """

        maxwin = 64000
        nintvals = 64000
        step = interval

        o_gti = []

        for i in range(len(gti)):

            start = gti[i][0]
            end = gti[i][1]

            results = gfdist_range(start, end, target, obsrvr, dist_min, dist_max, abcorr,
                                   step, nintvals, maxwin, adjust)

            if len(results) > 0:
                o_gti.extend(results)

        return o_gti

    def get_distance_periods(self, gti, target, obsrvr, ref_val, relate, abcorr, adjust, interval):
        """
        Returns valid periods according to observer to target distance ranges (min, max) [km]

        For all gti (the etime start/end periods) in gti list

        - Calculate distance ranges using spice global finder
            where (max > distance > min  in km (i.e. [900000:0])

        - Generate new gti lists (using consecutive tt for each gti)

        Finally clean the resulting o_gti list
            (Normalizing a the Good Time Interval (GTI) - no overlapping and adjoining)

        :param gti: list of period including a start and end ephemeris time
                    (internal time used by spice library)
        :param target: Name/Id of the target body.
        :param obsrvr: Name/Id of the observing body.
        :param interval: dt step (i.e 100 seconds)
        :param dist_min: minimal distance in km
        :param dist_max: maximal distancedistance in km
        :param abcorr: Aberration correction flag; None by default
        :return: o_gti: list of ephemeris periods (as gti)
        """

        maxwin = 64000
        nintvals = 64000
        step = interval

        o_gti = []

        for i in range(len(gti)):

            start = gti[i][0]
            end = gti[i][1]

            results = gfdist_related(start, end, target, obsrvr, ref_val, relate, abcorr,
                                   step, nintvals, maxwin, adjust)

            if len(results) > 0:
                o_gti.extend(results)

        return o_gti


def gfdist_range(e_stime, e_etime, target, obsrvr, dist_min, dist_max, abcorr='none', step=60,
                 nintvls=200, maxwin=4000, adjust=0):
    """
    Return the time window over which a specified constraint on
    observer-target distance is met.

    :param e_stime: ephemeris start time
    :param e_etime: ephemeris end time
    :param target: Name of the target body.
    :param obsrvr: Name of the observing body.
    :param abcorr: aberration correction; None by default
    :param step: number of seconds; 60s by default.
    :param nintvls: Workspace window interval count.
    :param maxwin: maximun number of pass allowed; 2000 by default
    :param relate: Relational operator.
    :param refval: Reference value.
    :param adjust: Adjustment value for absolute extrema searches.
    :return: results: SPICE window containing results.
    """

    cnfine = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    result = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    result_2 = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    spi.wninsd(e_stime, e_etime, cnfine)

    period = spi.wnfetd(cnfine, 0)
    # logging.debug("Period to search {} {} {}".format(spi.wncard(cnfine), spi.et2utc(period[0], 'C', 1, 35),
    #                                                spi.et2utc(period[1], 'C', 1, 35)))

    refval = dist_min
    relate = '>'

    spi.gfdist(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls, cnfine, result)

    nb_of_result = spi.wncard(result)

    results = []

    if nb_of_result == 0:
        logging.debug("Result window is empty!")
        return results
    else:

        refval = dist_max
        relate = '<'

        spi.gfdist(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls, result, result_2)

        nb_of_result = spi.wncard(result_2)

        results_2 = []

        if nb_of_result == 0:
            logging.debug("Result window is empty!")
        else:
            # logging.debug('Nb of events: {}'.format(nb_of_result))

            for i in range(nb_of_result):
                (start, end) = spi.wnfetd(result_2, i)
                results_2.append([start, end])

    return results_2


def gfdist_related(e_stime, e_etime, target, obsrvr, dist_condition, relate='>', abcorr='none', step=60,
                 nintvls=200, maxwin=4000, adjust=0):
    """
    Return the time window over which a specified constraint on
    observer-target distance is met.

    :param e_stime: ephemeris start time
    :param e_etime: ephemeris end time
    :param target: Name of the target body.
    :param obsrvr: Name of the observing body.
    :param abcorr: aberration correction; None by default
    :param step: number of seconds; 60s by default.
    :param nintvls: Workspace window interval count.
    :param maxwin: maximun number of pass allowed; 2000 by default
    :param relate: Relational operator.
    :param refval: Reference value.
    :param adjust: Adjustment value for absolute extrema searches.
    :return: results: SPICE window containing results.
    """

    cnfine = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    result = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    result_2 = spi_support_types.SPICEDOUBLE_CELL(maxwin)
    spi.wninsd(e_stime, e_etime, cnfine)

    period = spi.wnfetd(cnfine, 0)
    # logging.debug("Period to search {} {} {}".format(spi.wncard(cnfine), spi.et2utc(period[0], 'C', 1, 35),
    #                                                spi.et2utc(period[1], 'C', 1, 35)))

    refval = dist_condition

    spi.gfdist(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls, cnfine, result)

    nb_of_result = spi.wncard(result)

    results = []

    if nb_of_result == 0:

        logging.debug("Result window is empty!")

    else:

        for i in range(nb_of_result):
            (start, end) = spi.wnfetd(result, i)
            results.append([start, end])

    return results