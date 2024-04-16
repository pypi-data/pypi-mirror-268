"""
Created on August, 2022

@author: Marc Costa Sitja (ESAC)

Test download kernels from MK

"""

import logging
import os
import spiceypy


def test_download_metakernels():
    """Test downloading kernels from a meta-kernel """

    from esac_juice_pyutils.spiceypi.spice_kernel_utils import get_kernel_loaded_info

    spiceypy.furnsh('/Users/marc.costa/spice/juice/kernels/mk/juice_crema_5_0b23_1_local.tm')
    info = get_kernel_loaded_info()
    pass


if __name__ == '__main__':

    from esac_juice_pyutils.commons.my_log import setup_logger

    setup_logger('debug')
    print('local directory = ', os.getcwd())

    print('\n-----------------------------------------------\n')
    logging.debug('start test')

    test_download_metakernels()

    logging.debug('End test')
