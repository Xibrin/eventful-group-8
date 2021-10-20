import requests
import os
from decouple import config

class EventFinder:

    def __init__(self, date, city):
        self.date = date
        self.city = city

    def get_events_date(self):
        base_url = "https://app.ticketmaster.com/discovery/v2/events.json?&apikey="
        key = config("TICKETMASTER_API_KEY")
        added_url = "&locale=*&startDateTime=" + self.date + "T02:00:00Z&endDateTime=2021-10-31T02:00:00Z&city=" + self.city
        response = requests.get(base_url + key + added_url)
        print(response.json())
        return response
