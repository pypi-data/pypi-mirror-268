"""
Created on January 25, 2019

@author: Claudio Munoz Crego (ESAC)
"""

import logging


class DfDataRateAverage(object):
    """
    This class allows to handle (read, write) df_date_rate_avg produce as eps_output by MAPPS/EPS Tools
    """

    def __init__(self, df, start_date_time, end_date_time):

        self.df = self.get_data_frame_period(df, start_date_time, end_date_time)

        self.__get_eps_output_report_time_step__()

        self.start = self.df['datetime (UTC)'][0]
        self.end = self.df['datetime (UTC)'].iat[-1]  # iat faster than iloc if you only want value

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

    def get_generated_data_volume(self):
        """
        Return the total volume generated in Gbits
        This is the sum of uploaded data per instrument
        Note that is equivalent to Accum
        :return:
        """
        dic_summary = self.get_uploaded_data_volume()
        sum_of_uploaded_data = 0

        for k in sorted(dic_summary.keys()):
            sum_of_uploaded_data += dic_summary[k]

        return sum_of_uploaded_data

    def get_uploaded_data_volume(self, inst_filter=[]):
        """
        Returns a dictionary including the data volume uploaded for each instrument

        :param inst_filter: this list allow to filter a subset of instrument; by default all instrument.
        Note that is equivalent to Accum
        :return:
        """
        if len(inst_filter) == 0:
            inst_filter = [k for k in self.df.keys() if 'Upload' in k]

        dic_summary = {}
        for param in inst_filter:
            instrument = param.split(':')[0]
            dic_summary[instrument] = (self.df[param].sum() - self.df[param].iloc[0])\
                                      / 1000 / 1000 * self.report_time_step

        return dic_summary

    def get_total_accum_data_volume(self, inst_filter=[], label_to_ignore=['KAB_LINK', 'XB_LINK']):
        """
        Returns a dictionary including the data volume accumulated (downlink) for each instrument

        Note that assuming initial value could be no null we have to subtract it

        :param inst_filter: this list allow to filter a subset of instrument; by default all instrument.
        :param label_to_ignore: label use to remove Accum not related to experiments
        :return: dic_summary
        """

        if len(inst_filter) == 0:
            inst_filter = [k for k in self.df.keys() if 'Accum' in k and 'SSMM' not in k]
            for of in label_to_ignore:
                inst_filter = [k for k in inst_filter if of not in k]

        dic_summary = {}
        for param in inst_filter:
            instrument = param.split(':')[0]
            dic_summary[instrument] = self.df[param].iloc[-1] - self.df[param].iloc[0]

        return dic_summary

    def get_total_downlink(self, antenna_label=None):
        """
        Return the total downlink in Gbits including RF X-band + RF Ka-band
        Note: due to round errors could nul if report_time_step to big (i.e. 1day=86400)

        :param antenna_label: label use to filter antenna values
        return: df: dataframe including downlink per experiment
        """

        if antenna_label:

            total_downlink = self.df['{}:Downlink'.format(antenna_label)].sum() / 1000 / 1000 * self.report_time_step

        else:

            total_downlink = \
                self.df['KAB_LINK:Downlink'].sum() / 1000 / 1000 * self.report_time_step \
                + self.df['XB_LINK:Downlink'].sum() / 1000 / 1000 * self.report_time_step

        return total_downlink

    def get_total_ssmm_accum(self, experiment='SSMM'):
        """
        Return the values in Gbit of SSMM accumulated at the end of scenario
        This means the total (X + KA bands) data downlink to ground

        :param experiment: experiment; to use in case SSMM Platform and science are included
        :return: get_total_ssmm_accum
        """

        col_label = '{}:Accum'.format(experiment)
        return self.df[col_label].iloc[-1] - self.df[col_label].iloc[0]

    def get_x_band_accum(self):
        """
        Return the values in Gbit accumulated at the end of scenario
        This means the data downlink to ground in Gbit for RF X-band

        :return: X band Total downkink
        """
        col_label = 'XB_LINK:Accum'
        return self.df[col_label].iloc[-1] - self.df[col_label].iloc[0]

    def get_ka_band_accum(self):
        """
        Return the values in Gbit of accumulated data at the end of scenario
        This means the data downlink to ground in Gbit for RF Ka-band

        :return: K band Total downkink
        """

        col_label = 'KAB_LINK:Accum'
        return self.df[col_label].iloc[-1] - self.df[col_label].iloc[0]

    def get_ssmm_initial_value(self, ssmm_type='SSMM'):
        """
        Provide the SSMM value at the end of scenario
        :param ssmm_type: SSMM type; to use in case SSMM Platform and science are included
        :return: ssmm_last_value: SSMM last value in Gbit
        """

        return self.df['{}:Memory'.format(ssmm_type)].iloc[0]

    def get_ssmm_last_value(self, ssmm_type='SSMM'):
        """
        Provide the SSMM value at the end of scenario
        :param ssmm_type: SSMM type; to use in case SSMM Platform and science are included
        :return: ssmm_last_value: SSMM last value in Gbit
        """

        return self.df['{}:Memory'.format(ssmm_type)].iloc[-1]
