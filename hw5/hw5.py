#!/usr/bin/env python3

# Take an input from user

entered_data = input('-> ')

# Splitting data

splitted_data = entered_data.split()

# Creating an empty new_list

new_list = []

# Transforming strings from the list to integers and adding them the to new_list

for j in splitted_data:
    new_list.append(int(j))

# Find the max number in the new_list

max_num = max(new_list)

# Create an additional list for checking. The list starts from 1 (as it is the smallest positive integer).
# And the list ends with max_num + 1 (because in range the last number is not included, so adding 1 we include
# the last max_num

list = range(1, max_num + 1)

# Main algorithm searches for the smallest number in the list which is not in the entered list.
# If there is no such number then we add 1 to the max_num and this is going to be the smallest positive number
# which is not in the list

for j in list:
    if j not in new_list:
        smallest_positive = j
        break
    else:
        smallest_positive = max_num + 1

# Print the result

print(smallest_positive)
