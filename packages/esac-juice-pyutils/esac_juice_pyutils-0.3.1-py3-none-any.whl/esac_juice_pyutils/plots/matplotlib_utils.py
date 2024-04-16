"""
Created on November, 2017

@author: Claudio Munoz Crego (ESAC)

This file includes common maplotlib utils
"""

import os
import logging
import datetime

from matplotlib import dates, ticker


class MyUtilsMatplotlib(object):

    def __init__(self):

        self.formatter_timedelta = ticker.FuncFormatter(self.tick_seconds_2_str_timedelta)

    def tick_seconds_2_str_timedelta(self, t, pos):
        """
        Convert list of seconds to list of string 010_00:00:00 representing relative delta time.
        this method is required to include this string relative time in matplotlib graphs
        :param t: list of relative time in seconds
        :param pos: position within maplotlib axis
        :return: list of string
        """
        d = datetime.timedelta(seconds=t)
        h = d.seconds/3600
        m = int(d.seconds - h*3600)/60
        s = int(d.seconds - h*3600 - m*60)
        return '%03d_%02d:%02d:%02d' %(d.days, h, m, s)

    def set_plot_options(self, plt, output_path, fig_name='fig', option='png'):
        """
        set plot options

        :param input_path: path of the working directory
        :param plot: matplotlib object
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

    def add_unified_legend_box(self, ax1, ax2=None, shrink_perc=15):
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

    def add_ax1_datetime_ax2_timedelta(self, plt, ax1, dt_format='%Y-%m-%d\n%H:%M:%S',
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

        self.add_ax1_datetime(plt, ax1, dt_format=dt_format)
        ax2 = ax1.twiny()
        self.add_ax2_timedelta(plt, ax2)

        if ax_start_limit != ax_end_limit:
            ax1.set_xlim(ax_start_limit, ax_end_limit)  # ax1.get_xlim()[1])
            timedelta_max = (ax_end_limit - ax_start_limit).total_seconds()
            ax2.set_xlim(0, timedelta_max)  # ax2.get_xlim()[1])

        return ax2

    def add_ax2_timedelta(self, plt, ax2):
        """
        Add a second x axis labeled with deltatime

        :param plt: matplotlib plot
        :param ax2: matplotlib x axis 2
        """

        ax2.xaxis.set_major_formatter(self.formatter_timedelta)
        labels = ax2.get_xticklabels()
        plt.setp(labels, rotation=25, fontsize=9)

    def add_ax1_datetime(self, plt, ax1, dt_format='%Y-%m-%d\n%H:%M:%S'):
        """
        Add datetime label in ax1 axis

        :param plt: matplotlib plot
        :param ax2: matplotlib x axis 2
        :param dt_format: ax1 utc format
        """

        hfmt = dates.DateFormatter(dt_format)

        ax1.xaxis.set_major_formatter(hfmt)
        labels = ax1.get_xticklabels()
        plt.setp(labels, rotation=25, fontsize=9)

    # def plot_gantt(self, y_labels, event, title='my_gantt'):
    #     """
    #     plot gantt
    #     :param labels:
    #     :param event:
    #     :return:
    #     """
    #     import matplotlib.pyplot as plt
    #     import matplotlib.font_manager as font_manager
    #     import matplotlib.dates
    #     from matplotlib.dates import MONTHLY, DateFormatter, rrulewrapper, RRuleLocator
    #
    #     #y_labels = labels
    #     x_dates = event
    #
    #     pos = []
    #     for i in range(len(y_labels)):
    #         pos.append(0.5 +i)
    #
    #     plt.figure(title)
    #     plt.title(title)
    #     ax = plt.subplot(111)
    #
    #     # Format the y-axis separation
    #     plt.yticks(pos, y_labels)
    #
    #     # Tell matplotlib that these are dates... and set format
    #     ax.xaxis_date()  # Tell matplotlib that these are dates...
    #     rule = rrulewrapper(MONTHLY, interval=1)
    #     loc = RRuleLocator(rule)
    #     formatter = DateFormatter('%y-%m-%dT:%H:%M:%S')
    #     # ax.xaxis.set_major_locator(loc)
    #     ax.xaxis.set_major_formatter(formatter)
    #     labelsx = ax.get_xticklabels()
    #     plt.setp(labelsx, rotation=30, fontsize=12)
    #
    #     for k in range(len(y_labels)):
    #         y_pos = pos[k]
    #         for wocc in event[y_labels[k]]:
    #             # print 'wocc', y_labels[k], wocc
    #             start_date = matplotlib.dates.date2num(wocc[0])
    #             end_date = matplotlib.dates.date2num(wocc[1])
    #
    #             ax.barh(y_pos, end_date - start_date, left=start_date, height=0.1, align='center', alpha=0.75)
    #
    #     return plt
