"""
Created on January 25, 2019

@author: Claudio Munoz Crego (ESAC)
"""

import logging
import pandas


class DfDataLatency(object):
    """
    This class allows to handle (read, write) DS_latency produce as eps_output by MAPPS/EPS Tools
    """

    def __init__(self, df, start_date_time, end_date_time):

        self.df = self.get_data_frame_period(df, start_date_time, end_date_time)

        self.__get_eps_output_report_time_step__()

    def __get_eps_output_report_time_step__(self):
        """
        Calculates the eps output report time step in seconds.
        """

        self.report_time_step = (self.df['datetime (UTC)'][1]
                                 - self.df['datetime (UTC)'][0]).total_seconds()

        self.Kbits_sec_to_Gbits_dt = self.report_time_step / 1000 / 1000

        logging.debug('eps output report_time_step = {} seconds'.format(self.report_time_step))

    def get_data_frame_period(self, df_all, start_date_time, end_date_time):
        """
        Extract dataframe for a given period = [start_date_time, end_date_time]

        :param df_all: dataframe
        :param start_date_time: start time
        :param end_date_time: end time
        """

        df = df_all.copy(deep=False)

        df['datetime (UTC)'] = pandas.to_datetime(df['datetime (UTC)'], format='%Y-%m-%dT%H:%M:%S.%f')

        mask = (df['datetime (UTC)'] >= start_date_time) & (df['datetime (UTC)'] <= end_date_time)
        df = df.loc[mask]
        df = df.reset_index()

        return df

    def get_absolute_max_latency(self, antenna_label='HGA'):
        """
        Returns the absolute maximum latency

        :param antenna_label: label use to filter antenna values
        :return: df: dataframe including maximun latency per experiment
        """

        return self.df['{}:Maximum'.format(antenna_label)].max()

    def get_absolute_mean_latency(self, antenna_label='HGA'):
        """
        Returns the absolute mean latency

        :param antenna_label: label use to filter antenna values
        :return: df: dataframe including mean latency per experiment
        """
        return self.df['{}:Maximum'.format(antenna_label)].mean()

    def get_max_latency(self, inst_filter=None):
        """
        Returns a dictionary including the maximum latency for each instrument

        :param inst_filter: this list allow to filter a subset of instrument; by default all instrument.
        return: df: dataframe including maximun latency per experiment
        """
        if inst_filter is None:
            inst_filter = []
        if len(inst_filter) == 0:
            inst_filter = [k for k in self.df.keys()
                           if ':' in k and 'Maximum' not in k and 'MULTI' not in k]

        dic_summary = {}
        for param in sorted(inst_filter):

            packet_store = param.split(':')[1]
            dic_summary[packet_store] = self.df[param].max()

        return dic_summary

    def get_mean_latency(self, inst_filter=None):
        """
        Returns a dictionary including the mean latency for each instrument

        :param inst_filter: this list allow to filter a subset of instrument; by default all instrument.
        :return: dic_summary
        """
        if inst_filter is None:
            inst_filter = []
        if len(inst_filter) == 0:
            inst_filter = [k for k in self.df.keys()
                           if ':' in k and 'Maximum' not in k and 'MULTI' not in k]

        dic_summary = {}
        for param in sorted(inst_filter):

            packet_store = param.split(':')[1]
            dic_summary[packet_store] = self.df[param].mean()

        return dic_summary

    def get_total_latency_accum(self):
        """
        Return the values in Gbit of Total Latency (X-band + K-band) at the end of scenario
        :return: total_Latency:
        """

        return self.df['Total_Latency'].sum()


# def get_latency_accum(df, antenna_label='HGA'):
#     """
#     Build a data frame including eps downlink profiles
#
#     :param df: panda data frame including X_band_Downlink,K_band_Downlink and Total_Downlink
#     :param antenna_label: label use to filter antenna values
#     :return: dico
#     """
#
#     dico = {'Total_Latency': [0]}
#     col_label = '{}:Maximum'.format(antenna_label)
#
#     for i in range(len(df['datetime (UTC)']) - 1):
#         ant_total_latency = df[col_label][i + 1] + df[col_label][i + 1]
#         dico['Total_Latency'].append(ant_total_latency)
#
#     return dico
