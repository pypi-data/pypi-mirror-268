"""
Created on February 8, 2017

@author: Claudio Munoz Crego (ESAC)

This Module allows to read a configuration file
"""

try:
    import configparser as config_parser  # for Python 3
except ImportError:
    import ConfigParser as config_parser  # for Python

import logging
import os
import sys

import exm_pyutils.commons.os_utils as os_utils


class MyConfigParser(object):
    """
    This Class uses ConfigParser python Lib to handle commons Config Files
    """

    def __init__(self, config_file):

        self.config = config_parser.ConfigParser()
        self.configFile = config_file
        self.read()

    def read(self):
        """
        Reads input configuration file
        # """

        if os.path.exists(self.configFile):
            self.config.read(self.configFile)
        else:
            logging.error('Configuration File "{0}" not available'.format(self.configFile))

    def configSectionMap(self, section):
        """
        Returns a dictionary mapping a given configuration File sections

        :param section:
        :return:
        """

        sectionMap = {}
        options = self.config.options(section)
        for opt in options:
            sectionMap[opt] = self.config.get(section, opt)
            logging.debug('{0}:{1} =  {2} '.format(section, opt, self.config.get(section, opt)))

            if sectionMap[opt] is None:
                logging.debug('skip option {}'.format(opt))
                sys.exit(1)

        return sectionMap

    def configMap(self):
        """
        Returns a dictionary mapping the configuration File

        :return: configFileMap, a dictionary mapping the configuration File
        """

        configFileMap = {}
        for section in self.config.sections():
            configFileMap[section] = self.configSectionMap(section)

        return configFileMap

    def get_path(self, path_string):
        """
        Get path corresponding to a given string:

        :param path_string: absolute path (string)
        :return: path object
        """

        return os_utils.get_path(path_string)

    def missing_file(self, input_file_path, var_name, missing_file):
        """
        Check if the input file path exits
        if not raise an error and set missing_file = True
        :param input_file_path: path of input file
        :param var_name: name of configuration variable\
        :return: missing_file flag
        """

        if not os.path.exists(input_file_path):
            logging.error('path "{0}" does not exist; Review {1} parameter in {2}'.format(
                input_file_path, var_name, self.configFile))
            missing_file = True

        return missing_file
