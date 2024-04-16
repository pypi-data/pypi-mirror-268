"""
Created on November, 2018

@author: Claudio Munoz Crego (ESAC)

This module allows to handle event files (list of periods)
"""

import os
import sys
import datetime
import logging

import spiceypy as spi

from esac_juice_pyutils.eps.eps_events import EpsEvent


class EventHandler(object):

    def __init__(self, output_dir='./'):

        self.output_dir = output_dir

    def read_efinder_events(self, input_file_path):
        """
        Read event file containing one ephemeris time interval per line [s_etime, e_etime]
        :param input_file_path: path of the efinder file
        :return list of start and time
        """
        if not os.path.exists(input_file_path):
            logging.error('{} file {} does not exist'.format('event', input_file_path))

        event_name = os.path.basename(input_file_path).split('.')[0]
        events = EpsEvent(event_name)

        f = open(input_file_path, 'r')

        count_line = 0
        (start_previous, end_previous) = (datetime.datetime.now(), datetime.datetime.now())

        for line in f.readlines():

            if line.startswith('#'):  # reading file header
                line = line[1:].lstrip()
                metadata_header = line.split(':')[0]
                if ':' in line:
                    header_value = line.split(':')[1]
                else:
                    header_value = ''

                events.header.append(['#', metadata_header, header_value.lstrip()])

            elif line != '':  # Reading values

                (start, end) = (float(line.split()[0]), float(line.split()[1]))
                start = datetime.datetime.strptime(spi.et2utc(start, 'ISOC', 3), '%Y-%m-%dT%H:%M:%S.%f')
                end = datetime.datetime.strptime(spi.et2utc(end, 'ISOC', 3), '%Y-%m-%dT%H:%M:%S.%f')
                if start == start_previous and end == end_previous:
                    logging.warning('file "{}": line  {} duplicated value avoided [{}, {}])'.format(
                       input_file_path, count_line, start, end) )
                else:
                    (start_previous, end_previous) = (start, end)
                    events.data_value.append([start, end])

                # print count_line, (start, end), float(line.split()[0]), float(line.split()[1])

            count_line += 1

        if len(events.data_value) == 0:
            logging.error('event file {} is empty'.format('event', input_file_path))
        else:
            events.utc_start = events.data_value[0][0]
            events.utc_end = events.data_value[-1][1]

        return events

    def read_efinder_events_values(self, input_file_path):
        """
        Read event file containing one ephemeris time interval per line [s_etime, e_etime]
        Get only ephemeris time values

        :param input_file_path: path of the efinder file
        :return list of start and time
        """
        if not os.path.exists(input_file_path):
            logging.error('{} file {} does not exist'.format('event', input_file_path))
            sys.exit()
        else:
            logging.debug('Parsing event file {}'.format(input_file_path))

        intervals = []

        f = open(input_file_path, 'r')

        count_line = 0
        (start_previous, end_previous) = (0, 0)

        for line in f.readlines():

            if line.startswith('#'):  # reading file header
                pass

            elif line != '':  # Reading values

                (start, end) = (float(line.split()[0]), float(line.split()[1]))
                if start == start_previous and end == end_previous:
                    logging.warning('file "{}": line  {} duplicated value avoided [{}, {}])'.format(
                       input_file_path, count_line, start, end) )
                else:
                    (start_previous, end_previous) = (start, end)
                    intervals.append([start, end])

                # print count_line, (start, end), float(line.split()[0]), float(line.split()[1])

            count_line += 1

        if len(intervals) == 0:
            logging.error('event file {} is empty'.format('event', input_file_path))

        return intervals

    def read_eps_Events(self, input_file_path):
        """
        Read event file containing one ephemeris time interval per line [s_etime, e_etime]

        TODO

        :param input_file_path: path of the efinder file
        :return list of start and time
        """
        pass

    def create_event_file_header(self, start, end, nb_of_events, file_name,
                                 author='auto', revision='0001', id='TBD', description=''):
        """
        Generates event file header together with start and end time

        :param start: eps event start
        :param end: eps event stop
        :param nb_of_events: number of events
        :param file_name: file name
        :param author: author(s) reference; default 'auto'
        :param revision: number of revision
        :param id:
        :param description: Brief description of event
        :return:
        """
        """
        Generates event file header together with start and end time.
        :param author: 
        :param eps_events: eps events information
        :param file_name: event file name.
        :return: header
        :rtype: string
        """

        creation_date = datetime.datetime.now()

        header = '#\n# EVF Filename: {}'.format(os.path.basename(file_name)) \
                 + '\n# Generation Time: {}'.format(datetime.datetime.strftime(creation_date, '%d-%b-%Y_%H:%M:%S')) \
                 + '\n#\n# Author   : {}'.format(author) \
                 + '\n# ID  : {}'.format(id) \
                 + '\n# Revision : {}\n'.format(revision) \
                 + '\n# Description : {}\n'.format(description) \
                 + '\nStart_time: {}'.format(datetime.datetime.strftime(start, '%d-%B-%Y_%H:%M:%S')) \
                 + '\nEnd_time: {}\n\n'.format(datetime.datetime.strftime(end, '%d-%B-%Y_%H:%M:%S'))

        header += '\n# ({} events in list)\n'.format(nb_of_events)

        return header

    def create_event_file(self, event_list, event_type, eps_active=None, eps_inactive=None, description=None,
                          output_utc_format="%Y-%m-%dT%H:%M:%SZ"):
        """
        Write a given vent file to output_path

        :param eps_active:
        :param event_list: list of event
        :return N/A
        """

        event_type_start = '{}_START'.format(event_type)
        event_type_end = '{}_END'.format(event_type)
        if eps_active:
            event_type_start = eps_active
        if eps_inactive:
            event_type_end = eps_inactive

        file_name = os.path.join(self.output_dir, event_type + '.evf')
        f_out = open(file_name, 'w')

        number_of_events = len(event_list)

        if number_of_events == 0:
            logging.warning('Cannot create event file {}; not events found!'.format(file_name))

        else:

            (t_0, t_1) = (spi.et2utc(event_list[0][0], 'ISOC', 1, 35), spi.et2utc(event_list[-1][1], 'ISOC', 1, 35))
            (start, end) = (datetime.datetime.strptime(t_0, '%Y-%m-%dT%H:%M:%S.%f'),
                            datetime.datetime.strptime(t_1, '%Y-%m-%dT%H:%M:%S.%f'))

            f_out.write(self.create_event_file_header(start, end, number_of_events, file_name, description=description))

            count = 0
            for event in event_list:

                (t_0, t_1) = (spi.et2utc(event[0], 'ISOC', 1, 35), spi.et2utc(event[-1], 'ISOC', 1, 35))
                c_time_0 = datetime.datetime.strptime(t_0, '%Y-%m-%dT%H:%M:%S.%f')
                c_time_1 = datetime.datetime.strptime(t_1, '%Y-%m-%dT%H:%M:%S.%f')
                utc_start = datetime.datetime.strftime(c_time_0, output_utc_format)
                utc_end = datetime.datetime.strftime(c_time_1, output_utc_format)

                count += 1
                f_out.write('{} {} (COUNT = {})\n'.format(utc_start, event_type_start, count))
                f_out.write('{} {} (COUNT = {})\n'.format(utc_end, event_type_end, count))

            f_out.close()

            logging.info('event file {} created'.format(file_name))

    def create_event_dat_file(self, event_list, event_type, time_format='%Y-%m-%dT%H:%M:%S', header=None):
        """
        Write event file to output_path including one ephemeris time interval per line [s_etime, e_etime]

        :param event_list:
        :param event_type:
        :param time_format:
        :param header:
        :return:
        """
        """
        
        :param event_list: list of event

        :return N/A
        """
        file_name = os.path.join(self.output_dir, event_type + '.dat')

        f_out = open(file_name, 'w')

        if header:
            f_out.write(header)

        for event in event_list:

            (t_0, t_1) = (spi.et2utc(event[0], 'ISOC', 1, 35), spi.et2utc(event[1], 'ISOC', 1, 35))
            c_time_0 = datetime.datetime.strptime(t_0, '%Y-%m-%dT%H:%M:%S.%f')
            c_time_1 = datetime.datetime.strptime(t_1, '%Y-%m-%dT%H:%M:%S.%f')
            utc_start = datetime.datetime.strftime(c_time_0, time_format)
            utc_end = datetime.datetime.strftime(c_time_1, time_format)

            f_out.write('{}\t{}\n'.format(utc_start, utc_end))

        f_out.close()

        logging.info('event file {} created'.format(file_name))

    def create_event_ephemeris_txt_file(self, event_list, event_type, header=None, out_format='{:16.2f} {:16.2f}\n'):
        """
        Write event file to output_path including one ephemeris time interval per line [s_etime, e_etime]

        :param out_format: output format format for periods
        :param event_list: list of events
        :param event_type: tpy of event
        :param header: header to be print at the top of file
        :return:
        """

        file_name = os.path.join(self.output_dir, event_type + '.txt')

        f_out = open(file_name, 'w')

        if header:
            f_out.write(header)

        for event in event_list:
            f_out.write(out_format.format(event[0], event[1]))

        f_out.close()

        logging.info('event file {} created'.format(file_name))

    def create_multi_events_file(self, event_dico, event_type, description=None,
                                 output_utc_format="%Y-%m-%dT%H:%M:%SZ", event_file_name=None):
        """
        Write a given event file containing different events to output_path

        :param event_file_name: event file name which can be specified, if None is set to event_type + '.evf'
        :param output_utc_format:
        :param description:
        :param event_type: event type identifier
        :param event_dico: dictionary including single events periods
        :return N/A
        """

        if event_file_name:
            event_file_name += '.evf'
        else:
            event_file_name = event_type + '.evf'

        file_name = os.path.join(self.output_dir, event_file_name)
        f_out = open(file_name, 'w')

        number_of_events = sum([len(event_dico[k]) for k in event_dico.keys()])

        if number_of_events == 0:
            logging.warning('Cannot create event file {}; not events found!'.format(file_name))

        else:

            ev_times = []
            events = []

            for k in event_dico.keys():

                count = 0

                event_type_start = k

                for ev in event_dico[k]:

                    count += 1
                    t_0 = spi.et2utc(ev, 'ISOC', 1, 35)
                    c_time_0 = datetime.datetime.strptime(t_0, '%Y-%m-%dT%H:%M:%S.%f')
                    utc_start = datetime.datetime.strftime(c_time_0, output_utc_format)
                    events.append('{} {} (COUNT = {})\n'.format(utc_start, event_type_start, count))
                    ev_times.append(c_time_0)

            number_of_events = len(events)
            events = sorted(events)

            (start, end) = (min(ev_times), max(ev_times))
            f_out.write(self.create_event_file_header(start, end, number_of_events, file_name, description=description))

            for ev in events:

                f_out.write(ev)

            f_out.close()

            logging.info('event file {} created'.format(file_name))


