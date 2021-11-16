import requests
import os
from ..models import Event
from dateutil import parser
import datetime

class TicketMaster:

    # Method that returns a list of events, connecting with
    # the ticketmaster API and returning its response as a JSON,
    # ready to be parsed.

    # README: put your proprietary API key in the "key" field

    # @param the limitations set by the user (for now, only
    # start_time and location)

    # @return a list of events
    
    def get_events_date(self, location, start_time):
        event_list = []

        # Converts the given start time to ISO 8601 format for the API
        # End times are not given by Ticketmaster, so we must hard code for now
        end_time = start_time + 5256000
        end_convert = datetime.datetime.fromtimestamp(end_time)
        end_api_time = end_convert.isoformat()
        converted = datetime.datetime.fromtimestamp(start_time)
        input_time = converted.isoformat()

        # Request making
        base_url = "https://app.ticketmaster.com/discovery/v2/events.json?&apikey="
        key = "MwvGo5jGojI13TDq5rDzKB2t95MmMNsy"  # TODO: ADD TICKETMASTER API KEY HERE
        added_url = "&locale=*&startDateTime="+ input_time + "Z&endDateTime=" + end_api_time + "Z&city=Baltimore"
        req = requests.get(base_url + key + added_url)
        print(type(req))
        if req.status_code != 200:
                print("STATUS CODE: " + str(req.status_code))
                return None

        # Response processing
        response = req.json()
        for i in response['_embedded']['events'] :
            j = TicketMaster.parse_one_event(i)
            event_list.append(j)
        return event_list


    # Method that extracts the information from a JSON format and returns
    # an event in our proprietary event object.

    # @param takes in the subset of information under 'events' in the JSON

    # @return an event, unnamed, that contains all information from the JSON
    
    @staticmethod
    def parse_one_event(event):
        new_event = Event()
        # If no specific date/time announced, skip event altogether
        if event['dates']['start']['timeTBA'] == True or event['dates']['start']['noSpecificTime'] == True:
            return
        new_event.name = event['name']
        
        # Checks for the inclusion of info in the JSON for one event
        if ('info' in event):
            new_event.description = event['info']
        else:
            new_event.description = "No Info Provided"

        # If a price is present, set it. Otherwise, set to zero
        if ('priceRanges' in event):
            new_event.cost = event['priceRanges'][0]['min']
        else:
            new_event.cost = 0
        
        # Filling in the rest of the information which is guaranteed to be present
        new_event.category = event['classifications'][0]['segment']['name']
        new_event.picture = event['images'][0]['url']
        new_event.start_time = parser.parse(event['dates']['start']['dateTime'])

        # Since no endtimes are provided, we must hard-code a 3 hour event average time
        delta = datetime.timedelta(hours=3)
        new_event.end_time = new_event.start_time + delta

        # Checks if there is a seatmap to buy tickets from; will always be present unless free
        if(event['seatmap']['staticUrl']):
            new_event.tickets = event['seatmap']['staticUrl']
        else:
            new_event.tickets = ""

        new_event.address1 = event['_embedded']['venues'][0]['address']['line1']
        new_event.city = event['_embedded']['venues'][0]['city']['name']
        new_event.state = event['_embedded']['venues'][0]['state']['stateCode']
        zip = event['_embedded']['venues'][0]['postalCode']
        new_event.zip = int(zip) if zip and zip != '' else None
        new_event.country = event['_embedded']['venues'][0]['country']['countryCode']

        return new_event
