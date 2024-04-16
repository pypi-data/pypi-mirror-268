"""
Created on January, 2021

@author: Claudio Munoz Crego (ESAC)

This file include utilities derived from os python module
"""

import os
import logging
import numpy as np

import sys


class CurrentOs(object):

    def __init__(self):

        self.os = ''
        self.platform = ''
        self.release = ''

    def set_values(self):
        """
        Set Current OS information
        """

        from sys import platform

        import platform as _platform

        # print('os_name: {}'.format(os.name))
        # print('platform: {}'.format(platform))
        if os.name == 'posix':
            self.os = 'posix'
            if platform == "linux" or platform == "linux2":
                self.platform = "linux"
                self.release = _platform.release()
            else:  # Probably MAC OS : check it
                mac_os_version, _, _ = _platform.mac_ver()
                if mac_os_version:
                    # ' = float('.'.join(mac_os_version.split('.')[:2]))
                    self.platform = "mac_os"
                    self.release = platform + '_' + mac_os_version
                else:
                    sys.error('We have detected a unknow posix (unix like) version')
                    sys.exit()
        else:

            if platform == "win32":
                self.platform = "windows"
            elif platform == "win64":
                self.platform = "windows"

            self.release = _platform.release()

    @property
    def to_string(self):
        """
        Generate string report
        :return:
        """

        s = '\n os = "{}"'.format(self.os) \
            + '\n platform = "{}"'.format(self.platform) \
            + '\n release = "{}"'.format(self.release)

        return s


def get_current_os():
    """
    Get current os
    :return:
    """

    current_os = CurrentOs()
    current_os.set_values()
    return current_os