def create_event_files(ogti, e, print_option='ephemeris', output_dir='./', utc_format="%Y-%m-%dT%H:%M:%SZ",
                       event_description=None, event_file_name=None, include_event_id_in_header=True):
    """
    Create event files

    :param ogti: dictionary event
    :param e: structure containing needed attributes (i.e. body, station, elevation ...)
    :param print_option: print option ['ephemeris', ...]
    :param output_dir: path fo the putput directory
    :param event_description: if specified: overwrite the event description
    :param event_file_name: event file name which can be specified, if None is set to event_type + '.evf'
    :return:
    """
    p = EventHandler(output_dir)

    if not event_description:
        event_description = e.description

    if print_option == 'ephemeris':

        for k in ogti.keys():

            if include_event_id_in_header:
                description = '# {}: {}\n'.format(k, event_description)
            else:
                description = '# {}\n'.format(event_description)

            p.create_event_ephemeris_txt_file(ogti[k], k, header=description)

    elif print_option == 'eps_event_file':

        for k in ogti.keys():

            if include_event_id_in_header:
                description = '{}; {}\n'.format(k, event_description)
            else:
                description = '{}\n'.format(event_description)

            p.create_event_file(ogti[k], k, description=description, output_utc_format=utc_format)

    elif print_option == 'eps_multi_events_file':

        if include_event_id_in_header:
            description = '{}; {}\n'.format(e.even_id, event_description)
        else:
            description = '{}\n'.format(event_description)

        p.create_multi_events_file(ogti, e.even_id, description='{}; {}\n'.format(e.even_id, description),
                                   output_utc_format=utc_format, event_file_name=event_file_name)

    else:

        logging.error('Undefined print option "{}"'.format(print_option))


def create_event_files_nnadir(ogti, e, event_description, print_option='ephemeris', output_dir='./',
                              utc_format="%Y-%m-%dT%H:%M:%SZ", include_event_id_in_header=True):
    """
    Create event files

    :param event_description: if specified: overwrite the event description
    :param ogti: dictionary event
    :param e: structure containing needed attributes (i.e. body, station, elevation ...)
    :param print_option: print option ['ephemeris', ...]
    :param output_dir: path fo the putput directory
    :return:
    """
    p = EventHandler(output_dir)

    if print_option == 'ephemeris':

        for k in ogti.keys():

            if include_event_id_in_header:
                description = '# {}: {}\n'.format(k, event_description)
            else:
                description = '# {}\n'.format(event_description)

            # p.create_event_dat_file(ta_range[k], k, header='# {}: {}\n'.format(k, description))
            p.create_event_ephemeris_txt_file(ogti[k], k, header=description)

    elif print_option == 'eps_event_file':

        for k in ogti.keys():
            # p.create_event_dat_file(ta_range[k], k, header='# {}: {}\n'.format(k, description))
            p.create_event_file(ogti[k], k, description='{}; {}\n'.format(k, event_description[k]),
                                output_utc_format=utc_format)
