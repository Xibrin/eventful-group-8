import requests
import os


class EventFinder:

    def __init__(self):
        pass

    def events(self):
        base_url = "https://app.ticketmaster.com/discovery/v2/events.json?&apikey="
        key = os.getenv("TICKETMASTER_API_KEY")
        response = requests.get(base_url + key)
        print(response.json())
        return response
