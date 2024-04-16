"""
Created on Jun , 2019

@author: Claudio Munoz Crego (ESAC)

This file includes common maplotlib methods
"""

import os
import matplotlib.pyplot as plt

import soa_report.commons.matplotlib_utils as matplotlib_utils


def create_plot_power_avg(df, input_path, option='png',
                          fig_name='plot_power_avg', instruments=[], other_data=[],
                          y_label='Power (Watts)', my_periods=[], line_width=1,
                          plot_ax_start=None, plot_ax_end=None):
    """
    Creates a specific maplotlib graph

    :param plot_ax_end:
    :param plot_ax_start:
    :param line_width:
    :param df: dataframe including power profile
    :param y_label: label y axis
    :param my_periods: list of periods
    :param other_data: data not from EPS as for instance the power brf
    :param input_path: path of the working directory
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    :param instruments: instrument name
    """

    parameters = [k for k in df.keys() if 'time' not in k]

    if len(instruments) > 0:
        new_parameters = []
        for k in parameters:

            for inst in instruments:

                if k.startswith(inst):

                    new_parameters.append(k)

        parameters = new_parameters

    if plot_ax_start is None and plot_ax_end is None:
        (plot_ax_start, plot_ax_end) = (df['datetime (UTC)'][0], df['datetime (UTC)'].iloc[-1])

    plt.figure('fig_name', figsize=(16, 10))  # dpi=1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)
    # ax2 = matplotlib_utils.add_ax1_datetime_ax2_timedelta(
    #     plt, ax1, ax_start_limit=plot_ax_start, ax_end_limit=plot_ax_end)

    for key in parameters:
        short_key = key
        if 'Watts' in key:
            short_key = key.split(':')[0]
        if '_energy' in key:
            short_key = key.split('_energy')[0]
        if key in df.keys():
            ax1.plot(df['datetime (UTC)'], df[key], linewidth=line_width, label=short_key)
            # ax2.plot(df['timedelta (seconds)'], df[key], linewidth=line_width)

    ax1.set_ylim(bottom=0)

    include_phase_area_df(df, ax1, my_periods)
    # matplotlib_utils.add_unified_legend_box(ax1, ax2)
    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


def create_plot_bat_dod(df_power, input_path, option='png',
                        fig_name='plot_power_avg', instruments=[], other_data=[],
                        y_label='Power (Watts)', my_periods=[], line_width=1,
                        plot_ax_start=None, plot_ax_end=None):
    """
    Creates a specific maplotlib graph

    :param plot_ax_end:
    :param plot_ax_start:
    :param line_width:
    :param df: dataframe including power profile
    :param y_label: label y axis
    :param my_periods:
    :param other_data: data not from EPS as for instance the power brf
    :param input_path: path of the working directory
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    :param instruments: instrument name
    """

    df = df_power.df

    parameters = [k for k in df.keys() if 'time' not in k]

    if len(instruments) > 0:
        new_parameters = []
        for k in parameters:

            for inst in instruments:

                if k.startswith(inst):

                    new_parameters.append(k)

        parameters = new_parameters

    if plot_ax_start is None and plot_ax_end is None:
        (plot_ax_start, plot_ax_end) = (df['datetime (UTC)'][0], df['datetime (UTC)'].iloc[-1])

    plt.figure('fig_name', figsize=(14, 8))  # dpi=1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)

    # ax2 = matplotlib_utils.add_ax1_datetime_ax2_timedelta(
    #     plt, ax1, ax_start_limit=plot_ax_start, ax_end_limit=plot_ax_end)

    if hasattr(df_power, 'battery_capacity'):
        if df_power.battery_capacity is None:
            battery_capacity = 5000
        else:
            battery_capacity = df_power.battery_capacity

    for key in parameters:
        short_key = key
        if 'Watts' in key:
            short_key = key.split(':')[0]

        if key in df.keys() and ':%' not in key:
            ax1.plot(df['datetime (UTC)'], df[key], linewidth=line_width, label=short_key)
            # ax2.plot(df['timedelta (seconds)'], df[key], linewidth=line_width)

        if ':%' in key:

            if key in df.keys():

                ax1.set_ylim(0, 100)
                ax1.set_ylabel(key)
                ax1.plot(df['datetime (UTC)'], df[key], linewidth=line_width, label=key)
                t_0, t_final = df['datetime (UTC)'][0], df['datetime (UTC)'].iloc[-1]
                pos_x_anotate = t_0 + (t_final - t_0)/5
                ax1.plot([t_0, t_final], [80, 80], 'r--')
                ax1.plot([t_0, t_final], [70, 70], 'g--')
                # annotate(BATTERY_DOD_SOFT_LIMIT)
                ax1.annotate('BATTERY_CAPACITY = {} [Watts]'.format(battery_capacity),
                              xy=(t_0, 5), xytext=(pos_x_anotate, 5), color='r')
                ax1.annotate('BATTERY_DOD_HARD_LIMIT = 80%', xy=(t_0, 80), xytext=(pos_x_anotate, 81), color='r')
                ax1.annotate('BATTERY_DOD_SOFT_LIMIT = 70%', xy=(t_0, 70), xytext=(pos_x_anotate, 71), color='g')

    ax1.set_ylim(bottom=0)

    include_phase_area_df(df, ax1, my_periods)
    matplotlib_utils.add_unified_legend_box(ax1)
    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


