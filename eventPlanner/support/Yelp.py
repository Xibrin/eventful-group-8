import requests
import json
import os
from datetime import datetime
import calendar

class Yelp:

    def __init__(self, start_time, location):
        self.start_time = start_time
        self.location = location

    def get_events(self):
        headers = {'Authorization': 'Bearer %s' % os.getenv("YELP_API_KEY")}

        url = 'https://api.yelp.com/v3/events'

        # In the dictionary, term can take values like food, cafes or businesses like McDonalds

        #d = datetime.utcnow()
        #unixtime = calendar.timegm(d.utctimetuple())
        params = {'location': self.location, 'limit': 50, 'start_date': self.start_time}

        # Making a get request to the API
        req = requests.get(url, params=params, headers=headers)

        # proceed only if the status code is 200
        print('The status code is {}'.format(req.status_code))

        # printing the text from the response
        to_print = json.loads(req.text)
        print(to_print)

        return to_print

