"""
Created on September 2022

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
from soa_report.juice import colors
from soa_report.juice.soa.power_metrics import add_power_status_summary, calculate_power_status, \
    get_power_profiles_metrics, get_energy_profiles_metrics, \
    get_power_profiles_metrics_percent
from soa_report.juice.eps_data.df_data_latency import DfDataLatency
from soa_report.juice.eps_data.df_power_avg import DfPowerAverage
from soa_report.juice.eps_data.data_rate_avg import DataRateAverage
from soa_report.juice.eps_data.ds_latency import DsLatency
from soa_report.juice.eps_data.power_avg import PowerAverage
import soa_report.juice.report.soa_report_basics as soa_report_basics
import soa_report.commons.plots_utils as plots_utils

AVAILABLE_POWER_DEF = """
The available is:

    Available = JUICE + total_instruments + total_available_lost + total_available_stored_in_batt - total_bat_used

    where:

    * `Available`: Energy available from solar panels for platform, instruments, and charged battery;
    * `JUICE`: Energy used by the JUICE Platform including NAVCAM and RADEM;
    * `total_instruments`: Energy used by instruments;
    * `total_available_lost`: Available energy not used and therefore lost (not needed by platform/instruments and battery recharge);
    * `total_available_stored_in_batt`: Available energy used to charge battery;
    * `total_bat_used`: Energy provided by battery (when not enough energy is available).
    \n
