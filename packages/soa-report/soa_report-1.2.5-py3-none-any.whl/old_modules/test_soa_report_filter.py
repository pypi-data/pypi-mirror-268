"""
Created on March, 2018

@author: Claudio Munoz Crego (ESAC)

This Module allows to report exmgeo subsection including plots
"""

import logging


def test_1(root_dir):

    scenario = 'C2_simplified_phase3'

    Start_time = '2030-09-28T02:16:00'
    End_time = '2030-10-27T04:06:35'

    start = tds.str2datetime(Start_time)
    end = tds.str2datetime(End_time)
    mitad = tds.str2datetime('2030-10-15T00:00:00')

    my_date_partitions = [tds.str2datetime('2030-10-20T00:00:00'), mitad]
    # my_date_partitions = [mitad, tds.str2datetime('2030-10-20T00:00:00')]

    print('my_date_partitions= {}\n'.format(my_date_partitions))

    p = SoaReportFilter(my_date_partitions)

    p.create_report(scenario, root_dir, experiment_types=['target'])


def test_2(json_file):
    """
    Test generation of soa_report using json file
    :param json_file:
    :return:
    """

    from esac_juice_pyutils.commons import json_handler as my_json
    import esac_juice_pyutils.commons.tds as tds

    x = my_json.load_to_object(json_file)

    for simu in x.requests:
        partitions_times = [tds.str2datetime(t) for t in simu.partition_times]
        p = SoaReportFilter(partitions_times, simu.add_start_end_scenario)
        p.create_report(simu.scenario, simu.root_path,
                        experiment_types= simu.experiment_types, output_dir=simu.output_dir)


if __name__ == '__main__':

    import os
    from esac_juice_pyutils.commons import tds
    from esac_juice_pyutils.commons.my_log import setup_logger
    from soa_report.juice.segmentation_reporter import SoaReportFilter

    test_dir = os.path.abspath(os.path.dirname(__file__))
    project_dir = os.path.dirname(test_dir)

    setup_logger('debug')
    print('local directory = ', os.getcwd())

    root_dir = os.path.join(project_dir, 'test_files_2')

    print('\n-----------------------------------------------\n')
    logging.debug('start test')

    cfg_gile = os.path.join(root_dir, 'soa_report_filter_test_1.json')
    test_2(cfg_gile)

    logging.debug('end of test')