def create_plot_bat_status(df_power, input_path, option='png',
                           fig_name='plot_power_avg', instruments=[], other_data=[],
                           y_label='Power (Watts)', my_periods=[], line_width=1,
                           plot_ax_start=None, plot_ax_end=None):
    """
    Creates a specific maplotlib graph

    :param plot_ax_end:
    :param plot_ax_start:
    :param line_width:
    :param df: dataframe including power profile
    :param y_label: label y axis
    :param my_periods:
    :param other_data: data not from EPS as for instance the power brf
    :param input_path: path of the working directory
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    :param instruments: instrument name
    """

    df = df_power.df

    parameters = [k for k in df.keys() if 'time' not in k]

    if len(instruments) > 0:
        new_parameters = []
        for k in parameters:

            for inst in instruments:

                if k.startswith(inst):

                    new_parameters.append(k)

        parameters = new_parameters

    if plot_ax_start is None and plot_ax_end is None:
        (plot_ax_start, plot_ax_end) = (df['datetime (UTC)'][0], df['datetime (UTC)'].iloc[-1])

    plt.figure('fig_name', figsize=(14, 8))  # dpi=1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)

    # ax2 = matplotlib_utils.add_ax1_datetime_ax2_timedelta(
    #     plt, ax1, ax_start_limit=plot_ax_start, ax_end_limit=plot_ax_end)

    par1 = ax1.twinx()
    if hasattr(df_power, 'battery_capacity'):
        if df_power.battery_capacity is None:
            battery_capacity = 5000
        else:
            battery_capacity = df_power.battery_capacity

        ax1.set_ylim(0, battery_capacity * 1.1)

    for key in parameters:
        short_key = key
        if 'Watts' in key:
            short_key = key.split(':')[0]
        if key in df.keys() and ':%' not in key:
            ax1.plot(df['datetime (UTC)'], df[key], linewidth=line_width, label=short_key)
            # ax2.plot(df['timedelta (seconds)'], df[key], linewidth=line_width)

        if ':%' in key:

            if key in df.keys():

                par1.set_ylim(0, 110)
                par1.set_ylabel(key)
                par1.plot(df['datetime (UTC)'], df[key], linewidth=line_width, label=key)
                t_0, t_final = df['datetime (UTC)'][0], df['datetime (UTC)'].iloc[-1]
                pos_x_anotate = t_0 + (t_final - t_0)/5
                par1.plot([t_0, t_final], [20, 20], 'r--')
                par1.plot([t_0, t_final], [30, 30], 'g--')
                par1.plot([t_0, t_final], [100, 100], 'k--')
                par1.annotate('BATTERY_CAPACITY = {} [Watts]'.format(battery_capacity),
                              xy=(t_0, 101), xytext=(pos_x_anotate, 101), color='k')
                par1.annotate('BATTERY_DOD_HARD_LIMIT = 20%', xy=(t_0, 20), xytext=(pos_x_anotate, 21), color='r')
                par1.annotate('BATTERY_DOD_SOFT_LIMIT = 30%', xy=(t_0, 30), xytext=(pos_x_anotate, 31), color='g')

    ax1.set_ylim(bottom=0)

    include_phase_area_df(df, ax1, my_periods)
    matplotlib_utils.add_unified_legend_box(par1)
    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


