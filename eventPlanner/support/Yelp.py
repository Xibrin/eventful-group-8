import requests
import json
import os
import re
from datetime import datetime
import calendar


class Yelp:

    def __init__(self, start_time, location):
        self.start_time = start_time
        self.location = location

    def get_events(self):
        print("\nstarting YELP_API\n")
        headers = {'Authorization': 'Bearer %s' % os.getenv("YELP_API_KEY")}
        limit = 50
        url = 'https://api.yelp.com/v3/events'

        # In the dictionary, term can take values like food, cafes or businesses like McDonalds

        # d = datetime.utcnow()
        # unixtime = calendar.timegm(d.utctimetuple())
        for i in range(1):
            params = {'location': self.location, 'limit': limit, 'offset': i * 50, 'start_date': self.start_time}
            # Making a get request to the API
            req = requests.get(url, params=params, headers=headers)
            # Split request by event (separated by curly braces)
            events = req.text.split(sep="}, {")
            # throwaway variable to check if the number of events parsed equals total number of events
            j = 0
            for val in events:
                # increment throwaway, print (to ensure all events are read)
                j = j + 1
                print(j)
                # look for name of event, and print
                start = val.find("\"name\"")
                end = val.find("tickets_url")
                name = val[start + 7:end - 3]
                print("name:", name)

                # look for event category, and print
                start = val.find("category")
                end = val.find("cost")
                category = val[start + 11:end - 3]
                print("category: ", category)

                # look for event description(not full descriptor but close)
                start = val.find("description")
                end = val.find("\"event_site_url")
                description = val[start + 14:end - 3]
                print("description:", description)

                # look for cost of event
                start = val.find("cost\"")
                end = val.find("cost_max")
                cost = val[start + 7:end - 3]
                # check cost. if none given print cost: $ 0.0
                if cost == "null":
                    print("cost: $ 0.0")
                else:
                    print("cost: $", cost)

                # look for event address
                start = val.find("display_address")
                end = val.find("cross_streets")
                address = val[start + 19:end - 4]
                print("address: ", address, "\n")

            # proceed only if the status code is 200
            print('The status code is {}'.format(req.status_code))
            # convert full event list to text, and print below
            to_print = json.loads(req.text)
            print(to_print)

        return to_print
