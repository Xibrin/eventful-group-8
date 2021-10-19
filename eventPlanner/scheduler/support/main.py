# This is a sample Python script.
import os
from datetime import datetime
import calendar
from yelp import Yelp
from event_finder import EventFinder
from travel import Travel
import event_database
import user_database
from eventPlanner.support.schedule import Schedule
from datetime import timezone
from eventPlanner.support.user import User

if __name__ == '__main__':
    # travel = Travel("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    # travel.get_map_response()
    d = datetime.utcnow()
    current_time = calendar.timegm(d.utctimetuple())
    start_time = int((datetime(2021, 10, 17) - datetime(1970,1,1)).total_seconds())
    end_time = int((datetime(2022, 1, 1) - datetime(1970,1,1)).total_seconds())
    # find = Yelp(unixtime, '9E 33rd Baltimore, Maryland')
    # print(unixtime)
    print("Current time: " + str(current_time))
    print("Start time: " + str(start_time))
    tester = User(None, None)
    tester.find_events_naive(19, 10, 2021, 1, 12, 2022, 0, 0, "9E 33rd Baltimore, Maryland", 0, 1, 0)
    scheduling_alg = Schedule(0)
    # possible_events = scheduling_alg.find_events(start_time, end_time, '9E 33rd Baltimore, Maryland')
    # print(possible_events)
    # find = Yelp()
    # find.get_events()

    # find.parse_events('9E 33rd Baltimore, Maryland', current_time)
