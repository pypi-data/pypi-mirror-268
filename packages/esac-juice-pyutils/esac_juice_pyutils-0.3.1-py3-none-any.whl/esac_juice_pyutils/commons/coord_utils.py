"""
Created on February, 2020

@author: Claudio Munoz Crego (ESAC)

This Module include vectorized method fro coordinates transformation
The aim here is to improve the performance

"""

import logging
import numpy as np


def latlong2cartesian2(r, theta, phi):
    """
    Translate array of equatorial radius, latitude, longitude to cartesian coordinates

        X = R * cos(phi) * sin(theta)
        Y = R * sin(phi) * sin(theta)
        Z = R * cos(theta)

        where:
         R = (X**2 + Y**2 + Z**2)**(1/2)
         latitude = theta = acos(Z/R)
         longitude = phi = atang2(Y/X)

    - radius     Distance of the point from the origin.
    - longitude  Longitude of the point in radians.
    - latitude   Latitude of the point in radians.

    :param xyx_coord: numpy array of [x, y, z] cartesian/rectangular coordinates
    :return: r, lat, long rlatlong_coord: numpy array of [r, lat, lon]
    """

    x = r * np.cos(phi) * np.sin(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(theta)

    return np.vstack((x, y, z)).T


def cartesian2latlong(xyx_coord):
    """
    Translate array of cartesian coordinates to equatorial radius, latitude, longitude

        X = R * cos(phi) * sin(theta)
        Y = R * sin(phi) * sin(theta)
        Z = R * cos(theta)

        where:
         R = (X**2 + Y**2 + Z**2)**(1/2)
         latitude = theta = acos(Z/R)
         longitude = phi = atang2(Y/X)

    - radius     Distance of the point from the origin.
    - longitude  Longitude of the point in radians.
    - latitude   Latitude of the point in radians.

    :param xyx_coord: numpy array of [x, y, z] cartesian/rectangular coordinates
    :return: r, lat, long rlatlong_coord: numpy array of [r, lat, lon]
    """
    if xyx_coord.ndim == 1:

        [x, y, z] = list(xyx_coord)

    elif xyx_coord.ndim == 2:

        (x, y, z) = (xyx_coord[:, 0], xyx_coord[:, 1], xyx_coord[:, 2])

    r = np.sqrt(x*x + y*y + z*z)
    lat = np.arccos(z/r)
    long = np.arctan2(y, x)

    return r, lat, long


def rec2lat(xyx_coord, split=False):
    """
    Convert from rectangular coordinates to latitudinal coordinates.

    Note: This is a vectorized version using numpy providing the spiceypy reclat functionality
    - The default ouput is like as numpy.vstak(spiceypi.reclat(xyx_coord))
    - The flag split allows to get directly radius, latitude, longitude as three 1D arrays

    r: radius Distance of the point from the origin.

              The units associated with `radius' are those
              associated with the input `rectan'.

   long: longitude  Longitude of the input point.  This is angle between the
              prime meridian and the meridian containing `rectan'.  The
              direction of increasing longitude is from the +X axis
              towards the +Y axis.

              Longitude is output in radians. The range of `longitude'
              is [-pi, pi].


   lat: latitude   Latitude of the input point.  This is the angle from
              the XY plane of the ray from the origin through the
              point.

              Latitude is output in radians.  The range of `latitude'
              is [-pi/2, pi/2].

    :param xyx_coord:
    :param split: A flag allowing to split equatorial radius, latitude, longitude as three 1D arrays instead of (2D) array
    :return: radius, longitude, latitude
    """

    r, lat, long = cartesian2latlong(xyx_coord)
    lat = np.pi/2. - lat

    if split:

        return r, long, lat

    else:

        reclat = np.stack([r, long, lat]).T

        return reclat


def lat2rec(r, long, lat):
    """
    Convert from rectangular coordinates to latitudinal coordinates.

    Note: This is a vectorized version using numpy providing the spiceypy reclat functionality

    r: radius Distance of the point from the origin.

              The units associated with `radius' are those
              associated with the input `rectan'.

    long: longitude  Longitude of the input point.  This is angle between the
              prime meridian and the meridian containing `rectan'.  The
              direction of increasing longitude is from the +X axis
              towards the +Y axis.

              Longitude is output in radians. The range of `longitude'
              is [-pi, pi].


    lat: latitude   Latitude of the input point.  This is the angle from
              the XY plane of the ray from the origin through the
              point.

              Latitude is output in radians.  The range of `latitude'
              is [-pi/2, pi/2].

    :param xyx_coord:
    :param split: A flag allowing to split equatorial radius, latitude, longitude as three 1D arrays instead of (2D) array
    :return: radius, longitude, latitude
    """

    xyz = latlong2cartesian2(r, lat, long)

    return xyz

#
# if __name__ == '__main__':
#
#     from esac_cjmc_pyutils.commons.my_log import setup_logger
#
#     print('\n-----------------------------------------------\n')
#     # setup_logger()
#     setup_logger('debug')
#
#     a = 1. / np.sqrt(3.)
#     xyz = np.asarray([[0, 0, 1], [0, 1, 0], [1, 0, 0], [a, a, a]])
#
#     logging.info('xyz input')
#     print(xyz)
#
#     r, lat, long = cartesian2latlong(xyz)
#
#     reclat = rec2lat(xyz)
#     logging.info('xyz -- >reclat')
#     print(reclat)
#
#     logging.info('reclat -- >xyz')
#     my_xyz = np.round(latlong2cartesian2(r, lat, long), 8)
#     print(my_xyz)
#
#     logging.info('reclat -- >xyz')
#     my_xyz = np.round(lat2rec(r, long, lat), 8)
#     my_xyz = lat2rec(r, long, lat)
#     print(my_xyz)





