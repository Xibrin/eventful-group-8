# This is a sample Python script.
import requests
import os


# TicketMaster API use for reference
# def ticketmaster():
#     base_url = "https://app.ticketmaster.com/discovery/v2/events.json?postalCode=21218&apikey="
#     key = os.getenv("TICKETMASTER")
#     response = requests.get(base_url + key)
#     print(response.json())

class Travel:

    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.route = None

    def directions(self, start_pos, end_pos):
        base_url = "http://open.mapquestapi.com/directions/v2/route?key="
        locations = "&from=" + start_pos + "&to=" + end_pos
        key = os.getenv("MAPQUEST_API_KEY")
        response = requests.get(base_url + key + locations)
        print(response.json())
        self.route = response.json()
        return response.json()

    def createRoute(self):
        #use helper methods (or not depending on ease of implementation) to parse the directions into a route object

    #Helper Methods
    def get_fuel_cost(self):
        #parse Json to get fuel cost

    def get_distance(self):
        #parse Json to get distance

    def get_time(self):
        #parse Json to get time



# Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        directions("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    # ticketmaster()
