import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('KEY')
print(MY_ENV_VAR)
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
header = {"key": MY_ENV_VAR}
#the = None in the parameters means if we get no value for date2 date2 results iin None
def make_request(location, date1 = None, date2 = None):
    url = f"{base_url}{location}{"/" + date1 if date1 else ""}{"/" + date2 if date2 else ""}"
    print(url)
    response = requests.get(url, params=header)

    output = response.json() if response.status_code == 200 else None
        
    return output



