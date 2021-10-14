
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

