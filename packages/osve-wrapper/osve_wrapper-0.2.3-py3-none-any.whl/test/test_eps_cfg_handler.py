"""
Created on April, 2021

@author: Claudio Munoz Crego (ESAC)

This module allow to test eps_cfg_handler.py
"""

import os
import sys
import logging

from esac_juice_pyutils.commons.my_log import setup_logger

from osve_wrapper.commons.eps_cfg_handler import EpsCfgHandler

if __name__ == "__main__":

    setup_logger('debug')

    logging.info('Start Test: running OSVE from python')

    file = '../osve_wrapper/templates/CONFIG/ISE/eps.cfg'

    p = EpsCfgHandler(file)

    print('POWER_MODEL:BATTERY_CAPACITY = {} Watts  '.format(p.eps_cfg_parameters['POWER_MODEL']['BATTERY_CAPACITY']))