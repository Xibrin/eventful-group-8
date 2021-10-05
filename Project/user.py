
class User:

    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.budget = 0 #eventually set to median disposable income of area
        self.preferred_transport = None
        self.preferred_event_type = None
        self.schedule = None

    def set_transport(self, transport_type):
        self.preferred_transport = transport_type

    def set_event(self, event_type):
        self.preferred_event_type = event_type

    def get_schedule(self, url):
        #Set up Google Calendar API Authentication and then return list of events
        return None

    def find_events(self, time_start, time_end, area, category):
        #return list of events meeting criteria
        return None