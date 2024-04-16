"""
Created on March 2018

@author: Claudio Munoz Crego (ESAC)

This Module allows to report metrics from EPS output
"""

import os
import sys
import logging
import datetime
import numpy as np

import soa_report.commons.plots_utils as plots_utils

from soa_report.juice.eps_data.df_data_rate_avg import DfDataRateAverage


class SoaReportBasics(object):
    """
    This class allows to report EPS simulation Metrics
    """

    def __init__(self, my_date_partition=[], add_start_end_scenario=True):

        self.my_date_partition = sorted(my_date_partition)
        self.add_start_end_scenario = add_start_end_scenario

    def set_up_parameters(self, scenario, root_path, output_dir=''):
        """
        Set up parameters

        :param scenario: name of EPS package containing EPS output (it is a directory)
        :param root_path: base directory of scenario
        :param output_dir: path of output directory (there is a default values)
        :return: scenario, root_path, output_dir, plots_path
        """
        scenario_path = os.path.expandvars(os.path.join(root_path, scenario))
        if not os.path.exists(scenario_path):
            logging.error('bad directory: {}'.format(scenario_path))

        if output_dir == '':
            output_dir = os.path.join(scenario_path, 'soa_reports_output')
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
        else:
            output_dir = os.path.expandvars(output_dir)
            output_dir = os.path.abspath(output_dir)
            if not os.path.exists(output_dir):
                logging.warning('output dir does not exist: {}'.format(output_dir))
                output_base_dir = os.path.dirname(output_dir)

                if os.path.exists(output_base_dir):
                    logging.warning('output base directory exist; Trying to create output dir: {}'.format(output_dir))
                    os.mkdir(output_dir)

                else:

                    logging.error('Output dir nor output base directory exist; \ '
                                  'Please check ouput_dir in config file: {}'.format(output_dir))
                    sys.exit()

        plots_path = os.path.join(output_dir, 'plots')
        if not os.path.exists(plots_path):
            os.mkdir(plots_path)

        return scenario_path, root_path, output_dir, plots_path

    def get_template_rst2pdf(self):
        """
        Get the rst2pdf.style template hosted in source code within templates sub-directory

        :return: rst2pdf.style  path
        :rtype: python path
        """

        here = os.path.abspath(os.path.dirname(__file__))
        template_file = os.path.join(here, '../templates')
        template_file = os.path.join(template_file, 'default_rst2pdf.style')

        if not os.path.exists(template_file):
            logging.error('reference template file "%s" missing' % template_file)
            sys.exit()

        logging.info('{} loaded'.format(template_file))

        return template_file

    def set_partition_period(self, scenario_start, scenario_end, add_start_end_scenario=False):
        """
        Set Partition period

        :param scenario_start:
        :param scenario_end:
        :param add_start_end_scenario:
        :return:
        """

        logging.info('scenario period validity =[{}, {}]'.format(scenario_start, scenario_end))

        if add_start_end_scenario:
            self.my_date_partition.insert(0, scenario_start)
            self.my_date_partition.append(scenario_end)

        if len(self.my_date_partition) == 0:
            self.my_date_partition.append(scenario_start)
            self.my_date_partition.append(scenario_end)
            logging.warning('No date partition provided; We will used the total window (start, end) = ({}, {})'.format(
                scenario_start, scenario_end))

        else:

            for t in self.my_date_partition:

                if t < scenario_start or t > scenario_end:
                    logging.warning('{} time subset is out of scenario period [{}, {}]'.format(
                        t, scenario_start, scenario_end))

        my_date_partition_str = []
        for period in self.my_date_partition:
            my_date_partition_str.append(datetime.datetime.strftime(period, '%Y-%m-%dT%H:%M:%S.%f'))

        logging.info('my_date_partition_0 = {}'.format(my_date_partition_str))

    def get_periods(self, dv, df_type=DfDataRateAverage, my_date_partition=None):
        """
        Defines data_frames subset

        :param dv: pandas dataframe for the whole scenario
        :return: list of pandas dataframe corresponding to a given subset if periods
        """

        if my_date_partition is None:
            my_date_partition = self.my_date_partition

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        dv_time_step = (dv.df['datetime (UTC)'][1] - dv.df['datetime (UTC)'][0]).total_seconds()

        data_frames = {}
        for i in range(len(my_date_partition) - 1):
            (start, end) = (my_date_partition[i], my_date_partition[i + 1])
            start_str = datetime.datetime.strftime(start, date_format).split('.')[0]
            end_str = datetime.datetime.strftime(end, date_format).split('.')[0]
            period_label = '{}_{}'.format(start_str, end_str)

            if (end - start).total_seconds() > dv_time_step:
                new_df = df_type(dv.df, start, end)

                data_frames[period_label] = new_df
            else:
                logging.warning('Periods {} avoided; too short < {} sec'.format(
                    period_label, (end - start).total_seconds()))

        return data_frames

    def report_resources_info(self, n_level, proc_report, scenario_path, output_dir,
                              database_info_file='database.txt'):
        """
        Insert resources report info from database
        (included in the timeline Tool package export)

        :param n_level:
        :param proc_report: 
        :param scenario_path: scenario path
        :param output_dir: output directory
        :param database_info_file: text file name extracted from database
        :return:
        """

        report_resources = os.path.join(scenario_path, 'report_resources')
        if not os.path.exists(report_resources):
            logging.warning('report_resources directory does not exist in {}'.format(scenario_path))
        else:

            from shutil import copytree, ignore_patterns, rmtree
            source = report_resources
            destination = os.path.join(output_dir, 'report_resources')
            if os.path.exists(destination):
                rmtree(destination)
            copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

            report_resources = destination

            proc_report.write_head(n_level, 'Resources')

            report_resources_database = os.path.join(report_resources, database_info_file)
            if not os.path.exists(report_resources_database):
                logging.warning('database.txt does not exist in {}'.format(report_resources))
            else:
                proc_report.write_head(n_level + 1, database_info_file)
                relative_database_path = os.path.join(os.path.basename(os.path.dirname(report_resources_database)))
                proc_report.insert_literal(os.path.join(relative_database_path, database_info_file))

            # report_resources_overwritten = os.path.join(report_resources, 'overwritten.txt')
            # if not os.path.exists(report_resources_overwritten):
            #     logging.warning('database.txt does not exist in {}'.format(report_resources))
            # else:
            #     proc_report.write_head_subsubsection('overwritten.txt')
            #     proc_report.insert_literal(report_resources_overwritten)
            #
            #     if os.stat(report_resources_overwritten).st_size == 0:
            #         proc_report.write_text('\nNo overwritten data!\n')

    def report_spice_kernel_info(self, n_level, proc_report):
        """
        Report spice file currently loaded

        :param n_level:
        :param proc_report:
        :return:
        """

        from soa_report.commons.spice_kernel_utils import get_kernel_loaded_info

        proc_report.write_head(n_level, 'Spice Kernel files')

        kernel_info = get_kernel_loaded_info()
        logging.debug('kernel_info = {}'.format(kernel_info))
        metric = [['spice files']]
        my_list = ""
        for ele in kernel_info[1:]:
            tmp = os.path.basename(ele[0])
            if tmp:
                if not tmp.endswith('.tm'):
                    my_list += '{}\\n\\n'.format(tmp)
                    proc_report.write_text('{}\n\n'.format(tmp))

        metric.append([my_list])
        # proc_report.print_rst_table_2(metric)

    def generated_dv_summary(self, n_level, dv, data_frames, proc_report, experiment_type, my_periods):
        """
        Report summary section for a given experiment type

        :param dv: main dataframe
        :param data_frames: list of periods dataframes
        :param proc_report: report object
        :param experiment_type: experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
        :param my_periods: periods
        :param n_level: n_level: Report section level
        """

        report_summary_table_generated_dv_per_inst(n_level, data_frames, proc_report, experiment_type)

        create_plot_ssmm_status(dv, self.plots_path, proc_report, experiment_type, my_periods)

        create_plot_dv_to_ground(dv, self.plots_path, proc_report, experiment_type, my_periods)

    def generated_dv_accumulated_per_experiment(self, n_level, proc_report, df, experiment_type, my_periods):
        """
        Add a sub_section including plots for Generated Data Volume Accumulated per instruments

        :param n_level: Report header level
        :param proc_report: report object
        :param df: data_avg dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current window timw
        """

        proc_report.print_summary_section(n_level, 'Generated Data Volume Accumulated per {}'.format(experiment_type))

        create_plot_dv_accumulated_summary(df, self.plots_path, proc_report, experiment_type, my_periods)

        create_plots_dv_accumulated(df, self.plots_path, proc_report, experiment_type, my_periods)


