#!/usr/bin/env python3

# Import Image object from PIL and GPSTAGS, TAGS from PIL.ExifTags.
# Import path from os
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
from os import path

# Prompt asks from which file from the directory 'images' you want to get GPS coordinates
image = input("Enter the image name (image.jpg) from which you want to get GPS coordinates in the directory 'images': ")

# Checks if the file you entered is correct and exists in the directory '/images'.
if len(image) !=0 and path.exists(f"images/{image}"):
    print(f"You have chosen the image {image}")
else:
    print(f"Sorry, such image does not exist. Please, enter correct image name that exists in '/images' directory.")
    exit(1)

# Open image from directory ./images
img = Image.open(f'images/{image}')

# Create gps dictionary
gps = dict()

# Go through tags and values from image using '_getexif() function' and if tag contains info about GPS,
# then add this tag and its value to gps dictionary.
for tag, value in img._getexif().items():
    tag_name = TAGS.get(tag)
    if tag_name == "GPSInfo":
        for key, val in value.items():
            gps.update({GPSTAGS.get(key): val})


# Function converts decimals to degrees. And check if the direction is South of North and if yes,
# make that coordinate negative
def decimal2degree(degrees, minutes, seconds, direction):
    coordinate = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if direction == 'S' or direction == 'W' or direction == "South" or direction == "West":
        coordinate *= -1
    return coordinate

# Assign latitude and longitude to the corresponding value using decimal2degree function and GPS tags.
latitude = decimal2degree(gps['GPSLatitude'][0], gps['GPSLatitude'][1], gps['GPSLatitude'][2], gps['GPSLatitudeRef'])
longitude = decimal2degree(gps['GPSLongitude'][0], gps['GPSLongitude'][1], gps['GPSLongitude'][2], gps['GPSLongitudeRef'])


# Open gps_coordinates.txt file for writing and write latitude and longitude to the file
with open('gps_coordinates.txt', 'w') as data:
    data.write(f"{latitude},{longitude}")

# Print the result as a pair of the latitude and the longitude
print(f"Your GPS coordinates are:\n{latitude}'; {longitude}'")
