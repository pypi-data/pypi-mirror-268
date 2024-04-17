"""
Created on May 2023

@author: Claudio Munoz Crego (ESAC)

This Module allows run the Scenario reporter for several cases

All the data are available on test_data_set directory

1) Generate scenario report from ref test_case TDS/tds_scenario_marc
The result is compared against a previous run (here the rst report)

"""

import os
import logging
import unittest

from esac_juice_pyutils.commons.json_handler import load_to_dic
import soa_report.scenario_reporter_cmd as scenario_reporter


test_data_set = '../TDS/tds_scenario_marc'

# disable logging during unit test
logging.disable(logging.CRITICAL)


class MyTestCase(unittest.TestCase):

    maxDiff = None

    def test_scenario_report(self,):
        """
        Test (case 1) check scenario report generated as expected
        """

        here = os.getcwd()
        print(here)
        os.chdir(test_data_set)
        working_dir = os.getcwd()

        config_file = 'Reporter_Config_NAVCAM_modes.json'

        cfg = load_to_dic(config_file)
        output_ref = cfg['request']["output_dir"]

        report_name = 'report'
        if "report_file_name" in cfg['request'].keys():
            report_name = cfg['request']['report_file_name']

        report_name_tmp = report_name + '_tmp'
        cfg['request']['report_file_name'] = report_name_tmp

        scenario_reporter.run(config_file, cfg, working_dir)

        tmp_values = list(open(os.path.join(output_ref, f'{report_name_tmp}.rst'), 'r'))
        tmp_ref = list(open(os.path.join(output_ref, f'{report_name}.rst'), 'r'))

        self.assertListEqual(tmp_values, tmp_ref)

        for f_tmp in os.listdir():
            if report_name_tmp in f_tmp:
                os.remove(f_tmp)

        os.chdir(here)