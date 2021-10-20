# Itinerary Planning Application

## Built With

Django

## Application Explanation

For this application, a user will be able to search for events based on their location and the amount of free time they have available. We are using the Yelp and Ticketmaster APIs to get a list of available events given the schedule of the user and the Mapquest API to get the route between two locations. As a user of this product, you will be able to have a list of recommended events to attend and be able to see the different transportation modalities and associated costs for the transportation/event. Our recommendation system will prioritize the events based on the user's preferences which include budget, preferred transport and type of event.

Currently, to use our app (limited to the second iteration), the user must create a Yelp object and then pass in a string which represents the street address from which the program will begin searching local events for. The user can then call the get_events() function on the Yelp object to get local events centered at that point. In order for the user to find a route between two locations right now, the user must create a Travel object and then pass in a string representing the street address of their starting position and a string representing the street address of their end location. Calling get_map_response() on this Travel object will result in the printing of a Json file containing a route/map directions between these two locations. While other features (such as optimizing a route between multiple events is currently under development, these are not in a usable state yet).

## Getting started

## If not every installed, install:

` pip install python-dateutil ` (note: you may need to specify which python version you want to install `python-dateutil` on. For example, in my case, I was running Python3.10. So I did `python3.10 -m pip install python-dateutil`)

To install the project dependencies, from the root directory, eventPlanner, run the following command (Note that you might need to create a new virtual environment and activate it before installing the packages. For more information, refer to https://docs.python.org/3/tutorial/venv.html):

`pip install -r requirements.txt`


## Running the Program

git clone https://github.com/jhu-oose/2021-fall-group-group8.git and wait for authorization if not granted already

You need api keys to access information used in our program and set these values as environmental variables

You can receive an API Key for Yelp and more information at https://www.yelp.com/developers/documentation/v3/authentication

You can receive an API Key for MapQuest and more information at https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register

You can receive an API Key for TicketMaster and more information at https://developer.ticketmaster.com/products-and-docs/apis/getting-started/

Put all 3 API keys into a file named `.env` (note the dot in the file name) inside the root folder of the project, eventPlanner, in the exact format shown below:

`YELP_API_KEY=your_yelp_api_key`

`MAPQUEST_API_KEY=your_mapquest_api_key`

`TICKETMASTER_API_KEY=your_ticketmaster_api_key`

If for some reason the process outlined above does not work, insert the API keys into the following files as hard code.

The YELP_API_KEY should be put into `yelp.py` at the key variable (this has a TODO on it)

The MAPQUEST_API_KEY should be put into `schedule.py` (this has a TODO on it)

Use of the TICKETMASTER_API_KEY is not functional at this point so no action needs to be taken for this API key.

Finally, run the following commands from the root directory, eventPlanner:

`python manage.py makemigrations` (Commit the latest changes made to the databases)

`python manage.py migrate` (Push the latest changes to the databases)

`python manage.py runserver` (Start up the localhost server, click the provided link.)

## Roadmap
* We have accomplished our goal of using the Yelp Api to find events for users based on their desired time frame and location
* We still have to implement the use of the TicketMaster Api to find a greater range of events to offer to users 
* We still need to develop a robust recommendation algorithm to offer a comprehensive schedule to users based on their preferences


## Contact
*If you have any questions or concerns, you can reach the project link at https://github.com/jhu-oose/2021-fall-group-group8.git.
*If you would like to speak to one of the team members, feel free to email at pnovell1@jhu.edu

## Acknowledgements
*We would like to acknowledge the contributions of each of the team members in coming up with the design of the project and sharing their ideas on how to constantly improve the application.
*We received assistance by watching publicly available videos of CS50 Introduction to Web Programming with Python and Javascript at Harvard University
