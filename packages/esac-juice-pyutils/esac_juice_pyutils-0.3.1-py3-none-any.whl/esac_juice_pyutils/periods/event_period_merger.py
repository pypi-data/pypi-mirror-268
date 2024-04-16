"""
Created on July 12, 2017

@author: Claudio Munoz Crego (ESAC)

Class to merge event Periods

"""

import copy


class PeriodMerger(object):
    """
    This class allows to merge event periods where periods are list of  [start_datetime, end_datetime]
    """

    def __init__(self):
        pass

    def get_event_overlap(self, events_1, events_2):
        """
        Generate list of overlap periods between event periods 1 and 2

        :param events_1: list of periods
        :param events_2: list of periods
        :return: events_overlap, list of periods
        """

        events_overlap = []
        for ev1 in events_1:
            for ev2 in events_2:
                if ev2[0] > ev1[1]:
                    break
                ev_overlap = self.get_period_overlap(ev1, ev2)
                if ev_overlap is not None:
                    events_overlap.append(ev_overlap)

        return events_overlap

    def get_event_sub(self, events_1, events_2):
        """
        Remove event periods events_2 from event periods events_1

        :param events_1: list of periods
        :param events_2: list of periods
        :return: event period events_1 - events_2
        """

        events_sub_result = []
        for ev1 in events_1:
            # print "PER [{}][{}]".format(ev1[0], ev1[1])
            (ev_s, ev_e) = (ev1[0], ev1[1])

            for ev2 in events_2:
                if ev2[0] > ev_e:
                    if ev_s != ev_e:
                        events_sub_result.append([ev_s, ev_e])
                        # print '{} - {} >>'.format(ev_s, ev_e)
                        ev_s = ev_e
                    break

                ev_overlap = self.get_period_overlap([ev_s, ev_e], ev2)
                if ev_overlap is not None:
                    # print(" ev_overlap {} - {}".format(ev_overlap[0], ev_overlap[1]))
                    if ev_overlap[0] == ev_s and ev_overlap[1] == ev_e: # event overlap exactly
                        # print '{} - {} descartar'.format(ev_s, ev_e)
                        ev_s = ev_e
                        break
                    if ev_overlap[0] > ev_s and ev_overlap[1] < ev_e:
                        events_sub_result.append([ev_s, ev_overlap[0]])
                        # print '{} - {} <>'.format(ev_s, ev_overlap[0])
                        ev_s = ev_overlap[1]
                    elif ev_overlap[0] <= ev_s and ev_overlap[1] < ev_e:
                        ev_s = ev_overlap[1]
                    elif ev_overlap[0] > ev_s and ev_overlap[1] >= ev_e:
                        events_sub_result.append([ev_s, ev_overlap[0]])
                        # print '{} - {} <<'.format(ev_s, ev_overlap[0])
                        ev_s = ev_e
                else:
                    pass

            # Add remaining events
            if ev_e > ev_s:
                events_sub_result.append([ev_s, ev_e])
                # print '{} - {} >>'.format(ev_s, ev_e)

        return events_sub_result

    def get_not_event(self, events):
        """
        list first start and last end
        :param events_1: list of periods
        :return:
        """
        not_events = []
        for i in range(len(events[:-1])):
            not_events.append([events[i][1], events[i+1][0]])

        return not_events

    def get_period_overlap(self, p1, p2):
        """
        Get periods overlaps between p1 and p1

        :param p1: list of periods
        :param p2: list of periods
        :return:
        """

        overlap_start = max(p1[0], p2[0])
        overlap_end = min(p1[1], p2[1])

        if overlap_end >= overlap_start:
            return [overlap_start, overlap_end]
        else:
            return None