def report_summary_table_data_avg_periods(n_level, dfs, proc_report,
                                          title='Generated DV, downlink, and SSMM status in Gbits'):
    """
    Create a summary report including for all sub-periods:
    - Generated data Volume (total)
    - Total Downlink Data Volume capability
    - Actual Total Downlink Data Volume to ground
    - data in the SSMM at the beginning of scenario
    - Remaining data in the SSMM at the end of scenario

    Notes:
    - The sum of all (sub-periods) is included in an additional (last) column if the number of sub-periods > 1.
    - The table is transposed (rows <-> lines) if number of sub-periods > 3 for user readability.

    :param n_level: Report section level
    :param dfs: dictionary including a subset of dataframes; keys are labels <start>_<end>
    :param proc_report: report structure
    :param title: default title
    """

    logging.debug(title)
    text = ''

    metrics = get_summary_table_data_avg_periods(dfs)

    proc_report.print_summary_section(n_level, title, objective_summary=text, metrics=metrics, figure=[])


def report_summary_table_generated_dv_per_inst(n_level, dfs, proc_report, experiment_type,
                                               title=''):
    """
    Report data volume generated per instrument.

    Notes:
    - The sum of all (sub-periods) in included in a an additional (last) column if the number of sub-periods > 1.
    - The table is transposed (rows <-> lines) if number of sub-periods > 3 for user readability.

    :param n_level: Report section level
    :param dfs: dictionary including a subset of dataframes; keys are labels <start>_<end>
    :param proc_report: report structure
    :param experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
    :param title: default title
    """

    if not title:
        title = 'Generated DV per {}'.format(experiment_type)
        logging.debug(title)

    text = ''

    df_key = list(dfs.keys())[0]
    list_of_experiments = sorted(dfs[df_key].get_total_accum_data_volume().keys())

    periods = [s.replace('_', ' ') for s in sorted(dfs.keys())]
    periods = [s.replace('T', ' ') for s in periods]
    metrics = [['Metric'] + periods + ['Total']]

    for inst in list_of_experiments:
        values = [round(dfs[k].get_total_accum_data_volume()[inst], 2) for k in sorted(dfs.keys())]
        metrics.append([inst] + values + [round(sum(values), 2)])

    if len(dfs) <= 1:
        metrics = [row[:-1] for row in metrics]

    if len(dfs.keys()) > 3:
        metrics = np.array(metrics).T.tolist()

    proc_report.print_summary_section(n_level, title, objective_summary=text, metrics=metrics, figure=[])


