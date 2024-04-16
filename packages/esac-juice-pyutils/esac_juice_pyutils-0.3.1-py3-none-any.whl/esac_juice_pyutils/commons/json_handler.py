"""
Created on June, 2017

@author: Claudio Munoz Crego (ESAC)

Json handler

"""

import os
import sys
import logging
import json

from collections import namedtuple


def _json_object_hook(d):
    """

    :param d:
    :return:
    """
    return namedtuple('X', d.keys())(*d.values())


def load_data(file_name):
    """

    :param file_name:
    :return:
    """

    with open(file_name, 'r') as file_data:
        return file_data.read().replace('\n', '')


def json2obj(file_name):
    """

    :param file_name:
    :return:
    """

    return json.loads(load_data(file_name), object_hook=_json_object_hook)


def create_file(file_name, data_store):
    """
    Create json file
    :param file_name:
    :param data_store:
    :return:
    """

    if file_name:

        with open(file_name, 'w') as f:
            json.dump(data_store, f, indent=4)

        f.close()

        logging.debug('file {} created'.format(file_name))


def load_to_dic(file_name):
    """

    :param file_name:
    :return: a python dictionary
    """

    data_store = {}

    if not os.path.exists(file_name):
        logging.error('path to json file does not exist: {}'.format(file_name))
        sys.exit()
    elif not os.path.isfile(file_name):
        logging.error('{} is not a file'.format(file_name))
        sys.exit()
    else:
        try:
            fd = open(file_name, 'r')
            data_store = json.load(fd)
            logging.debug('json file loaded:{}'.format(file_name))
        except Exception as ex:
            logging.error('Cannot read file; Please check file format: {}'.format(file_name))
            logging.error('Error args {} in {}'.format(file_name, ex.args))
            sys.exit()

    return data_store


def load_to_object(file_name):
    """

    :param file_name:
    :return: the corresponding object if to_object=True
    """

    data_object = None

    if not os.path.exists(file_name):
        logging.error('path to json file does not exist: {}'.format(file_name))
        sys.exit()
    elif not os.path.isfile(file_name):
        logging.error('{} is not a file'.format(file_name))
        sys.exit()
    else:
        try:
            data_object = json2obj(file_name)
            logging.debug('json file to object completed')
        except Exception as ex:
            logging.error('Cannot read file; Please check file format: {}'.format(file_name))
            logging.error('Error args {} in {}'.format(file_name, ex.args))
            sys.exit()

    return data_object
