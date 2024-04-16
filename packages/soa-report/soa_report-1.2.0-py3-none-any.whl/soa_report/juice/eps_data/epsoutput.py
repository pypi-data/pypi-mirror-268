"""
Created on April 17, 2017

@author: Claudio Munoz Crego (ESAC)
"""

import os
import sys
import logging
import datetime


class EpsOutput(object):
    """
    This class allows to store and handle eps_output Objects
    """

    def __init__(self, name='OBS'):

        self.name = name
        self.start_utc = None  # datetime.datetime.now()
        self.header = []
        self.data_title = []
        self.data_value = []
