from ..support import yelp
from ..support import ticketmaster
import datetime
#from ..support import ticketmaster


def comparator():
   def lessThan(event1, event2):
       if event1.end_time < event2.end_time:
          return -1
       elif event2.end_time < event1.end_time:
           return 1
       else:
           return 0

   return lessThan




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

        return event_list

    def get_ticketmaster_events(self):
        ticketmaster_access_object = ticketmaster.TicketMaster()
        ticketmaster_event_list = ticketmaster_access_object.get_events_date(self.location, self.start_time)

        return ticketmaster_event_list

    def save_all_events(self):
        event_list = self.get_yelp_events()
        ticketmaster_event_list = self.get_ticketmaster_events()
        for event in ticketmaster_event_list:
            event_list.append(event)
        for event in event_list:
            event.save()