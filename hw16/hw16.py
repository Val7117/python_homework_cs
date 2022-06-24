#!/usr/bin/env python3

# Import Nominatim from geopy.geocoders
from geopy.geocoders import Nominatim

# Open file 'gps_coordinates.txt' in the directory ../hw17/ for reading and read the file.
with open("../hw17/gps_coordinates.txt", 'r') as file:
    coordinates = file.read()

# Slit data and get latitude and longitude as float numbers. Print the values.
split_data = coordinates.split(',')
latitude = float(split_data[0])
longitude = float(split_data[1])
print(f"Input data: {latitude}'; {longitude}'")

# Define the location using latitude, longitude and Nominatim. Print the location.
geo = Nominatim(user_agent="my_map")
location = geo.reverse(f"{latitude},{longitude}")
print(f"Location: {location}")

# Construct the URL and print the result.
url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
print(f"Goggle Maps URL: {url}")
