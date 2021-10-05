# This is a sample Python script.
import requests
import os


# TicketMaster API use for reference
# def ticketmaster():
#     base_url = "https://app.ticketmaster.com/discovery/v2/events.json?postalCode=21218&apikey="
#     key = os.getenv("TICKETMASTER")
#     response = requests.get(base_url + key)
#     print(response.json())

def directions(startPos, endPos):
    base_url = "http://open.mapquestapi.com/directions/v2/route?key="
    locations = "&from=" + startPos + "&to=" + endPos
    key = os.getenv("MAPQUEST_API_KEY")
    response = requests.get(base_url + key + locations)
    print(response.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directions("9E 33rd Baltimore, Maryland", "107 W 29th St, Baltimore, Maryland")
    # ticketmaster()
