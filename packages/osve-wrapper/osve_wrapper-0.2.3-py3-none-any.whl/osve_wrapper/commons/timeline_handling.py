"""
Created on April, 2021

@author: Claudio Munoz Crego (ESAC)

This file include utilities to handle timeline (json versus itl)
"""

import os
import sys
import datetime
import logging

from operator import itemgetter

import esac_juice_pyutils.commons.json_handler as my_json
from esac_juice_pyutils.periods.intervals_handler import get_overlap


def cut_ptr(path_itl_top_file, path_ptr_file, exact_cut=False):
    """
    Cut PTR file according to TOP ITL start/end

    Note: input times from top itl file are UTC (Though not specified)

    :param path_itl_top_file: path to the top itl
    :param path_ptr_file: path the (json response nadir file to create)
    :param exact_cut: if True cut PTR to start/end ITL; if false
    :return reduced_ptr_file: path of ptr reduced file
    """

    logging.info('Get start/end from ITL: {}'.format(path_itl_top_file))
    start_time, end_time = get_timeline_period(path_itl_top_file)

    logging.info('Parsing PTR: {}'.format(path_ptr_file))
    json_dic = my_json.load_to_dic(path_ptr_file)
    segments = sorted(json_dic['segments'], key=itemgetter('start', 'end'))

    ptr_original_start = parse_date_time(segments[0]["start"])
    ptr_original_end = parse_date_time(segments[-1]["end"])

    # print(start_time, end_time, ptr_original_start, ptr_original_end)

    if ptr_original_start > start_time or ptr_original_end < end_time:

        # The PTR must cover the full timeline period, if not the simulation should no cover thee full timeline

        logging.error('TOP_itl start/end = [{}, {}] not included in PTR time [{}, {}]'.format(
            start_time, end_time,ptr_original_start, ptr_original_end))
        logging.error('Please check PTR file: {}'.format(path_ptr_file))
        sys.exit()

    cutted_segments = []

    for segment in segments:

        seg_start = parse_date_time(segment["start"])
        seg_end = parse_date_time(segment["end"])
        seg_slew_policy = segment["slew_policy"]

        # print(start_time, end_time, seg_start, seg_end)
        overlap = get_overlap(start_time, end_time, seg_start, seg_end)

        if overlap:

            if exact_cut:

                segment["start"] = overlap[0].replace(tzinfo=SimpleUtc()).isoformat().replace("+00:00", "Z")
                segment["end"] = overlap[1].replace(tzinfo=SimpleUtc()).isoformat().replace("+00:00", "Z")

            cutted_segments.append(segment)

    json_dic['segments'] = cutted_segments

    reduced_ptr_file = path_ptr_file.replace('.', '_reduced.')
    os.remove(path_ptr_file)
    my_json.create_file(reduced_ptr_file, json_dic)
    logging.info('PTR files cutted to Top ITl period [{},{}]'.format(start_time, end_time))

    return reduced_ptr_file


