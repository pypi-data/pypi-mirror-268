"""
Created on September 04, 2018

@author: Claudio Munoz Crego (ESAC)

This Module calculates the ground stations pass
"""

import spiceypy as spi
import numpy as np
from esac_juice_pyutils.gti import gti_handler


class GsElevation:

    def __call__(self, gti, body, g_station, elevation, interval):
        """
        Returns ground station pass according to elevation constraint (>elevation)

        For all git (the etime start/end periods) in gti list:
            for all the time tt in git:

            - Get the position y rectangular (cartesian) coordinates within <body>_TOPO, the topocentric reference of body

            - Convert latitude from rectangular coordinates to latitudinal coordinates.

            - Select time tt with latitude > elevation  in degrees (i.e. 10)

            - Generate new gti lists (using consecutive tt for each gti)

        Finally clean the resulting o_gti list
        (Normalizing a the Good Time Interval (GTI) - no overlapping and adjoining)

        :param body is the source object
        :param g_station: ground station ID
        :param gti: list of period including a start and end ephemeris time
                    (internal time used by spice library)
        :param: elevation in degrees (i.e. 10)
        :return: o_gti: list of ephemeris periods (as gti)
        """

        o_gti = []

        for i in range(len(gti)):

            start = gti[i][0]
            end = gti[i][1]

            n = int((end - start) / interval)
            dt = (end - start) / (n - 1)
            tt = np.array(range(n)) * dt + start

            (pos_body_vect, lvsta) = spi.spkpos(body, tt, g_station + '_TOPO', 'lt+s', g_station)

            # (radius, longitude, latitude) = spi.reclat(pos_body_vect)
            latitude = [spi.reclat(pos)[2] for pos in pos_body_vect]

            gs_index = [i for i, x in enumerate(latitude) if x > elevation * spi.rpd()]
            gs_etimes = list(tt[gs_index])

            t_gti = []
            if gs_index:
                t_gti = gti_handler.gti_seg(gs_etimes, min_gti=2*dt, max_gap=dt*1.05)

            if len(t_gti) > 0:
                if len(o_gti) == 0:
                    o_gti = t_gti
                else:
                    o_gti = o_gti.extend(t_gti)

        # if gti was not cleaned, we need to do it now
        o_gti = gti_handler.gti_trim(o_gti, max_gap=dt * 1.05, min_gti=dt)

        return o_gti
