"""
Created on January 25, 2017

@author: Claudio Munoz Crego (ESAC)
"""

import os
import sys
import logging
import datetime
import numpy as np
# from operator import itemgetter
import pandas

from esac_juice_pyutils.commons import tds
from soa_report.juice.eps_data.epsoutput import EpsOutput
from soa_report.juice.eps_data.df_data_latency import DfDataLatency


class DsLatency(DfDataLatency):
    """
    This class allows to handle (read, write) DS_latency file produced by bepiColombo SOA Tool
    """

    def __init__(self, input_file_path, read_start=None, experiment_to_ignore=[]):

        # self.df = self.get_data_frame_extended(input_file_path, experiment_to_ignore=[])
        self.df = self.get_data_frame(input_file_path, read_start, experiment_to_ignore)

        if self.df is not None:

            self.__get_eps_output_report_time_step__()

            self.start = pandas.to_datetime(self.df['datetime (UTC)'][0])
            self.end = pandas.to_datetime(self.df['datetime (UTC)'].iloc[-1])

    def __get_eps_output_report_time_step__(self):
        """
        Calculates the eps output report time step in seconds.
        """

        self.report_time_step = (self.df['datetime (UTC)'][1]
                                 - self.df['datetime (UTC)'][0]).total_seconds()

        self.Kbits_sec_to_Gbits_dt = self.report_time_step / 1000 / 1000

        logging.debug('eps output report_time_step = {} seconds'.format(self.report_time_step))

    def read(self, input_file_path):
        """
        Read event file

        :param input_file_path: path of the input data_rate_avg.out file
        :return EpsOutput Object
        """
        if not os.path.exists(input_file_path):
            logging.error('{} file {} does not exist'.format('Juice SOA data latency', input_file_path))

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
                    for ele in line.split(',')[1:]:
                        ele = ele.rstrip()
                        if ele.isdigit():
                            list_of_values.append(float(ele))
                        else:
                            list_of_values.append(ele)
                    data_out.data_value.append(list_of_values)

        return data_out

    def get_data_frame(self, input_file_path, read_start=None, experiment_to_ignore=[]):
        """
        Return eps data_latency as pandas frames

        :param input_file_path:
        :param read_start: Allow to specify the first time to read
        :param experiment_to_ignore: list of experiment to ignore
        :return: df: panda data frame
        """

        import pandas as pd

        data_out = self.read(input_file_path)

        # Create data frame keys
        df_keys = []
        for j in range(len(data_out.data_title[0])):
            df_keys.append(data_out.data_title[0][j] + ':' + data_out.data_title[1][j])

        # Fill data frame dictionary
        df_dictionary = {}
        for i in range(len(df_keys)):
            df_dictionary[df_keys[i]] = []
            # print df_keys[i]
            for line in data_out.data_value:
                # Remove undefined values +, - are set to 'NaN
                if line[i] == '+' or line[i] == '-':
                    line[i] = np.nan
                df_dictionary[df_keys[i]].append(line[i])

        ref_date = data_out.start_utc
        logging.debug('reference start time = {}'.format(ref_date))

        if not df_dictionary:

            logging.info('There is no latency; Latency file empty: {}'.format(input_file_path))
            return None

        if ':Elapsed time' in df_dictionary.keys():

            if len(df_dictionary['Elapsed time:ddd_hh:mm:ss']) == 0:

                logging.info('There is no latency; Latency file empty: {}'.format(input_file_path))
                return None

            df_dictionary['Elapsed time'] = df_dictionary.pop('Elapsed time:ddd_hh:mm:ss')

            # Check if relative first start time for latency is not 000_00:00:00
            # and in affirmative case insert this corresponding values
            if df_dictionary['Elapsed time'] != '000_00:00:00':
                for key in df_dictionary:
                    df_dictionary[key].insert(0, 0)

                df_dictionary['Elapsed time'][0] = '000_00:00:00'
                df_dictionary['timedelta (seconds)'] = [0]
                df_dictionary['datetime (UTC)'] = [ref_date]

            else:
                df_dictionary['timedelta (seconds)'] = []
                df_dictionary['datetime (UTC)'] = []

            df_dictionary['Elapsed time'] = df_dictionary.pop(':Elapsed time')

            df_dictionary['timedelta (seconds)'] = []
            df_dictionary['datetime (UTC)'] = []

            if ref_date:
                for t in df_dictionary['Elapsed time']:
                    dt = datetime.timedelta(days=int(t[0:3])) \
                         + datetime.timedelta(hours=int(t[4:6])) \
                         + datetime.timedelta(minutes=int(t[7:9])) \
                         + datetime.timedelta(seconds=int(t[10:]))

                    df_dictionary['timedelta (seconds)'].append(dt.total_seconds())
                    df_dictionary['datetime (UTC)'].append(ref_date + dt)

        elif 'Current time:dd-mmm-yyyy_hh:mm:ss' in df_dictionary.keys():

            if len(df_dictionary['Current time:dd-mmm-yyyy_hh:mm:ss']) == 0:
                logging.info('There is no latency; Latency file empty: {}'.format(input_file_path))
                return None

            df_dictionary['Current time'] = df_dictionary.pop('Current time:dd-mmm-yyyy_hh:mm:ss')

            # Check if relative first start time for latency is not 000_00:00:00
            # and in affirmative case insert this corresponding values

            df_dictionary['datetime (UTC)'] = []

            for t in df_dictionary['Current time']:
                date_time = datetime.datetime.strptime(t, "%d-%b-%Y_%H:%M:%S")

                df_dictionary['datetime (UTC)'].append(date_time)

            data_out.start_utc = datetime.datetime.strptime(df_dictionary['Current time'][0], "%d-%b-%Y_%H:%M:%S")

        else:

            logging.error('Please check eps file files format: {}'.format(input_file_path))
            sys.exit()

        df_dictionary = {k: v for k, v in df_dictionary.items() if not k.startswith("JUICE:")}
        for experiment in experiment_to_ignore:
            df_dictionary = {k: v for k, v in df_dictionary.items() if not k.startswith(f"{experiment}:")}

        df = pd.DataFrame(df_dictionary)

        if read_start:
            df = df[df['datetime (UTC)'] >= read_start]
            df.reset_index(drop=True, inplace=True)

        return df

    def get_data_frame_extended(self, input_file_path):
        """
        Return extended eps data_latency as pandas frames
        :param input_file_path:
        :return: df: panda data frame
        """

        df_ds_latency = self.get_data_frame(input_file_path)

        if df_ds_latency is None:
            return None

        dico = get_latency_accum(df_ds_latency)
        # print '\n', dico.keys()
        for dp in dico.keys():
            df_ds_latency[dp] = dico[dp]

        return df_ds_latency


def get_latency_accum(df, antenna_label='HGA'):
    """
    Build a data frame including eps downlink profiles

    :param df: panda data frame including X_band_Downlink,K_band_Downlink and Total_Downlink
    :param antenna_label: label use to filter antenna values
    :return: dico
    """

    dico = {'Total_Latency': [0]}
    col_label = '{}:Maximum'.format(antenna_label)

    for i in range(len(df['datetime (UTC)']) - 1):
        ant_total_latency = df[col_label][i + 1] + df[col_label][i + 1]
        dico['Total_Latency'].append(ant_total_latency)

    return dico
