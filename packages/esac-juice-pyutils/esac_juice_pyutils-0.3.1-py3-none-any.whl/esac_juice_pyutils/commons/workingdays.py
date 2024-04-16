"""
Created on Nov, 2020

@author: Claudio Munoz Crego (ESAC)

This Module allows get working days
"""

import datetime


def working_days(start, end, excluded=(6, 7)):
    """
    Get working_days between to input dates
    :param start: datetime start
    :param end: datetime end
    :param excluded: list of weekly days not working days (6: Saturday, 7: Sunday)
    :return:
    """

    days = []
    dt = datetime.timedelta(days=1)

    date_start = start.date()
    date_end = end.date()

    while date_start <= date_end:
        if date_start.isoweekday() not in excluded:
            days.append(date_start)
        date_start += dt
    return days


if __name__ == '__main__':

    date_1 = datetime.datetime(2021, 1, 21)
    date_2 = datetime.datetime(2021, 1, 30)
    my_working_days = working_days(date_1, date_2)

    print(len(my_working_days))

