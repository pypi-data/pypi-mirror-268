"""
Created on June, 2017

@author: Claudio Munoz Crego (ESAC)

Json handler

"""

import logging
import os

from exm_pyutils.commons import json_handler as my_json


def test_create_json_file(file_name='exm_scheduler.json'):
    """
    Create jason file
    :param file_name:
    :param data_store:
    :return:
    """

    data = {"people":[{"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}]}
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    data = '{"name": "John Smith", "exmgeo_event": {"ATNS": "New York", "ATNE": 123}}'

    data = {"parameters": {"rcal_list": "New York"}, "exmgeo_event": {"ATNS": "New York", "ATNE": 123}}

    my_json.create_file(filename, data)


def test_create_json_file_and_generate_object(file_name='exm_scheduler.json'):
    """
    Create jason file
    :param file_name:
    :param data_store:
    :return:
    """

    data = {"people":[{"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}]}
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    data = '{"name": "John Smith", "exmgeo_event": {"ATNS": "New York", "ATNE": 123}}'

    data = '{"parameters": {"rcal_list": "New York"}, "exmgeo_event": {"ATNS": "New York", "ATNE": 123}}'

    my_json.create_file(filename, data)

    x = my_json.load_to_object('exm_scheduler.json')

    print(x.exmgeo_event.ATNE)


def test_create_json_file_for_exmgeo(file_name='exm_scheduler.json'):
    """
    Create jason file
    :param file_name:
    :param data_store:
    :return:
    """

    data = {"parameters": {"slew_orbit_nadir": 600,
                           "slew_relay_communication": 300,
                           "rcal_list": [["2018-08-22T10:00:00", 8 * 3600],
                                        ["2018-08-23T12:00:00", 8 * 3600],
                                        ["2018-08-24T12:00:00", 8 * 3600],
                                        ["2018-08-25T12:00:00", 8 * 3600],],
                           "pattern": ["NO", "NO", "AS"],
                           "lno_night_limit": 1320,
                           "uvis_night_limit": 720,
                           "merge_limit": 720,
                           "grazing_limit": 150,
                           "occ_ptr_offset": 3.5,
                           "acs_nir_nadir": 20.,
                           "acs_nirnad_tn2d_offset": 20.,
                           "na": 4,
                           "ca": 0,
                           "flip_beta_limit": 30.8,
                           "flip_alt_orbit_limit": 3135,
                           "flip_alt_td2n_limit": 2627,
                           "cas_s_tn2d_offset": 20,
                           "cas_s_duration": 5,
                           "cas_c_tn2d_offset": 45,
                           "cas_c_duration": 1,
                           "wol_duration": 30,
                           "wol_tn2d_offset": 14.5,
                           "flip_offset": 29.5,
                           "flip_nad_duration": 10,
                           "occ_beta_limit": 59.2,
                           },
            "exmgeo_event":{
                             "FRND": "EXMGEO_FRND",
                             "FEND": "EXMGEO_FEND",
                             "MASN": "EXMGEO_MASN",
                             "TN2D": "EXMGEO_TN2D",
                             "OWOL": "EXMGEO_OWOL",
                             "OWOM": "EXMGEO_OWOM",
                             "MWOL": "EXMGEO_MWOL",
                             "MWOM": "EXMGEO_MWOM",
                             "CSSS": "EXMGEO_CSSS",
                             "CSSE": "EXMGEO_CSSE",
                             "CSIS": "EXMGEO_CSIS",
                             "CSIE": "EXMGEO_CSIE",
                             "ADNS": "EXMGEO_ADNS",
                             "ADNE": "EXMGEO_ADNE",
                             "FLIP": "EXMGEO_FLIP",
                             "I250": "EXMGEO_I250",
                             "I000": "EXMGEO_I000",
                             "E000": "EXMGEO_E000",
                             "E250": "EXMGEO_E000",
                             "ATNE": "EXMGEO_ATNE",
                             "ATNS": "EXMGEO_ATNS",
                             "AUI0": "EXMGEO_AUI0",
                             "AUI2": "EXMGEO_AUI2",
                             "AUIS": "EXMGEO_AUIS",
                             "AUIE": "EXMGEO_AUIE",
                             "AUMI": "EXMGEO_AUMI",
                             "AUMO": "EXMGEO_AUMO",
                             },
            }

    # data = '{}'.format(data)
    my_json.create_file(filename, data)


def test_read_json_file(file_name='exm_scheduler.json'):
    """

    :param file_name:
    :return:
    """

    data_store = my_json.load_to_dic(file_name)

    print(data_store)

if __name__ == '__main__':

    from exmgeo.commons.my_log import setup_logger

    setup_logger('debug')
    print('local directory = ', os.getcwd())

    print('\n-----------------------------------------------\n')
    logging.debug('start test')

    filename = '../test_files_2/exm_scheduler.json'

    # test_create_json_file(filename)

    test_create_json_file_for_exmgeo(filename)
    test_read_json_file(filename)
    # #
    # print '------'
    x = my_json.load_to_object(filename)
    print(x.exmgeo_event.ATNE)
    #
    # print x.parameters.rcal_list
