#!/usr/bin/env python3                                                                 

entered_data = input("-> ")
splitted_data = entered_data.split()
result = list(dict.fromkeys(splitted_data))

print(' '.join(result))