def get_summary_table_data_avg_periods(dfs):
    """
    Create a summary report including for all sub-periods:
    - Generated data Volume (total)
    - Total Downlink Data Volume capability
    - Actual Total Downlink Data Volume to ground
    - data in the SSMM at the beginning of scenario
    - Remaining data in the SSMM at the end of scenario

    Notes:
    - The sum of all (sub-periods) in included in an additional (last) column if the number of sub-periods > 1.
    - The table is transposed (rows <-> lines) if number of sub-periods > 3 for user readability.

    :param dfs: collection of data frames
    """

    title = 'Generated DV, downlink, and SSMM status in Gbits'
    logging.debug(title)

    periods = [s.replace('_', ' ') for s in sorted(dfs.keys())]
    periods = [s.replace('T', ' ') for s in periods]
    sub_phases_header = ['Metric'] + periods + ['Total All periods']
    metrics = [sub_phases_header]
    values = [round(sum(dfs[k].get_total_accum_data_volume().values()), 2) for k in sorted(dfs.keys())]
    metrics.append(['Generated data Volume (total)'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_total_downlink('XB_LINK'), 2) for k in sorted(dfs.keys())]
    metrics.append(['Total Downlink Data Volume capability  X band'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_total_downlink('KAB_LINK'), 2) for k in sorted(dfs.keys())]
    metrics.append(['Total Downlink Data Volume capability Ka band'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_total_downlink(), 2) for k in sorted(dfs.keys())]
    metrics.append(['Total Downlink Data Volume capability'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_x_band_accum(), 2) for k in sorted(dfs.keys())]
    metrics.append(['Actual Total Downlink Data Volume to ground X band'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_ka_band_accum(), 2) for k in sorted(dfs.keys())]
    metrics.append(['Actual Total Downlink Data Volume to ground Ka band'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_total_ssmm_accum(), 2) for k in sorted(dfs.keys())]
    metrics.append(['Actual Total Downlink Data Volume to ground'] + values + [round(sum(values), 2)])
    values = [round(dfs[k].get_ssmm_initial_value(), 2) for k in sorted(dfs.keys())]
    metrics.append(['data in the SSMM at the beginning of scenario'] + values + [round(values[0], 2)])
    values = [round(dfs[k].get_ssmm_last_value(), 2) for k in sorted(dfs.keys())]
    metrics.append(['Remaining data in the SSMM at the end of scenario'] + values + [round(values[-1], 2)])

    if len(dfs) <= 1:
        metrics = [row[:-1] for row in metrics]

    if len(dfs.keys()) > 3:
        metrics = np.array(metrics).T.tolist()

    return metrics


