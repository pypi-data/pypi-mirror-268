"""
Created on February, 2021

@author: Claudio Munoz Crego (ESAC)

This module allows to wrap C++ OSVE tool, building the OSVE config file and CONF structure on the fly
for a given EPS package.

"""

import os
import sys
import shutil
import glob
import logging
from operator import itemgetter

import esac_juice_pyutils.commons.json_handler as my_json
import esac_juice_pyutils.spiceypi.spice_kernel_utils as spice_kernels_utils
from esac_juice_pyutils.commons.json_handler import load_to_object

from osve_wrapper.commons.eps_cfg_handler import EpsCfgHandler, reset_brf, reset_cell_efficiency
from osve_wrapper.commons.timeline_handling import create_itl_with_new_timeline_period, \
    set_simulation_start_end_time_filters


class OsveWrapper(object):

    def __init__(self, working_dir_path, scenario_dir, osve_parameters, no_ptr_cut=False):

        self.osve_parameters = osve_parameters
        self.scenario = scenario_dir
        self.working_dir = os.path.abspath(working_dir_path)
        self.no_ptr_cut = no_ptr_cut

        self.default_root_path = self.set_default_path()

        self.path_to_config_dir = self.get_copy_osve_config_structure()

        self.eps_cfg_path = self.add_eps_cfg()
        self.eps_cfg = EpsCfgHandler(self.eps_cfg_path)

        self.add_files_to_config_structure()

        self.metakernel_file_name = None

        self.top_itl = None

    def set_default_path(self):
        """
        set default path
        """

        here = os.path.abspath(os.path.dirname(__file__))
        template_file = os.path.join(here, 'templates')
        template_file = os.path.join(template_file, 'osve_wrapper_default_values.json')

        if not os.path.exists(template_file):
            logging.error('reference template file "%s" missing' % template_file)
            sys.exit()

        logging.info('{} loaded'.format(template_file))

        return my_json.load_to_object(template_file).default_paths

    def get_template_osve_config_file(self):
        """
        Get the default config_osve_template.json

        :return: eps_soa_template.cfg path
        :rtype: python path
        """

        here = os.path.abspath(os.path.dirname(__file__))
        template_file = os.path.join(here, 'templates')
        template_file = os.path.join(template_file, 'config_osve_template.json')

        if not os.path.exists(template_file):
            logging.error('reference template file "%s" missing' % template_file)
            sys.exit()

        logging.info('{} loaded'.format(template_file))

        return template_file

    def set_metakernel_path(self, osve_parameters):
        """
        Set metakernel path

        :param osve_parameters: osve parameters
        :return: path_to_metakernel
        """

        if hasattr(osve_parameters, 'metakernel'):

            path_to_metakernel = os.path.expandvars(osve_parameters.metakernel)
            if not os.path.exists(path_to_metakernel):
                path_to_metakernel = os.path.abspath(path_to_metakernel)

        elif hasattr(self.osve_parameters, 'juice_conf'):

            juice_conf = self.osve_parameters.juice_conf
            juice_conf = os.path.expandvars(juice_conf)
            crema_id = self.osve_parameters.crema_id
            eps_tm_file_param = self.default_root_path.eps_tm_file
            mk_file = '{}{}.{}'.format(eps_tm_file_param.prefix, crema_id, eps_tm_file_param.ext)
            # path_to_metakernel = os.path.join(juice_conf, *('internal', 'common', 'osve_config', crema_id, mk_file))
            path_to_metakernel = os.path.join(juice_conf, *(eps_tm_file_param.dir, mk_file))

        else:

            logging.error('"juice_conf" or "metakernel" must be defined in configuration file')
            sys.exit()

        if not os.path.exists(path_to_metakernel):

            logging.error('file does not exist: {}'.format(path_to_metakernel))
            sys.exit()

        return path_to_metakernel

    def get_copy_spice_metakernel(self, osve_parameters):
        """
        Copy metakernel file, and optionally reset "PATH_VALUES" to spice kernel

        1) set kernel local dir path
        2) set metakernel_path and copy to local directory
        3) update kernel local dir path in metakernel local copy if needed

        :param osve_parameters: osve parameters
        :return: des: the path of the metakernel file copy
        """

        kernel_root_dir = None
        print('>>>')
        print('kernel', osve_parameters.kernel)
        print('update', osve_parameters.kernel['update'])
        print('remote_url', osve_parameters.kernel['remote_url'])
        print(osve_parameters.kernel['local_root_dir'])

        if not hasattr(osve_parameters, 'kernel'):
            logging.error('kernel for osve configuration')
            sys.exit()

        if 'local_root_dir' in osve_parameters.kernel:

            kernel_root_dir = os.path.expandvars(osve_parameters.kernel['local_root_dir'])
            kernel_root_dir = os.path.abspath(kernel_root_dir)

            if not os.path.exists(kernel_root_dir):
                logging.warning('"kernel_root_dir" does not exists; {}'.format(kernel_root_dir))

        elif 'update' in osve_parameters.kernel:

            if osve_parameters.kernel['update']:

                kernel_root_dir = './kernels'
                if not os.path.exists(kernel_root_dir):
                    os.mkdir(kernel_root_dir)

        path_to_metakernel = self.set_metakernel_path(osve_parameters)
        file_name = os.path.basename(path_to_metakernel)
        dest = os.path.join(self.working_dir, file_name)

        shutil.copy(path_to_metakernel, dest)
        logging.info('metakernel file copy create: {}'.format(dest))

        self.metakernel_file_name = dest

        if kernel_root_dir is not None and kernel_root_dir != '':

            spice_kernels_utils.update_path_val_in_mk_file(self.metakernel_file_name, kernel_root_dir)

        if 'update' in osve_parameters.kernel:

            if osve_parameters.kernel['update']:

                kernel_to_load = spice_kernels_utils.read_files_in_mk_file(self.metakernel_file_name)

                if 'remote_url' in osve_parameters.kernel:
                    spice_kernels_utils.update_local_kernel_copy(kernel_to_load, osve_parameters.kernel['remote_url'])
                else:
                    spice_kernels_utils.update_local_kernel_copy(kernel_to_load)

        return dest

    def get_copy_osve_config_structure(self, src=None):
        """
        Copy the OSVE CONFIG directory structure within scenario path

        Note: This structure is in line with osve_template file and contain a set of fixed files

        CONFIG/
        ├── AGE
        └── ISE

        :param scenario_dir: scenario directory path
        :param src: path to a template CONF directory; Default None; take from template
        :return: osve_config_dir:  path the the OSVE CONFIG base directory
        """

        if src is None:

            here = os.path.abspath(os.path.dirname(__file__))
            conf_base_dir = os.path.join(here, 'templates')
            conf_base_dir = os.path.join(conf_base_dir, 'CONFIG')

        else:

            conf_base_dir = src

        osve_config_dir = os.path.join(self.working_dir, 'CONFIG')

        if os.path.exists(osve_config_dir):
            shutil.rmtree(osve_config_dir)

        shutil.copytree(conf_base_dir, osve_config_dir)
        logging.info('Copy of CONF structure copied to {}'.format(osve_config_dir))

        return osve_config_dir

    def add_files_to_config_structure(self):
        """
        Add all needed files to OSVE CONFIG directory structure within scenario path

        Note: This structure is in line with osve_template file. the file to copy are
        - eps.cfg; The EPS configuration file (Crema dependent)
        - events.juice.def; EPS condif file specifying even identifiers (no Crema dependent)
        - brf: the bite rate file (Crema dependent):  for instance BRF_MAL_HGA_290102_370523.asc
        - RES_C30_SA_CELLS_EFFICIENCY_yymmdd_yymmdd.asc; cell_efficiency file (Crema dependent)

        CONFIG/
        └── AGE
            ├── AGMConfig_PT.xml
            ├── CFG_AGM_JUI_MULTIBODY_FIXED_DEFINITIONS.xml
            ├── cfg_agm_jui_multibody_event_definitions.xml
            └── CFG_AGM_JUI_MULTIBODY_PREDEFINED_BLOCK.xml
        └── ISE
            ├── eps.cfg
            ├── events.juice.def
            ├── BRF_MAL_HGA_yymmdd_yymmdd.asc
            ├── RES_C30_SA_CELLS_EFFICIENCY_yymmdd_yymmdd.asc
            └── units.def
        """

        self.add_event_juice_def()

        brf = self.eps_cfg.get_brf()
        cell_eff = self.eps_cfg.get_cell_efficiency_file()
        cell_counter = self.eps_cfg.get_cell_counter_file()

        self.add_brf(brf)

        self.add_cells_efficiency(cell_eff)

        self.add_cells_counter(cell_counter)

        self.add_unit_file()

        self.add_agm_multibody_definition_files()

    def get_ptr_copy(self, experiment_type, root_dir):
        """
        Copy PTR (attitude file) to EPS output experiment sub-folder

        :param root_dir: root directory
        :param experiment_type: name of EPS experiment sub_folder (i.e. instrument_type, target)
        :return dest: path of ptr copy
        """

        if hasattr(self.osve_parameters, 'ptr'):

            ptr_path = os.path.expandvars(self.osve_parameters.ptr)

            if not os.path.isfile(ptr_path):

                if not os.path.exists(ptr_path):

                    ptr_path = os.path.join(root_dir, ptr_path)

                    if not os.path.exists(ptr_path):
                        logging.error('PTR file does not exists: {}'.format(ptr_path))
                        sys.exit()

        # elif hasattr(self.osve_parameters, 'juice_conf'):
        #
        #     juice_conf = self.osve_parameters.juice_conf
        #     juice_conf = os.path.expandvars(juice_conf)
        #     crema_id = self.osve_parameters.crema_id
        #     ptr_file_name = 'spice_segmentation_attitude_{}.json'.format(crema_id.replace('crema_', ''))
        #
        #     ptr_path = os.path.join(juice_conf, *(self.default_root_path.ptr_path.dir, crema_id, ptr_file_name))
        #
        # else:
        #
        #     logging.error('"juice_conf" or "ptr_path" must be defined in configuration file')
        #     sys.exit()

        if not os.path.exists(ptr_path):

            ptr_path = os.path.join(root_dir, ptr_path)

            if not os.path.exists(ptr_path):
                logging.error('PTR file does not exists: {}'.format(ptr_path))
                sys.exit()

        dest = os.path.join(self.working_dir, experiment_type)
        dest = os.path.join(dest, os.path.basename(ptr_path))
        shutil.copy(ptr_path, dest)

        logging.info('Copy of Attitude file (PTR) created: {}'.format(dest))

        return dest

    def add_eps_cfg(self):
        """
        Copy eps.cfg template to OSVE CONF
        """

        if hasattr(self.osve_parameters, 'path_eps_cfg'):

            path_eps_cfg = os.path.expandvars(self.osve_parameters.path_eps_cfg)
            if not os.path.isfile(path_eps_cfg):

                path_eps_cfg = os.path.join(self.scenario, path_eps_cfg)
                if not os.path.isfile(path_eps_cfg):
                    logging.error('"path_eps_cfg" file does not exists; {}'.format(path_eps_cfg))
                    sys.exit()

        elif hasattr(self.osve_parameters, 'juice_conf'):

            juice_conf = self.osve_parameters.juice_conf
            juice_conf = os.path.expandvars(juice_conf)
            crema_id = self.osve_parameters.crema_id
            eps_file = '{}{}.cfg'.format(self.default_root_path.eps_config_file.prefix, crema_id)
            # path_eps_cfg = os.path.join(juice_conf, *('internal', 'common', 'osve_config', crema_id, mk_file))
            path_eps_cfg = os.path.join(juice_conf, *(self.default_root_path.eps_config_file.dir, crema_id, eps_file))

            if not os.path.isfile(path_eps_cfg):

                logging.error('eps.cfg default path does not exist: {}'.format(path_eps_cfg))
                sys.exit()

        else:

            logging.error('"juice_conf" or "path_eps_cfg" must be defined in configuration file')
            sys.exit()

        eps_cfg_dest_path = os.path.join(self.path_to_config_dir, 'ISE')
        eps_cfg_dest_path = os.path.join(eps_cfg_dest_path, 'eps.cfg')

        shutil.copy(path_eps_cfg, eps_cfg_dest_path)
        logging.info('eps.cfg file template copied to osve CONF {} --> {}'.format(path_eps_cfg, eps_cfg_dest_path))

        return eps_cfg_dest_path

    def add_event_juice_def(self):
        """
        Copy events.juice.def
        """

        ise_dir = os.path.join(self.path_to_config_dir, 'ISE')

        if hasattr(self.osve_parameters, 'path_eps_cfg'):
            path_eps_cfg = os.path.expandvars(self.osve_parameters.path_eps_cfg)
            path_event_juice_def = os.path.dirname(os.path.dirname(path_eps_cfg))
            path_event_juice_def = os.path.join(path_event_juice_def, 'events.juice.def')

        elif hasattr(self.osve_parameters, 'juice_conf'):

            juice_conf = self.osve_parameters.juice_conf
            juice_conf = os.path.expandvars(juice_conf)
            # path_event_juice_def = os.path.join(juice_conf, *('internal', 'common', 'osve_config', 'events.juice.def'))
            path_event_juice_def = os.path.join(juice_conf,
                                                *(self.default_root_path.event_def_file.dir,
                                                  self.default_root_path.event_def_file.name))

            if not os.path.isfile(path_event_juice_def):

                logging.error('events.juice.def default path does not exist: {}'.format(path_event_juice_def))
                sys.exit()

        else:

            logging.error('"juice_conf" or "path_eps_cfg" must be defined in configuration file')
            sys.exit()

        if os.path.isfile(path_event_juice_def):

            juice_event_def_dest_path = ise_dir
            juice_event_def_dest_path = os.path.join(juice_event_def_dest_path, 'events.juice.def')

            shutil.copy(path_event_juice_def, juice_event_def_dest_path)
            logging.info('events.juice.def file template copied to osve CONF {} --> {}'.format(
                path_event_juice_def, juice_event_def_dest_path))

        else:

            logging.warning('events.juice.def default')

    def add_brf(self, brf_file_name):
        """
        Copy brf to OSVE CONF

        Note: reset within eps.cfg only if path_eps_brf in osve_parameters (testing purpose only)

        :param brf_file_name: Bit rate file name
        """

        ise_dir = os.path.join(self.path_to_config_dir, 'ISE')

        if not hasattr(self.osve_parameters, 'path_eps_brf'):

            if hasattr(self.osve_parameters, 'path_to_geopipeline_data'):

                data_dir = os.path.expandvars(self.osve_parameters.path_to_geopipeline_data)

            elif hasattr(self.osve_parameters, 'juice_conf'):

                juice_conf = self.osve_parameters.juice_conf
                juice_conf = os.path.expandvars(juice_conf)
                # data_dir = os.path.join(juice_conf, *('internal', 'geopipeline', 'output'))
                data_dir = os.path.join(juice_conf, self.default_root_path.bit_rate_file.dir)

            else:

                logging.error('"juice_conf" or "path_to_geopipeline_data" must be defined in configuration file')
                sys.exit()

            data_dir = os.path.expandvars(data_dir)

            for f in brf_file_name:

                brf = os.path.join(data_dir, f)

                if not os.path.isfile(brf):
                    logging.error('brf file does not exists; {}'.format(brf))
                    sys.exit()

                brf_dest_path = os.path.join(ise_dir, f)

                shutil.copy(brf, brf_dest_path)
                logging.info('BRF file copied to osve CONF {} --> {}'.format(brf, brf_dest_path))

        else:

            brf = os.path.expandvars(self.osve_parameters.path_eps_brf)

            if not os.path.isfile(brf):

                brf = os.path.join(self.scenario, brf)

                if not os.path.isfile(brf):
                    logging.error('"path_eps_brf" file does not exists; {}'.format(brf))
                    sys.exit()

                brf_file_name = os.path.basename(brf)
                eps_file = os.path.join(ise_dir, 'eps.cfg')
                reset_brf(eps_file, brf_file_name)

            brf_dest_path = os.path.join(ise_dir, brf_file_name)
            shutil.copy(brf, brf_dest_path)
            logging.info('BRF file copied to osve CONF {} --> {}'.format(brf, brf_dest_path))

    def add_cells_efficiency(self, cell_efficiency_file_name):
        """
        Copy brf to OSVE CONF and reset within eps.cfg

        :param cell_efficiency_file_name: Cells efficiency file name
        """

        ise_dir = os.path.join(self.path_to_config_dir, 'ISE')

        if not hasattr(self.osve_parameters, 'path_eps_cells_efficiency'):

            if hasattr(self.osve_parameters, 'path_to_geopipeline_data'):

                data_dir = os.path.expandvars(self.osve_parameters.path_to_geopipeline_data)

            elif hasattr(self.osve_parameters, 'juice_conf'):

                juice_conf = self.osve_parameters.juice_conf
                juice_conf = os.path.expandvars(juice_conf)
                # data_dir = os.path.join(juice_conf, *('internal', 'geopipeline', 'output'))
                data_dir = os.path.join(juice_conf, self.default_root_path.solar_cell_efficiency_file.dir)

            else:

                logging.error('"juice_conf" or "path_to_geopipeline_data" must be defined in configuration file')
                sys.exit()

            data_dir = os.path.expandvars(data_dir)
            data_dir = os.path.join(data_dir, self.osve_parameters.crema_id)

            cells_eff = os.path.join(data_dir, cell_efficiency_file_name)

            if not os.path.isfile(cells_eff):
                logging.error('Cells efficiency file does not exists; {}'.format(cells_eff))
                sys.exit()

            cell_eff_dest_path = os.path.join(ise_dir, cell_efficiency_file_name)

            shutil.copy(cells_eff, cell_eff_dest_path)
            logging.info('Cells efficiency file  file copied to osve CONF {} --> {}'.format(
                    cells_eff, cell_efficiency_file_name))

        else:

            cells_eff = os.path.expandvars(self.osve_parameters.path_eps_cells_efficiency)

            if not os.path.isfile(cells_eff):

                cells_eff = os.path.join(self.scenario, cells_eff)

                if not os.path.isfile(cells_eff):
                    logging.error('"path_eps_cells_efficiency" file does not exists; {}'.format(cells_eff))
                    sys.exit()

                cells_eff_file_name = os.path.basename(cells_eff)
                eps_file = os.path.join(ise_dir, 'eps.cfg')
                reset_cell_efficiency(eps_file, cells_eff_file_name)

            cell_eff_dest_path = os.path.join(ise_dir, cells_eff_file_name)
            shutil.copy(cells_eff, cell_eff_dest_path)
            logging.info('Cell efficiency file copied to osve CONF {} --> {}'.format(cells_eff, cell_eff_dest_path))

    def add_cells_counter(self, cell_counter_file_name):
        """
        Copy cells counter file to OSVE CONF and reset within eps.cfg

        :param cell_counter_file_name: Cells counter file name
        """

        ise_dir = os.path.join(self.path_to_config_dir, 'ISE')

        if hasattr(self.osve_parameters, 'juice_conf'):

            juice_conf = self.osve_parameters.juice_conf
            juice_conf = os.path.expandvars(juice_conf)
            data_dir = os.path.join(juice_conf, self.default_root_path.solar_cell_counter_file.dir)

        else:

            logging.error('"juice_conf" must be defined in configuration file')
            sys.exit()

        data_dir = os.path.expandvars(data_dir)

        if not os.path.isdir(data_dir):
            logging.error('invalid cell counter root directory: {}'.format(data_dir))
            sys.exit()

        if cell_counter_file_name:

            cells_counter = os.path.join(data_dir, cell_counter_file_name)

            if not os.path.isfile(cells_counter):
                logging.error('Cells counter file does not exists; {}'.format(cells_counter))
                sys.exit()

            cell_eff_dest_path = os.path.join(ise_dir, cell_counter_file_name)

            shutil.copy(cells_counter, cell_eff_dest_path)
            logging.info('Cells counter file copied to osve CONF {} --> {}'.format(
                cells_counter, cell_counter_file_name))

    def add_unit_file(self):
        """
        Copy unit file to init CONF

        """

        ise_dir = os.path.join(self.path_to_config_dir, 'ISE')

        if hasattr(self.osve_parameters, 'juice_conf'):

            juice_conf = self.osve_parameters.juice_conf
            juice_conf = os.path.expandvars(juice_conf)
            data_dir = os.path.join(juice_conf, self.default_root_path.unit_file.dir)

        else:

            logging.error('"OSVE/EPS unit_file" must be defined in configuration file')
            sys.exit()

        data_dir = os.path.expandvars(data_dir)

        if not os.path.isdir(data_dir):
            logging.error('invalid OSVE/EPS unit_file root directory: {}'.format(data_dir))
            sys.exit()

        unit_file = os.path.join(data_dir,  self.default_root_path.unit_file.name)

        if not os.path.isfile(unit_file):
            logging.error('unit_file does not exists; {}'.format(unit_file))
            sys.exit()

        unit_file_dest_path = os.path.join(ise_dir, 'units.def')

        shutil.copy(unit_file, unit_file_dest_path)
        logging.info('unit_file copied to osve CONF {} --> {}'.format(
                unit_file, unit_file_dest_path))

    def add_agm_multibody_definition_files(self):
        """
        Copy CFG_AGM_JUI_MULTIBODY_*_DEFINITIONS.xml to OSVE CONF

        """

        age_dir = os.path.join(self.path_to_config_dir, 'AGE')

        if not hasattr(self.osve_parameters, 'agm_multibody_definition_files'):

            if not hasattr(self.osve_parameters, 'juice_conf'):

                logging.error('"juice_conf" must be defined in configuration file')
                sys.exit()

            else:

                juice_conf = self.osve_parameters.juice_conf
                juice_conf = os.path.expandvars(juice_conf)
                # base_dir = os.path.join(juice_conf, *('internal','common','agm_config')
                base_dir_1 = os.path.join(juice_conf, self.default_root_path.agm_cfg_predefined_file.dir)
                base_dir_2 = os.path.join(juice_conf, self.default_root_path.agm_cfg_fixed_def_file.dir)
                base_dir_3 = os.path.join(juice_conf, self.default_root_path.agm_cfg_event_def_file.dir)
                base_dir_4 = os.path.join(juice_conf, self.default_root_path.agm_config_ptr_file.dir)
                path_agm_files = [os.path.join(base_dir_1, self.default_root_path.agm_cfg_predefined_file.name),
                                  os.path.join(base_dir_2, self.default_root_path.agm_cfg_fixed_def_file.name),
                                  os.path.join(base_dir_3, self.default_root_path.agm_cfg_event_def_file.name),
                                  os.path.join(base_dir_4, self.default_root_path.agm_config_ptr_file.name)]

            for agm_file in path_agm_files:

                if not os.path.exists(agm_file):

                    logging.error('AGM file does not exist: {}'.format(agm_file))
                    sys.exit()

                logging.info('AGM Definition file copied: {}'.format(agm_file))

        else:

            path_agm_files = []

            for f in self.osve_parameters.agm_multibody_defintion_files:

                fi = os.path.expandvars(f)

                if not os.path.isfile(fi):
                    logging.error('"path_eps_cfg" file does not exists; {}'.format(fi))
                    sys.exit()

                else:

                    path_agm_files.append(fi)

        for f in path_agm_files:

            dest_path = os.path.join(age_dir, os.path.basename(f))

            shutil.copy(f, dest_path)
            logging.info('eps.cfg file template copied to osve CONF {} --> {}'.format(f, dest_path))

    def get_start_end_ptr(self, path_ptr_file):
        """
        Return start/end PTR

        :param path_ptr_file: path the (json response nadir file to create)
        :return
        """

        logging.info('Parsing PTR: {}'.format(path_ptr_file))
        json_dic = my_json.load_to_dic(path_ptr_file)
        segments = sorted(json_dic['segments'], key=itemgetter('start', 'end'))

        # ptr_start = parse_date_time(segments[0]["start"])
        # ptr_end = parse_date_time(segments[-1]["end"])

        ptr_start = segments[0]["start"]
        ptr_end = segments[-1]["end"]

        return ptr_start, ptr_end

    def create_osve_config_file(self, experiment_type):
        """
        Build osve config file on the fly from template "config_osve_template.json" using osve_parameters

        param: experiment_type: name of experiment type (i.e. target)
        """

        parameters = self.osve_parameters

        template_file = self.get_template_osve_config_file()

        param = my_json.load_to_dic(template_file)

        session_configuration = param['sessionConfiguration']

        session_configuration['sessionID'] = parameters.scenario
        session_configuration['version'] = "1.0.0"

        session_configuration['simulationConfiguration']['timeStep'] = parameters.simu_time_step
        session_configuration['simulationConfiguration']['outputTimeStep'] = parameters.output_time_step

        if not 'attitudeSimulationConfigurationREMOVED' in session_configuration.keys():
            atttitude = session_configuration['attitudeSimulationConfiguration']
            kernels_list = atttitude['kernelsList']
            crema_id = str(parameters.crema_id).upper()
            kernels_list['id'] = crema_id
            kernels_list['version'] = "1.0.0"
            kernels_list['baselineRelPath'] = './'
            root_path = os.path.abspath(kernels_list['baselineRelPath'])
            kernels_list['fileList'] = [{
                        "fileRelPath": "{}".format(os.path.basename(self.metakernel_file_name)),
                        "description": "metakernel {}".format(str(parameters.crema_id).lower().replace('_', ' '))
                    }]

            atttitude['userDefinitionFile'] = self.default_root_path.agm_cfg_fixed_def_file.name
            atttitude['predefinedBlockFile'] = self.default_root_path.agm_cfg_predefined_file.name
            atttitude['eventDefinitionsFile'] = self.default_root_path.agm_cfg_event_def_file.name

        experiment_simulation = session_configuration['instrumentSimulationConfiguration']
        # path_to_edf_top_file = os.path.join(os.path.join('../../', experiment_type), parameters.edf_data)
        # experiment_simulation['edfFileName'] = path_to_edf_top_file

        input_files = session_configuration['inputFiles']
        root_path = os.path.abspath('./')
        input_files['baselineRelPath'] = experiment_type
        input_files_path = os.path.join(root_path, input_files['baselineRelPath'])

        modellingConfiguration = input_files['modellingConfiguration']
        modellingConfiguration['baselineRelPath'] = os.path.dirname(parameters.edf_data)
        modellingConfiguration['edfFileName'] = os.path.basename(parameters.edf_data)

        if hasattr(parameters, 'ptr'):
            ptr_file_name = os.path.basename(parameters.ptr)
            if ptr_file_name.split('.')[-1] == 'json':
                input_files['jsonSegmentFilePath'] = os.path.basename(parameters.ptr)
            else:
                input_files['xmlPtrPath'] = os.path.basename(parameters.ptr)
            ptr_path = os.path.join(input_files_path, parameters.ptr)
        else:
            logging.error('PTR file must be defined iin configuration file')
            sys.exit()

        top_itl_relative_path_to_input_files = create_itl_with_new_timeline_period(input_files_path, parameters)
        self.top_itl = os.path.join(input_files_path, top_itl_relative_path_to_input_files)

        set_simulation_start_end_time_filters(input_files_path, parameters,
                                              session_configuration['simulationConfiguration'], ptr_path)

        input_files['segmentTimelineFilePath'] = top_itl_relative_path_to_input_files
        input_files['eventTimelineFilePath'] = parameters.evf_data
        output_files = session_configuration['outputFiles']
        output_files['baselineRelPath'] = parameters.simu_output_dir
        # output_files.simOutputFIlesPath = "run_errorFile.out"
        # output_files.runtimeErrorFilePath = "run_errorFile.out"
        # output_files.runtimeLogFilePath = "run_logFile.out"

        if hasattr(parameters, 'create_ckAttitudeFile'):
            output_files['ckAttitudeFilePath'] = ''
            if parameters.create_ckAttitudeFile:
                output_files['ckAttitudeFilePath'] = 'segment_with_pointing_' + crema_id + '.ck'

        if hasattr(parameters, 'create_simDataFilePath'):
            output_files['simDataFilePath'] = ''
            if parameters.create_simDataFilePath:
                output_files['simDataFilePath'] = 'segment_with_pointing_' + crema_id + '.csv'

        if hasattr(parameters, 'create_attitudeXmlPtr'):
            output_files['attitudeXmlPtr'] = ''
            if parameters.create_attitudeXmlPtr:
                output_files['attitudeXmlPtr'] = 'segment_with_pointing_' + crema_id + '.ptx'

        simu_output_dir = os.path.join(self.working_dir, parameters.simu_output_dir)
        if os.path.exists(simu_output_dir):
            shutil.rmtree(simu_output_dir)

        os.mkdir(simu_output_dir)

        dest = os.path.join(self.working_dir, os.path.basename(template_file))
        my_json.create_file(dest, param)

        logging.info('osve config file created: {}'.format(dest))


