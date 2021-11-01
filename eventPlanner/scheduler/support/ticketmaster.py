import requests
import os
from ..models import Event

class TicketMaster:
    def __init__(self, date, city):
        self.date = date
        self.city = city

    def get_events_date(self):
        base_url = "https://app.ticketmaster.com/discovery/v2/events.json?&apikey="
        key = ""  # TODO: ADD TICKETMASTER API KEY HERE
        added_url = "&locale=*&startDateTime=" + self.date + "T02:00:00Z&endDateTime=2021-10-31T02:00:00Z&city=" + self.city
        req = requests.get(base_url + key + added_url)

        if req.status_code != 200:
                print("STATUS CODE: " + str(req.status_code))
                return None
        event_list = []
        for i in req['events'] :
            j = TicketMaster.parse_one_event(i)
            #excludes events that have no time announced
            if j != None :
                event_list.append(j)
        # TODO: please check my formatting for json; also, i noticed that there is a json built in parser for python. do we need to import that?
        return event_list

    @staticmethod
    def parse_one_event(event):
        new_event = Event()
        new_event.name = event['name']
        # new_event.id = event['id']
        new_event.picture = event['images']['url']
        if event['dates']['start']['timeTBA'] == True or event['dates']['start']['noSpecificTime'] == True:
            return None
        new_event.start_time = event['dates']['start']['dateTime']
        new_event.end_time = new_event.start_time + 5
        new_event.tickets = event['dates']['start']['status']
        new_event.address1 = event['_embedded']['venues']['address']['line1']
        new_event.city = event['_embedded']['venues']['city']['name']
        new_event.state = event['_embedded']['venues']['state']['name']
        zip = event['_embedded']['venues']['postalCode']
        new_event.zip = int(zip) if zip and zip != '' else None
        new_event.country = event['_embedded']['venues']['country']['countryCode']
        # new_event.disp = ""
        new_event.description = event['info']
        # new_event.loc = Location(addressLine, city, zipcode, state, country, disp)
        #ticket price i have no idea how to get
        new_event.cost = event['_embedded']['venues']['markets']['id']
        new_event.category = event['classifications']['segment']['name']

        return new_event
