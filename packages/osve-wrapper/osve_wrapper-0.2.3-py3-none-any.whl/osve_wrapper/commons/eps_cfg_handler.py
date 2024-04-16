"""
Created on March, 2021

@author: Claudio Munoz Crego (ESAC)

This Module allows to handle (parse, load) eps.cfg file
"""

import logging
import os

import sys
import pandas as pd
import datetime

from esac_juice_pyutils.commons.my_log import setup_logger


class EpsCfgHandler(object):
    """
    This Class allows read and parse Juice eps.cfg file
    """

    def __init__(self, file_input, output_dir="./"):

        self.output_dir = output_dir

        self.input_file = file_input

        self.eps_lines = self.read()

        self.eps_cfg_parameters = self.get_eps_cfg_info()

    def read(self):
        """
        Read eps.cfg file

        :return: key_values
        """

        if not os.path.exists(self.input_file):
            logging.error('eps.cfg file does not exist: {}'.format(self.input_file))
            sys.exit()

        f = open(self.input_file, 'r')

        eps_lines = []

        record = ''
        for line in f.read().splitlines():

            if not line.startswith('#') and line != '':

                eps_lines.append(line.strip())

        return eps_lines

    def get_eps_cfg_info(self):
        """
        get power and resource info from eps.cfg
        :return:
        """

        eps_contents = {}

        for line in self.eps_lines:

            if line.startswith('Power_model') or line.startswith('Resource'):

                record = line.strip().split(':')

                key = record[0].replace(' ', '').upper()

                if '#' in record[1]:

                    record[1] = record[1].split('#')[0]

                values = record[1].rstrip().split()

                if len(values) > 1:

                    if values[1][0].isdigit():
                        values[1] = float(values[1])

                    val = [values[1:]]

                    if key not in eps_contents.keys():
                        eps_contents[key] = {}

                    if values[0] not in eps_contents[key].keys():

                        eps_contents[key][values[0]] = val

                    else:

                        eps_contents[key][values[0]].extend(val)

        # from collections import namedtuple
        #
        # power_model = namedtuple('Struct', eps_contents['Power_model'].keys())(*eps_contents['Power_model'].values())
        # resource = namedtuple('Struct', eps_contents['Power_model'].keys())(*eps_contents['Power_model'].values())

        return eps_contents

    def get_brf(self):
        """
        get brf file name in eps.cfg
        :return: file_name
        """

        file_names = []
        for ele in self.eps_cfg_parameters['RESOURCE']['DOWNLINK_RATE']:

            file_name = ele[-2]
            file_name = file_name.replace('"', '')
            if file_name not in file_names:
                file_names.append(file_name)

        return file_names

    def get_cell_efficiency_file(self):
        """
        get cell efficiency file name in eps.cfg
        :return: file_name
        """

        file_name = self.eps_cfg_parameters['RESOURCE']['PM_SA_CELL_EFFICIENCY'][0][1]
        file_name = file_name.replace('"', '')

        return file_name

    def get_cell_counter_file(self):
        """
        get cell counter file name in eps.cfg
        :return: file_name
        """

        if len(self.eps_cfg_parameters['RESOURCE']['PM_SA_CELL_COUNT'][0]) > 1:
            file_name = self.eps_cfg_parameters['RESOURCE']['PM_SA_CELL_COUNT'][0][1]
            file_name = file_name.replace('"', '')
        else:
            logging.warning("cannot get RES_SA_CELLS_COUNT file name from eps_crema_X_Y.cfg; using default value {}".format(self.eps_cfg_parameters['RESOURCE']['PM_SA_CELL_COUNT'][0][0]))
            file_name = None

        return file_name


def reset_brf(eps_file_path, bite_rate_file_name):
    """
    Reset bit rate file (name) within eps.cfg file

    :param bite_rate_file_name: brf file name
    :param eps_file_path: eps.cfg pat
    """

    f = open(eps_file_path, 'r')
    lines = f.readlines()
    f.close()

    f = open(eps_file_path, 'w')
    for record in lines:

        if record.startswith('Resource'):

            if 'DOWNLINK_RATE' in record:
                brf_fields = record.split('"')
                brf_fields[1] = bite_rate_file_name
                record = '"'.join(brf_fields)

                logging.info(
                    'BRF file name for DOWNLINK_RATE reset in eps.cfg to "{}" in{}'.format(
                        bite_rate_file_name, eps_file_path))

        f.write(record)

    f.close()


def reset_cell_efficiency(eps_file_path, cell_efficiency_file_name):

    f = open(eps_file_path, 'r')
    lines = f.readlines()
    f.close()

    f = open(eps_file_path, 'w')
    for record in lines:

        if record.startswith('Resource'):

            if 'PM_SA_CELL_EFFICIENCY' in record:
                fields = record.split('"')
                fields[1] = cell_efficiency_file_name
                record = '"'.join(fields)

                logging.info(
                    'Cells efficiency file name for PM_SA_CELL_EFFICIENCY reset in eps.cfg to "{}" in{}'.format(
                        cell_efficiency_file_name, eps_file_path))

        f.write(record)

    f.close()