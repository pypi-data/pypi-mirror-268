"""
Created on November, 2017

@author: Claudio Munoz Crego (ESAC)

This file include utilities derived from os python module
"""

import os
import sys
import logging
import subprocess
import datetime


def get_path(path_string):
    """
    Get path corresponding to a given string:
    - Handle posix (windows) and no posix OS (unix like, mac os)
    - Expand OS environment variable

    :param path_string: absolute path (string)
    :return: path object
    """

    # Update slash according to OS (if needed)
    if os.name == 'posix':
        path_string = path_string.replace('\\', '/')
    else:
        path_string = path_string.replace('/', '\\')

    return os.path.expandvars(path_string)


class CurrentOs (object):

    def __init__(self):

        self.os = ''
        self.platform = ''
        self.release = ''

    def get_value(self):

        from sys import platform

        import platform as _platform

        if os.name == 'posix':
            self.os = 'posix'
            if platform == "linux" or platform == "linux2":
                self.platform = "linux"
                self.release = platform.release()
            else:   # Probably MAC OS : check it
                mac_os_version , _, _ = _platform.mac_ver()
                if mac_os_version:
                    # ' = float('.'.join(mac_os_version.split('.')[:2]))
                    self.platform = "mac_os"
                    self.release = platform + '_' + mac_os_version
                else:
                    sys.error('We have detected a unknow posix (unix like) version')
                    sys.exit()
        else:
            if platform == "win32":
                self.platform = "win32"
            elif platform == "win64":
                self.platform = "win32"

            self.release = platform.release()

    @property
    def to_string(self):

        s = '\n os = "{}"'.format(self.os) \
          + '\n platform = "{}"'.format(self.platform) \
          + '\n release = "{}"'.format(self.release) \

        return s
