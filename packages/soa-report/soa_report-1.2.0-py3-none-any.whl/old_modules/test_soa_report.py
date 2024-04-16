#!/usr/bin/python
"""
Created on Feb 17, 2017

@author: Claudio Munoz Crego (ESAC)

This Module allows to test soa_eps_cmd.py
"""

import logging
import sys
import os


def test_soa(cfg_file):
    """
    Run Soa_report
    :param cfg_file: SOA configuration file
    :return:
    """
    if not os.path.exists(cfg_file):
        logging.error('Soa configuration file does not exist: {}'.format(cfg_file))
        sys.exit()

    soa = SoaReport(cfg_file)
    soa.generate_intercept_periods()


def test_soa_report(init_file_path):
    pass


if __name__ == '__main__':

    from esac_juice_pyutils.commons.my_log import setup_logger
    from soa_report.juice.scenario_reporter import SoaReport

    here = os.path.abspath(os.path.dirname(__file__))
    test_dir = os.path.dirname(here)
    package_dir = os.path.dirname(test_dir)

    print(here)
    print(test_dir)
    print(package_dir)

    setup_logger('debug')
    print(os.getcwd())

    print('\n-----------------------------------------------\n')

    logging.debug('Start of test')

    cfg_file = os.path.join(package_dir, 'test_files/soa_report/soaReport.ini')
    print(cfg_file)
    test_soa(cfg_file)

    logging.debug('end of test')
