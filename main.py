from flask import Flask

from requester import make_request
from time_helper import find_date_range
from validater import validate_range, validate_time_type

app = Flask(__name__)

#to run your flask api locally use the command flask --app main run   
#main is the name of this file (main.py)

#when we use the @app.route followed by a function we tell flask what endpoint should trigger the function
#in the case the / endpoint triggers the test function when used

#we can add the methods parameter and set what kind of request triggers ther function followed by the endpoint
# @app.route("/", methods=['get'])
# def test():
#     return "<p>Hello, World!</p>"


#we mostly use zip codes 

#<parameter> is the parameter we extract from the api call
#this route is getting the current weather based on location
@app.route("/location/<location>", methods=["get"])
def by_location(location):
    response = make_request(location)
    if(response):
        weather = response['currentConditions']['temp']
        feels_like = response['currentConditions']['feelslike']
        return {"weather": weather ,"feels_like": feels_like}
    else:
        return {"error": "invalid request check docs"}
    
    return {"error": "invalid parameter"}


#get weather history given a time range ex: 7days, 1 year etc
#raange can be negative -7 , -10 etc
#range can be negative
#limit is up to two weeks
@app.route("/history/<location>/<time_type>/<range>", methods=["get"])
def weather_history(location,time_type, range):
    is_time_type_valid = validate_time_type(time_type)
    is_range_valid = validate_range(range)
    if (is_time_type_valid and is_range_valid):
        time_ranges = find_date_range(time_type, int(range))
        print(time_ranges)
        response = make_request(location, time_ranges[0], time_ranges[1])
        
        if(response):
            return response
        else:
            return {"error": "invalid request or request max reached, check docs"}
    
    
    return {"error": "Inavlid parameters provided"}





#keys for location
# queryCost
 
# latitude
 
# longitude
 
# resolvedAddress
 
# address
 
# timezone
 
# tzoffset
 
# description
 
# days
 
# alerts
 
# stations
 
# currentConditions