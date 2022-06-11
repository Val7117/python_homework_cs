#!/usr/bin/env python3

# Define first_num and last_num in the range (default is [1, 100]
# Define the number of last digits in the number (default is 10)

first_num = 1
last_num = 1000
number_of_digits = 10

# Main list comprehension

res = str(sum([a ** a for a in range(first_num, last_num + 1)]))

# Print the result

print(f"The last {number_of_digits} digit(s) of series {first_num} ^ {first_num} + ... + {last_num} ^ {last_num} \
is", res[-number_of_digits::1])
