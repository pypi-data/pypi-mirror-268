"""
Created on March 2019

@author: Claudio Munoz Crego (ESAC)

This Module allows to report soa_report subsection including plots
"""

import logging
import numpy as np


def add_power_status_summary(n_level, proc_report, df_power, available_power_def):
    """
    Add power per experiment subsection in the report

    :param n_level: Report header level
    :param proc_report: report object
    :param df_power: df power dataframe
    :param available_power_def: Power available definition
    """

    if df_power.df is None:

        logging.info('There is no power_avg; file empty')

    else:

        proc_report.print_summary_section(n_level, 'Power Status')

        title = 'Power Average'
        logging.debug(title)

        bat_percent = [label for label in df_power.df.keys() if '%' in label]
        inst_platform = \
            ['Available:Watts', 'Available_power_for_science:Watts', 'Batt. DoD:Watts', 'Batt.:Watts',
             'XB_LINK:Watts', 'KAB_LINK:Watts', 'NAVCAM:Watts', 'RADEM:Watts', 'SSMM:Watts', 'JUICE:Watts',
             'Batt_discharges:Watts']
        no_intruments = bat_percent + inst_platform
        inst_experiment = [label for label in df_power.df.keys() if label not in no_intruments and "Watts" in label]
        inst_platform = [label for label in inst_platform if label in df_power.df.keys()]

        # Platform metrics
        # df_power_total = df_power # DfPowerAverage(my_df_power.df, start, end)
        tmp_platform = calculate_power_status(df_power.df, inst_filter=inst_platform)
        tmp_experiment = calculate_power_status(df_power.df, inst_filter=inst_experiment)
        tmp_bat_per = calculate_power_status(df_power.df, inst_filter=bat_percent)

        proc_report.print_rst_table(get_power_profiles_metrics(tmp_platform))
        proc_report.print_rst_table(get_power_profiles_metrics(tmp_experiment))
        proc_report.print_rst_table(get_power_profiles_metrics_percent(tmp_bat_per))

        proc_report.print_summary_section(n_level, 'Energy Status')

        proc_report.write_text(available_power_def)

        metrics = get_energy_profiles_metrics(tmp_platform)
        proc_report.print_rst_table(metrics)

        metrics = get_energy_profiles_metrics(tmp_experiment)
        proc_report.print_rst_table(metrics)


def calculate_power_status(df, inst_filter=[]):
    """
    Generate a dictionary including the power status

    :param df: dataframe
    :param inst_filter: this list allow to filter a subset of instrument; by default all instrument.
    :return: dic_summary: power metrics
    """

    if len(inst_filter) == 0:
        inst_filter = [k for k in df.keys() if ':' in k]  # to avoid datetime column

    dic_summary = {}
    for param in inst_filter:
        val_start = df[param].iloc[0]
        val_end = df[param].iloc[-1]
        val_max = df[param].max()
        val_min = df[param].min()
        val_mean = df[param].mean()

        val_energy_start = df[param.replace(':Watts', '_energy_accum:Wh')].iloc[0]
        val_energy_end = df[param.replace(':Watts', '_energy_accum:Wh')].iloc[-1]
        delta_energy = val_energy_end - val_energy_start

        dic_summary[param.replace(':Watts', '')] = \
            [val_start, val_end, val_max, val_min, val_mean, val_energy_start, val_energy_end, delta_energy]

    return dic_summary