def run_osve(working_dir, osve_parameters, experiment_type, no_ptr_cut=False):
    """
    Run osve in the base directory of a given config file


    :param working_dir: working directory path
    :param osve_parameters: object containing osve parameters
    :param experiment_type: name of experiment type (i.e. target)
    :param env_var: dictionary including environment variable to set
    :param no_ptr_cut: flag to allow PTR cut according the Top ITL
    :return: eps_cfg.eps_cfg_parameters, spice_kernel_md_path
    """

    scenario_dir = os.getcwd()

    # here = os.path.abspath(os.path.dirname(__file__))

    os.chdir(working_dir)

    osve_wrapper = OsveWrapper(working_dir, scenario_dir, osve_parameters, no_ptr_cut)

    spice_kernel_md_path = osve_wrapper.get_copy_spice_metakernel(osve_parameters)

    osve_wrapper.get_ptr_copy(experiment_type, scenario_dir)

    osve_wrapper.create_osve_config_file(experiment_type)

    # osve.get_ptr_copy(experiment_type, scenario_dir)

    os.chdir(scenario_dir)

    eps_output = os.path.join(working_dir, experiment_type)
    eps_output = os.path.join(eps_output, 'eps_output')

    osve_config_file_path = os.path.join(working_dir, 'config_osve_template.json')

    import osve.osve as osve

    sim = osve.osve()
    version = sim.get_app_version()
    logging.info(f'OSVE version: {version}')
    sim.execute(working_dir, osve_config_file_path)

    if eps_output is not None:
        move_osve_ouput_to_scenario_output(working_dir, osve_config_file_path, eps_output)

    return osve_wrapper.eps_cfg.eps_cfg_parameters, spice_kernel_md_path


