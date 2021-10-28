import datetime
from datetime import date
import math
import calendar

# returns 12am of the day of start in unix timestamp
def real_day(time):
    if time is None:
        print("ERROR")
    print(time)
    today = date.fromtimestamp(time)
    return datetime.datetime(today.year, today.month, today.day).timestamp()



class EventStorage:

    # start_time parameter is unix time stamp for start time
    # start date time is the day in unix time stamp at 12 am + number of seconds from 12 am
    # start time instance variable is the number of seconds from 12am
    def __init__(self, name, start_time, end_time, location, category, info, price, outdoor, tickets, id, picture):
        self.name = name

        if start_time is None:
            d = datetime.utcnow()
            curr_time = calendar.timegm(d.utctimetuple())
            self.start_date_time = curr_time

        else:
            self.start_date_time = start_time

        self.start_time = self.start_date_time - real_day(self.start_date_time)
        self.start_time_display = datetime.datetime.fromtimestamp(self.start_date_time)

        if end_time is None:
            self.end_date_time = self.start_date_time + 86399
        else:
            self.end_date_time = end_time

        self.end_time = self.end_date_time - real_day(self.end_date_time)
        self.duration = self.set_duration()
        self.end_time_display = datetime.datetime.fromtimestamp(self.end_date_time)

        self.location = location
        if self.location is None:
            print("NO LOCATION")
        self.category = category
        self.info = info
        self.price = price
        self.outdoor = outdoor
        self.tickets = tickets
        self.id = id
        self.picture = picture

    def print_name(self):
        return self.name

    def __str__(self):
        return self.name

    def set_duration(self):
        if self.end_date_time is None:
            duration = 7200  # manually set as 2 hours for events with no end time,  may need future adjustment
            self.end_date_time = self.start_date_time + 7200
        else:
            duration = self.end_time - self.start_time
        return duration
