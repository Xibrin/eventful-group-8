import requests
from dateutil import parser

from ..models import Event

class Yelp:

    def __init__(self):
        self.URL = 'https://api.yelp.com/v3/events'
        self.KEY = "ch0KHsoQZVMqSS13Q9Hsl5hsl2hAmy4WMoyeBjUVf_I4s4VJMXetUO7XnoBNj3K6d4jW0uD9DkqpkEk2lIlcpPVSqHoIw-G6dCVO6sfUNGi9zvkcQ9GpCTT6gY5cYXYx"  # TODO: INSERT YELP API KEY HERE
        self.HEADERS = {'Authorization': 'Bearer %s' % self.KEY}
        self.LIMIT = 50

    def parse_events(self, location, start_time):
        event_list = []
        for i in range(1):
            params = {'location': location, 'limit': self.LIMIT, 'offset': i * self.LIMIT, 'start_date': start_time}
            # Making a get request to the API
            req = requests.get(self.URL, params=params, headers=self.HEADERS)
            # Split request by event (separated by curly braces)
            print(req.url)
            if req.status_code != 200:
                print("STATUS CODE: " + str(req.status_code))
                continue
            response = req.json()
            for event in response['events']:
                e = Yelp.parse_one_event(event)
                if e:
                    event_list.append(e)
        return event_list

    @staticmethod
    def parse_one_event(event):
        new_event = Event()
        new_event.name = event['name']
        if event['time_start']:
            print(event['time_start'])
            new_event.start_time = parser.parse(event['time_start'])
        else:
            return None
        if event["time_end"]:
            new_event.end_time = parser.parse(event['time_end'])
        else:
            return None
        new_event.category = event['category']
        new_event.description = event['description']
        new_event.cost = float(event['cost']) if event['cost'] else 0.0

        new_event.tickets = event['tickets_url']
        new_event.picture = event['image_url']

        new_event.address1 = event['location']['address1']
        new_event.city = event['location']['city']
        new_event.country = event['location']['country']
        new_event.state = event['location']['state']
        zip = event['location']['zip_code']
        new_event.zip = int(zip) if zip and zip != '' else None

        return new_event

