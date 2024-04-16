"""
Created on October 2019

@author: Claudio Munoz Crego (ESAC)

Unit Tests for litl_parser

"""

import os
import unittest

from exm_ptr.commons.eps_def_file_handler import EpsDefHandler

test_files_dir = '../../test_files'


class MyTestCase(unittest.TestCase):

    def test_read_config_data_def_file(self):
        """
        Test read and parse TGO config_data def file
        """

        path_to_def_file = os.path.join(test_files_dir, 'MAPPS/CONFIG_DATA/events.tgo.def')

        p = EpsDefHandler(path_to_def_file)

        # print(p.event_defs['GS_DUMP'].to_dic())

        self.assertEqual(p.event_defs['GS_DUMP'].to_dic(), {
            'id': '0001',
            'eps_names': {'eps_ev_active': 'GS_DUMP_START',
                          'eps_ev_inactive': 'GS_DUMP_END',
                          'eps_ev_name': 'GS_DUMP'}})

