"""
Created on January, 2021

@author: Claudio Munoz Crego (ESAC)

This module allows to wrap C++ OSVE tool
"""

import os
import logging

from esac_juice_pyutils.commons.my_log import setup_logger

from old_code.osve_wrapper import osve_exec_timeline

TDS_BASED_DIR = os.path.abspath('../TDS')


def test_osve_exec_timeline_ref():

    test_path = os.path.join(TDS_BASED_DIR, 'ref_crema_5_0_new_edf')
    config = os.path.join(test_path, 'config_osve_template.json')

    osve_exec_timeline(test_path, config)


def test_osve_exec_timeline_ref_renaming_eps_ouput():

    test_path = os.path.join(TDS_BASED_DIR, 'ref_crema_5_0_new_edf')
    config = os.path.join(test_path, 'config_osve_template.json')

    eps_output = os.path.join(test_path,'target/eps_output')

    osve_exec_timeline(test_path, config, eps_output=eps_output)


if __name__ == "__main__":

    setup_logger('debug')

    logging.info('Start Test: running OSVE from python')

    test_osve_exec_timeline_ref()

    # test_osve_exec_timeline_ref_renaming_eps_ouput()

    logging.info('End Test!')