def create_response_nadir(path_itl_top_file, trajectory_id, path_to_response_nadir_file):
    """
    Create default nadir pointing file

    Note: input times from top itl file are UTC (Though not specified)

    :param path_itl_top_file: path to the top itl
    :param trajectory_id: Trajectory if (i.e. crema_3_0)
    :param path_to_response_nadir_file: path the (json response nadir file to create)
    """

    start_time, end_time = get_timeline_period(path_itl_top_file)

    template_file = get_template_response_nadir_file()

    json_dic = my_json.load_to_dic(template_file)

    json_dic['trajectory'] = trajectory_id
    json_dic['mnemonic'] = "POINTING_TEST"
    json_dic['name'] = "Pointing Test"
    json_dic['description'] = "Pointing test to be pass to OSVE"

    segments = json_dic['segments'][0]
    segments['start'] = datetime.datetime.strftime(start_time, '%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    segments['end'] = datetime.datetime.strftime(end_time, '%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    segments['segment_definition'] = "NADIR_TEST"
    segments['timeline'] = "PRIME"
    segments['pointing_request_snippet'] = "<block ref=\"OBS\">\n" \
                                           "      <attitude ref=\"track\">\n" \
                                           "        <boresight ref=\"SC_Zaxis\" />\n" \
                                           "        <target ref=\"Ganymede\" />\n" \
                                           "        <phaseAngle ref=\"powerOptimised\">\n" \
                                           "          <yDir>false </yDir>\n" \
                                           "        </phaseAngle>\n" \
                                           "      </attitude>\n" \
                                           "      <metadata>\n" \
                                           "        <comment>Track Power Optimised Ganymede</comment>\n" \
                                           "      </metadata>\n" \
                                           "    </block>\n"
    segments['slew_policy'] = "EXTEND_BLOCK"

    json_dic['default_block'] = "<block ref=\"OBS\">\r\n" \
                                "      <attitude ref=\"track\">\r\n" \
                                "        <boresight ref=\"SC_Zaxis\" />\r\n" \
                                "        <target ref=\"JUPITER\" />\r\n" \
                                "        <phaseAngle ref=\"powerOptimised\">\r\n" \
                                "          <yDir>false </yDir>\r\n" \
                                "        </phaseAngle>\r\n" \
                                "      </attitude>\r\n" \
                                "      <metadata>\r\n" \
                                "        <comment>Track Power Optimised Jupiter</comment>\r\n" \
                                "      </metadata>\r\n" \
                                "    </block>"

    json_dic['default_slew_policy'] = "KEEP_BLOCK"

    dest = os.path.join(path_to_response_nadir_file, os.path.basename(template_file))
    my_json.create_file(dest, json_dic)


def get_template_response_nadir_file():
    """
    Get the default response_nadir_file.json

    TBC if no longer needed or to be maintained for testing

    :return: path to config_osve_template.json
    :rtype: python path
    """

    here = os.path.abspath(os.path.dirname(__file__))
    template_file = os.path.join(here, 'templates')
    template_file = os.path.join(template_file, 'response_nadir.json')

    if not os.path.exists(template_file):
        logging.error('reference template file "%s" missing' % template_file)
        sys.exit()

    logging.info('{} loaded'.format(template_file))

    return template_file


def get_timeline_period(itl_top_file):
    """
    Get start and time from top file ITL. That is the timeline simulation period

    :param itl_top_file: path to Timeline top file
    :return: start_time, end_time
    """

    if not os.path.exists(itl_top_file):
        logging.error('file path does not exist: {}'.format(itl_top_file))
        sys.exit()

    f = open(itl_top_file)

    start_time = None
    end_time = None

    for line in f.readlines():

        if line.startswith('Start_time'):

            time_str = line.replace(' ', '').replace('\n', '').split('Start_time:')[1]
            start_time = parse_date_time(time_str)

            # tz = start_time.tzname()
            # if tz is None:
            #     start_time = start_time.replace(tzinfo=SimpleUtc())

        elif line.startswith('End_time'):

            time_str = line.replace(' ', '').replace('\n', '').split('End_time:')[1]
            end_time = parse_date_time(time_str)

            # tz = end_time.tzname()
            # if tz is None:
            #     end_time = end_time.replace(tzinfo=SimpleUtc())

    return start_time, end_time


def set_simulation_start_end_time_filters(input_files_path, parameters, simulation_configuration, path_ptr_file):
    """
        Set simulation start and time (amd PTR cut)
        only if 'filterStartTime' and 'filterEndTime' and resizePtrBlocks are set in configuration file,
        include them in osve template

        :param path_ptr_file: PTR file path
        :param input_files_path: path to Timeline top file
        :param parameters: structure including configuration parameters
        :param simulation_configuration: osve template dictionary
        """

    top_itl_relative_path_to_input_files = parameters.itl_data
    top_itl_path = os.path.join(input_files_path, top_itl_relative_path_to_input_files)

    if not os.path.exists(top_itl_path):
        logging.error('file path does not exist: {}'.format(top_itl_path))
        sys.exit()

    itl_start_time, itl_end_time = get_timeline_period(top_itl_path)

    eps_start, eps_end = (None, None)

    if hasattr(parameters, 'filterStartTime'):

        if parameters.filterStartTime:

            eps_start = parse_date_time(parameters.filterStartTime)
            # tz = eps_start.tzname()
            # if tz is None:
            #     eps_start = eps_start.replace(tzinfo=SimpleUtc())

            if eps_start < itl_start_time or eps_start > itl_end_time:

                logging.error('"filterStartTime" specified in config file must be within original Top ITL '
                              'period [{}: {}]'.format(itl_start_time.isoformat(), itl_end_time.isoformat()))
                logging.error('Please fix "filterStartTime" in {}'.format(top_itl_path))
                sys.exit()

            else:

                simulation_configuration['filterStartTime'] = parameters.filterStartTime

    elif hasattr(parameters, 'no_ptr_cut'):

        if not parameters.no_ptr_cut:

            simulation_configuration['filterStartTime'] = itl_start_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    if hasattr(parameters, 'filterEndTime'):

        if parameters.filterEndTime:

            eps_end = parse_date_time(parameters.filterEndTime)
            # tz = eps_end.tzname()
            # if tz is None:
            #     eps_end = eps_end.replace(tzinfo=SimpleUtc())

            if eps_end < itl_start_time or eps_end > itl_end_time:

                logging.error('"filterEndTime" specified in config file must be within original Top ITL '
                              'period [{}: {}]'.format(itl_start_time, itl_end_time))
                logging.error('Please fix "filterEndTime" in {}'.format(top_itl_path))
                sys.exit()

            else:

                simulation_configuration['filterEndTime'] = parameters.filterEndTime

    elif hasattr(parameters, 'no_ptr_cut'):

        if not parameters.no_ptr_cut:

            simulation_configuration['filterEndTime'] = itl_end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        # else:
        #
        #     # Whe no cut enforce to set filterEndTime = end of PTR file if no osve crash
        #     simulation_configuration['filterEndTime'] = get_start_end_ptr(path_ptr_file)[1]

    if hasattr(parameters, 'resizePtrBlocks'):

        if parameters.resizePtrBlocks:

            simulation_configuration['resizePtrBlocks'] = parameters.resizePtrBlocks

        else:

            simulation_configuration['resizePtrBlocks'] = False

    if 'filterEndTime' in simulation_configuration:

        if simulation_configuration['filterEndTime'] is not None:

            simulation_configuration['resizePtrBlocks'] = True

    if 'filterStartTime' in simulation_configuration:

        if simulation_configuration['filterStartTime'] is not None:

            simulation_configuration['resizePtrBlocks'] = True

    if hasattr(parameters, 'simulateTimeline'):

        if parameters.simulateTimeline:

            simulation_configuration['simulateTimeline'] = parameters.simulateTimeline  # True

        else:

            simulation_configuration['simulateTimeline'] = False


def create_itl_with_new_timeline_period(input_files_path, parameters):
    """
    Create a copy of top file ITL setting new start and time.
    only if 'start_timeline' and/or 'start_timeline' are set in configuration

    That is reset the timeline simulation period

    :param input_files_path: path to Timeline top file
    :param parameters: structure including configuration parameters
    :return: top_itl_relative_path_to_input_files
    """

    logging.info('Creating new Top ITL')

    top_itl_relative_path_to_input_files = parameters.itl_data
    top_itl_path = os.path.join(input_files_path, top_itl_relative_path_to_input_files)

    if not os.path.exists(top_itl_path):
        logging.error('file path does not exist: {}'.format(top_itl_path))
        sys.exit()

    fi = open(top_itl_path, 'r')
    current_start_time, current_end_time = get_timeline_period(top_itl_path)

    eps_start = current_start_time
    if hasattr(parameters, 'start_timeline'):

        if parameters.start_timeline:

            eps_start = parse_date_time(parameters.start_timeline)
            # tz = eps_start.tzname()
            # if tz is None:
            #     eps_start = eps_start.replace(tzinfo=SimpleUtc())

            if eps_start < current_start_time or eps_start > current_end_time:

                logging.error('"Start_time" specified in config file must be within original Top ITL '
                              'period [{}: {}]'.format(current_start_time.isoformat(), current_end_time.isoformat()) )
                logging.error('Please fix "Start_time" in {}'.format(top_itl_path))
                sys.exit()

    eps_end = current_end_time
    if hasattr(parameters, 'end_timeline'):

        if parameters.end_timeline:

            eps_end = parse_date_time(parameters.end_timeline)
            # tz = eps_end.tzname()
            # if tz is None:
            #     eps_end = eps_end.replace(tzinfo=SimpleUtc())

            if eps_end < current_start_time or eps_end > current_end_time:
                logging.error('"End_time" specified in config file must be within original Top ITL '
                              'period [{}: {}]'.format(current_start_time, current_end_time))
                logging.error('Please fix "End_time" in {}'.format(top_itl_path))

    if eps_start != current_start_time or eps_end != current_end_time:

        reduced_itl = top_itl_path.replace(".", "_reduced.")
        top_itl_relative_path_to_input_files  = top_itl_relative_path_to_input_files.replace(".", "_reduced.")
        fo = open(reduced_itl, 'w')

        if eps_end < eps_start:

            logging.error('"Start_time" must > "End Time" in config file')
            sys.exit()

        for line in fi.readlines():

            if line.startswith('Start_time'):

                eps_start_str = datetime.datetime.strftime(eps_start, '%d-%b-%Y_%H:%M:%S')

                line = 'Start_time: {}\n'.format(eps_start_str)

            elif line.startswith('End_time'):

                eps_end_str = datetime.datetime.strftime(eps_end, '%d-%b-%Y_%H:%M:%S')

                line = 'End_time: {}\n'.format(eps_end_str)

            fo.write(line)

        fi.close()
        fo.close()

        logging.info('Reduced Top ITL file created for period [{}: {}]:{}'.format(
            eps_start, eps_end, reduced_itl))

    return top_itl_relative_path_to_input_files


def parse_date_time(str_date, only_date_format=True):
    """
    Parse date time

    1) Try some specific format first
    2) use datetutils, which support most common formats
    :return: dt
    """

    from dateutil.parser import parse

    datetime_formats = ['%d-%b-%Y_%H:%M:%S',
                        '%d-%B-%Y_%H:%M:%S',
                        '%d/%m/%y',
                        '%Y-%m-%dT%H:%M:%SZ',
                        '%Y-%m-%dT%H:%M:%S.%fZ',
                        '%Y-%m-%dT%H:%M:%S',
                        '%Y-%m-%d %H:%M:%S']

    dt = None

    for dt_format in datetime_formats:

        try:

            dt = datetime.datetime.strptime(str_date, dt_format)

            if dt:
                break

        except IOError as e:
            logging.debug(("I/O error({0}): {1}".format(e.errno, e.strerror)))

        except ValueError:
            logging.debug('Bad date time format "{}"; Expected format is "{}"'.format(
                str_date, datetime.datetime.strftime(datetime.datetime.now(), dt_format)))

    if not only_date_format:

        try:

            if dt is None:
                dt = parse(str_date)

        except IOError as e:
            logging.debug(("I/O error({0}): {1}".format(e.errno, e.strerror)))

        except ValueError:
            logging.debug('Bad date time format "{}"; Expected format is "{}"'.format(
                str_date, datetime.datetime.strftime(datetime.datetime.now(), dt_format)))

    if dt is None:
        logging.error('Cannot parse "{}" to datetime format!'.format(str_date))
        sys.exit()

    return dt


def get_start_end_ptr(path_ptr_file):
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


class SimpleUtc(datetime.tzinfo):
    """
    class to define ISO 8601 format UTC, Zoulou time (+00:00), no time (or +00:00 time) zone
    """

    def tzname(self,**kwargs):
        return "UTC"

    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def dst(self, dt):
        return datetime.timedelta(0)