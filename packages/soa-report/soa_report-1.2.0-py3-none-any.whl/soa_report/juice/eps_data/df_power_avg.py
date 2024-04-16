"""
Created on March 24, 2021

@author: Claudio Munoz Crego (ESAC)
"""

import logging


class DfPowerAverage(object):
    """
    This class allows to handle (read, write) df_power_avg produce as eps_output by MAPPS/EPS Tools
    """

    def __init__(self, df, start_date_time, end_date_time):

        self.df = self.get_data_frame_period(df, start_date_time, end_date_time)

        self.__get_eps_output_report_time_step__()

        self.start = self.df['datetime (UTC)'][0]
        self.end = self.df['datetime (UTC)'].iat[-1]  # iat faster than iloc if you only whant value

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
        :param start_datetime:
        :param end_date_time:
        :return:
        """

        import pandas

        df = df_all.copy(deep=False)
        df['datetime (UTC)'] = pandas.to_datetime(df['datetime (UTC)'], format='%Y-%m-%dT%H:%M:%S.%f')
        mask = (df['datetime (UTC)'] >= start_date_time) & (df['datetime (UTC)'] <= end_date_time)
        df = df.loc[mask]
        df = df.reset_index()
        return df

    def get_total_duration(self):
        """
        Return total time cover by power
        :return: total duration
        """
        return self.end - self.start

