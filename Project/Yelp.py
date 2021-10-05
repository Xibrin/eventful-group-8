import requests
import json
import os
from datetime import datetime
import calendar


if __name__ == '__main__':
    headers = {'Authorization': 'Bearer %s' % os.getenv("YELP_API_KEY")}

    url = 'https://api.yelp.com/v3/events'

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds

    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    params = {'location': '9E 33rd Baltimore, Maryland', 'limit': 50, 'start_date': unixtime}

    # Making a get request to the API
    req = requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    print('The status code is {}'.format(req.status_code))

    # printing the text from the response
    print(json.loads(req.text))

