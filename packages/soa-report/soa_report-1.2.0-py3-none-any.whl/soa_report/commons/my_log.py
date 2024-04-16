#!/usr/bin/python
"""
Created on March 31, 2017

@author: Claudio Munoz Crego (ESAC)

This Module define the log format
"""

import logging
import sys


def setup_logger(level='info'):
    """
    Setup logging level
    :param level: logger level define in ['info', 'debug']. Default value is 'info'.
    """

    logging_level = logging.INFO
    logging_format = '%(asctime)s[%(levelname)s]: %(message)s'
    logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

    if level == 'debug':
        logging_level = logging.DEBUG
        logging_format = '%(asctime)s[%(module)s.%(funcName)s][%(levelname)s]: %(message)s'
        # logging_format = '%(asctime)s[%(module)s][%(levelname)s]: %(message)s'
        logging_datefmt = '[%m/%d/%Y %H:%M:%S]'

        print('\nreset log level to "{}"'.format(level))

    logging.basicConfig(level=logging_level,
                        # filename='a.log',
                        stream=sys.stdout,
                        format=logging_format,
                        datefmt=logging_datefmt)
