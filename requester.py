import json

import requests

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
#the = None in the parameters means if we get no value for date2 date2 results iin None
def make_request(location, date1, date2 = None):
    url = f"{base_url}{location}/{date1}{"/" + date2 if date2 else ""}"
    print(url)
    
    return None


make_request("NY", "2025", "2024")