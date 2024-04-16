"""
Created on May 2023

@author: Claudio Munoz Crego (ESAC)

This Module allows run the Segmentation reporter for several cases

All the data are available on test_data_set directory

1) Generate segmentation report from ref test_case TDS/crema_5_0
The result is compared against a previous run (here the rst report)

"""

import os
import logging
import unittest

from esac_juice_pyutils.commons.json_handler import load_to_dic
import soa_report.segmentation_reporter_cmd as segmentation_reporter


test_data_set = '../TDS/crema_5_0'

# disable logging during unit test
logging.disable(logging.CRITICAL)


class MyTestCase(unittest.TestCase):

    maxDiff = None

    def test_segmentation_report(self,):
        """
        Test (case 1) check Segmentation report generated as expected
        """

        test_data_set = '../TDS/crema_5_0'

        here = os.getcwd()
        print(here)
        os.chdir(test_data_set)
        working_dir = os.getcwd()

        config_file = 'Reporter_Config.json'

        cfg = load_to_dic(config_file)
        output_ref = cfg['request']["output_dir"]

        report_name = 'report'
        if "report_file_name" in cfg['request'].keys():
            report_name = cfg['request']['report_file_name']

        report_name_tmp = report_name + '_tmp'
        cfg['request']['report_file_name'] = report_name_tmp

        segmentation_reporter.run(config_file, cfg, working_dir)

        tmp_values = list(open(os.path.join(output_ref, f'{report_name_tmp}.rst'), 'r'))
        tmp_ref = list(open(os.path.join(output_ref, f'{report_name}.rst'), 'r'))

        self.assertListEqual(tmp_values, tmp_ref)

        for f_tmp in os.listdir():
            if report_name_tmp in f_tmp:
                os.remove(f_tmp)

        os.chdir(here)