class MatplotlibUtils(object):
    """
    This class allow to create mission specific matplotlib elements
    """

    def create_advanced_plot_downlink_to_gs(self, input_path, parameters,
                                            my_periods=[], option='png',
                                            fig_name='fig', y_label='Gbits'):
        """
        Creates advanced plot including 2 x-axis and 1 y-axis

        :param input_path: path of the working directory
        :param parameters: list of parameters
        :param my_periods: list of periods
        :param option: plot option; plot display the plot.
        :param fig_name: Name of the graph and corresponding image.
        :param y_label: label name for y axis
        """

        df_a = self.get_data_to_plot(parameters)[0]

        (plot_ax_start, plot_ax_end) = (df_a['datetime (UTC)'][0], df_a['datetime (UTC)'].iloc[-1])

        plt.figure('fig_name', figsize=(16, 10))  # dpi=1200)

        ax1 = plt.subplot(111)
        ax1.set_ylabel(y_label)
        # ax2 = matplotlib_utils.add_ax1_datetime_ax2_timedelta(
        #     plt, ax1, ax_start_limit=plot_ax_start, ax_end_limit=plot_ax_end)

        for key in parameters:
            short_key = key
            if 'SSMM ' in key:
                short_key = key.split(':')[0].split('SSMM ')[1]
            if key in df_a.keys():
                ax1.plot(df_a['datetime (UTC)'], df_a[key], label=short_key)
                # ax2.plot(df_a['timedelta (seconds)'], df_a[key])

        ax1.set_ylim(bottom=0)

        include_phase_area_df(df_a, ax1, my_periods)
        # matplotlib_utils.add_unified_legend_box(ax1, ax2)
        matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

        plt.close()


def create_plot_latency_presentation(df_l, input_path, option='png',
                                     fig_name='plot_latency_presentation',
                                     y_label='Days', my_periods='', antenna_label='HGA'):
    """
    Creates a specific maplotlib graph

    :param df_l: input dataframe
    :param input_path: path of the working directory
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    :param y_label: y axis label
    :param my_periods: period to be plot
    :param antenna_label: label use to filter antenna values
    """

    latency_days = [k for k in df_l.keys() if antenna_label in k]  # and 'Maximum' in k]

    plt.figure('fig_name', figsize=(12, 8))  # figsize=(16, 10)) =1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)

    for key in latency_days:
        short_key = key
        if 'SSMM ' in key:
            short_key = key.split(':')[0].split('SSMM ')[1]
        if 'Maximum' in key:
            short_key = key.replace('Maximum', 'Total_Latency')
        if key in df_l.keys():
            ax1.plot(df_l['datetime (UTC)'], df_l[key], label=short_key)

    ax1.set_ylim(bottom=0)  # , top=5)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    include_phase_area_df(df_l, ax1, my_periods)

    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


def create_advanced_plot_ssmm_vs_max(df_a, input_path, option='png',
                                     fig_name='fig', y_label='Gbits', my_periods=[]):
    """
    Creates SSMM plot

    :param my_periods: list of window periods
    :param y_label: label of y axis
    :param input_path: path of the working directory
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    """

    parameters = [k for k in df_a.keys() if 'Memory' in k and 'SSMM' in k]

    dic = {}
    dic['datetime (UTC)'] = [t for t in df_a['datetime (UTC)']]
    dic['SSMM:Memory'] = [t for t in df_a['SSMM:Memory']]

    (plot_ax_start, plot_ax_end) = (df_a['datetime (UTC)'][0], df_a['datetime (UTC)'].iloc[-1])

    plt.figure('fig_name', figsize=(16, 10))  # figsize=(16, 10)) =1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)

    for key in parameters:
        short_key = key
        if 'SSMM ' in key:
            short_key = key.split(':')[0].split('SSMM ')[1]
        if key in df_a.keys():
            ax1.plot(df_a['datetime (UTC)'], df_a[key], label=short_key)

    ax1.set_ylim(bottom=0)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    include_phase_area_df(df_a, ax1, my_periods)

    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