def run_osve_from_cfg_file(config_file_path, no_ptr_cut=False):
    """
    Run osve in the base directory of a given config file

    :param config_file_path: path of config file
    """

    if not os.path.exists(config_file_path):
        logging.error('file does not exist: {}'.format(config_file_path))
        sys.exit()

    config = my_json.load_to_dic(config_file_path)

    experiment_type = config['experiment_type']

    preproc(config)
    osve_parameters = my_json.load_to_object(config_file_path).osve

    working_dir = os.path.dirname(config_file_path)
    experiment_type_relative_path = os.path.join(osve_parameters.scenario, experiment_type)

    run_osve(working_dir, osve_parameters, experiment_type_relative_path, no_ptr_cut)


def preproc(conf):
    """
    Set PTR start/end time cut

    :param conf: structure containing configuration parameters
    :return:
    """

    conf['osve']['start_timeline'] = None
    conf['osve']['end_timeline'] = None

    if 'osve' not in list(conf.keys()):

        logging.error('osve section missing in configuration file')
        sys.exit()

    else:

        if 'start_timeline' in conf['osve'].keys():

            if conf['osve']['start_timeline']:

                conf['osve']['filterStartTime'] = conf['osve']['start_timeline']

        if 'end_timeline' in conf['osve'].keys():

            if conf['osve']['end_timeline']:

                conf['osve']['filterEndTime'] = conf['osve']['end_timeline']

        # no_ptr_cut = True

        if conf['osve']['start_timeline'] is None and conf['osve']['end_timeline'] is None:

            if 'no_ptr_cut' not in conf['osve']:

                conf['osve']['no_ptr_cut'] = False  # cutting to Top ITL


