"""
Created on June, 2017

@author: Claudio Munoz Crego (ESAC)

Json handler

"""

import logging
import os


def check_current_os():
    """

    :return:
    """

    from esac_juice_pyutils.commons.os_utils import CurrentOs

    current_os = CurrentOs()
    current_os.get_value()

    print('\nCurrent OS:')
    print(current_os.to_string)


if __name__ == '__main__':

    from esac_juice_pyutils.commons.my_log import setup_logger

    setup_logger('debug')
    print('local directory = ', os.getcwd())

    print('\n-----------------------------------------------\n')
    logging.debug('start test')

    check_current_os()

    logging.debug('End test')
