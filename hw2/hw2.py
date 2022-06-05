#!/usr/bin/env python3

entered_data = input("-> ")
splitted_data = entered_data.split()

result = []

for i in splitted_data:
    if i in  splitted_data and  i not in result:
        result.append(i)

print(' '.join(result))
