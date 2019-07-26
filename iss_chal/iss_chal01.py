#!/usr/bin/python3

'''
Script to pull the time the ISS will pass over warrenton, va
38.717137, -77.792576
'''
import requests
import pprint

lat = input("What Latitude are you requesting? ")
lon = input("What Longitude are you requesting? ")

url = (f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}')
#create r, which is out requests object
r = requests.get(url)

print("\nThe next time the International Space Station will fly over your location is: \n")

for i in r.json()["response"]:
    print(f"Time: {i['risetime']} and Duration: {i['duration']}")

print("\n")
pprint.pprint(r.json())
