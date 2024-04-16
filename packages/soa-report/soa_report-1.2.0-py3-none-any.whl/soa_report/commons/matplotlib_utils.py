"""
Created on November 2017

@author: Claudio Munoz Crego (ESAC)

This file is a container including common maplotlib utils
"""

import os
import logging
import datetime

from matplotlib import dates, ticker


def set_plot_options(plt, output_path, fig_name='fig', option='png'):
    """
    set plot options

    :param output_path: path of the output directory for plots
    :param plt: matplotlib object
    :param option: plot option; plot display the plot.
    :param fig_name: Name of the graph and corresponding image.
    """

    if option == 'plot':
        plt.show()
    elif option in ['pdf', 'jpg', 'png', 'eps']:
        plt.savefig(os.path.join(output_path, fig_name + '.' + option))
        logging.info('file {} created'.format(os.path.join(output_path, fig_name + '.' + option)))
    elif option == 'svg':
        plt.savefig(os.path.join(output_path, fig_name + '.svg'))
        logging.info('file {} created'.format(os.path.join(output_path, fig_name + '.svg')))
    else:
        logging.warning(
            'file {0}.{1} not created; format .{1} unknown'.format(os.path.join(output_path, fig_name), option))


def add_ax2_timedelta(plt, ax2):
    """
    Add a second x axis labeled with deltatime

    :param plt: matplotlib plot
    :param ax2: matplotlib x axis 2
    """

    formatter_timedelta = ticker.FuncFormatter(tick_seconds_2_str_timedelta)
    ax2.xaxis.set_major_formatter(formatter_timedelta)
    labels = ax2.get_xticklabels()
    plt.setp(labels, rotation=25, fontsize=9)


def add_ax1_datetime_ax2_timedelta(plt, ax1, dt_format='%Y-%m-%d\n%H:%M:%S',
                                   ax_start_limit='', ax_end_limit=''):
    """
    Add two x axis for date & time
    - ax1 labeled with UTC time as per format
    - ax2 labeled with time delta

    :param ax_end_limit: final date time for ax1 and ax2
    :param ax_start_limit: start date time for ax1 and ax2
    :param dt_format: ax1 utc format
    :param plt: matplotlib plot
    :param ax1: matplotlib x axis 1
    """

    add_ax1_datetime(plt, ax1, dt_format=dt_format)
    ax2 = ax1.twiny()
    add_ax2_timedelta(plt, ax2)

    if ax_start_limit != ax_end_limit:
        ax1.set_xlim(ax_start_limit, ax_end_limit)
        timedelta_max = (ax_end_limit - ax_start_limit).total_seconds()
        ax2.set_xlim(0, timedelta_max)

    return ax2


def add_unified_legend_box(ax1, ax2=None, shrink_perc=15):
    """
    Add a legend box to the top right.
    In case there are 2 x-axis unify the box

    :param ax1: matplotlib x axis 1
    :param ax2: matplotlib x axis 2
    :param shrink_perc: use to shrink the graph to a given % (to include legend box)
    :return:
    """

    # Shrink current axis by 20%
    shrink = 1.00 - shrink_perc/100.
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * shrink, box.height])
    if ax2:
        ax2.set_position([box.x0, box.y0, box.width * shrink, box.height])

    ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


def tick_seconds_2_str_timedelta(t):
    """
    Convert list of seconds to list of string 010_00:00:00 representing relative delta time.
    this method is required to include this string relative time in matplotlib graphs
    :param t: list of relative time in seconds
    :return: list of string
    """
    d = datetime.timedelta(seconds=t)
    h = d.seconds/3600
    m = int(d.seconds - h*3600)/60
    s = int(d.seconds - h*3600 - m*60)
    return '%03d_%02d:%02d:%02d' %(d.days, h, m, s)


def add_ax1_datetime(plt, ax1, dt_format='%Y-%m-%d\n%H:%M:%S'):
    """
    Add datetime label in ax1 axis

    :param plt: matplotlib plot
    :param ax1: matplotlib x axis 1
    :param dt_format: ax1 utc format
    """

    hfmt = dates.DateFormatter(dt_format)

    ax1.xaxis.set_major_formatter(hfmt)
    labels = ax1.get_xticklabels()
    plt.setp(labels, rotation=25, fontsize=9)