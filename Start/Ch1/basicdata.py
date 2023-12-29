# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
maxTemp = -10
for i in weatherdata:
    maxTemp = max(maxTemp, i["tmax"])
print(maxTemp)
# TODO: What was the coldest day in the data set?
minTemp = 1000
for i in weatherdata:
    minTemp = min(minTemp, i["tmin"])
print(minTemp)

# TODO: How many days had snowfall?
snowdays = 0
for i in weatherdata:
    if i["snow"]>0:
        snowdays+=1
print(snowdays)
