from ..support import yelp
#from ..support import ticketmaster
from functools import cmp_to_key

def comparator():
   def lessThan(event1, event2):
       if event1.end_time < event2.end_time:
          return -1
       elif event2.end_time < event1.end_time:
           return 1
       else:
           return 0

   return lessThan


def less_than(event1, event2):
    print("Hi")
    if event1.end_time < event2.end_time:
        return -1
    elif event2.end_time < event1.end_time:
        return 1
    else:
        return 0

def make_comparator(less_than):
    def comp(event1, event2):
        return less_than(event1, event2)
    return comp


class EventFinder:


    def __init__(self, location, start_time):
        self.location = location
        self.start_time = start_time

    def get_yelp_events(self):
        yelp_access_object = yelp.Yelp()
        event_list = yelp_access_object.parse_events(self.location, self.start_time)
        to_ret = sorted(event_list, key=cmp_to_key(less_than))
        return to_ret

    def get_ticketmaster_events(self):
        # TODO: Add ticketmaster implementation
        return None

    def save_all_events(self):
        event_list = self.get_yelp_events()
        # TODO: Append events from ticketmaster here
        # TODO: Check to see if ticketmaster events already exist in event_list
        for event in event_list:
            event.save()

