"""
Created on October, 2019

@author: Claudio Munoz Crego (ESAC)

This Module allows to handle EDF files

"""

import os
import sys
import logging
import datetime
import pandas as pd


class EpsDefHandler(object):
    """
    This Class allows read and parse config data def file
    """

    def __init__(self, file_input, output_dir="./"):

        self.output_dir = output_dir

        self.event_defs = self.read(file_input)

    def read(self, input_file):
        """
        Read DEF File

        Note: We only get eps event names from this file

        :return: event_defs: dictionary including (key=event_name,values)
        """

        logging.debug('Reading def file: {}'.format(input_file))

        event_defs = {}

        if not os.path.exists(input_file):
            logging.error('DEF file "{0}" missing'.format(input_file))
            sys.exit()

        else:

            df = pd.read_csv(input_file, header=None, comment='#', engine='python')

            for line in list(df[0]):

                cols = line.split()
                (id, ev_name, ev_active, ev_inactive) = tuple(cols[:4])

                event_def = EventDef(id, ev_name, ev_active, ev_inactive)

                event_defs[ev_name] = event_def

        return event_defs

    def get_event_contents(self, event_id):
        """
        Get event content

        :return:
        """

        return self.event_defs[event_id]


class EventDef(object):
    """
    Model for event def file contents
    """

    def __init__(self, id, ev_name, ev_active, ev_inactive):

        self.id = id
        self.eps_names = EpsEventNames(ev_name, ev_active, ev_inactive)

    def to_dic(self):

        return {'id': self.id, 'eps_names': self.eps_names.to_dic()}


class EpsEventNames(object):
    """
    Model for event Eps Event Names contents
    """

    def __init__(self, ev_name, ev_active, ev_inactive):

        self.ev_name = ev_name
        self.ev_active = ev_active
        self.ev_inactive = ev_inactive

        single_ev = False
        if ev_active == ev_inactive:
            single_ev = True

        self.single_ev = single_ev

    def to_dic(self):

        return {'eps_ev_name': self.ev_name,
                'eps_ev_active': self.ev_active,
                'eps_ev_inactive': self.ev_inactive}