def move_osve_ouput_to_scenario_output(scenario_path, config_file_path, eps_output):
    """
    Move and rename OSVE ouput_dir to scenario. this include eps_output, and ck, ptx

    :param scenario_path: path to scenario base directory
    :param config_file_path: path to config file path
    :param eps_output: path to eps_output directory
    """

    last_eps_output = None

    o = load_to_object(config_file_path)
    output_dir = os.path.join(scenario_path, o.sessionConfiguration.outputFiles.baselineRelPath)

    if not os.path.exists(output_dir):
        logging.error('OSVE output directory does not exist: {}'.format(output_dir))
        logging.error('Please fix sessionConfiguration.outputFiles.baselineRelPath in {}'.format(config_file_path))
        sys.exit()

    # get last dir of output_dir

    logging.info('osve output directory contents: {}'.format(output_dir))
    for f in glob.glob(os.path.join(output_dir, '*')):
        print('\t{}'.format(f))
        if os.path.isdir(f) and os.path.basename(f) == 'eps_output':
            last_eps_output = f

    # last_eps_output = max(glob.glob(os.path.join(output_dir, '*/')), key=os.path.getmtime)
    if last_eps_output is None:
        logging.error('eps_output not generated in {}'.format(output_dir))
        sys.exit()

    if os.path.exists(eps_output):
        shutil.rmtree(eps_output)

    shutil.move(last_eps_output, eps_output)
    logging.info('New simulation files:  {} --> {}'.format(last_eps_output, eps_output))

    # Move other osve ouput to scenario dir in 'other_osve_ouput'
    other_osve_ouput = os.path.join(os.path.dirname(eps_output), 'other_osve_ouput')

    if os.path.exists(other_osve_ouput):
        shutil.rmtree(other_osve_ouput)

    shutil.move(output_dir, other_osve_ouput)
    logging.info('New simulation files:  {} --> {}'.format(output_dir, other_osve_ouput))
