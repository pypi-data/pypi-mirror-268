"""
Created on March 2019

@author: Claudio Munoz Crego (ESAC)

This Module allows to report soa_report subsection including plots
"""

import os
import sys
import logging
import datetime
import numpy as np

from collections import namedtuple

import esac_juice_pyutils.commons.tds as tds

from soa_report.commons.rst_report import RstReport
from soa_report.commons.plots_utils import create_plot_pie
from soa_report.juice.segmentation.power_metrics import add_power_status_summary, calculate_power_status, \
    get_power_profiles_metrics, get_energy_profiles_metrics, get_power_profiles_metrics_percent
from soa_report.juice.eps_data.df_data_rate_avg import DfDataRateAverage
from soa_report.juice.eps_data.df_data_latency import DfDataLatency
from soa_report.juice.eps_data.df_power_avg import DfPowerAverage
from soa_report.juice.eps_data.data_rate_avg import DataRateAverage
from soa_report.juice.eps_data.ds_latency import DsLatency
from soa_report.juice.eps_data.power_avg import PowerAverage
import soa_report.juice.report.soa_report_basics as report_basics
import soa_report.commons.plots_utils as plots_utils


class SoaReportFilter(report_basics.SoaReportBasics):
    """
    This class allows to report EPS simulation Metrics
    """

    def __init__(self, x, simu, working_dir):

        o_simu = namedtuple('Struct', simu.keys())(*simu.values())

        partitions_times = [tds.str2datetime(t) for t in o_simu.partition_times]

        report_basics.SoaReportBasics.__init__(self, partitions_times, o_simu.add_start_end_scenario)

        self.simu = o_simu

        # battery_capacity_if_sim_not_run allows to set the battery capacity in case OSVE sim not run;
        # Only take into account if run_sin is 0/False
        self.battery_capacity_if_sim_not_run = None

        self.eps_cfg_parameters = self.preproc(x, o_simu, working_dir)

        root_path = os.path.expandvars(o_simu.root_path)
        self.root_path = os.path.abspath(root_path)

        self.plots_path = None

        self.experiment_to_ignore = []
        if 'experiment_to_ignore' in list(x['request'].keys()):
            self.experiment_to_ignore = x['request']['experiment_to_ignore']

    def preproc(self, x, simu, working_dir):
        """
        Run OSVE/EPS simulation

        :param x: config parameter object
        :param simu: simulation parameters (OSVE, EPS)
        :param working_dir: working directory
        :return: eps_cfg_parameters: configuration parameters
        """

        import spiceypy as spi

        from osve_wrapper.osve_advanced_wrapper import run_osve
        from collections import namedtuple

        eps_cfg_parameters = None

        run_simu = True
        if hasattr(simu, 'run_simu'):
            run_simu = simu.run_simu

        if run_simu:

            if 'osve' not in list(x.keys()):
                logging.error('"osve" section not defined in configuration file; Please check')
                logging.error('"osve" is required if run_simu is true/1 or not specified in configuration file')
                sys.exit(0)

            # Reduce simulation period to the start/end of partitions
            if simu.add_start_end_scenario:

                x['osve']['start_timeline'] = None
                x['osve']['end_timeline'] = None

                # Enforce OSVE  to cut Top ITL
                x['osve']['no_ptr_cut'] = False

            else:

                if len(self.my_date_partition) == 0:

                    x['osve']['start_timeline'] = None
                    x['osve']['end_timeline'] = None

                    if 'no_ptr_cut' not in x['osve']:
                        x['osve']['no_ptr_cut'] = False  # OSVE cutting to Top ITL by default

                elif len(self.my_date_partition) == 1:

                    logging.error('partition_times require at least two time when add_start_end_scenario is False (0)')
                    logging.error('Please review your setting for partition time')
                    sys.exit()

                else:

                    x['osve']['start_timeline'] = None
                    x['osve']['end_timeline'] = None

                    x['osve']['filterStartTime'] = self.my_date_partition[0].isoformat()
                    x['osve']['filterEndTime'] = self.my_date_partition[-1].isoformat()

            o_x_osve = namedtuple('Struct', x['osve'].keys())(*x['osve'].values())

            for experiment_type in simu.experiment_types:
                osve_working_directory = os.path.join(working_dir, o_x_osve.scenario)

                eps_cfg_parameters, spice_kernel_md_path = run_osve(osve_working_directory, o_x_osve, experiment_type)
                spi.furnsh(spice_kernel_md_path)

        elif hasattr(simu, 'battery_capacity_if_sim_not_run'):
            self.battery_capacity_if_sim_not_run = simu.battery_capacity_if_sim_not_run
            logging.info('Osve not run; Battery_capacity set to battery_capacity_if_sim_not_run '
                         'configuration parameter: {}'.format(simu.battery_capacity_if_sim_not_run))

        return eps_cfg_parameters

    def create_report(self):
        """
        Creates Soa reports

        1) Set Parameter and global objects
            - Simu, eps/osve parameters, and root path
        2) Initialize rst report object
            - Instantiate object, and set title and introduction
        3) fill report
        4) generate rst, html and docx report
        """

        simu = self.simu
        root_path = self.root_path

        (scenario_path, root_path, output_dir, self.plots_path) = \
            self.set_up_parameters(simu.scenario, root_path, simu.output_dir)
        experiment_types = simu.experiment_types

        proc_report = RstReport(self.plots_path, out='rst', output_path=output_dir)
        objective = 'Generate Summary Report'
        if hasattr(simu, 'report_title'):
            objective = simu.report_title

        proc_report.insert_page_break()
        proc_report.print_summary_intro(objective)

        proc_report.write_text('* Resources: See ANNEX\n')
        if self.eps_cfg_parameters is not None:
            proc_report.write_text('* Spice kernels: See ANNEX\n')

        if len(experiment_types) == 0:
            experiment_types = ['instrument_type', 'segment_type', 'target', 'all']
        elif len(experiment_types) == 1:
            if experiment_types[0].lower() == 'all':
                experiment_types = ['instrument_type', 'segment_type', 'target']

        self.fill_report(proc_report, scenario_path, experiment_types, output_dir)

        proc_report.rst_to_html()

        here = os.getcwd()
        os.chdir(output_dir)
        proc_report.pandoc_html_to_docx(docx_style_file=get_template_docx())
        os.chdir(here)

        if hasattr(simu, 'report_file_name'):
            proc_report.rename_report(simu.report_file_name, just_rename=True)

    def fill_report(self, proc_report, scenario_path, experiment_types, output_dir, n_level_base=1):
        """
        Fill Sequential report

        For each experiment type
            1) Load and parse data_avg, power_avg and DS_latency
            2) Set partitions
            3) Report DS, SSMM, downlink Summary
            4) if requested report Power and Energy summary
            5) add DS, SSMM, downlink Summary for each partition
            6) if requested report Power and Energy summary for each partition

        Note: dv.df is the dataframe for the entire simulation;
            # data_frames a list ad dataframe for each partition_period

        :param proc_report: report object
        :param scenario_path: scenario root directory
        :param experiment_types:  list of experiment types  ['instrument_type', 'segment_type', 'target', 'all']
        :param output_dir: output directory path
        :param n_level_base: title section baseline number
        """

        experiment_to_ignore = self.experiment_to_ignore

        eps_cfg_parameters = self.eps_cfg_parameters

        dv_exp_type = {}
        ds_exp_type = {}
        df_pow_exp_type = {}
        for experiment_type in experiment_types:

            n_level = n_level_base

            proc_report.insert_page_break()
            if len(experiment_types) > 1:
                proc_report.write_head(n_level, experiment_type.capitalize())
                n_level += 1

            experiment_type_dir = os.path.join(scenario_path, experiment_type)
            eps_output_dir = os.path.join(experiment_type_dir, 'eps_output')
            data_avg = os.path.join(eps_output_dir, 'data_rate_avg.out')
            ds_latency = os.path.join(eps_output_dir, 'DS_latency.out')
            if self.simu.include_power_metrics:
                power_avg = os.path.join(eps_output_dir, 'power_avg.out')

            read_start = None
            if not self.simu.add_start_end_scenario and len(self.my_date_partition) != 0:
                read_start = self.my_date_partition[0]

            dv0 = DataRateAverage(data_avg, experiment_to_ignore=experiment_to_ignore)
            dv = dv_exp_type[experiment_type] = DataRateAverage(data_avg, read_start=read_start,
                                                                experiment_to_ignore=experiment_to_ignore)
            ds = ds_exp_type[experiment_type] = load_ds_latency_dataframe(ds_latency)

            if self.simu.include_power_metrics:
                df_power = df_pow_exp_type[experiment_type] = \
                    load_power_avg_dataframe(power_avg, eps_cfg_parameters, read_start=read_start,
                                             bat_capacity=self.battery_capacity_if_sim_not_run)

            self.set_partition_period(dv0.start, dv0.end, self.simu.add_start_end_scenario)
            data_frames = self.get_periods(dv)

            my_periods = [[x, self.my_date_partition[i + 1]] for i, x in enumerate(self.my_date_partition[:-1])]

            # Report Data Volume budget summary
            report_basics.report_summary_table_data_avg_periods(n_level, data_frames, proc_report,
                                                                title='Data Volume budget summary')

            proc_report.insert_page_break()

            # Report estimated data volume generated per science experiment
            report_basics.report_summary_table_generated_dv_per_inst(
                n_level, data_frames, proc_report, experiment_type,
                title=f'Estimated data volume generated per science {experiment_type} [Gb]')

            # Plot DV Accumulated
            report_basics.create_plot_dv_accumulated_summary(
                dv.df, self.plots_path, proc_report, experiment_type, my_periods,
                title=f'Generated DV Accumulated for {experiment_type}s [Gb]')

            # Plot SSMM Status
            title = 'SSMM Filling Status [Gb]'
            proc_report.write_head(n_level, title)
            report_basics.create_plot_ssmm_status(
                dv, self.plots_path, proc_report, experiment_type, my_periods, title=title)

            # Plot Downlink Data Volume to ground/ DV Accumulated on Ground
            title = 'Data Volume accumulated on ground (X, Ka and X+Ka) [Gb]'
            proc_report.write_head(n_level, title)
            report_basics.create_plot_dv_to_ground(dv, self.plots_path, proc_report, experiment_type, my_periods)

            # self.generated_dv_summary(n_level + 1, dv, data_frames, proc_report, experiment_type, my_periods)

            # self.generated_dvs(proc_report, data_frames, experiment_type)
            # Generated DV vs Downlink per experiment (target)
            #
            proc_report.print_summary_section(n_level, 'Generated DV vs Downlink per {}'.format(experiment_type))

            if hasattr(self.simu, "overwrite_periods"):
                if self.simu.overwrite_periods and experiment_type == 'target':
                    self.generated_overwrite_all_periods(
                        n_level + 1, proc_report, dv.df, experiment_type, self.simu.overwrite_periods)
                    self.generated_overwrite_periods(
                        n_level + 1, proc_report, dv.df, experiment_type, self.simu.overwrite_periods)

            self.generated_dvs_and_dvs_vs_downlink(n_level + 1, proc_report, data_frames, experiment_type)
            #
            # Report Data volume share per "experiment_type: detailed analysis (per period)
            #
            proc_report.print_summary_section(
                n_level, f'Data volume share per {experiment_type}: detailed analysis (per period)')

            report_basics.create_plot_dv_accumulated_summary(
                dv.df, self.plots_path, proc_report, experiment_type, my_periods)

            report_basics.create_plots_dv_accumulated(
                dv.df, self.plots_path, proc_report, experiment_type, my_periods)

            # self.generated_dv_accumulated_per_experiment(n_level + 1, proc_report, dv.df, experiment_type, my_periods)

            # Plot Accumulated data volume per target (details)
            report_basics.create_plots_dv_accumulated(
                dv.df, self.plots_path, proc_report, experiment_type, my_periods)

            # Instantaneous data rate per instrument
            if self.simu.include_instantaneous_data_rate_per_experiment:
                self.add_instantaneous_data_rate_per_experiment(n_level + 1,
                                                                proc_report, dv.df, experiment_type, my_periods)

            # Report SSMM filling status [Gb] per instrument type store
            if self.simu.include_ssmm_status_per_instruments:
                self.add_ssmm_status_per_instrument(
                    n_level, proc_report, dv.df, experiment_type, my_periods)  # no pkt store for non instrument

            # Instantaneous data rate per instrument
            if self.simu.include_instantaneous_data_rate_per_experiment:
                self.add_instantaneous_data_rate_per_experiment(
                    n_level, proc_report, dv.df, experiment_type, my_periods)

            # Report Data Latency
            self.add_latency_report_juice(n_level, proc_report, ds, experiment_type, my_periods)

            # Report Power and Energy (Not for now at least for segmentation) if requested only
            if self.simu.include_power_metrics:
                self.add_power_metrics_if_requested(n_level, proc_report, df_power, experiment_type,
                                                my_periods, eps_cfg_parameters)

        proc_report.insert_page_break()
        proc_report.write_head(n_level, "ANNEX")

        self.report_resources_info(n_level, proc_report, scenario_path, output_dir)
        if self.eps_cfg_parameters is not None:
            proc_report.insert_page_break()
            self.report_spice_kernel_info(n_level + 2, proc_report)
        else:
            logging.info('OSVE not processed')

        proc_report.print_summary_end()

    def generated_dv_per_experiment_vs_downlink_capacity(self, proc_report, dic_sum_accum,
                                                         experiment_type, my_period='',
                                                         total_downlink_capacity=0, title='Generated DV'):
        """
        Generate rst table including Data volume generated in Gbits for all instruments.

        The % of generated dv versus downlink capacity is added in last column
        - if the input total_downlink_capacity=0, then last column is removed

        - a pie chart showing generated DV per experiment against total generated DV is added at the end of subsection.

        :param proc_report:
        :param dic_sum_accum:
        :param experiment_type:
        :param my_period:
        :param total_downlink_capacity:
        :param title:
        :return:
        """

        if 'NAVIGATION' not in dic_sum_accum.keys():
            dic_sum_accum['NAVIGATION'] = 0
            logging.warning('Experiment NAVIGATION (Navcam) not included in simulation; Set to 0')

        title = '{} per {} [{}]'.format(title, experiment_type, my_period)

        text_table = ('\n\nThe table bellow provides for each {} in [{}]: \n\n'
                      '* Generated DV in Gbits;\n\n'
                      '* Percentage Generated DV against Total generated in Gbits\n\n'
                      ).format(experiment_type, my_period.replace('_', ', '))

        metric_header = [experiment_type, 'Generated DV (Gbits)', '[%] Generated DV']

        total_dv_generated = sum(dic_sum_accum.values())

        if total_downlink_capacity:
            text_table += '* Percentage Generated DV against Total Downlink Capacity in Gbits\n\n'
            text_table += '* Percentage Generated DV against Science downlink Capacity in Gbits\n\n'

        # Add a column for % of downlink capacity
        metric_header = metric_header + ['[%] downlink capacity']
        metric_header = metric_header + ['[%] Science downlink capacity']

        metrics = [metric_header]

        percent = {}
        percent_vc_downlink_capacity = {}
        for k in sorted(dic_sum_accum.keys()):

            if total_dv_generated == 0:  # to handle unexpected case
                percent[k] = 0
            else:
                percent[k] = round(dic_sum_accum[k] / total_dv_generated * 100.0, 2)

            if total_downlink_capacity == 0:  # to handle unexpected case
                percent_vc_downlink_capacity[k] = 0
            else:
                percent_vc_downlink_capacity[k] = round(dic_sum_accum[k] / total_downlink_capacity * 100.0, 2)

        total_percent = round(sum(percent.values()), 1)
        total_percent_vs_downlink_capacity = round(sum(percent_vc_downlink_capacity.values()), 1)

        # Add a column for % of Science downlink capacity

        percent = {}
        percent_vs_sc_downlink_capacity = {}
        total_sc_downlink_capacity = total_downlink_capacity - dic_sum_accum['NAVIGATION']
        for k in sorted(dic_sum_accum.keys()):

            if total_dv_generated == 0:  # to handle unexpected case
                percent[k] = 0
            else:
                percent[k] = round(dic_sum_accum[k] / total_dv_generated * 100.0, 2)

            if total_downlink_capacity == 0:
                percent_vs_sc_downlink_capacity[k] = 0
            elif k == 'NAVIGATION':
                percent_vs_sc_downlink_capacity[k] = 0
            else:
                percent_vs_sc_downlink_capacity[k] = \
                    round(dic_sum_accum[k] / total_sc_downlink_capacity * 100.0, 2)

            metrics.append([k, round(dic_sum_accum[k], 2), percent[k],
                            percent_vc_downlink_capacity[k],
                            percent_vs_sc_downlink_capacity[k]])

        total_percent_vs_sc_downlink_capacity = round(sum(percent_vs_sc_downlink_capacity.values()), 1)

        metrics.append(
            ['Total', round(sum(dic_sum_accum.values()), 2),
             total_percent,
             total_percent_vs_downlink_capacity,
             total_percent_vs_sc_downlink_capacity])

        if not total_downlink_capacity:
            metrics = [row[:-1] for row in metrics]

        proc_report.write_text(text_table)
        if len(metrics) > 0:
            proc_report.print_rst_table(metrics)

        for ch in [':', 'T', '-', '=']:
            my_period = my_period.replace(ch, '').replace(' ', '_')

        my_period_label = my_period.replace('otal_', 'Total')
        plot_name = experiment_type + '_' + my_period_label
        plot_file_path = create_plot_pie(self.plots_path, plot_name, percent, min_values=0.01)
        plot_file_path = os.path.join('plots', os.path.basename(plot_file_path))
        figure = [plot_file_path]

        for fig in figure:
            fig = os.path.expandvars(fig)
            proc_report.rst_insert_figure(fig, title=title, text='')

    def generated_dvs_and_dvs_vs_downlink(self, n_level, proc_report, dfs, experiment_type):
        """
        Generates rst table including Data volume generated in Gbits for all instruments
        - Generate a subsection with a table including the Generated dv for the entire simulation
        - if there are more than on period/partition, add a subsection with on table per partition

        :param n_level: headking level number
        :param proc_report:
        :param dfs: dictionary including a subset of dataframes; keys are labels <start>_<end>
        :param experiment_type:
        :return:
        """

        dico_total = {}
        for key in dfs.keys():
            dic_sum_accum = dfs[key].get_total_accum_data_volume()
            for k in dic_sum_accum.keys():
                if k not in dico_total.keys():
                    dico_total[k] = dic_sum_accum[k]
                else:
                    dico_total[k] += dic_sum_accum[k]

        # Total Downlink Data Volume capability
        values = [round(dfs[k].get_total_downlink(), 2) for k in dfs.keys()]

        date_format = '%Y-%m-%dT%H:%M:%S'
        total_window = 'Total = {}_{}'.format(datetime.datetime.strftime(self.my_date_partition[0], date_format),
                                              datetime.datetime.strftime(self.my_date_partition[-1], date_format))

        proc_report.print_summary_section(n_level + 1, 'All Periods')
        self.generated_dv_per_experiment_vs_downlink_capacity(
            proc_report, dico_total, experiment_type, total_window, total_downlink_capacity=sum(values),
            title='Generated DV vs Downlink')

        if len(dfs.keys()) > 1:

            for key in sorted(dfs.keys()):
                proc_report.print_summary_section(n_level + 1, 'Sub-period [{}]'.format(key))

                dic_sum_accum = dfs[key].get_total_accum_data_volume()
                total_downlink = dfs[key].get_total_downlink()
                self.generated_dv_per_experiment_vs_downlink_capacity(
                    proc_report, dic_sum_accum, experiment_type + '_vs_Downlink', key,
                    total_downlink_capacity=total_downlink, title='Generated DV vs Downlink')

    def add_latency_report_juice(self, n_level, proc_report, ds, experiment_type, my_periods,
                                 objective_summary=''):
        """
        Generate rst table including Data volume generated in Gbits for all instruments

        :param n_level: Report header level
        :param proc_report: report object
        :param ds: ds latency dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: curent period [start, end]
        :param objective_summary: text summary
        :return:
        """

        if ds.df is None:

            logging.info('There is no latency; Latency file empty')

        else:

            dfs = self.get_periods(ds, DfDataLatency)

            title = 'Data Latency'
            logging.debug(title)

            text = """The table bellow provides for each packet store:
                      \n * Latency: The Maximum latency in days
                      \n * Average: The mean value of the latency in days
                      \n * Instrument: instrument name\n\n"""

            sub_phases_header = ['Metric'] + [s.replace('_', ' ') for s in sorted(dfs.keys())] + ['All']
            metrics = [sub_phases_header]
            values = [max(dfs[k].get_max_latency().values()) for k in sorted(dfs.keys())]
            metrics.append(['Maximum latency in days'] + values + [max(values)])
            values = [round(np.mean(list(dfs[k].get_mean_latency().values())), 2) for k in sorted(dfs.keys())]
            metrics.append(['Average latency in days'] + values + [round(np.mean(values), 2)])

            if len(metrics[0]) > 4:
                metrics = np.array(metrics).T.tolist()

            proc_report.print_summary_section(n_level, title, objective_summary=text, metrics=metrics, figure=[])

            sub_phases_header = [experiment_type.capitalize(), 'Mean latency [Days]', 'Max latency [Days]']
            latency_days = [k for k in ds.df.keys() if 'B-LINK' in k]  # and 'Maximum' in k]

            # for k in sorted(dfs.keys()):
            #     title = 'Sub-period per {} [{}]'.format(experiment_type, k)
            #     metrics = [sub_phases_header]
            #     mean_latency = dfs[k].get_mean_latency()
            #     max_latency = dfs[k].get_max_latency()
            #     # print mean_latency
            #     # print max_latency
            #     for l in mean_latency.keys():
            #         if 'Maximum' in l:
            #             to_end = [l, round(mean_latency[l], 2), round(max_latency[l], 2)]
            #         else:
            #             metrics.append([l, round(mean_latency[l], 2), round(max_latency[l], 2)])
            #             # metrics.append([l, round(mean_latency[l], 10), round(max_latency[l], 10)])
            #
            #     proc_report.print_summary_section(n_level + 1, title, objective_summary=text, metrics=metrics,
            #                                       figure=[])

            fig_name = 'data_latency_' + experiment_type
            plots_utils.create_plot_latency_presentation(ds.df, self.plots_path, option='png',
                                                         fig_name=fig_name, y_label='Days', my_periods=my_periods)
            plot_file_path = os.path.join('plots', os.path.basename(fig_name + '.png'))
            proc_report.rst_insert_figure(plot_file_path, title='Data Latency', text=objective_summary)

    def add_instantaneous_data_rate_per_experiment(self, n_level, proc_report, df, experiment_type, my_periods):
        """
        Add Data rate Generation per instrument subsection in the report

        :param n_level: Report header level
        :param proc_report: report object
        :param df: data_avg dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current windows time
        """

        proc_report.print_summary_section(n_level, 'Datarate Generation per {}'.format(experiment_type))

        fig_name = 'plot_datarate_generation_{}'.format(experiment_type)

        list_of_experiments = [k for k in df.keys() if 'Upload' in k]

        plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, list_of_experiments,
                                                 option='png', fig_name=fig_name, my_periods=my_periods,
                                                 y_label='kbits / sec')

        fig_path = os.path.join('plots', fig_name + '.png')
        proc_report.rst_insert_figure(fig_path, title='Datarate Generation for {}'.format(experiment_type), text='')

        for k in list_of_experiments:
            fig_name = 'plot_datarate_generation_{}_{}'.format(experiment_type, k.split(':')[0])
            plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, [k], option='png',
                                                     fig_name=fig_name, my_periods=my_periods, y_label='kbits / sec')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='{} Datarate Generation'.format(k.split(':')[0]),
                                          text='')

    def add_ssmm_status_per_instrument(self, n_level, proc_report, df, experiment_type, my_periods):
        """
        Add SSMM packet store status per experiment subsection in the report

        :param n_level: Report header level
        :param proc_report: report object
        :param df: data_avg dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current windows time
        """

        proc_report.print_summary_section(n_level, 'SSMM Status per {}'.format(experiment_type))

        fig_name = 'plot_ssmm_pkstore_{}'.format(experiment_type)

        list_of_experiments = [k for k in df.keys() if 'Memory' in k]

        plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, list_of_experiments,
                                                 option='png', fig_name=fig_name, my_periods=my_periods,
                                                 y_label='Gbits')

        proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                      title='SSMM Packet Store [Gbits] for {}'.format(experiment_type),
                                      text='')

        list_of_experiments = [k for k in df.keys() if 'Memory' in k and 'SSMM' not in k]

        for k in list_of_experiments:
            fig_name = 'plot_sssm_pkstore_{}_{}'.format(experiment_type, k.split(':')[0])
            plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, [k], option='png',
                                                     fig_name=fig_name, my_periods=my_periods, y_label='Gbits')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='{} SSMM Packet Store [Gbits]'.format(k.split(':')[0]),
                                          text='')

    def generated_overwrite_all_periods(self, n_level, proc_report, dfs, experiment_type, overwrite_periods,
                                    date_format='%Y-%m-%dT%H:%M:%S'):
        """
        Generates rst table including Data volume generated in Gbits for all instruments

        - Generate a subsection with a table including the Generated dv for the entire simulation
        - if there are more than on period/partition, add a subsection with on table per partition

        :param n_level: Report header level
        :param proc_report: report object
        :param dfs: dictionary including a subset of dataframes; keys are labels <start>_<end>
        :param experiment_type: experiment type (i.e. instrument, target)
        :param overwrite_periods: applicable window time
        :param date_format: format date use for reporting
        """

        from esac_juice_pyutils.periods.event_period_merger import PeriodMerger
        from dateutil.parser import parse

        period_merger = PeriodMerger()

        over_periods = []
        for over_period in overwrite_periods['target']:
            (start, end) = (parse(over_period['start']), parse(over_period['end']))
            over_periods.append([start, end])

        (start_sim_period, end_sim_period) = (dfs['datetime (UTC)'].iloc[0], dfs['datetime (UTC)'].iloc[-1])
        no_over_periods = [[start_sim_period, end_sim_period]]
        no_over_periods = period_merger.get_event_sub(no_over_periods, over_periods)

        dico_total = {}

        for p in no_over_periods:

            df_tmp = DfDataRateAverage(dfs, p[0], p[1])
            dic_sum_accum = df_tmp.get_total_accum_data_volume()

            for k in dic_sum_accum.keys():
                if k not in dico_total.keys():
                    dico_total[k] = dic_sum_accum[k]
                else:
                    dico_total[k] += dic_sum_accum[k]

        for p in overwrite_periods['target']:

            (start, end) = (parse(over_period['start']), parse(over_period['end']))
            df_tmp = DfDataRateAverage(dfs, start, end)

            period_downlink = df_tmp.get_total_downlink()
            logging.debug('period_downlink: {}'.format(period_downlink))

            # proc_report.write_head(n_level + 1, f'Period [{start}, {end}]:')
            # metrics = [[experiment_type, '% of downlink Capacity', 'DV [Gbits]']]

            for [k, val] in p['experiments']:
                k = str(k).upper()
                if k not in list(dico_total.keys()):
                    logging.warning('Invalid experiment: {}'.format(k))
                else:
                    dico_total[k] += val * period_downlink / 100.
                    # metrics.append([k, val, round(val * period_downlink / 100., ndigits=2)])

            # proc_report.print_rst_table(metrics)

        # Generate metrics about generate DV vs downlink for full simulation including overwriting
        dfs_all = DfDataRateAverage(dfs, start_sim_period, end_sim_period)
        values_total = round(dfs_all.get_total_downlink(), 2)

        proc_report.print_summary_section(n_level + 1, 'All Periods with overwrite')

        total_window = 'Total = {}_{}'.format(datetime.datetime.strftime(start_sim_period, date_format),
                                              datetime.datetime.strftime(end_sim_period, date_format))
        self.generated_dv_per_experiment_vs_downlink_capacity(proc_report, dico_total, experiment_type,
                                                              total_window, total_downlink_capacity=values_total,
                                                              title='Generated DV vs Downlink')

    def generated_overwrite_periods(self, n_level, proc_report, dfs, experiment_type, overwrite_periods,
                                    date_format='%Y-%m-%dT%H:%M:%S'):
        """
        Generates rst table including Data volume generated in Gbits for all instruments

        - Generate a subsection with a table including the Generated dv for the entire simulation
        - if there are more than on period/partition, add a subsection with on table per partition

        :param n_level: Report header level
        :param proc_report: report object
        :param dfs: dictionary including a subset of dataframes; keys are labels <start>_<end>
        :param experiment_type: experiment type (i.e. instrument, target)
        :param overwrite_periods: applicable window time
        :param date_format: format date use for reporting
        """

        from dateutil.parser import parse

        # proc_report.write_head(n_level, 'Sub Period(s) Overwrite')

        for over_period in overwrite_periods['target']:

            (start, end) = (parse(over_period['start']), parse(over_period['end']))
            df_over_period = DfDataRateAverage(dfs, start, end)

            period_downlink = df_over_period.get_total_downlink()
            logging.debug('period_downlink: {}'.format(period_downlink))

            proc_report.write_head(n_level + 1, f'Sub Period Overwrite [{start}, {end}]:')
            metrics = [[experiment_type, '% of downlink Capacity', 'DV [Gbits]']]

            dico_over_period = {}
            for [k, val] in over_period['experiments']:
                k = str(k).upper()
                if k not in list(dico_over_period.keys()):
                    dico_over_period[k] = val * period_downlink / 100.
                else:
                    dico_over_period[k] += val * period_downlink / 100.

                metrics.append([k, val, round(val * period_downlink / 100., ndigits=2)])

            # proc_report.print_rst_table(metrics)

            values = round(df_over_period.get_total_downlink(), 2)
            self.generated_dv_per_experiment_vs_downlink_capacity(proc_report, dico_over_period, experiment_type,
                                                                  f'Period Overwrite [{start}, {end}]',
                                                                  total_downlink_capacity=values,
                                                                  title='Generated DV vs Downlink')

    def add_power_metrics_if_requested(self, n_level, proc_report, df_power, experiment_type,
                                       my_periods, eps_cfg_parameters):
        """
        Add power metrics if requested.

        :param n_level: Report header level
        :param proc_report: report object
        :param df_power: df power dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current period [start, end]
        :param eps_cfg_parameters: epd.cfg parameters
        """

        if self.simu.include_power_metrics:
            add_power_status_summary(n_level, proc_report, df_power, my_periods[0][0], my_periods[-1][-1])

        if self.simu.include_power_metrics:

            if hasattr(self.simu, 'include_power_metrics_partition_details'):
                add_pwr_metrics_details = self.simu.include_power_metrics_partition_details
            else:
                add_pwr_metrics_details = 0

            self.add_power_status_per_experiment(n_level + 1, proc_report, df_power, experiment_type, my_periods,
                                                 self.plots_path, my_periods[0][0], my_periods[-1][-1],
                                                 eps_cfg_parameters=eps_cfg_parameters,
                                                 include_power_metrics_partition_details=add_pwr_metrics_details,
                                                 include_plot_experiment_power=False)

    def add_power_status_per_experiment(self, n_level, proc_report, df_power, experiment_type,
                                        my_periods, plots_dir, start, end, objective_summary='',
                                        eps_cfg_parameters=None,
                                        include_power_metrics_partition_details=False,
                                        include_plot_experiment_power=False):
        """
        Add power per experiment subsection in the report

        :param n_level: Report header level
        :param proc_report: report object
        :param df_power: df power dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current period [start, end]
        :param plots_dir: path to plot directory
        :param start: absolute stat time
        :param end: absolute end time
        :param objective_summary: text summary
        :param eps_cfg_parameters: epd.cfg parameters
        :param include_plot_experiment_power: flag to add power info; False by default
        :param include_power_metrics_partition_details: flag to add sub-periods details; False by default to reduce report size.
        """

        if df_power.df is None:

            logging.info('There is no power_avg; file empty')

        else:

            dfs = self.get_periods(df_power, DfPowerAverage)

            proc_report.print_summary_section(n_level, 'Power Status per {}'.format(experiment_type))

            title = 'Power Average'
            logging.debug(title)

            bat_percent = [label for label in df_power.df.keys() if '%' in label]
            inst_platform = \
                ['Available:Watts', 'Available_power_for_science:Watts', 'Batt. DoD:Watts', 'Batt.:Watts',
                 'XB_LINK:Watts', 'KAB_LINK:Watts', 'NAVIGATION:Watts', 'SSMM:Watts', 'PLATFORM:Watts',
                 'Batt_discharges:Watts']
            no_instruments = bat_percent + inst_platform
            inst_experiment = [label for label in df_power.df.keys() if
                               label not in no_instruments and "Watts" in label]
            inst_platform = [label for label in inst_platform if label in df_power.df.keys()]

            proc_report.write_head(n_level + 1, 'Total Periods ')
            proc_report.write_head(n_level + 2, 'Power Status')

            import copy
            my_df_power = copy.copy(df_power)
            df_power_total = DfPowerAverage(my_df_power.df, start, end)
            tmp_platform = calculate_power_status(df_power_total.df, inst_filter=inst_platform)
            tmp_experiment = calculate_power_status(df_power_total.df, inst_filter=inst_experiment)
            tmp_bat_per = calculate_power_status(df_power_total.df, inst_filter=bat_percent)

            proc_report.print_rst_table(get_power_profiles_metrics(tmp_platform))
            proc_report.print_rst_table(get_power_profiles_metrics(tmp_experiment))
            proc_report.print_rst_table(get_power_profiles_metrics_percent(tmp_bat_per))

            proc_report.print_summary_section(n_level, 'Energy Status')

            metrics = get_energy_profiles_metrics(tmp_platform)
            proc_report.print_rst_table(metrics)

            metrics = get_energy_profiles_metrics(tmp_experiment)
            proc_report.print_rst_table(metrics)

            percent = {}
            for k, val in metrics:
                if 'SEGMENT' not in k and 'otal' not in k:
                    percent[k] = float(val)
                elif k == 'total_used_by_science':
                    total_percent = float(val)
            if total_percent > 0:
                for k, val in percent.items():
                    percent[k] = round(val / total_percent * 100, ndigits=2)

                fig_name = 'pie_energy_{}'.format(experiment_type)
                create_plot_pie(plots_dir, fig_name, percent, min_values=0.01)
                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='science Instrument: Energy Sharing',
                                              text='')

            # fig_name = 'donut_energy_{}'.format(experiment_type)
            # plot_file_path = proc_report.create_plot_donut(self.plots_path, fig_name, percent, min_values=0.01,
            #                                              colors=colors)
            # proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
            #                               title='science Instrument: Energy Sharing',
            #                               text='')

            # fig_name = 'plot_power_avg_{}'.format(experiment_type)
            # self.create_plot_power_avg(ds.df, self.plots_path, fig_name=fig_name,
            #                            instruments=['Total:Watts', 'Available:Watts', 'Batt. DoD:Watts'],
            #                            my_periods = my_periods)
            #
            # proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
            #                               title='Total Power Average for {}'.format(experiment_type),
            #                               text='')

            fig_name = 'Power_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available:Watts', 'total_Juice_science:Watts',
                                                           'PLATFORM:Watts', 'total_power_used_by_science:Watts',
                                                           'Batt_discharges:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Status',
                                          text='')

            fig_name = 'Power_used{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['total_Available_not_used:Watts', 'total_bat_used:Watts', ],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Status Used',
                                          text='')

            fig_name = 'Batt Discharge and Charge'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Batt_discharges:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Batt Discharge',
                                          text='')

            fig_name = 'plot_energy_accum_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available_energy_accum:Wh', 'Total_energy_accum:Wh'],
                                              my_periods=my_periods,
                                              y_label='Energy (Wh)')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Energy Accum',
                                          text='')

            fig_name = 'plot_energy_accum_science_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available_accum_energy_for_science:Wh',
                                                           'total_energy_accum_used_by_science:Wh'],
                                              my_periods=my_periods,
                                              y_label='Energy (Wh)')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Energy Accum',
                                          text='')

            fig_name = 'Science_Power_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available_power_for_science:Watts',
                                                           'total_power_used_by_science:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Science Power',
                                          text='')

            fig_name = 'plot_power_batt_dod_{}'.format(experiment_type)
            plots_utils.create_plot_bat_dod(df_power, plots_dir, fig_name=fig_name,
                                            instruments=['Batt. DoD:Watts', 'Batt. DoD:%'],
                                            my_periods=my_periods, y_label='Batt. DoD:Watts')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Batt DoD for {}'.format(experiment_type),
                                          text='')

            fig_name = 'plot_power_batt_status_{}'.format(experiment_type)
            plots_utils.create_plot_bat_status(df_power, plots_dir, fig_name=fig_name,
                                               instruments=['Batt.:Watts', 'Batt.:%'],
                                               my_periods=my_periods, y_label='Batt.:Watts')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Batt Status for {}'.format(experiment_type),
                                          text='')

            for inst in inst_experiment:
                fig_name = 'plot_power_avg_{}_{}'.format(experiment_type, inst.split(':')[0])
                plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                                  instruments=[inst],
                                                  my_periods=my_periods)

                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='Power Average for {}:{}'.format(experiment_type, inst),
                                              text='')

            if include_power_metrics_partition_details:

                if len(my_periods) == 1:
                    logging.info('There is only one period!; So need to add partition details')
                    return 0

                for k in sorted(dfs.keys()):

                    title = 'Sub-period per {} [{}]'.format(experiment_type, k)

                    proc_report.write_head(n_level + 1, title)

                    percent = {}
                    for l, val in metrics:
                        if 'SEGMENT' not in k and 'otal' not in l:
                            percent[l] = float(val)
                        elif l == 'total_used_by_science':
                            total_percent = float(val)

                    if total_percent > 0:

                        for l, val in percent.items():
                            percent[l] = round(val / total_percent * 100, ndigits=2)

                        fig_name = 'pie_energy_{}{}'.format(experiment_type,
                                                            k.replace(':', '').replace('_', '').replace('-', ''))
                        create_plot_pie(plots_dir, fig_name, percent, min_values=0.01)
                        proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                      title='science Instrument: Energy Sharing',
                                                      text='')

                    fig_name = 'plot_power_available_{}_{}'.format(experiment_type,
                                                                   k.replace(':', '').replace('_', '').replace('-', ''))

                    plots_utils.create_plot_power_avg(dfs[k].df, plots_dir, fig_name=fig_name,
                                                      instruments=['Available:Watts', 'total_Juice_science:Watts',
                                                                   'PLATFORM:Watts',
                                                                   'total_power_used_by_science:Watts'],
                                                      my_periods=my_periods)

                    proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                  title='Power Status',
                                                  text='')

                    tmp_platform = calculate_power_status(dfs[k].df, inst_filter=inst_platform)
                    tmp_experiment = calculate_power_status(dfs[k].df, inst_filter=inst_experiment)
                    tmp_bat_per = calculate_power_status(dfs[k].df, inst_filter=bat_percent)

                    proc_report.print_rst_table(get_power_profiles_metrics(tmp_platform))
                    proc_report.print_rst_table(get_power_profiles_metrics(tmp_experiment))
                    proc_report.print_rst_table(get_power_profiles_metrics_percent(tmp_bat_per))

                    metrics = get_energy_profiles_metrics(tmp_platform)
                    proc_report.print_rst_table(metrics)

                    metrics = get_energy_profiles_metrics(tmp_experiment)
                    proc_report.print_rst_table(metrics)

                    if include_plot_experiment_power:
                        for inst in inst_experiment:
                            fig_name = 'plot_power_avg_{}_{}_{}'.format(experiment_type, inst,
                                                                        k.replace(':', '').replace('_', '').replace('-',
                                                                                                                    ''))

                            plots_utils.create_plot_power_avg(dfs[k].df, plots_dir, fig_name=fig_name,
                                                              instruments=[inst],
                                                              my_periods=my_periods)

                            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                          title='Power Average for {}:{}'.format(experiment_type, inst),
                                                          text='')


