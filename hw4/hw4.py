#!/usr/bin/env python3

while 1:

# Prompt -> for entering data

    entered_data = input('-> ')

# Create useful string and integer objects

    new_string = ' '
    result = 0

# Main algorithm that checks if a sign in entered_data is digit or not. If yes then add this sign to new_string.
# 2 elif check the number of '-' signs. 
# If the new and the previous signs are '-' then pass.
# If the new sign is '-' and the previous sign is NOT '-' then add ' -' to avoid conflicts.
# Any other sign adds ' ' to new_string.

    for i in entered_data:
        if i.isdigit():
            new_string = new_string + i
        elif i == '-' and (new_string[-1] == '-'):
            pass
        elif i == '-' and (new_string[-1] != '-'):
            new_string = new_string + ' -'
        else:
            new_string = new_string + ' '

# Additional check. If the last sign is '-' then add zero to the end. It avoids error.

    if  new_string[-1] == '-':
            new_string = new_string + '0'

# Split data and get a list of valid positive and negative numbers (which are still strings in the list).

    splitted_data = new_string.split()

# If the string in the list is not empty or has only '-' sign then transform each string to integer and calculate the sum of integers.

    for j in splitted_data:
        if j != '-' and j != '':                
            result = result + int(j)

# Print the result

    print(result)
    print('')

