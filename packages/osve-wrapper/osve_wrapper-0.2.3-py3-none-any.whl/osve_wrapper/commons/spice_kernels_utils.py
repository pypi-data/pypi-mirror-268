"""
Created on April, 2021

@author: Claudio Munoz Crego (ESAC)

This file include utilities for spice kernel handling
"""

import os
import sys
import logging


def update_path_val_in_mk_file(path_to_metakernel, kernel_root_dir):
    """
    Update PATH_VALUES within a given mk file

    :param path_to_metakernel: metakernel file path
    :param kernel_root_dir: path to the spice kernel base directory (local copy)
    :return des: the path of the updated kernel file
    """

    if not os.path.exists(path_to_metakernel):
        logging.error('metakernel file does not exist: {}'.format(path_to_metakernel))
        sys.exit()

    if not os.path.exists(kernel_root_dir):
        logging.error('directory does not exist: {}'.format(kernel_root_dir))
        sys.exit()

    fi = open(path_to_metakernel, 'r')
    lines = fi.readlines()
    fi.close()

    fo = open(path_to_metakernel, 'w')
    for line in lines:

        if 'PATH_VALUES' in line:

            line_without_space = line.replace(' ', '').replace('\t', '')

            if line_without_space.startswith('PATH_VALUES'):
                s = line.split("'")
                line = "'".join([s[0], kernel_root_dir, s[2]])

        fo.write(line)

    fo.close()

    logging.info('PATH_VALUES set to "{}" in metakernel file copy: {}'.format(kernel_root_dir, path_to_metakernel))
