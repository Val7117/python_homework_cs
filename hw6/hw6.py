#!/usr/bin/env python3

palindromic_both = []
start = 1
end = 1000000

for i in list(range(start, end)):
    if i == int((str(i)[::-1])) and bin(i)[2:] == bin(i)[::-1][:-2]:
        palindromic_both.append(i)

result = sum(palindromic_both)
print(f"The sum of all palindromic numbers in both bases between {start} and {end} is", result)