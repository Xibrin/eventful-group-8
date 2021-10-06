# This is a sample Python script.
import json
import requests
import os

import event_finder
import json
import route
from Project.route import Route


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

    def get_map_response(self):
        base_url = "https://open.mapquestapi.com/directions/v2/route?key="
        locations = "&from=" + self.start_pos + "&to=" + self.end_pos
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        return route.Route(json.loads(response.text))

    def optimized_directions(self):
        base_url = "https://open.mapquestapi.com/directions/v2/optimizedroute?key="
        locations = "&json=" + self.location_list
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        return Route(json.loads(response.text))

    #def create_route(self):
    #    # use helper methods (or not depending on ease of implementation) to parse the directions into a route object
    #    json_map = self.get_map_response()
    #    route = Route(self.start_pos, self.end_pos, 0, 0, 0, 0)
    #    route.end_pos = self.end_pos
    #    route.start_pos = self.start_pos
    #    route.distance = json_map.route.distance
    #    route.cost = json_map.cost
    #    route.time = json_map.time
    #    route.means = json_map.means
    #    return route

    # Helper Methods
    #def get_fuel_cost(self):
    #    # parse Json to get fuel cost
    #    route = self.create_route()
    #    return route.cost

    #def get_distance(self):
    #    route = self.create_route()
    #    return route.distance

    #def get_time(self):
    #    route = self.create_route()
    #    return route.time




if __name__ == '__main__':
    travel = Travel("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    travel.get_map_response()
    travel.create_route()