def get_extra_df(df, battery_capacity, batt_percent):
    """
    Get extra dataframe

    Note: JUICE:Watts means Juice_platform power consumption in Watts

    :param df:
    :param battery_capacity:
    :param batt_percent:
    :return:
    """

    n = len(df)

    df_total_platform_and_science_watts = df['Total:Watts']
    df = df.drop(columns=['Total:Watts'])

    experiments = [k for k in df.keys() if k.endswith(':Watts')]

    df['JUICE:Watts'] = df['JUICE:Watts'] + df['NAVCAM:Watts'] + df['RADEM:Watts']

    total_available_not_used = np.array([0.0] * n)
    total_available_not_used_stored_in_batt = np.array([0.0] * n)
    total_available_lost = np.array([0.0] * n)

    total_bat_used = np.array([0.0] * n)
    for i in range(1, n):
        my_diff = df['Available:Watts'][i] - df_total_platform_and_science_watts[i]
        if my_diff >= 0:
            total_available_not_used[i] = my_diff
            batt_stat_i_to_charge = battery_capacity - (batt_percent[i] * battery_capacity / 100)
            if batt_percent[i] < 100:
                if my_diff <= batt_stat_i_to_charge:
                    total_available_not_used_stored_in_batt[i] = my_diff
                else:
                    total_available_not_used_stored_in_batt[i] = batt_stat_i_to_charge
                    total_available_lost[i] = my_diff - batt_stat_i_to_charge
            else:
                total_available_lost[i] = my_diff
        else:
            total_bat_used[i] = my_diff

    df['total_bat_used:Watts'] = - total_bat_used
    df['total_available_stored_in_batt:Watts'] = total_available_not_used_stored_in_batt
    df['total_available_lost:Watts'] = total_available_lost
    df['total_instruments:Watts'] = df_total_platform_and_science_watts - df['JUICE:Watts']

    for exp in experiments + [
                              'total_bat_used:Watts',
                              'total_instruments:Watts',
                              'total_available_stored_in_batt:Watts',
                              'total_available_lost:Watts']:

        power = df[exp]
        energy = np.array([0.0] * n)
        energy_sum = 0
        energy_accum = np.array([0.0] * n)

        for i in range(1, n):
            dt = (df['datetime (UTC)'][i] - df['datetime (UTC)'][i - 1]).total_seconds()
            energy[i] = power[i] * dt / 3600.0  # * 1h
            energy_sum += energy[i]
            energy_accum[i] = energy_sum

        exp_energy = exp.split(':')[0] + '_energy:Wh'
        exp_energy_accum = exp.split(':')[0] + '_energy_accum:Wh'
        df[exp_energy] = energy
        df[exp_energy_accum] = energy_accum

    return df


def get_power_profiles_metrics(df, instruments=[]):
    """
    Return  power profile metrics

    :param instruments:
    :param df:
    :return: Return a dictionary including power max/min/mean per instrument
    """

    metrics = [['Instrument', 'start [W]', 'end [W]', 'Mean [W]', 'Max [W]', 'Min [W]']]

    if len(instruments) > 0:
        keys = instruments
    else:
        keys = [k for k in df.keys() if 'SSMM' not in k]

    total_metric = None
    for inst in sorted(keys):

        (val_start, val_end, val_max, val_min, val_mean, energy_start, energy_end, delta_energy) = tuple(df[inst])
        inst_metric = [inst, '{0:12.2f}'.format(val_start), '{0:12.2f}'.format(val_end), '{0:12.2f}'.format(val_mean),
                       '{0:12.2f}'.format(val_max), '{0:12.2f}'.format(val_min)]
        if 'Total' not in inst:
            metrics.append(inst_metric)
        else:
            total_metric = inst_metric

    if total_metric:
        metrics.append(total_metric)

    return metrics


def get_power_profiles_metrics_percent(df, instruments=[]):
    """
    Return  power profile metrics

    :param instruments:
    :param df:
    :return: Return a dictionary including power max/min/mean per instrument
    """

    metrics = [['Instrument', 'start', 'end', 'Mean', 'Max', 'Min']]

    if len(instruments) > 0:
        keys = instruments
    else:
        keys = [k for k in df.keys() if 'SSMM' not in k]

    total_metric = None
    for inst in sorted(keys):

        (val_start, val_end, val_max, val_min, val_mean, energy_start, energy_end, delta_energy) = tuple(df[inst])
        inst_metric = [inst, '{0:12.2f}'.format(val_start), '{0:12.2f}'.format(val_end), '{0:12.2f}'.format(val_mean),
                       '{0:12.2f}'.format(val_max), '{0:12.2f}'.format(val_min)]
        if 'Total' not in inst:
            metrics.append(inst_metric)
        else:
            total_metric = inst_metric

    if total_metric:
        metrics.append(total_metric)

    return metrics


def get_energy_profiles_metrics(df, instruments=[]):
    """
    Return  power profile metrics

    :param instruments:
    :param df:
    :return: Return a dictionary including power max/min/mean per instrument
    """

    metrics = [['Instrument', 'Energy Start [Wh]', 'Energy End [Wh]', 'Delta Energy [Wh]']]

    if len(instruments) > 0:
        keys = instruments
    else:
        keys = [k for k in df.keys() if 'SSMM' not in k]

    total_metric = None
    for inst in sorted(keys):

        (val_start, val_end, val_max, val_min, val_mean, energy_start, energy_end, delta_energy) = tuple(df[inst])
        inst_metric = [inst,
                       '{0:12.2f}'.format(energy_start),
                       '{0:12.2f}'.format(energy_end),
                       '{0:12.2f}'.format(delta_energy)]
        if 'Total' not in inst:
            metrics.append(inst_metric)
        else:
            total_metric = inst_metric

    if total_metric:
        metrics.append(total_metric)

    return metrics
