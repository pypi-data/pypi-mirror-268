"""
Created on March, 2021

@author: Claudio Munoz Crego (ESAC)
"""

import os
import sys
import logging
import datetime
import pandas as pd


class PowerProFile(object):
    """
    This class allows to handle (read, write) power profile file (*.pwr) used by bepiColombo SOA Tool
    """

    def __init__(self, input_file_path):

        self.input_file_path = input_file_path
        self.__read__(input_file_path)

    def __read__(self, input_file_path):
        """
        Read bit rate file
        :param input_file_path: path of the input .brf file
        :return EpsOutput Object
        """

        bit_rate_file = os.path.expandvars(input_file_path)
        if not os.path.exists(bit_rate_file):
            logging.error('{} file "{}" does not exist'.format('BepiColombo SOA power bite rate file: ', bit_rate_file))
            sys.exit()

        self.dico_pwr_values = {}
        self.dico_pwr_header = []

        f = open(bit_rate_file, 'rU')
        for line in f.readlines():

            if line.startswith('#'):  # reading file header
                line = line[1:].lstrip()
                metadata_header = line.split(':')[0]
                if ':' in line:
                    header_value = line.split(':')[1]
                else:
                    header_value = ''

                self.dico_pwr_header.append(['#', metadata_header, header_value.lstrip()])

            elif line[0].isdigit():  # Reading values
                pwr_date_str = line[0:20][:-1] + '000Z'

                pwr_date_utc = datetime.datetime.strptime(pwr_date_str, '%y-%jT%H:%M:%S.%fZ')

                if '#' in line[21:]:
                    pwr_value = float(line[21:].split('#')[0])
                    pwr_comment = line[21:].split('#')[1]
                else:
                    pwr_value = float(line[21:])
                    pwr_comment = ''

                self.dico_pwr_values[pwr_date_utc] = pwr_value

    def get_data_frame(self):
        """
        Return power profile information

        :return: df: panda data frame
        """

        df_dictionary = {'datetime (UTC)': [], 'Power brf (Watts)': []}

        for key in sorted(self.dico_pwr_values.keys()):
            df_dictionary['datetime (UTC)'].append(key)
            df_dictionary['Power brf (Watts)'].append(self.dico_pwr_values[key])

        df = pd.DataFrame(df_dictionary)
        return df
