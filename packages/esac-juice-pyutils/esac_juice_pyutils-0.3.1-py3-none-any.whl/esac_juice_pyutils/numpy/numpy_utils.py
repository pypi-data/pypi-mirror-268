#!/usr/bin/python
"""
Created on November 20, 2018

@author: Claudio Munoz Crego (ESAC)

This module is a container included functions to handle numpy arrays
Mainly to simplify code reading

"""
import numpy as np
import logging


def normalize(x, axis):
    """
    Normalize numpy array following axis

    :param x : array_like
        Input array.  If `axis` is None, `x` must be 1-D or 2-D.
    :param axis : {int, 2-tuple of ints, None}, optional
        If `axis` is an integer, it specifies the axis of `x` along which to
        compute the vector norms.  If `axis` is a 2-tuple, it specifies the
        axes that hold 2-D matrices, and the matrix norms of these matrices
        are computed.  If `axis` is None then either a vector norm (when `x`
        is 1-D) or a matrix norm (when `x` is 2-D) is returned.
    :return: x_normed, normalized array according to a given axis
    """

    if type(x) is np.ndarray:
        pass
    else:
        logging.warning('x is not a numpy array!; Convert it ')
        x = np.array(x, dtype=np.float64)

    if x.ndim > 1:

        if axis == 1:

            # x_norm = np.apply_along_axis(np.linalg.norm, 1, x)
            x_norm = np.linalg.norm(x, axis=1)
            x_normed = (x.T / x_norm.T).T

    else:

        x_norm = np.linalg.norm(x, axis=axis)
        
        if x_norm == 0:
            x_norm = np.finfo(x.dtype).eps

        x_normed = x / x_norm

    return x_normed


def normalize_2(x, axis):
    """
    Normalize numpy array following axis

    :param x : array_like
        Input array.  If `axis` is None, `x` must be 1-D or 2-D.
    :param axis : {int, 2-tuple of ints, None}, optional
        If `axis` is an integer, it specifies the axis of `x` along which to
        compute the vector norms.  If `axis` is a 2-tuple, it specifies the
        axes that hold 2-D matrices, and the matrix norms of these matrices
        are computed.  If `axis` is None then either a vector norm (when `x`
        is 1-D) or a matrix norm (when `x` is 2-D) is returned.
    :return: x_normed, normalized array according to a given axis
    """

    import vectormath as vmath

    v_array = vmath.Vector3Array(x)
    return v_array.normalize()


def norm(x, ord=None, axis=None, keepdims=False):
    """
    Matrix or vector norm.

    This function is able to return one of eight different matrix norms,
    or one of an infinite number of vector norms (described below), depending
    on the value of the ``ord`` parameter.

    Parameters
    ----------
    x : array_like
        Input array.  If `axis` is None, `x` must be 1-D or 2-D.
    ord : {non-zero int, inf, -inf, 'fro', 'nuc'}, optional
        Order of the norm (see table under ``Notes``). inf means numpy's
        `inf` object.
    axis : {int, 2-tuple of ints, None}, optional
        If `axis` is an integer, it specifies the axis of `x` along which to
        compute the vector norms.  If `axis` is a 2-tuple, it specifies the
        axes that hold 2-D matrices, and the matrix norms of these matrices
        are computed.  If `axis` is None then either a vector norm (when `x`
        is 1-D) or a matrix norm (when `x` is 2-D) is returned.
    keepdims : bool, optional
        If this is set to True, the axes which are normed over are left in the
        result as dimensions with size one.  With this option the result will
        broadcast correctly against the original `x`.
    """

    return np.linalg.norm(x, ord, axis, keepdims)


def normalize_array_of_3d_vectors(x):
    """

    :return:
    """

    x_norm = np.linalg.norm(x, axis=1)
    x_normed = (x.T / x_norm.T).T

    return x_normed
