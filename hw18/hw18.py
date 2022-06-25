#!/usr/bin/env python3

# Import needed packages
from PIL import Image
import os
from os import path


# Define function to output human-readable size format. Divide by 1000 and not by 1024 for the purpose of
# having the same result with the Linux filesystem.
def size_of_file(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1000:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1000
    return f"{num:.1f}Yi{suffix}"


# Input prompt that offers to choose the needed file to ve miniatured
image_name = input("Enter the name of an image from directory 'images': ")

# If statement checks, if the entered name's length is not 0 and file exists in the 'images' directory.
# If there is not such file or file's length is 0, then terminate program. Otherwise, continue program and
# print that image with the corresponding size has been chosen.
if len(image_name) != 0 and path.exists(f"images/{image_name}"):
    old_size = size_of_file(os.path.getsize(f"images/{image_name}"))
    print(f"You have chosen the file {image_name} with the size {old_size}")
else:
    print("There is no such image. Please enter the name of an image that exists in the directory 'images'.")
    exit(1)

# Opens chosen image in the directory 'images'
image = Image.open(f'images/{image_name}')

# Default parameters for a miniature of an image
height = 200
width = 300

# Create a miniature of an image and save the miniature to the 'miniatures' directory, adding 'min_' to
# the image name.
# Get the size of the miniature in the human-readable format
image.thumbnail((width, height))
image.save(f'miniatures/min_{image_name}', quality=90)
new_size = size_of_file(os.path.getsize(f"miniatures/min_{image_name}"))

# Print the result (image name and its size) and open the miniature of the picture.
print(f"The miniature of you picture {image_name} has been saved to 'miniatures' directory as min_{image_name}")
print(f"The size of min_{image_name} is {new_size}")
image.show()
