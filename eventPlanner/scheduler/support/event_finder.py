import requests
import os

from ..support import yelp
from ..support import ticketmaster
from ..support import event


def comparator():
    def lessThan(event1, event2):
        if event1.end_date_time < event2.end_date_time:
            return -1
        elif event2.end_date_time < event1.end_date_time:
            return 1
        else:
            return 0

    return lessThan


class EventFinder:
    def __init__(self, location, start_time, end_time):
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def find_all_events(self):
        yao = yelp.Yelp()
        event_list = yao.parse_events(self.location, self.start_time, self.end_time)
        # append events from ticketmaster here
        sorted_event_list = sorted(event_list, key=comparator())
        return sorted_event_list
