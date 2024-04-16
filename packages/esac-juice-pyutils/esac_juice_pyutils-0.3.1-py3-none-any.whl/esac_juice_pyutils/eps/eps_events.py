"""
Created on April 3, 2017

@author: Claudio Munoz Crego (ESAC)

Class to handle eps event file

"""

import datetime


class EpsEvent(object):
    """
    This class allows to store and handle EPS event Objects
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
