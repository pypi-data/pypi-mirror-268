"""
Created on February 2021

@author: Claudio Munoz Crego (ESAC)

This Module allow to set environment variables like $HOME
only defined for python when running this code.


"""

import os
import sys
import logging


class EnvVar(object):
    """
    This class allows to set environment variables
    """

    def __init__(self, var_names):

        self.var_names = var_names
        self.set_env_var(var_names)

    def set_env_var_to_path(self, var_name, var_path):
        """
        Set local Environment to a given path (if exists)

        :param var_name: Local variable name
        :param var_path: Local path
        :return:
        """

        var_path = os.path.expandvars(var_path)

        if os.path.exists(var_path):
            os.environ[var_name] = var_path
            logging.info('{} set to {}'.format(var_name, os.getenv(var_name)))
            if var_name not in os.environ.keys():
                logging.error('{} has just be set and should be defined!')
        else:
            logging.error('Bad Environment variable "{}"; path does not exist: {}'.format(var_name, var_path))
            sys.exit()

    def set_env_var(self, var_names):
        """
        Set env variables
        :param var_names:
        """

        for k, v in var_names.items():

            self.set_env_var_to_path(k, v)


if __name__ == '__main__':

    from esac_juice_pyutils.commons.my_log import setup_logger

    here = os.path.abspath(os.path.dirname(__file__))
    test_dir = os.path.dirname(here)

    print(here)
    print(test_dir)

    setup_logger('debug')
    print(os.getcwd())

    print('\n-----------------------------------------------\n')

    logging.debug('Start of test')

    my_env_var = {'$HOME': '/Users/cmunoz',
                  '$DESKTOP': '$HOME/Desktop'}

    EnvVar(my_env_var)

    print('$HOME = {}'.format(os.getenv('HOME')))
    print('$DESKTOP = {}'.format(os.getenv('$DESKTOP')))

    logging.debug('End of test')

