#!/usr/bin/env python3

# Enter the limit (the sum of a Pythagorean triplet: a + b + c = limit). Default is 1000.

limit = 1000

print("Please wait =) I am calculating your triplet(s) and product ...")

# I delete limit by 2 to reduce the time of calculation. If the program does not give you any result, then
# increase the limit or remove /2 below from ranges.

[print("Your Pythagorean triplet is [", a, b, c, "].","The product of the triplet is", (a * b * c), ".")
 for a in range(1, int(limit/2) + 1) for b in range(a, int(limit/2) + 1) for c in range(b, int(limit/2) + 1) if a + b + c == limit
 and (a < b < c) and (a ** 2 + b ** 2 == c ** 2)]
