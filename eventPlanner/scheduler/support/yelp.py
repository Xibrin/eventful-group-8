import requests
import json
import requests
import json
import os
import re
from datetime import datetime

from ..support.event import eventStorage
from ..support.location import Location
from dateutil import parser


class Yelp:

    def __init__(self):
        pass
        # self.start_time = start_time
        # self.location = location

    def parse_events(self, location, start_time):
        print("\nstarting YELP_API\n")
        # headers = {'Authorization': 'Bearer %s' % os.getenv("YELP_API_KEY")}
        key = ""  # TODO: INSERT YELP API KEY HERE
        headers = {'Authorization': 'Bearer %s' % key}
        limit = 50
        url = 'https://api.yelp.com/v3/events'
        event_list = []
        for i in range(1):
            params = {'location': location, 'limit': limit, 'offset': i * 50, 'start_date': start_time}
            # Making a get request to the API
            req = requests.get(url, params=params, headers=headers)
            # Split request by event (separated by curly braces)
            if req.status_code != 200:
                print("STATUS CODE: " + str(req.status_code))
                return None
            data = req.json()

            # print(data['total'])
            for val in data['events']:
                # print(val)
                event_list.append(Yelp.parse_one_event(val))

        return event_list

    @staticmethod
    def parse_one_event(val):
        name = val['name']
        start_time = val['time_start']
        end_time = val['time_end']
        category = val['category']
        info = val['description']
        price = val['cost']
        address1 = val['location']['address1']
        city = val['location']['city']
        zip_code = val['location']['zip_code']
        country = val['location']['country']
        state = val['location']['state']
        display_address = val['location']['display_address']
        disp = ""
        for i in display_address:
            disp += " " + i
        loc = Location(address1, city, zip_code, state, country, disp)
        tickets = val['tickets_url']
        id = val['id']
        picture = val['image_url']

        # print("name:", name)
        # print("starts:", start_time)
        # print("ends:", end_time, "\n")
        # Currently does not account for timezones --> issue to resolve eventually
        dt_start = parser.parse(start_time)
        uts_start = datetime.timestamp(dt_start)

        if end_time is not None:
            dt_end = parser.parse(end_time)
            uts_end = datetime.timestamp(dt_end)
        else:
            uts_end = None

        if price is None:
            price = 0.0
        to_add = eventStorage(name, uts_start, uts_end, loc, category, info, float(price), None, tickets, id, picture)
        return to_add

