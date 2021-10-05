# This is a sample Python script.
import requests
import os
import event_finder

class Travel:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.route = None

    def directions(self):
        base_url = "https://open.mapquestapi.com/directions/v2/route?key="
        locations = "&from=" + self.start_pos + "&to=" + self.end_pos
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        self.route = response.json()
        return response.json()

    def createRoute(self):
        # use helper methods (or not depending on ease of implementation) to parse the directions into a route object
        pass

    # Helper Methods
    def get_fuel_cost(self):
        # parse Json to get fuel cost
        pass

    def get_distance(self):
        # parse Json to get distance
        pass

    def get_time(self):
        # parse Json to get time
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    travel = Travel("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    travel.directions()
    # ticketmaster()
