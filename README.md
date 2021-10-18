# Itinerary Planning Application

For this application, a user will be able to search for events based on their location and the amount of free time they have available. We are using the Yelp and Ticketmaster APIs to get a list of available events given the schedule of the user and the Mapquest API to get the route between two locations. As a user of this product, you will be able to have a list of recommended events to attend and be able to see the different transportation modalities and associated costs for the transportation/event. Our recommendation system will prioritize the events based on the user's preferences which include budget, preferred transport and type of event.

Currently, to use our app (limited to the first iteration), the user must create a Yelp object and then pass in a string which represents the street address from which the program will begin searching local events for. The user can then call the get_events() function on the Yelp object to get local events centered at that point. In order for the user to find a route between two locations right now, the user must create a Travel object and then pass in a string representing the street address of their starting position and a string representing the street address of their end location. Calling get_map_response() on this Travel object will result in the printing of a Json file containing a route/map directions between these two locations. While other features (such as optimizing a route between multiple events is currently under development, these are not in a usable state yet).

For this iteration, we apologize that we have not yet created a front-end / user-friendly interface for any of our currently implemented features. Thanks!

# If not every installed, install:

pip install python-dateutil (note: you may need to specify which python version you want to install python-dateutil on. For example, in my case, I was running Python3.10. So I did python3.10 -m pip install python-dateutil)

To install the project dependencies, from the root directory, eventPlanner, run the following command (Note that you might need to create a new virtual environment and activate it before installing the packages. For more information, refer to https://docs.python.org/3/tutorial/venv.html):

`pip install -r requirements.txt`

To install the latest version of npm run

`{npm install -g npm}`

And install the latest version of Node.js from

https://nodejs.org/en/

Additionally the following packages:

`{npm install react-scripts}`
`{npm install basscss}`
`{npm install react-router-dom}`

# Running the Program

`cd` into the root directory, `eventPlanner`

If not already activated, activate your virtual environment using `source <environment_name>/bin/activate`

From the root directory, `eventPlanner`, run

`cd frontend` 

to move into the `frontend` directory and run

`npm run build` 

to generate the build files necessary for the front end to run. If for some reason, the build fails ro compile, run 

`npm install` 

to install all the required dependencies.

If you receive an error that states a build cannot be compiled due to 

`./node_modules/basscss/css/basscss.min.css`

run the following command

`npm install basscss@8.0.2`

Once you have the required packages installed, run the command

`npm start`

in order to run the application on a local host in your browser



Next, run 

`cd ..` to return to the root directory, eventPlanner

Finally, run the following commands:

`python manage.py makemigrations` (Commit the latest changes made to the databases)

`python manage.py migrate` (Push the latest changes to the databases)

`python manage.py runserver` (Start up the localhost server, Click the provided link.)