def load_power_avg_dataframe(power_avg, eps_cfg_parameters, read_start=None, bat_capacity=None):
    """
    Get power_avg data frame

    :param power_avg: power_avg latency file path
    :param eps_cfg_parameters: dictionary including eps parameter from eps.cfg
    :param read_start: Allow to specify the first time to read
    :return: df_power: power_avg dataframe
    """

    df_power = PowerAverage(power_avg, eps_cfg_parameters, read_start, bat_capacity)

    return df_power


def load_ds_latency_dataframe(ds_latency):
    """
    Get ds_latency data frame
    :param ds_latency: data latency file path
    :return: ds: ds_latency dataframe
    """

    ds = DsLatency(ds_latency)

    return ds


def get_template_docx():
    """
    Get the style.docx template hosted in source code within templates sub-directory

    :param: orientation_landscape: Flag to enforce A4 landscape orientation; default False
    :return: style.docx   path
    :rtype: python path
    """

    default_template = 'custom-reference.docx'

    here = os.path.abspath(os.path.dirname(__file__))
    template_file = os.path.join(here, 'templates')
    template_file = os.path.join(template_file, default_template)

    if not os.path.exists(template_file):
        logging.error('reference template file "%s" missing' % template_file)
        sys.exit()

    logging.info('{} loaded'.format(template_file))

    return template_file
