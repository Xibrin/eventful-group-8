from datetime import datetime
import calendar
from ..support.yelp import Yelp
from ..support.travel import Travel
import math
# from eventPlanner.support.Yelp import parse_events

class Schedule:

    def __init__(self, filters):
        self.filters = filters  # filters for events

    def create_recommendations(self):
        # Default implementation for when user does not set filters
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
    # Assumption: start_time and end_time are on the same day
    @staticmethod
    def find_events_today(start_time, end_time, start_pos, commute_ratio=0.25):
        duration = end_time - start_time
        commute_time = int(math.ceil(duration * commute_ratio))

        yao = Yelp()

        event_start_time = start_time + commute_time

        print(start_pos)
        print(event_start_time)
        event_list = yao.parse_events(start_pos, event_start_time)
        if event_list is None:
            return "ERROR: no events found within timeframe"
        possible = []
        for event in event_list:
            travel = Travel(start_pos, event.location.display)
            travel_time = travel.get_travel_time()
            print("Travel time: " + str(travel_time) + "for event: ")
            print(event)
            if travel_time < commute_time:
                possible.append(event)

        return possible

    @staticmethod
    def find_events_generally(start_time, end_time, start_pos, max_travel_time):
        duration = end_time - start_time
        commute_time = int(math.ceil(max_travel_time))

        yao = Yelp()

        event_start_time = start_time + commute_time

        print(start_pos)
        print(event_start_time)
        event_list = yao.parse_events(start_pos, event_start_time)
        if event_list is None:
            return "ERROR: no events found within timeframe"
        possible = []
        for event in event_list:
            if event:
                print(event)
                travel = Travel(start_pos, event.location.display)
                travel_time = travel.get_travel_time()
                print("Travel time: " + str(travel_time) + " from " + start_pos + " to" + event.location.display)
                # print("Start pos: " + start_pos)
                # print("End pos: " + event.location.display)
                if travel_time < commute_time:
                    possible.append(event)

        print("POSSIBLE: ")
        return possible

    # Function to calculate ideal commute_ratio based on duration; currently logistic though may need to be optimized
    @staticmethod
    def commute_ratio(duration, growth_rate, max_ratio):
        return max_ratio / (1 + math.exp(-growth_rate(duration - 4)))
