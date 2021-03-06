from datetime import datetime
from dateutil import parser

from ..support import schedule

class User:

    def __init__(self, name, area):
        self.name = name
        self.area = area
        # eventually set to median disposable income of area
        self.budget = 0
        self.preferred_transport = None
        self.category_preference = {'music': 0, 'visual-arts': 0, 'performing-arts': 0, 'film': 0,
                                    'lectures-books': 0, 'fashion': 0, 'food-and-drink': 0, 'festivals-fairs': 0,
                                    'charities': 0, 'sports-active-life': 0, 'nightlife': 0, 'kids-family': 0, 'other': 0}
        self.schedule = None

    def set_transport(self, transport_type):
        self.preferred_transport = transport_type

    def set_event(self, event_type):
        self.preferred_event_type = event_type

    def get_schedule(self, url):
        # Set up Google Calendar API Authentication and then return list of events
        return None

    def find_events_ratio(self, start_day, start_month, start_year, end_day, end_month, end_year, start_time, end_time, loc):
        # return list of events meeting criteria
        # d = datetime.utcnow()
        # current_time = calendar.timegm(d.utctimetuple())
        start_time = int((datetime(start_year, start_month, start_day) - datetime(1970, 1, 1)).total_seconds())
        end_time = int((datetime(end_year, end_month, end_day) - datetime(1970, 1, 1)).total_seconds())
        # print("Current time: " + str(current_time))
        print("Start time: " + str(start_time))
        scheduling_alg = schedule.Schedule(0)
        possible_events = scheduling_alg.find_events_today(start_time, end_time, loc)
        print(possible_events)
        return possible_events

    def find_events_naive(self, start_time, end_time, loc, days, hours, minutes):
        # start_day, start_month, start_year, end_day, end_month, end_year,
        # return list of events meeting criteria
        # d = datetime.utcnow()
        # current_time = calendar.timegm(d.utctimetuple())
        # start_time = int((datetime(start_year, start_month, start_day) - datetime(1970, 1, 1)).total_seconds())
        # end_time = int((datetime(end_year, end_month, end_day) - datetime(1970, 1, 1)).total_seconds())

        start = int((parser.isoparse(start_time) - datetime(1970, 1, 1)).total_seconds())
        print(start)
        end = int((parser.isoparse(end_time) - datetime(1970, 1, 1)).total_seconds())
        max_travel_time = 86400 * days + hours * 3600 + 60
        # print("Current time: " + str(current_time))
        print("Start time: " + str(start_time))
        scheduling_alg = schedule.Schedule(0)
        possible_events = scheduling_alg.find_events_generally(start, end, loc, max_travel_time)
        print(possible_events)
        return possible_events

    def setFavorites(self, category1, category2, category3):
        self.category_preference[category1] = 3
        self.category_preference[category2] = 2
        self.category_preference[category3] = 1


