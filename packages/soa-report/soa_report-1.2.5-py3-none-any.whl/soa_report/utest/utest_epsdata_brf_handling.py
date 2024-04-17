"""
Created on October 2023

@author: Claudio Munoz Crego (ESAC)

This Module allows run check bite rate file handling

All the data are available on test_data_set directory

1) check bit rate file parsing

"""

import os
import logging
import unittest
from pandas import Timestamp

from esac_juice_pyutils.commons.json_handler import load_to_dic
from soa_report.juice.eps_data.brf import Brf


test_data_set = '../TDS/CONFIG/ISE'

# disable logging during unit test
logging.disable(logging.CRITICAL)


class MyTestCase(unittest.TestCase):

    def test_brf_handling(self,):
        """
        Test (case 1) check brf
        """
        here = os.getcwd()
        print(here)

        input_file = os.path.join(test_data_set, 'BRF_MAL_SGICD_2_1_300101_351005.brf')
        brf = Brf(input_file)

        df = brf.df

        tmp = df.iloc[0].tolist()

        self.assertListEqual(tmp,
                             ['2030-01-01T00:00:00Z',
                              87366.69723,
                              2730.209293,
                              69165.30198,
                              69165.30198,
                              1820.139529,
                              1820.139529,
                              Timestamp('2030-01-01 00:00:00+0000', tz='UTC')])