# This is a sample Python script.
import os
from datetime import datetime
import calendar
from Yelp import Yelp
from travel import Travel
import event_database
import user_database

if __name__ == '__main__':
    travel = Travel("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    travel.get_map_response()
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    find = Yelp(unixtime, '9E 33rd Baltimore, Maryland')
    find.get_events()
