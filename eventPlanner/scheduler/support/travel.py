import requests
import os
from . import route
import json
from datetime import timedelta

INFI = 10000000

# from Project.route import Route


# def __init__(self, start_pos=None, end_pos=None, location_list=None):
#     self.start_pos = start_pos
#     self.end_pos = end_pos
#     self.location_list = location_list
#     self.route = None
#     if start_pos is not None:
#         self.route = self.get_map_response()
#     elif location_list is not None:
#         self.route = self.optimized_directions()
#     else:
#         print("Both start_pos and location_lists are None")
#         raise

def get_map_response(start_pos, end_pos):
    base_url = "https://open.mapquestapi.com/directions/v2/route?key="
    locations = "&from=" + start_pos + "&to=" + end_pos
    key = "xVp6Qgy7SK7vhjRMGbJw49weeg79JnaT"  # TODO: INSERT MAPQUEST API KEY HERE
    response = requests.get(base_url + key + locations)
    if response.status_code != 200:
        print(response.status_code)
        print("ERROR ISSUE WITH API")
        return None
    else:
        print("All GOOD SERVERS")
    # print("Status code: " + str(response.status_code))
    # print(response.json())

    # Return Route object
    # route.Route(json.loads(response.text))
    dictionary = None
    try:
        dictionary = json.loads(response.text)
    except:
        print("JSON DECODE ERROR WARNING WARNING")
        return None

    # print(dictionary)
    if dictionary['info']['statuscode'] != 0:
        return None
    else:
        return dictionary['route']


def get_travel_time(start_pos, end_pos):
    route = get_map_response(start_pos, end_pos)
    if route is None:
        return timedelta(hours=2)
    else:
        format = route['formattedTime']
        time_split = format.split(":")
        # seconds = time_split[0] * 3600 + time_split[1] * 60 + time_split[2]
        return timedelta(seconds=int(time_split[2]), minutes=int(time_split[1]), hours=int(time_split[0]))


def optimized_directions(location_list):
    base_url = "https://open.mapquestapi.com/directions/v2/optimizedroute?key="
    locations = "&json=" + location_list
    key = "JEq6beD60zZZFpjDPAGR9gnuO0k3B0IX"  # TODO: INSERT MAPQUEST API KEY HERE
    response = requests.get(base_url + key + locations)
    # print(response.json())
    # Return Route object
    return route.Route(json.loads(response.text))

# def get_fuel_cost(self):
#    # parse Json to get fuel cost
#    route = self.create_route()
#    return route.cost
