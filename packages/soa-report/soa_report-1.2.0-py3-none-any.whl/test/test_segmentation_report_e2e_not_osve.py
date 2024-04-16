"""
Created on May 2023

@author: Claudio Munoz Crego (ESAC)

This Module allows run the Segmentation reporter for several cases

All the data are available on test_data_set directory

1) Generate segmentation report from ref test_case TDS/crema_5_0
The result is compared against a previous run (here the rst report)

2) Generate segmentation report from ref test_case TDS/overwrite_with_2_experiments
The result is compared against a previous run (here the rst report)

"""

import os
import logging
import unittest

from esac_juice_pyutils.commons.json_handler import load_to_dic
import soa_report.segmentation_reporter_cmd as segmentation_reporter

# disable logging during unit test
logging.disable(logging.CRITICAL)


class MyTestCase(unittest.TestCase):

    maxDiff = None

    def test_segmentation_report(self,):
        """
        Test (case 1) check Segmentation report generated as expected

        Here we do not run osve but only check the reporting part.
        This test is used for CI/DL purpose
        """

        test_data_set = '../TDS/crema_5_0'

        here = os.getcwd()
        print(f'here:{here}')
        os.chdir(test_data_set)
        working_dir = os.getcwd()

        config_file = 'Reporter_Config_e2e_test.json'

        cfg = load_to_dic(config_file)
        output_ref = cfg['request']["output_dir"]

        report_name = 'report'
        if "report_file_name" in cfg['request'].keys():
            report_name = cfg['request']['report_file_name']

        report_name_tmp = report_name + '_tmp'
        cfg['request']['report_file_name'] = report_name_tmp
        cfg['request']['run_simu'] = False

        segmentation_reporter.run(config_file, cfg, working_dir)

        tmp_values = list(open(os.path.join(output_ref, f'{report_name_tmp}.rst'), 'r'))
        tmp_ref = list(open(os.path.join(output_ref, f'{report_name}.rst'), 'r'))

        self.assertListEqual(tmp_values, tmp_ref)

        for f_tmp in os.listdir():
            if report_name_tmp in f_tmp:
                os.remove(f_tmp)

        os.chdir(here)

    def test_segmentation_report_overwrite_with_2_experiments(self,):
        """
        Test (case e) check Segmentation report generated as expected
        this exercise the overwrite period functionality with 2 experiments TARGETS, and EXPERIMENT_TYPE

        Here we do not run osve but only check the reporting part.
        This test is used for CI/DL purpose
        """

        test_data_set = '../TDS/overwrite_with_2_experiments'

        here = os.getcwd()
        print(here)
        os.chdir(test_data_set)
        working_dir = os.getcwd()

        config_file = 'config_json_2_claudio.json'

        cfg = load_to_dic(config_file)
        output_ref = cfg['request']["output_dir"] = 'output_generate_segmentation_for_e2e_test'
        cfg['request']['run_simu'] = 0

        report_name = 'report'
        if "report_file_name" in cfg['request'].keys():
            report_name = cfg['request']['report_file_name']

        report_name_tmp = report_name + '_tmp'
        cfg['request']['report_file_name'] = report_name_tmp
        cfg['request']['run_simu'] = False

        segmentation_reporter.run(config_file, cfg, working_dir)

        tmp_values = list(open(os.path.join(output_ref, f'{report_name_tmp}.rst'), 'r'))
        tmp_ref = list(open(os.path.join(output_ref, f'{report_name}.rst'), 'r'))

        self.assertListEqual(tmp_values, tmp_ref)

        for f_tmp in os.listdir():
            if report_name_tmp in f_tmp:
                os.remove(f_tmp)

        os.chdir(here)

