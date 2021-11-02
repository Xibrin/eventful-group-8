from ..support import yelp
#from ..support import ticketmaster


# def comparator():
#    def lessThan(event1, event2):
#        if event1.end_time < event2.end_time:
#           return -1
#        elif event2.end_time < event1.end_time:
#            return 1
#        else:
#            return 0
#
#    return lessThan

def lessThan(event1, event2):
    if event1.end_time < event2.end_time:
        return -1
    elif event2.end_time < event1.end_time:
        return 1
    else:
        return 0



class EventFinder:


    def __init__(self, location, start_time):
        self.location = location
        self.start_time = start_time

    def get_yelp_events(self):
        yelp_access_object = yelp.Yelp()
        event_list = yelp_access_object.parse_events(self.location, self.start_time)
        event_list.sort(key=lessThan)
        return event_list

    def get_ticketmaster_events(self):
        # TODO: Add ticketmaster implementation
        return None

    def save_all_events(self):
        event_list = self.get_yelp_events()
        # TODO: Append events from ticketmaster here
        # TODO: Check to see if ticketmaster events already exist in event_list
        for event in event_list:
            event.save()

