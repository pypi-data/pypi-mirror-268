"""
Created on April, 2021

@author: Claudio Munoz Crego

Python module including Spice kernel utils
"""


import logging

import spiceypy as spi


def print_kernel_info():
    """
    Include the list of kernel loaded

    """
    kernel_info = get_kernel_loaded_info()
    for ele in kernel_info[1:]:
        logging.debug('\t{:^6}:{}'.format(ele[1], ele[0]))


def get_kernel_loaded_info():
    """
    Returns the current list of kernel loaded in spice

    """
    kernel_info = []
    kcount = spi.ktotal('All')
    kernel_info.append(kcount)
    for i in range(kcount):
        kernel_info.append(spi.kdata(i, 'All', 256, 256, 256))

    return kernel_info