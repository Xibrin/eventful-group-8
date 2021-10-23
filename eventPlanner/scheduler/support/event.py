import datetime
from datetime import date
import math


def real_day(time):
    today = date.fromtimestamp(time)
    return datetime.datetime(today.year, today.month, today.day).timestamp()



class EventStorage:

    def __init__(self, name, start_time, end_time, location, category, info, price, outdoor, tickets, id, picture):
        self.name = name
        self.start_date_time = start_time
        self.start_time = start_time - self.Real_day(start_time)
        self.start_time_display = datetime.datetime.fromtimestamp(self.start_date_time)
        self.end_date_time = end_time
        self.duration = self.set_duration()
        self.end_time = end_time - self.Real_day(end_time)
        self.end_time_display = datetime.datetime.fromtimestamp(self.end_date_time)
        self.location = location
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
            self.end_date_time = self.start_time + 7200
        else:
            duration = self.end_time - self.start_time
        return duration
