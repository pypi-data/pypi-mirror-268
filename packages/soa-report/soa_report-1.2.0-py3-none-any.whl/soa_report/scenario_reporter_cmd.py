"""
Created on October 2022

@author: Claudio Munoz Crego (ESAC)

This Module generates resource Report using EPS output
"""

import argparse
import logging
import os
import shutil
import signal
import sys

from esac_juice_pyutils.commons.my_log import setup_logger
from esac_juice_pyutils.commons import json_handler as my_json

from soa_report.commons.env_variables import EnvVar
from soa_report.juice.scenario_reporter import SoaReportFilter
from soa_report import version

setup_logger()


def func_signal_handler(signal, frame):
    logging.error("Aborting ...")
    logging.info("Cleanup not yet implemented")
    sys.exit(0)


def parse_options():
    """
    This function allow to specify the input parameters
    - OutputDir: path of the Output directory
    - JsonFile: path of the configuration file
    - loglevel: debug, info
    - version: package version number
    :returns args; argument o parameter list passed by command line
    :rtype list
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--JsonFile",
                        help="Path of JsonFile defining report(s) to be generated",
                        required=False)

    parser.add_argument("-l", "--loglevel",
                        help=" Must be debug, info ",
                        required=False)

    parser.add_argument("-v", "--version",
                        help="return version number and exit",
                        action="version",
                        version='%(prog)s {}'.format(version))

    parser.add_argument("-g", "--getTemplate",
                        help="generate a configuration file template and exit",
                        action="store_true")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return args


def main():
    """
        Entry point for processing
        """

    signal.signal(signal.SIGINT, func_signal_handler)

    args = parse_options()

    if args.loglevel:
        if args.loglevel in ['info', 'debug']:
            setup_logger(args.loglevel)
        else:
            setup_logger()
            logging.warning(
                'log level value "{0}" not valid (use debug);  So default INFO level applied'.format(args.loglevel))
    else:
        setup_logger()

    here = os.path.abspath(os.path.dirname(__file__))

    if args.getTemplate:
        generate_configuration_file_template()

    if args.JsonFile:
        cfg_file = os.path.abspath(args.JsonFile)
        if not os.path.exists(cfg_file):
            logging.error('Configuration File "{}" does not exist'.format(cfg_file))
            sys.exit(0)

    else:
        logging.error('Please define Configuration File')
        sys.exit(0)

    working_dir = os.path.dirname(cfg_file)

    os.chdir(working_dir)

    cfg = my_json.load_to_dic(cfg_file)

    run(cfg_file, cfg, working_dir)

    os.chdir(here)
    logging.debug('goto root original directory: {}'.format(here))


def run(cfg_file, x_dic, working_dir):
    """
    Launch reporter generation

    :param cfg_file: configuration file
    :param x_dic: configuration parameters
    :param working_dir: working directory
    """
    if "config_for_command_line_tool" in list(x_dic.keys()):
        name_current_module = os.path.basename(str(sys.modules[__name__]))
        if '_cmd' in name_current_module:
            name_current_module = name_current_module.split('_cmd')[0]
        if x_dic['config_for_command_line_tool'] != name_current_module:
            logging.error('The config file "{}" is to run "{}" and not "{}"'.format(
                cfg_file, x_dic['config_for_command_line_tool'], name_current_module
            ))
            sys.exit()

    if 'env_var' in list(x_dic.keys()):
        env_var = x_dic['env_var']

        EnvVar(env_var)

    if 'run_sim' not in x_dic.keys():
        x_dic['run_sim'] = True

    if 'request' in list(x_dic.keys()):

        simu = x_dic['request']

        set_request_parameters(simu)

        p = SoaReportFilter(x_dic, simu, working_dir)
        p.create_report()

    else:

        logging.error('request section missing in configuration file: {}'.format(cfg_file))
        logging.error('This configuration file is not a valid configuration file, please check it!')
        sys.exit()


def set_request_parameters(simu):
    """
    Reset request parameters

    :param simu: report parameters
    """

    if 'include_power_metrics' not in list(simu.keys()):
        simu['include_power_metrics'] = True

    if 'include_ssmm_status_per_instruments' not in list(simu.keys()):
        simu['include_ssmm_status_per_instruments'] = True

    if 'include_downlink_status_per_instruments' not in list(simu.keys()):
        simu['include_downlink_status_per_instruments'] = True

    if 'include_instantaneous_data_rate_per_experiment' not in list(simu.keys()):
        simu['include_instantaneous_data_rate_per_experiment'] = False


def generate_configuration_file_template():
    """
    Generate a local copy of the template configuration file
    """

    here = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(here, 'templates', 'scenario_reporter.json')
    template_path_local_copy = os.path.join(os.getcwd(), os.path.basename(template_path))
    shutil.copyfile(template_path, template_path_local_copy)
    logging.info('configuration template file generated: {}'.format(template_path_local_copy))
    sys.exit(0)


def debug():
    """
    debug: Print exception and stack trace
    """

    e = sys.exc_info()
    print("type: %s" % e[0])
    print("Msg: %s" % e[1])
    import traceback
    traceback.print_exc(e[2])
    traceback.print_tb(e[2])


if __name__ == "__main__":

    try:
        main()
    except SystemExit as e:
        print(e)
        print("<h5>Internal Error. Please contact JUICE SOC </h5>")
        raise

    sys.exit(0)
