"""
Created on January, 2021

@author: Claudio Munoz Crego (ESAC)

This module allows to wrap C++ OSVE tool
"""

import os
import sys
import logging

from esac_juice_pyutils.commons.my_log import setup_logger
from esac_juice_pyutils.commons.env_variables import EnvVar

from osve_wrapper.osve_advanced_wrapper import run_osve, preproc

TDS_BASED_DIR = os.path.abspath('../TDS')


def test_run_osve_automated(path_to_osve_lib_dir="../../osve/lib/mac"):
    """
    Test run_osve automated for a given EPS package and experiment type(s)
    """

    working_dir = os.path.join(TDS_BASED_DIR, "ref_crema_5_0_new_edf")

    here = os.path.abspath(os.path.dirname(__file__))
    os.chdir(working_dir)

    experiment_types = ['instrument_type']
    experiment_type = experiment_types[0]

    json_data = \
        {
            'scenario': 'eps_package',
            'crema_id': 'crema_5_0',
            'juice_conf': "$JUICE_CONF",
            "no_used_metakernel": "$JUICE_CONF/internal/common/osve_config/crema_5_0/osve_crema_5_0.tm",
            "kernel": {
                 "local_root_dir":"$HOME/juice_kernels",
                 "remote_url": "ftp://spiftp.esac.esa.int/data/SPICE/JUICE/kernels/",
                 "update": 1
            },
            "evf_data": "TOP_events.evf",
            "itl_data": "ITL/TOP_timelines.itl",
            "edf_data": "EDF/TOP_experiments.edf",
            "ptr": "spice_segmentation_attitude_5_0.json",
            "no_used_path_to_geopipeline_data": "$JUICE_CONF/internal/geopipeline/output",
            "no_path_eps_cfg": "$JUICE_CONF/internal/common/osve_config/crema_3_0/eps_crema_3_0.cfg",
            'simu_time_step': 60,
            'output_time_step': 600,
            "simu_output_dir": 'simu',
            "create_ckAttitudeFile": 1,
            "create_simOutputFile": 1,
            "create_attitudeXmlPtr": 1,
            "path_to_osve_lib_dir": path_to_osve_lib_dir,
            "start_timeline": "2031-06-11T22:15:00",
            "end_timeline": "2031-06-12T03:50:00"
        }

    from collections import namedtuple

    osve_parameters = namedtuple('Struct', json_data.keys())(*json_data.values())

    experiment_type_relative_path = os.path.join(json_data['scenario'], experiment_type)
    run_osve(working_dir, osve_parameters, experiment_type_relative_path)

    os.chdir(here)


if __name__ == "__main__":

    setup_logger('info')

    logging.info('Start Test: running OSVE from python')

    my_env_var = {'HOME': '/Users/cmunoz',
                  'OSVE_LIB': '$HOME/python3/osve_wrapper/osve/lib/mac',
                  'JUICE_KERNELS': '$HOME/juice_kernels',
                  'JUICE_CONF': '$HOME/python3/juice_configuration'}

    EnvVar(my_env_var)

    # test_run_osve_automated('$OSVE_LIB')
    # test_run_osve_automated('$HOME/python3/osve_wrapper/test')
    test_run_osve_automated('../../../simphony-deliveries/osve/bin/mac')

    logging.info('End Test!')

