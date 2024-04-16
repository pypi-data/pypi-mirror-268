"""
Created on January, 2021

@author: Claudio Munoz Crego (ESAC)

This is a simple wrapper Python wrapper for the C shared library

"""
# ctypes_test.py

import os
import sys
import ctypes, ctypes.util

from esac_juice_pyutils.commons.my_log import setup_logger
from esac_juice_pyutils.commons.env_variables import EnvVar


def load_c_lib(lib_path):
    """
    Load c/c++ library
    :return: c_lib
    """

    lib_path = os.path.expandvars(lib_path)

    c_lib_path = ctypes.util.find_library(lib_path)

    if not os.path.exists(c_lib_path):
        print("Unable to find the specified library in {}".format(lib_path))
        sys.exit()

    try:

        c_lib = ctypes.CDLL(c_lib_path)

    except OSError as err:
        print("Unable to load the system C library\n")
        print("OS error: {0}".format(err))
        sys.exit()

    return c_lib


if __name__ == "__main__":

    print('Start Test: running OSVE from python')
    setup_logger()

    my_env_var = {'HOME': '/Users/cmunoz',
                  'OSVE_LIB': '$HOME/python3/osve_wrapper/osve/lib/mac'}

    EnvVar(my_env_var)

    # Load c/c++ lib
    c_lib = load_c_lib(os.path.join('$OSVE_LIB', 'libosve-sim-if-sr'))

    # (if needed) make the function names visible at the module level and add types
    # And Run OSVE

    test_path = b'/Users/cmunoz/python3/osve_wrapper/TDS/ref_crema_5_0_new_edf'
    config = b'/Users/cmunoz/python3/osve_wrapper/TDS/ref_crema_5_0_new_edf/config_osve_template.json'

    # print('OSVE Version: {}'.format(c_lib.getAppVersion()))

    osve_exec = c_lib.executeTimeline
    osve_exec(test_path, config)

    print('End Test!')

