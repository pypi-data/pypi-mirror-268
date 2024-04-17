"""
Created on March, 2019

@author: Claudio Munoz Crego (ESAC)

This Module allows to report soa_report subsection including plots
"""

import logging

import numpy as np

from soa_report.juice.eps_data.df_power_avg import DfPowerAverage


def add_power_status_summary(n_level, proc_report, df_power, start, end):
    """
    Add power per experiment subsection in the report

    :param n_level: Report header level
    :param proc_report: report object
    :param df_power: df power dataframe
    """

    if df_power.df is None:

        logging.info('There is no power_avg; file empty')

    else:

        proc_report.print_summary_section(n_level, 'Power Status')

        title = 'Power Average'
        logging.debug(title)

        bat_percent = [label for label in df_power.df.keys() if '%' in label]
        inst_platform = \
            ['Available:Watts', 'Available_power_for_science:Watts', 'Batt. DoD:Watts',  'Batt.:Watts',
             'XB_LINK:Watts', 'KAB_LINK:Watts', 'Navigation:Watts', 'SSMM:Watts', 'PLATFORM:Watts',
             'Batt_discharges:Watts']
        no_intruments = bat_percent + inst_platform
        inst_experiment = [label for label in df_power.df.keys() if label not in no_intruments and "Watts" in label]
        inst_platform = [label for label in inst_platform if label in df_power.df.keys()]

        # Platform metrics
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


def calculate_power_status(df, inst_filter=[]):
    """
    Generate a dictionary including the power status

    :param inst_filter:
    :param df:
    :param filter: this list allow to filter a subset of instrument; by default all instrument.
    :return:
    """

    n = len(df['datetime (UTC)'])

    duration = []
    for i in range(n-1):

        duration.append((df['datetime (UTC)'][i+1] - df['datetime (UTC)'][i]).total_seconds())

    if len(inst_filter) == 0:
        inst_filter = [k for k in df.keys() if ':' in k]  # to avoid datetime column

    dic_summary = {}
    for param in inst_filter:

        val_start = df[param].iloc[0]
        val_end = df[param].iloc[-1]
        val_max = df[param].max()
        val_min = df[param].min()
        val_mean = df[param].mean()

        dt = np.array(duration)
        power = np.array(df[param])

        val_energy = 0
        for i in range(n-1):
            val_energy += power[i] * dt[i]/3600  # * 1h

        experiment, unit = param.split(':')

        dic_summary[param.replace(':Watts', '')] = \
            [val_start, val_end, val_max, val_min, val_mean, val_energy]

    return dic_summary


def calculate_energy_status(df, inst_filter=[]):
    """
    Generate a dictionary including the energy status

    :param filter: this list allow to filter a subset of instrument; by default all instrument.
    :return:
    """

    n = len(df['datetime (UTC)'])

    duration = []
    for i in range(n-1):

        duration.append((df['datetime (UTC)'][i+1] - df['datetime (UTC)'][i]).total_seconds())

    if len(inst_filter) == 0:
        inst_filter = [k for k in df.keys() if ':' in k]  # to avoid datetime column

    dic_summary = {}
    for param in inst_filter:

        dt = np.array(duration)
        power = np.array(df[param])

        val_energy = []
        energy = 0
        for i in range(n-1):
            energy += power[i] * dt[i]/3600  # * 1h
            val_energy = energy

        experiment, unit = param.split(':')

        dic_summary['{} [{}]'.format(experiment, unit)] = [val_energy]

    return dic_summary


def get_extra_df(df):
    """
    Get extra dataframe

    :param df:
    :return: df
    """

    n = len(df)

    experiments = ['Available:Watts', 'Total:Watts', 'PLATFORM:Watts']

    for exp in experiments:

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

    df['total_Juice_science:Watts'] = df['Total:Watts']
    df['Available_power_for_science:Watts'] = df['Available:Watts'] - df['PLATFORM:Watts']
    df['total_used_by_science:Watts'] = df['Total:Watts'] - df['PLATFORM:Watts']
    df['Available_energy_for_science:Wh'] = df['Available_energy:Wh'] - df['PLATFORM_energy:Wh']
    df['total_used_by_science:Wh'] = df['Total_energy:Wh'] - df['PLATFORM_energy:Wh']
    df['Available_accum_energy_for_science:Wh'] = df['Available_energy_accum:Wh'] - df['PLATFORM_energy_accum:Wh']
    df['total_energy_accum_used_by_science:Wh'] = df['Total_energy_accum:Wh'] - df['PLATFORM_energy_accum:Wh']

    total_available_not_used = np.array([0.0] * n)
    total_bat_used = np.array([0.0] * n)
    for i in range(1, n):
        my_diff = df['Available:Watts'][i] - df['Total:Watts'][i]
        if my_diff >= 0:
            total_available_not_used[i] = my_diff
        else:
            total_bat_used[i] = my_diff
    df['total_Available_not_used:Watts'] = total_available_not_used
    df['total_bat_used:Watts'] = - total_bat_used

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

        (val_start, val_end, val_max, val_min, val_mean, val_energy) = tuple(df[inst])
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

        (val_start, val_end, val_max, val_min, val_mean, val_energy) = tuple(df[inst])
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

    metrics = [['Instrument', 'Energy [Wh]']]

    if len(instruments) > 0:
        keys = instruments
    else:
        keys = [k for k in df.keys() if 'SSMM' not in k]

    total_metric = None
    for inst in sorted(keys):

        (val_start, val_end, val_max, val_min, val_mean, val_energy) = tuple(df[inst])
        inst_metric = [inst, '{0:12.2f}'.format(val_energy)]
        if 'Total' not in inst:
            metrics.append(inst_metric)
        else:
            total_metric = inst_metric

    if total_metric:
        metrics.append(total_metric)

    return metrics