"""


class SoaReportFilter(soa_report_basics.SoaReportBasics):
    """
    This class allows to report EPS simulation Metrics
    """

    def __init__(self, x, simu, working_dir):

        o_simu = namedtuple('Struct', simu.keys())(*simu.values())

        partitions_times = [tds.str2datetime(t) for t in o_simu.partition_times]

        soa_report_basics.SoaReportBasics.__init__(self, partitions_times, o_simu.add_start_end_scenario)

        self.simu = o_simu

        # battery_capacity_if_sim_not_run allows to set the battery capacity in case OSVE sim not run;
        # Only take into account if run_sin is 0/False
        self.battery_capacity_if_sim_not_run = None

        self.eps_cfg_parameters = self.preproc(x, o_simu, working_dir)

        root_path = os.path.expandvars(o_simu.root_path)
        self.root_path = os.path.abspath(root_path)

        self.plots_path = None

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

        run_simu = False
        if hasattr(simu, 'run_simu'):
            run_simu = simu.run_simu

        if 'osve' in list(x.keys()):

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
                if run_simu:
                    eps_cfg_parameters, spice_kernel_md_path = \
                        run_osve(osve_working_directory, o_x_osve, experiment_type)
                    spi.furnsh(spice_kernel_md_path)

        if not run_simu:

            if hasattr(simu, 'battery_capacity_if_sim_not_run'):
                self.battery_capacity_if_sim_not_run = simu.battery_capacity_if_sim_not_run
                logging.info('Osve not run; Battery_capacity set to battery_capacity_if_sim_not_run '
                             'configuration parameter: {}'.format(simu.battery_capacity_if_sim_not_run))
            else:
                logging.error(
                    'It seems battery_capacity_if_sim_not_run parameters is not defined in configuration file; Please define it')
                sys.exit()

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
            objective = simu.report_title + f': {self.simu.scenario}'
        proc_report.print_summary_intro(objective)

        if experiment_types != ["instrument"]:
            logging.warning('experiment type must be set to "instrument"')

        self.fill_report(proc_report, scenario_path, experiment_types, output_dir)

        proc_report.rst_to_html()

        here = os.getcwd()
        os.chdir(output_dir)
        proc_report.pandoc_html_to_docx(docx_style_file=get_template_docx())
        os.chdir(here)

        if hasattr(simu, 'report_file_name'):
            proc_report.rename_report(simu.report_file_name, just_rename=True)

    def fill_report(self, proc_report, scenario_path, experiment_types, output_dir, n_level=1):
        """
        Fill Sequential report

        For each experiment type
            1) Load and parse data_avg, power_avg and DS_latency
            2) Set partitions
            3) Report DS, SSMM, downlink Summary
            4) if requested report Power and Energy summary
            5) add DS, SSMM, downlink Summary for each partition
            6) if requested report Power and Energy summary for each partition

        :param proc_report: report object
        :param scenario_path: scenario root directory
        :param experiment_types:  list of experiment types  ['instrument_type', 'segment_type', 'target', 'all']
        :param output_dir: output directory path
        :param n_level: title section baseline number
        """

        proc_report.insert_page_break()

        eps_cfg_parameters = self.eps_cfg_parameters

        dv_exp_type = {}
        ds_exp_type = {}
        df_pow_exp_type = {}
        for experiment_type in experiment_types:

            proc_report.insert_page_break()
            proc_report.write_head(n_level, experiment_type.capitalize())

            experiment_type_dir = os.path.join(scenario_path, experiment_type)
            eps_output_dir = os.path.join(experiment_type_dir, 'eps_output')
            data_avg = os.path.join(eps_output_dir, 'data_rate_avg.out')
            ds_latency = os.path.join(eps_output_dir, 'DS_latency.out')
            if self.simu.include_power_metrics:
                power_avg = os.path.join(eps_output_dir, 'power_avg.out')

            read_start = None
            if not self.simu.add_start_end_scenario and len(self.my_date_partition) != 0:
                read_start = self.my_date_partition[0]

            dv = dv_exp_type[experiment_type] = DataRateAverage(data_avg, read_start=read_start)
            self.set_partition_period(dv.start, dv.end, self.simu.add_start_end_scenario)
            my_periods = [[x, self.my_date_partition[i + 1]] for i, x in enumerate(self.my_date_partition[:-1])]
            dv.df = dv.df[dv.df['datetime (UTC)'] >= my_periods[0][0]]
            dv.df = dv.df[dv.df['datetime (UTC)'] <= my_periods[-1][-1]]
            dv.df.reindex()
            data_frames = self.get_periods(dv)

            ds = ds_exp_type[experiment_type] = load_ds_latency_dataframe(ds_latency)
            # filter ds.df = ds.df[ds.df['datetime (UTC)'] >= my_periods[0][0]]
            # filter ds.df = ds.df[ds.df['datetime (UTC)'] >= my_periods[-1][-1]]
            # filter ds.df.reindex()

            if self.simu.include_power_metrics:
                df_power = df_pow_exp_type[experiment_type] = \
                    load_power_avg_dataframe(power_avg, eps_cfg_parameters, read_start=read_start,
                                             bat_capacity=self.battery_capacity_if_sim_not_run)
                df_power.df = df_power.df[df_power.df['datetime (UTC)'] >= my_periods[0][0]]
                df_power.df = df_power.df[df_power.df['datetime (UTC)'] <= my_periods[-1][-1]]
                df_power.df.reindex()
                df_power_frames = self.get_periods(df_power)

            # Report Data Budget Summary
            soa_report_basics.report_summary_table_data_avg_periods(n_level + 1, data_frames, proc_report)

            if self.simu.include_power_metrics:
                add_power_status_summary(n_level + 1, proc_report, df_power, AVAILABLE_POWER_DEF)

            proc_report.insert_page_break()
            proc_report.write_head(n_level, experiment_type.capitalize() + ' Details per Experiment and Periods')

            self.generated_dv_summary(n_level + 1, dv, data_frames, proc_report, experiment_type, my_periods)

            self.generated_dvs_and_dvs_vs_downlink(n_level + 1, proc_report, data_frames, experiment_type)

            # dv.df is the dataframe for the entire simulation;
            # data_frames a list ad dataframe for each partition_period
            self.generated_dv_accumulated_per_experiment(n_level + 1, proc_report, dv.df, experiment_type, my_periods)

            # Instantaneous data rate per instrument
            if self.simu.include_instantaneous_data_rate_per_experiment:
                self.add_instantaneous_data_rate_per_experiment(
                    n_level + 1, proc_report, dv.df, experiment_type, my_periods)

            # SSMM Status per instrument
            if self.simu.include_ssmm_status_per_instruments:
                self.add_ssmm_status_per_instrument(n_level + 1, proc_report, dv.df, experiment_type,
                                                    my_periods)  # no pkt store for non instrument

            # Downlink Status
            if self.simu.include_downlink_status_per_instruments:
                self.add_downlink_status_per_instrument(n_level + 1, proc_report, dv.df, experiment_type, my_periods)

            self.add_latency_report_juice(n_level + 1, proc_report, ds, experiment_type, my_periods)

            if self.simu.include_power_metrics:

                if hasattr(self.simu, 'include_power_metrics_partition_details'):
                    add_pwr_metrics_details = self.simu.include_power_metrics_partition_details
                else:
                    add_pwr_metrics_details = 0

                self.add_power_status_per_experiment(n_level + 1, proc_report, df_power, df_power_frames,
                                                     experiment_type,
                                                     my_periods,
                                                     self.plots_path, my_periods[0][0], my_periods[-1][-1],
                                                     eps_cfg_parameters=eps_cfg_parameters,
                                                     include_power_metrics_partition_details=add_pwr_metrics_details,
                                                     include_plot_experiment_power=False)

        # proc_report.insert_page_break()
        # proc_report.write_head(n_level, "ANNEX")
        #
        # self.report_resources_info(n_level + 1, proc_report, scenario_path, output_dir)
        # if self.eps_cfg_parameters is not None:
        #     proc_report.insert_page_break()
        #     self.report_spice_kernel_info(n_level + 1, proc_report)
        # else:
        #     logging.info('OSVE not processed')

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

        if 'NAVCAM' not in dic_sum_accum.keys():
            dic_sum_accum['NAVCAM'] = 0
            logging.warning('Experiment NAVCAM not included in simulation; Set to 0')

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
        total_sc_downlink_capacity = total_downlink_capacity - dic_sum_accum['NAVCAM'] - dic_sum_accum['RADEM']
        for k in sorted(dic_sum_accum.keys()):

            if total_dv_generated == 0:  # to handle unexpected case
                percent[k] = 0
            else:
                percent[k] = round(dic_sum_accum[k] / total_dv_generated * 100.0, 2)

            if total_downlink_capacity == 0:
                percent_vs_sc_downlink_capacity[k] = 0
            elif k == 'NAVCAM' or k == 'RADEM':
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
        plot_file_path = create_plot_pie(self.plots_path, plot_name, percent, min_values=0.01,
                                         colors=colors)
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

        proc_report.print_summary_section(n_level, 'Generated DV vs Downlink per {}'.format(experiment_type))

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

        proc_report.print_summary_section(n_level + 1, 'Total Periods')
        self.generated_dv_per_experiment_vs_downlink_capacity(
            proc_report, dico_total, experiment_type, total_window, total_downlink_capacity=sum(values),
            title='Generated DV vs Downlink')

        if len(dfs.keys()) > 1:

            for key in sorted(dfs.keys()):
                proc_report.print_summary_section(n_level + 1, 'Sub-periods [{}]'.format(key))

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

            # sub_phases_header = [experiment_type.capitalize(), 'Mean latency [Days]', 'Max latency [Days]']
            # latency_days = [k for k in ds.df.keys() if 'B-LINK' in k]  # and 'Maximum' in k]

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
        Add Datarate Generation per instrument subsection in the report

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

        for k in list_of_experiments:

            fig_name = 'plot_sssm_pkstore_{}_{}'.format(experiment_type, k.split(':')[0].replace(' ', '_'))
            plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, [k], option='png',
                                                     fig_name=fig_name, my_periods=my_periods, y_label='Gbits')

            if df[k].max() > 0:

                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='{} SSMM Packet Store [Gbits]'.format(k.split(':')[0]),
                                              text='')

            else:
                proc_report.write_text('\n{} SSMM Packet Store = 0 [Gbits] (always empty)\n'.format(k.split(':')[0]))

    def add_downlink_status_per_instrument(self, n_level, proc_report, df, experiment_type, my_periods):
        """
        Add packet store downlink status per experiment subsection in the report

        :param n_level: Report header level
        :param proc_report: report object
        :param df: data_avg dataframe
        :param experiment_type: experiment type (i.e. instrument, target)
        """

        proc_report.print_summary_section(n_level, 'Downlink Status per {}'.format(experiment_type))

        fig_name = 'plot_downlink_{}'.format(experiment_type)

        list_of_experiments = [k for k in df.keys() if 'Downlink' in k or 'Download' in k]

        plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, list_of_experiments,
                                                 option='png', fig_name=fig_name, my_periods=my_periods,
                                                 y_label='Gbits')

        proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                      title='Downlink [Gbits] for {}'.format(experiment_type),
                                      text='')

        for k in list_of_experiments:
            fig_name = 'plot_downlink_{}_{}'.format(experiment_type, k.split(':')[0].replace(' ', '_'))
            plots_utils.create_advanced_plot_1ax_2ay(df, self.plots_path, [k], option='png',
                                                     fig_name=fig_name, my_periods=my_periods, y_label='Gbits')

            if df[k].max() > 0:

                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='{} Downlink [Gbits]'.format(k.split(':')[0]),
                                              text='')

            else:
                proc_report.write_text('\n{} SSMM Packet Store = 0 [Gbits] (always empty)\n'.format(k.split(':')[0]))

    def add_power_status_per_experiment(self, n_level, proc_report, df_power, df_power_frames, experiment_type,
                                        my_periods, plots_dir, start, end, objective_summary='',
                                        eps_cfg_parameters=None,
                                        include_power_metrics_partition_details=False,
                                        include_plot_experiment_power=False):
        """
        Add power per experiment subsection in the report

        :param n_level: Report header level
        :param proc_report: report object
        :param df_power: df power dataframe
        :param df_power_frames: df power dataframe for current period
        :param experiment_type: experiment type (i.e. instrument, target)
        :param my_periods: current period [start, end]
        :param plots_dir: path to plot directory
        :param start: absolute stat time
        :param end: absolute end time
        :param objective_summary: text summary
        :param eps_cfg_parameters: epd.cfg parameters
        :param include_plot_experiment_power: flag to add power info; False by default
        :param include_power_metrics_partition_details: flag to add sub-periods details;
            False by default to reduce report size.
        """

        if df_power.df is None:

            logging.info('There is no power_avg; file empty')

        else:

            dfs = df_power_frames

            proc_report.write_head(n_level, 'Power Status per {}'.format(experiment_type))

            title = 'Power Average'
            logging.debug(title)

            bat_percent = [label for label in df_power.df.keys() if '%' in label]
            inst_platform = \
                ['Available:Watts', 'Available_power_for_science:Watts', 'Batt. DoD:Watts', 'Batt.:Watts',
                 'XB_LINK:Watts', 'KAB_LINK:Watts', 'NAVCAM:Watts', 'RADEM:Watts', 'SSMM:Watts', 'JUICE_platform:Watts',
                 'JUICE:Watts', 'Batt_discharges:Watts']
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

            fig_name = 'Power_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available:Watts', 'total_instruments:Watts',
                                                           'JUICE_platform:Watts',
                                                           'Batt_discharges:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Status',
                                          text='')

            fig_name = 'Power_RF_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['XB_LINK:Watts', 'KAB_LINK:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Status RF',
                                          text='')

            fig_name = 'Power_used{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['total_bat_used:Watts',
                                                           'total_available_not_used_stored_in_batt:Watts',
                                                           'total_available_lost:Watts'],
                                              my_periods=my_periods)

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Power Status Used',
                                          text='')

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

            proc_report.write_head(n_level + 2, 'Power  Accum')

            for inst in inst_experiment:
                fig_name = 'plot_power_avg_{}_{}'.format(experiment_type, inst.split(':')[0])
                plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                                  instruments=[inst],
                                                  my_periods=my_periods)

                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='Power Average for {}:{}'.format(experiment_type, inst),
                                              text='')

            proc_report.write_head(n_level + 2, 'Energy Status')

            proc_report.write_text(AVAILABLE_POWER_DEF)

            metrics = get_energy_profiles_metrics(tmp_platform)
            proc_report.print_rst_table(metrics)

            metrics = get_energy_profiles_metrics(tmp_experiment)
            proc_report.print_rst_table(metrics)

            percent = {}
            for [k, val_start, val_end, val_delta] in metrics:
                if 'SEGMENT' not in k and 'otal' not in k:
                    percent[k] = float(val_delta)
                elif k.startswith('total_instruments'):
                    total_percent = float(val_delta)

            if total_percent > 0:

                for k, val in percent.items():
                    percent[k] = round(val / total_percent * 100, ndigits=2)

                fig_name = 'pie_energy_{}'.format(experiment_type)
                plots_utils.create_plot_pie(plots_dir, fig_name, percent, min_values=0.01, colors=colors)
                proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                              title='science Instrument: Energy Sharing',
                                              text='')
            else:

                logging.warning('no instrument consumption during this periods')

            proc_report.write_head(n_level + 2, 'Energy Accum')

            fig_name = 'plot_energy_accum_{}'.format(experiment_type)
            plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                              instruments=['Available_energy_accum:Wh',
                                                           'total_platform_and_science_energy_accum:Wh',
                                                           'total_available_stored_in_batt_energy_accum:Wh',
                                                           'total_available_lost_energy_accum:Wh',
                                                           'total_bat_used_energy_accum:Wh'],
                                              my_periods=my_periods, y_label='Energy (Wh)')

            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                          title='Energy Accum',
                                          text='')

            for inst in inst_experiment:

                inst_key = inst.replace(':Watts', "_energy_accum:Wh")
                fig_name = 'plot_energy_accum_{}_{}'.format(experiment_type, inst.split(':')[0])
                plots_utils.create_plot_power_avg(df_power.df, plots_dir, fig_name=fig_name,
                                                  instruments=[inst_key], y_label='Energy [Wh]',
                                                  my_periods=my_periods)

                if df_power.df[inst_key].max() > 0:

                    proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                  title='Accumulate Energy for {}:{}'.format(experiment_type,
                                                                                             inst_key),
                                                  text='')
                else:

                    proc_report.write_text('\n {} = 0 [Wh] (always empty).\n'.format(inst_key))

            if include_power_metrics_partition_details:

                if len(my_periods) == 1:
                    logging.info('There is only one period!; So need to add partition details')
                    return 0

                for k in sorted(dfs.keys()):

                    title = 'Sub-period per {} [{}]'.format(experiment_type, k)

                    proc_report.write_head(n_level + 1, title)

                    proc_report.write_head(n_level + 2, 'Power')

                    fig_name = 'plot_power_available_{}_{}'.format(experiment_type,
                                                                   k.replace(':', '').replace('_', '').replace('-', ''))

                    plots_utils.create_plot_power_avg(dfs[k].df, plots_dir, fig_name=fig_name,
                                                      instruments=['Available:Watts', 'total_instruments:Watts',
                                                                   'JUICE_platform:Watts'],
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

                    if include_plot_experiment_power:
                        for inst in inst_experiment:
                            fig_name = 'plot_power_avg_{}_{}_{}'.format(
                                experiment_type, inst, k.replace(':', '').replace('_', '').replace('-', ''))

                            plots_utils.create_plot_power_avg(dfs[k].df, plots_dir, fig_name=fig_name,
                                                              instruments=[inst],
                                                              my_periods=my_periods)

                            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                          title=f'Power Average for {experiment_type}:{inst}',
                                                          text='')

                    proc_report.write_head(n_level + 2, 'Energy Status')

                    proc_report.write_text(AVAILABLE_POWER_DEF)

                    metrics = get_energy_profiles_metrics(tmp_platform)
                    proc_report.print_rst_table(metrics)

                    metrics = get_energy_profiles_metrics(tmp_experiment)
                    proc_report.print_rst_table(metrics)

                    percent = {}
                    for val, val_start, val_end, val_delta in metrics:
                        if 'SEGMENT' not in k and 'otal' not in val:
                            percent[val] = float(val_delta)
                        elif val.startswith('total_instruments'):
                            total_percent = float(val_delta)
                    for key, val in percent.items():
                        percent[key] = round(val / total_percent * 100, ndigits=2)

                    fig_name = 'pie_energy_{}{}'.format(experiment_type,
                                                        k.replace(':', '').replace('_', '').replace('-', ''))
                    plots_utils.create_plot_pie(plots_dir, fig_name, percent, min_values=0.01, colors=colors)
                    proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                  title='science Instrument: Energy Sharing',
                                                  text='')

                    for inst in inst_experiment:

                        inst_key = inst.replace(':Watts', "_energy_accum:Wh")
                        fig_name = 'plot_energy_accum_{}_{}'.format(experiment_type, inst.split(':')[0])
                        plots_utils.create_plot_power_avg(dfs[k].df, plots_dir, fig_name=fig_name,
                                                          instruments=[inst_key], y_label='Energy [Wh]',
                                                          my_periods=my_periods)

                        if df_power.df[inst_key].max() > 0:

                            proc_report.rst_insert_figure(os.path.join('plots', fig_name + '.png'),
                                                          title=f'Accumulate Energy for {experiment_type}:{inst_key}',
                                                          text='')
                        else:

                            proc_report.write_text('\n {} = 0 [Wh] (always empty).\n'.format(inst_key))


def load_power_avg_dataframe(power_avg, eps_cfg_parameters, read_start=None, bat_capacity=None):
    """
    Get power_avg data frame

    :param power_avg: power_avg latency file path
    :param eps_cfg_parameters: dictionary including eps parameter from eps.cfg
    :param read_start: Allow to specify the first time to read
    :param bat_capacity: maximum battery capacity in Watts
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
