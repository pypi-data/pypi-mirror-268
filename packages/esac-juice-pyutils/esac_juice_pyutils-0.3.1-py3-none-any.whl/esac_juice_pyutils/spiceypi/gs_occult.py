"""
Created on November, 2019

@author: Claudio Munoz Crego (ESAC)

This Module calculates the periods when an observer sees one target
    occulted by, or in transit across, another..
"""

import logging
import spiceypy as spi

from spiceypy import support_types as spi_support_types
from spiceypy.utils.exceptions import SpiceyError

import esac_juice_pyutils.commons.tds_spicey as tds_spicey
from esac_juice_pyutils.gti import gti_handler


class GfOccult:

    def get_occultation_periods(self, gti, occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr,
                 interval=60):
        """
        Returns intervals when an observer sees one target occulted by, or in transit across, another..

        For all git (the etime start/end periods) in gti list
            call  gfoclt spice global finder method.

        :param gti: list of period including a start and end ephemeris time
                    (internal time used by spice library)
        :param occtyp: Type of occultation.
        :param front: Name of body occulting the other.
        :param fshape: Type of shape model used for front body.
        :param fframe: Body-fixed, body-centered frame for front body.
        :param back: Name of body occulted by the other.
        :param bshape: Type of shape model used for back body.
        :param bframe: Body-fixed, body-centered frame for back body.
        :param abcorr: Aberration correction flag; None by default
        :param obsrvr: Name of the observing body.
        :param step: number of seconds; 60s by default.
        :return: o_gti: list of ephemeris periods (as gti)
        """

        maxwin = 20000
        step = interval

        o_gti = []

        for i in range(len(gti)):

            start = gti[i][0]
            end = gti[i][1]

            try:

                results = self.gfoccult(start, end, occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr,
                                  step, maxwin)

                if len(results) > 0:
                    o_gti.extend(results)

            except SpiceyError as exc:

                # Display a message if an exception was thrown.
                # For simplicity, we treat this as an indication that the point of intersection was not found,
                # although it could be due to other errors. Otherwise, continue with the calculations.

                message = [l for l in exc.message.split('\n')[4:-1] if l != '']
                message = '; '.join(message)

                logging.warning(('{:s} at [{:d}: {:d}]: [{:s}: {:s}]'.format(
                    message, round(start), round(end),
                    tds_spicey.et2utc(start, format='%d-%b-%Y_%H:%M:%S'),
                                      tds_spicey.et2utc(end, format='%d-%b-%Y_%H:%M:%S'))))

        # Clean any empty gti/period
        o_gti = gti_handler.gti_trim(o_gti)

        return o_gti

    def gfoccult(self, e_stime, e_etime, occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr,
                 step=60, maxwin=4000):
        """
        Determine time intervals when an observer sees one target
        occulted by, or in transit across, another..

        :param e_stime: ephemeris start time
        :param e_etime: ephemeris end time
        :param occtyp: Type of occultation.
        :param front: Name of body occulting the other.
        :param fshape: Type of shape model used for front body.
        :param fframe: Body-fixed, body-centered frame for front body.
        :param back: Name of body occulted by the other.
        :param bshape: Type of shape model used for back body.
        :param bframe: Body-fixed, body-centered frame for back body.
        :param abcorr: Aberration correction flag; None by default
        :param obsrvr: Name of the observing body.
        :param step: number of seconds; 60s by default.
        :param maxwin: maximun number of pass allowed; 2000 by default
        :return: results: SPICE window containing results.
        """

        cnfine = spi_support_types.SPICEDOUBLE_CELL(maxwin)
        result = spi_support_types.SPICEDOUBLE_CELL(maxwin)
        spi.wninsd(e_stime, e_etime, cnfine)

        period = spi.wnfetd(cnfine, 0)
        logging.debug("Period to search {} {} {}".format(spi.wncard(cnfine), spi.et2utc(period[0], 'C', 1, 35),
                                                         spi.et2utc(period[1], 'C', 1, 35)))

        spi.gfoclt(occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr,
                   step, cnfine, result)

        nb_of_result = spi.wncard(result)

        results = []

        if nb_of_result == 0:
            logging.debug("Result window is empty!")
        else:
            logging.debug('Nb of events: {}'.format(nb_of_result))

            for i in range(nb_of_result):
                (start, end) = spi.wnfetd(result, i)
                results.append([start, end])

        return results


def get_non_occulted_periods(start, end, config):
    """
    Get the periods when the observer (i.e juice) cannot see the earth

    :return: non_occulted_period
    """

    gti = [[start, end]]

    occ_type = config['occtype']  # Full
    front = config['front']  # Jupiter
    fframe = config['fframe']  # IAU_JUPITER
    fshape = config['fshape']  # ELLIPSOID
    back = config['back']  # EARTH
    bframe = config['bframe']  # IAU_EARTH
    bshape = config['bshape']  # ELLIPSOID
    abcorr = config['abcorr']  # LT+S
    observer = config['observer']  # Juice
    interval = config['interval']  # 600 seconds usually used by global find

    occulted_periods = GfOccult().get_occultation_periods(
        gti, occ_type, front, fshape, fframe, back, bshape, bframe, abcorr, observer, interval=interval)

    non_occulted_period = gti_handler.gti_inverse(occulted_periods, start=start, end=end)

    return non_occulted_period


def get_occulted_periods_by_moon_plama_torus_dsk(gti, config_main):
    """
    Get the periods when the observer (i.e juice) cannot see the earth

    :return: non_occulted_period
    """

    config = config_main['earth_not_occulted']

    occ_type = 'ANY'  # Full
    front = config_main['torus_target_id']  # Jupiter
    fframe = config_main['dsk_frame']  # IAU_JUPITER
    fshape = 'DSK/UNPRIORITIZED'  # config['fshape']  # ELLIPSOID
    back = config['back']  # EARTH
    bframe = config['bframe']  # IAU_EARTH
    bshape = 'point'  # ELLIPSOID
    abcorr = "None"  # LT+S
    observer = config['observer']  # Juice
    interval = 600  # config['interval']  # 600 seconds usually used by global find

    occulted_periods = GfOccult().get_occultation_periods(
        gti, occ_type, front, fshape, fframe, back, bshape, bframe, abcorr, observer, interval=interval)

    # non_occulted_period = gti_handler.gti_inverse(occulted_periods, start=start, end=end)

    return occulted_periods