def create_advanced_plot_1ax_2ay(df_a, input_path, parameters, option='png',
                                 fig_name='fig', y_label='Latency (days)', my_periods=[], line_width=1):
    """
    Creates advanced plot including 2 x-axis and 2 y-axis

    :param input_path: path of the working directory
    :param parameters: list of experiments
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    :param y_label: y axis label of plots
    :param my_periods: list of window periods
    :param line_width: line width of plots.
    """

    (plot_ax_start, plot_ax_end) = (df_a['datetime (UTC)'][0], df_a['datetime (UTC)'].iloc[-1])

    plt.figure('fig_name', figsize=(16, 10))  # dpi=1200)

    ax1 = plt.subplot(111)
    ax1.set_ylabel(y_label)

    for key in parameters:
        short_key = key
        if 'SSMM ' in key:
            short_key = key.split(':')[0].split('SSMM ')[1]
        if key in df_a.keys():
            ax1.plot(df_a['datetime (UTC)'], df_a[key], linewidth=line_width, label=short_key)

    ax1.set_ylim(bottom=0)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    include_phase_area_df(df_a, ax1, my_periods)

    matplotlib_utils.set_plot_options(plt, input_path, fig_name=fig_name, option=option)

    plt.close()


def create_plot_pie(plots_path, title, percent, min_values=0, colors=None):
    """
    Create pie plot

    :param min_values: the min value to plot, i.e. 0.01 %; mainly remove too small values
    :param plots_path: path od plot directory
    :param title: plot title
    :param percent: plot percentage table
    :param colors: plot colours table
    """

    import matplotlib.pyplot as plt

    percent_keys = list(percent.keys())
    for k in reversed(percent_keys):
        if percent[k] < min_values:
            del percent[k]

    labels = sorted(percent.keys())
    sizes = [percent[k] for k in labels]
    labels = ['{} [{}%]'.format(k, percent[k]) for k in labels]
    if colors:
        pie_colors = [colors[k.split()[0]] for k in labels]

    explode = [i % 2 * 0.1 for i, x in enumerate(percent.keys())]

    if colors:
        pies = plt.pie(sizes, startangle=90, autopct='%1.0f%%', pctdistance=0.9, radius=1.2,
                       explode=explode, colors=pie_colors)
    else:
        pies = plt.pie(sizes, startangle=90, autopct='%1.0f%%', pctdistance=0.9, radius=1.2,
                       explode=explode)

    plt.legend(pies[0], labels, bbox_to_anchor=(1, 0.5), loc="center right", fontsize=8,
               bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.50)

    plt.axis('equal')
    plot_file_path = os.path.join(plots_path, title + '.png')
    plt.savefig(plot_file_path)
    plt.close()

    return plot_file_path


def create_plot_donut(plots_path, title, percent, min_values=0, colors=None):
    """
    Create donut plot

    :param min_values: the min value to plot, i.e. 0.01 %; mainly remove too small values
    :param plots_path:
    :param title:
    :param percent:
    :return:
    """

    import matplotlib.pyplot as plt

    percent_keys = list(percent.keys())
    for k in reversed(percent_keys):
        if percent[k] < min_values:
            del percent[k]

    labels = sorted(percent.keys())
    sizes = [percent[k] for k in labels]
    labels = ['{} [{}%]'.format(k, percent[k]) for k in labels]
    labels_short = [k.split()[0] for k in labels]
    if colors:
        pie_colors = [colors[k] for k in labels_short]

    if colors:
        pies = plt.pie(sizes, startangle=90, autopct='%1.1f%%', radius=1., labels=labels_short,
                       colors=pie_colors)
    else:
        pies = plt.pie(sizes, startangle=90, autopct='%1.1f%%', radius=1., labels=labels_short)

    plt.legend(pies[0], labels, bbox_to_anchor=(1, 0.5), loc="center right", fontsize=8,
               bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.50)

    centre_circle = plt.Circle((0, 0), 0.80, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()

    plt.axis('equal')
    plot_file_path = os.path.join(plots_path, title + '.png')
    plt.savefig(plot_file_path)
    plt.close()

    return plot_file_path


def include_phase_area_df(df_a, ax, my_periods):
    """
    Set background colors:
    - Default is green
    - Aphelion rose
    - Perihelion orange
    :param ax: matplotlib x axis
    :param df_a: dataframe
    :param my_periods: list of datetime period
    :return:
    """

    # Default background color
    ax.patch.set_facecolor('mintcream')  # ('aliceblue') # ('palegreen') mistyrose

    if not df_a.empty:
        for i in range(len(my_periods)):
            if i % 2 == 0:
                ax.fill_between([my_periods[i][0], my_periods[i][1]], 0,
                                [ax.get_ylim()[1], ax.get_ylim()[1]], facecolor='navajowhite', interpolate=True)
