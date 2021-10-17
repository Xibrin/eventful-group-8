# Itinerary Planning Application

For this application, a user will be able to search for events based on their location and the amount of free time they have available. We are using the Yelp and Ticketmaster APIs to get a list of available events given the schedule of the user and the Mapquest API to get the route between two locations. As a user of this product, you will be able to have a list of recommended events to attend and be able to see the different transportation modalities and associated costs for the transportation/event. Our recommendation system will prioritize the events based on the user's preferences which include budget, preferred transport and type of event. 

Currently, to use our app (limited to the first iteration), the user must create a Yelp object and then pass in a string which represents the street address from which the program will begin searching local events for. The user can then call the get_events() function on the Yelp object to get local events centered at that point. In order for the user to find a route between two locations right now, the user must create a Travel object and then pass in a string represnting the street address of their starting position and a string representing the street address of their end location. Calling get_map_response() on this Travel object will result in the printing of a Json file containing a route/map directions between these two locations. While other features (such as optimizing a route between multiple events is currently under development, these are not in a usable state yet).

For this iteration, we apologize that we have not yet created a front-end / user-friendly interface for any of our currently implemented features. Thanks!

# If not every installed, install:
pip install python-dateutil
