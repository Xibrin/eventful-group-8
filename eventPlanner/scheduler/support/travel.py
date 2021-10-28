
import requests
import os
from . import route
import json
# from Project.route import Route


class Travel:
    def __init__(self, start_pos=None, end_pos=None, location_list=None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.location_list = location_list
        self.route = None
        if start_pos is not None:
            self.route = self.get_map_response()
        elif location_list is not None:
            self.route = self.optimized_directions()
        else:
            print("Both start_pos and location_lists are None")
            raise

    def get_map_response(self):
        base_url = "https://open.mapquestapi.com/directions/v2/route?key="
        locations = "&from=" + self.start_pos + "&to=" + self.end_pos
        key = "JEq6beD60zZZFpjDPAGR9gnuO0k3B0IX"  # TODO: INSERT MAPQUEST API KEY HERE
        response = requests.get(base_url + key + locations)
        # print(response.json())

        #Return Route object
        return route.Route(json.loads(response.text))

    def get_travel_time(self):
        return self.route.time

    def optimized_directions(self):
        base_url = "https://open.mapquestapi.com/directions/v2/optimizedroute?key="
        locations = "&json=" + self.location_list
        key = "JEq6beD60zZZFpjDPAGR9gnuO0k3B0IX"  # TODO: INSERT MAPQUEST API KEY HERE
        response = requests.get(base_url + key + locations)
        # print(response.json())

        #Return Route object
        return route.Route(json.loads(response.text))

    #def get_fuel_cost(self):
    #    # parse Json to get fuel cost
    #    route = self.create_route()
    #    return route.cost