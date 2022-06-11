#!/usr/bin/env python3

# first_num and last_num define the range (default is [1, 100]).

first_num = 1
last_num = 100

# Main list comprehension

diff = (sum([a for a in range(first_num, last_num + 1)])) ** 2 - sum([a ** 2 for a in range(first_num, last_num + 1)])

# Print the result

print(f"The difference for range [{first_num}, {last_num}] is", diff)