def create_plot_ssmm_status(dv, plots_path, proc_report, experiment_type, my_periods, title='SSMM Status [Gb]'):
    """
    Create SSMM status plot and insert in report

    :param dv: main dataframe
    :param plots_path: plots directory path
    :param proc_report: report object
    :param experiment_type: experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
    :param my_periods: current periods
    :param title: Plot title
    """

    objective_summary = ''

    fig_name = 'ssmm_status_' + experiment_type
    plots_utils.create_advanced_plot_ssmm_vs_max(dv.df, plots_path, option='png',
                                                 fig_name=fig_name, y_label='Gbits', my_periods=my_periods)

    plot_file_path = os.path.join('plots', os.path.basename(fig_name + '.png'))
    proc_report.rst_insert_figure(plot_file_path, title=title, text=objective_summary)


def create_plot_dv_to_ground(dv, plots_path, proc_report, experiment_type, my_periods,
                             title='Downlink Data Volume to ground'):
    """
    Create Downlink Data Violume to ground station(s) plot and insert in report

    :param dv: main dataframe
    :param plots_path: plots directory path
    :param proc_report: report object
    :param experiment_type: experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
    :param my_periods: current periods
    :param title: Plot title
    """

    fig_name = 'Downlink_Data_Volume_to_ground_' + experiment_type
    plots_utils.create_advanced_plot_1ax_2ay(dv.df, plots_path,
                                             ['XB_LINK:Accum', 'KAB_LINK:Accum', 'SSMM:Accum'],
                                             option='png', fig_name=fig_name, y_label='Gbits',
                                             my_periods=my_periods)
    plot_file_path = os.path.join('plots', os.path.basename(fig_name + '.png'))
    proc_report.rst_insert_figure(plot_file_path, title=title,
                                  text="")

    proc_report.write_text("\n")
    text = """\n\n* XB_LINK:Accum: data downlink to ground in Gbit for RF X-band\n\n
              \n\n* KAB_LINK:Accum: data downlink to ground in Gbit for RF Ka-band\n\n
              \n\n* SSMM:Accum: total (X + KA bands) data downlink to ground\n"""
    proc_report.write_text(text)


def create_plot_dv_accumulated_summary(df, plots_path, proc_report, experiment_type, my_periods, title=''):
    """
    Create a plot including all the experiment Data volume generated accumulated,
    and insert in report

    :param df: current dataframe
    :param plots_path: plots directory path
    :param proc_report: report object
    :param experiment_type: experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
    :param my_periods: current periods
    :param title: Plot title
    """

    if not title:
        title = 'Generated DV Accumulated for {}'.format(experiment_type)

    fig_name = 'plot_dv_generated_accum_all_{}'.format(experiment_type)

    list_of_experiments = [k for k in df.keys() if 'Accum' in k and 'SSMM' not in k and 'B_LINK' not in k]

    plots_utils.create_advanced_plot_1ax_2ay(df, plots_path, list_of_experiments,
                                             option='png', fig_name=fig_name, my_periods=my_periods,
                                             y_label='Gbits')

    proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                  title=title,
                                  text='')


def create_plots_dv_accumulated(df, plots_path, proc_report, experiment_type, my_periods):
    """
    Create one data volume generated accumulated plot for each experiment
    and insert in report

    :param df: current dataframe
    :param plots_path: plots directory path
    :param proc_report: report object
    :param experiment_type: experiment_type: experiment type from the list ['instrument_type', 'segment_type', 'target']
    :param my_periods: periods
    """

    list_of_experiments = [k for k in df.keys() if 'Accum' in k and 'SSMM' not in k and 'B_LINK' not in k]

    for k in list_of_experiments:
        fig_name = 'plot_dv_generated_accum_{}_{}'.format(experiment_type, k.split(':')[0])
        plots_utils.create_advanced_plot_1ax_2ay(df, plots_path, [k], option='png',
                                                 fig_name=fig_name, my_periods=my_periods, y_label='Gbits')

        proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                      title='{} Generated DV Accumulated'.format(k.split(':')[0]),
                                      text='')
