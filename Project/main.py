# This is a sample Python script.
import requests
import os
import event_finder
import json
import Route

class Travel:
    def __init__(self, start_pos=None, end_pos=None, location_list=None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.location_list = location_list
        self.route = None
        if start_pos is not None:
            self.route = self.directions()
        elif location_list is not None:
            self.route = self.optimized_directions()
        else:
            print("Both start_pos and location_lists are None")
            raise

    def directions(self):
        base_url = "https://open.mapquestapi.com/directions/v2/route?key="
        locations = "&from=" + self.start_pos + "&to=" + self.end_pos
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        return Route(json.loads(response.text))

    def optimized_directions(self):
        base_url = "https://open.mapquestapi.com/directions/v2/optimizedroute?key="
        locations = "&json=" + self.location_list
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        return Route(json.loads(response.text))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    travel = Travel("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    travel.directions()
    travel.get_tolls()
    # ticketmaster()
