"""
Created on April 17, 2017

@author: Claudio Munoz Crego (ESAC)

This module allows to load, parse and handle power_avg.out eps simulated data
"""

import os
import sys
import logging
import datetime
from operator import itemgetter
import numpy as np
import pandas

from esac_juice_pyutils.commons import tds
from soa_report.juice.eps_data.epsoutput import EpsOutput

from soa_report.juice.eps_data.df_power_avg import DfPowerAverage
from soa_report.juice.segmentation.power_metrics import get_extra_df as get_extra_df_segmentation
from soa_report.juice.soa.power_metrics import get_extra_df as get_extra_df_scenarios


class PowerAverage(DfPowerAverage):
    """
    This class allows to handle (read, write) power_avg file produced by bepiColombo SOA Tool
    """

    def __init__(self, input_file_path, eps_cfg_parameters=None, read_start=None, bat_capacity=None):

        self.battery_capacity = None

        self.df = self.get_data_frame_extended(input_file_path,
                                               read_start=read_start,
                                               bat_capacity=bat_capacity)

        if self.df is not None:
            self.__get_eps_output_report_time_step__()

            self.start = pandas.to_datetime(self.df['datetime (UTC)'][0])
            self.end = pandas.to_datetime(self.df['datetime (UTC)'].iloc[-1])

    def write(self, event_list, output_path):
        """
        Write event file to output_path
        :param event_list: list of event
        :param output_path: path of the ouput file name.
        :return N/A
        """
        event_list = sorted(event_list, key=itemgetter(0))

        f = open(output_path, 'w')

        f.write('Start_time: {}\n'.format(tds.et2utc(event_list[0][0])))
        f.write('End_time: {}\n\n'.format(tds.et2utc(event_list[-1][0])))

        for event in event_list:
            f.write('%s\t\t%s(COUNT=%d)\n' % (tds.et2utc(event[0]), event[1], event[2]))

        f.close()

    def read(self, input_file_path):
        """
        Read event file

        :param input_file_path: path of the input data_rate_avg.out file
        :return EpsOutput Object
        """
        if not os.path.exists(input_file_path):
            logging.error('{} file {} does not exist'.format('Juice SOA power average', input_file_path))

        data_out = EpsOutput(os.path.basename(input_file_path))

        f = open(input_file_path, 'r')
        for line in f.read().splitlines():

            if line.startswith('#'):  # reading file header
                line = line[1:].lstrip()
                metadata_header = line.split(':')[0]
                if ':' in line:
                    header_value = line.split(':')[1]
                    if 'Ref_date:' in line:
                        ref_date_str = line.split(':')[1].strip().split('\n')[0]
                        data_out.start_utc = tds.str2datetime(ref_date_str, d_format="%d-%B-%Y")
                        if not data_out.start_utc:
                            sys.exit()
                else:
                    header_value = ''

                data_out.header.append(['#', metadata_header, header_value.lstrip()])

            elif line != '':  # Reading values

                if not line[0].isdigit():

                    data_out.data_title.append(line.split(','))

                else:

                    list_of_values = [line.split(',')[0]]
                    list_of_float = [float(x) for x in line.split(',')[1:]]
                    list_of_values.extend(list_of_float)
                    data_out.data_value.append(list_of_values)

        return data_out

    def get_data_frame(self, input_file_path):
        """
        Return eps power_avg as pandas frames

        :param input_file_path:
        :return: df: panda data frame
        """

        import pandas as pd

        data_out = self.read(input_file_path)

        #  Create data frame keys
        df_keys = []
        for j in range(len(data_out.data_title[0])):
            df_keys.append(data_out.data_title[0][j]
                           + ':' + data_out.data_title[1][j].replace('(', '').replace(')', ''))
        df_dictionary = {}
        for i in range(len(df_keys)):
            df_dictionary[df_keys[i]] = []

            for line in data_out.data_value:
                df_dictionary[df_keys[i]].append(line[i])

        ref_date = data_out.start_utc
        logging.debug('reference start time = {}'.format(ref_date))

        if 'Elapsed time:ddd_hh:mm:ss' in df_dictionary.keys():

            df_dictionary['Elapsed time'] = df_dictionary.pop('Elapsed time:ddd_hh:mm:ss')

        elif 'Current time:dd-mmm-yyyy_hh:mm:ss' in df_dictionary.keys():

            df_dictionary['Current time'] = df_dictionary.pop('Current time:dd-mmm-yyyy_hh:mm:ss')

        if 'Elapsed time' in df_dictionary.keys():

            df_dictionary['timedelta (seconds)'] = []
            df_dictionary['datetime (UTC)'] = []

            for t in df_dictionary['Elapsed time']:
                dt = datetime.timedelta(days=int(t[0:3])) \
                     + datetime.timedelta(hours=int(t[4:6])) \
                     + datetime.timedelta(minutes=int(t[7:9])) \
                     + datetime.timedelta(seconds=int(t[10:]))

                df_dictionary['timedelta (seconds)'].append(dt.total_seconds())
                df_dictionary['datetime (UTC)'].append(ref_date + dt)

        elif 'Current time' in df_dictionary.keys():

            df_dictionary['timedelta (seconds)'] = []
            df_dictionary['datetime (UTC)'] = []

            t_0 = df_dictionary['Current time'][0]
            ref_time = datetime.datetime.strptime(t_0, "%d-%b-%Y_%H:%M:%S")

            for t in df_dictionary['Current time']:
                date_time = datetime.datetime.strptime(t, "%d-%b-%Y_%H:%M:%S")

                df_dictionary['datetime (UTC)'].append(date_time)

                dt = date_time - ref_time
                df_dictionary['timedelta (seconds)'].append(dt.total_seconds())

            data_out.start_utc = datetime.datetime.strptime(df_dictionary['Current time'][0], "%d-%b-%Y_%H:%M:%S")

        else:

            logging.error('Please check eps file files format: {}'.format(input_file_path))
            sys.exit()

        df = pd.DataFrame(df_dictionary)
        return df

    def get_data_frame_extended(self, input_file_path, read_start=None, bat_capacity=None, read_stop=None):
        """
        Return extended eps data_latency as pandas frames

        :param input_file_path:
        :param read_start: Allow to specify the first time to read
        :param read_stop: Allow to specify the final time to read
        :param bat_capacity: number of Watts
        :return: df: panda data frame
        """

        df = self.get_data_frame(input_file_path)

        if df is None:
            return None

        if bat_capacity:

            bat_cap = bat_capacity

            if 'Batt. DoD:%' in list(df.keys()):

                df['Batt.:%'] = 100 - df['Batt. DoD:%']

                self.battery_capacity = bat_cap

        # Platform is PLATFORM in segmentation and JUICE in scenario
        if 'JUICE:Watts' in list(df.keys()):
            df = get_extra_df_scenarios(df, self.battery_capacity, df['Batt.:%'])
        else:
            df = get_extra_df_segmentation(df)

        if read_start:
            df = df[df['datetime (UTC)'] >= read_start]
            df.reset_index(drop=True, inplace=True)
        if read_stop:
            df = df[df['datetime (UTC)'] <= read_stop]
            df.reset_index(drop=True, inplace=True)

        return df