"""
Created on February 2021

@author: Claudio Munoz Crego (ESAC)

This Module allow to set environment variables like $HOME
only defined for python when running this code.


"""

import os
import sys
import logging


class EnvVar(object):
    """
    This class allows to set environment variables
    """

    def __init__(self, var_names):

        self.var_names = var_names
        self.set_env_var(var_names)

    def set_env_var_to_path(self, var_name, var_path):
        """
        Set local Environment to a given path (if exists)

        :param var_name: Local variable name
        :param var_path: Local path
        :return:
        """

        var_path = os.path.expandvars(var_path)

        if os.path.exists(var_path):

            os.environ[var_name] = var_path
            logging.info('{} set to {}'.format(var_name, os.getenv(var_name)))

            if var_name not in os.environ.keys():

                logging.error('Env var should be defined: {}'.format(var_name))
                logging.error('List of Env var')

                for k in sorted(os.environ.keys()):
                    print('\t{}: {}'.format(k, os.environ[k]))

        else:

            logging.error('Bad Environment variable "{}" path: {}'.format(var_name, var_path))
            sys.exit()

    def set_env_var(self, var_names):
        """
        Set env variables
        :param var_names:
        """

        for k, v in var_names.items():

            self.set_env_var_to_path(k, v)

    def subsitute_env_vars_in_path(self, my_path):
        """
        Substitute local variable within a given path

        :param my_path: Local path
        :param var_name: dictionary of variables
        :return:
        """

        for k, v in self.var_names.items():

            my_path = my_path.replace(k, v)

        return my_path

