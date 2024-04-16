"""
Created on April 3, 2017

@author: Claudio Munoz Crego (ESAC)

Class to handle eps event file

TODO: use antlr to parse and check the file

"""

import os
import re
import sys
import logging
import datetime
import pandas as pd
from operator import itemgetter


def read_eps_events(event_file_path):
    """
    Read event file in evf eps/MAPPS format
    :param event_file_path: path of the input event file
    :return list of events
    """
    if not os.path.exists(event_file_path):
        logging.error('event file {} does not exist'.format(event_file_path))

    df_dictionary = {}
    f = open(event_file_path, 'r')

    for line in f.readlines():
        # Try to read 24-Feb-2026_23:01:29
        mValue  = re.match(r'^([0-9]{1,2})\-([A-Za-z]{3})\-([0-9]{4})([0-9_:]{0,9})', line , re.M | re.I)
        mValue2 = re.match(r'^([0-9]{4})\-([0-9]{2})\-([0-9]{2})([0-9T:]{0,9})Z', line , re.M | re.I)

        if (mValue):
            date_time_str = mValue.group(1) + '-' + mValue.group(2) + '-' + mValue.group(3) + mValue.group(4)
            date_time = datetime.datetime.strptime(date_time_str, "%d-%b-%Y_%H:%M:%S")
            event_name = line.split()[1]

            if event_name not in df_dictionary.keys():
                df_dictionary[event_name] = [date_time]
            else:
                df_dictionary[event_name].append(date_time)

        elif (mValue2):
            date_time_str = mValue2.group(1) + '-' + mValue2.group(2) + '-' + mValue2.group(3) + mValue2.group(4)
            date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S")
            event_name = line.split()[1]

            if event_name not in df_dictionary.keys():
                df_dictionary[event_name] = [date_time]
            else:
                df_dictionary[event_name].append(date_time)

    return df_dictionary


def get_list_of_periods(file_path):
    """
    Get list of periods [[start, end], ...] fro EPS EVF file

    Note: The EVF file contain one unique event type

    :param file_path: evf file path
    :return: opp_periods: list of periods [[start, end], ...]
    """


    dico = read_eps_events(file_path)

    [val_start, val_stop] = list(dico.values())
    if len(val_start) != len(val_stop):

        logging.error('There is no pair of start/end values in SOE evf; Please Check file {}'.format(file_path))
        sys.exit()

    else:

        opp_periods = []
        for i in range(len(val_start)):
            s = datetime.datetime.strftime(val_start[i], '%Y-%m-%dT%H:%M:%S')
            e = datetime.datetime.strftime(val_stop[i], '%Y-%m-%dT%H:%M:%S')
            opp_periods.append([s, e])

    return opp_periods


class Evf(object):
    """
    This class allows to handle (read, write) eps event files
    """

    def __init__(self):
        pass

    def read_eps_events_aphelion_perihelion(self, event_file_path):
        """
        Read event file  the aphelion perihelion events
        :param event_file_path: path of the input event file
        :return panda frame
        """

        df_dictionary = read_eps_events(event_file_path)

        df = pd.DataFrame(df_dictionary)

        return df

    def write_aphelion_perihelion(self, eps_events, output_dir):

        df = self.read_eps_events_aphelion_perihelion(eps_events)
        df.to_csv(os.path.join('aphelion.csv'), sep=',')


class Eps_events(object):
    """
    This class allows to store and handle DataRateAvg Objects
    """

    def __init__(self, name=''):
        self.__name = name
        self.name_active = '{}_START'.format(name)
        self.name_inactive = '{}_END'.format(name)
        self.name_efinder = 'same'
        self.utc_start = datetime.datetime.now()
        self.utc_end = datetime.datetime.now()
        self.header = []
        self.data_title = []
        self.data_value = []

    def set_name(self, name):
        """
        Name setter
        :param name:
        """
        self.__name = name
        self.name_active = '{}_START'.format(name)
        self.name_inactive = '{}_END'.format(name)

    def get_name(self):
        """
        Name getter
        :return name: the event name
        """

        return self.__name

    def to_string(self):
        return 'name={}, {} - {}, {}'.format(self.name, self.utc_start, self.utc_end, self.data_value)
