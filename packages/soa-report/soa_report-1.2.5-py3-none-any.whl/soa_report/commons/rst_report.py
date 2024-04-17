"""
Created on February, 2018

@author: Claudio Munoz Crego (ESAC)

This Module allows to generate an rst report
"""

import logging
import os
import sys

from esac_juice_pyutils.commons.rst_handler import RstHandler


class RstReport(RstHandler):
    """
    This class allows to generate an rst report
    """

    def __init__(self, input_path, output_path='', out=sys.stdout):
        """
        :param output_path:
        :param out:
        :param input_path: path of directory containing plots
        """

        if not os.path.exists(input_path):
            logging.error(f'input path "{input_path}" does not exist')
        else:
            self.input_path = os.path.abspath(os.path.expandvars(input_path))

        if output_path == '':
            output_path = self.input_path
            if not os.path.exists(output_path):
                logging.error('output path "{}" does not exist'.format(output_path))

        self.output_dir = output_path

        super(RstReport, self).__init__(output_path, out)

    def print_summary_intro(self, title='Title', objective_summary='', metrics=[]):
        """
        Produces summary intro

        :param title: section level
        :param objective_summary: objective summary of the section
        :param metrics: metric table (list of list)
        """

        # self.write_head_chapter(title.upper())
        self.write_head(0, title.upper())
        self.out.write('.. contents:: Table of Contents\n')
        # self.out.write('\n.. section - numbering::\n\n')

        # self.write_head_section('Introduction')
        self.insert_page_break()
        self.write_head(1, 'Introduction')
        intro = ("\n"
                 ".. |date| date::\n"
                 ".. |time| date:: %H:%M:%S\n"
                 "\n"
                 "This document was automatically generated on |date| at |time|.\n\n")

        self.out.write(intro)

        self.out.write('\n' + objective_summary + '\n')
        if len(metrics) > 0:
            # self.print_rst_metrics_summary_table([['uno', 1.00,'unit']])
            self.print_rst_table(metrics)

    def print_summary_end(self):
        """
        Produces summary end
        """

        self.out.close()

        logging.info('rst file {} generated'.format(self.rst_file_name))

    def print_summary_section(self, n_level, title, objective_summary='', metrics=[], figure=[]):
        """
        Print summary section

        :param n_level: number form 0 to 6
        :param title: section level
        :param objective_summary: objective summary of the section
        :param metrics: metric table (list of list)
        :param figure: list of figure

        """

        self.write_head(n_level, title)
        self.out.write('\n' + objective_summary + '\n\n')

        if len(metrics) > 0:
            self.print_rst_table(metrics)

        if len(figure) > 0:
            for fig in figure:
                fig = os.path.expandvars(fig)
                if not os.path.exists(fig):
                    logging.error('input path "{}" does not exist'.format(fig))
                else:
                    self.rst_insert_figure(fig, title=title, text=objective_summary)

    def print_summary_subsection(self, title, objective_summary='', metrics=[], figure=[]):
        """
        Produces summary intro

        :param title: section level
        :param objective_summary: objective summary of the section
        :param metrics: metric table (list of list)
        :param figure: list of figure
        """

        self.write_head_subsection(title)
        self.out.write('\n' + objective_summary + '\n')

        if len(metrics) > 0:
            self.print_rst_table(metrics)

        if len(figure) > 0:
            for fig in figure:
                fig = os.path.expandvars(fig)
                if not os.path.exists(fig):
                    logging.error('input path "{}" does not exist'.format(fig))
                else:
                    self.rst_insert_figure(fig, title=title, text=objective_summary)

    def print_summary_sub_subsection(self, title, objective_summary='', metrics=[], figure=[]):
        """
        print summary intro for sub section

        :param title: section level
        :param objective_summary: objective summary of the section
        :param metrics: metric table (list of list)
        :param figure: list of figure
        """

        self.write_head_subsubsection(title)
        self.out.write('\n' + objective_summary + '\n')

        if len(metrics) > 0:

            self.print_rst_csv_table(metrics, title)
            self.out.write('\n')

        if len(figure) > 0:
            for fig in figure:
                fig = os.path.expandvars(fig)
                self.rst_insert_figure(fig, title=title, text=objective_summary)

    def print_rst_table_2(self, metrics, title=True, return_line_sep='\\n'):
        """
        Generate (print) a table in rst format

        :param title: flag which specify if the table have a title line or not.
        :param metrics: list of table lines, if title=True, the title must be in metrics[0]
        :param return_line_sep: return carrier
        """

        self.out.write('\n')

        d = [0] * len(metrics[0])

        extended_metrics = []
        for line in metrics:
            nb_of_next_line = 0
            for cell in line:
                if not isinstance(cell, str):  # avoid non string casting them str
                    cell = str(cell)
                if cell.count(return_line_sep) > nb_of_next_line:
                    nb_of_next_line = cell.count(return_line_sep)

            columns = []

            n_col = len(line)

            for i in range(n_col):
                cell = line[i]
                if not isinstance(cell, str):  # avoid non string casting them str
                    cell = str(cell)

                column = [''] * (nb_of_next_line + 1)
                sub_lines = cell.split(return_line_sep)
                sub_lines = [str(ele) for ele in sub_lines]
                if len(max([str(ele) for ele in sub_lines], key=len)) > d[i]:
                    d[i] = len(max([str(ele) for ele in sub_lines], key=len))
                column[:len(sub_lines)] = sub_lines
                columns.append(column)

            rows = [list(i) for i in zip(*columns)]
            extended_metrics.append(rows)

        metrics = extended_metrics

        table_title_format = '|'
        table_line_format = '|'

        for i in range(len(metrics[0][0])):  # we use the first line of the title (Most of time there is only one)

            table_title_format += ' {' + str(i) + ':' + str(d[i]) + 's} |'
            table_line_format += ' {' + str(i) + ':' + str(d[i]) + 's} |'
        table_title_format += '\n'
        table_line_format += '\n'

        table_line = ''
        table_line_title = ''
        for i in range(len(d)):
            table_line += '+{}'.format('-' * (d[i] + 2))
            table_line_title += '+{}'.format('=' * (d[i] + 2))

        table_line += '+\n'
        table_line_title += '+\n'

        if title:
            self.out.write(table_line)

            for ele in metrics[0]:
                print(table_title_format.format(*ele))
                self.out.write(table_title_format.format(*ele))

            self.out.write(table_line_title)

            metrics.pop(0)

        else:
            self.out.write(table_line)

        for ele in metrics:
            for sub_ele in ele:
                self.out.write(table_line_format.format(*sub_ele))

            self.out.write(table_line)

        self.out.write('\n')

