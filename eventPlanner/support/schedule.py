from eventPlanner.support.location import Location
from datetime import datetime
import calendar
from eventPlanner.support.Yelp import Yelp
from eventPlanner.support.travel import Travel
from eventPlanner.support.event import eventStorage

class Schedule:

    def __init__(self, filters):
        self.filters = filters #filters for events


    def create_recommendations(self):
        # creates recommendations for a block of time: Event A vs Event B vs Event C; returns top n ranks
        pass

    def create_schedule(self, event_list):
        # determines which events to go to
        # provides transportation options between events
        pass

    # Helper Functions
    def find_in_vicinity(self, area, radius, type):
        # returns lists of events of type in vicinity of area
        pass

    def compare_events_for_user(self, event1, event2, user):
        # compare 2 events based on user preferences and determine which one is better
        pass

    # Finds events with a given start time and end time that accounts for transportation
    # commute_ratio, the ratio of commute_time:time_available; eventually maybe should be function
    # start_time and end_time in unix timestamp
    def find_events(self, start_time, end_time, start_pos, commute_ratio = 0.25):
        duration = start_time - end_time
        commute_time = duration*commute_ratio

        yao = Yelp()

        event_list = Yelp.parse_events(location.state, start_time + commute_time)
        possible = []
        for event in event_list:
            travel = Travel(start_pos, event.location.display)
            travel_time = travel.get_travel_time()
            if travel_time < commute_time:
                possible.append(event)

        return possible